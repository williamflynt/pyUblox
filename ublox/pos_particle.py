#!/usr/bin/env python

from optparse import OptionParser

import numpy
import pybayes
import pybayes.filters
import pybayes.pdfs
import pylab

from . import ublox, satelliteData, util

parser = OptionParser("pos_particlew.py [options] <file>")
parser.add_option("--seek", type='float', default=0, help="seek percentage to start in log")
parser.add_option("-f", "--follow", action='store_true', default=False, help="ignore EOF")

(opts, args) = parser.parse_args()

# --- Parameters
n = 10
state_cov = 0.1
gps_cov = 10
# --- End Parameters

dev = ublox.UBlox(args[0])

if opts.seek != 0:
    dev.seek_percent(opts.seek)

satinfo = satelliteData.SatelliteData()
filt = None


def p_xt_xtp_mu(xtp):
    '''Return mean of Gaussian PDF for state xt given x(t-1).  Assume static receiver, Mean at old state'''
    return xtp


def p_xt_xtp_R(xtp):
    '''Return covariance of Gaussian PDF for state xt given x(t-1).'''
    return numpy.diag([state_cov, state_cov, state_cov, state_cov / util.speedOfLight])


def p_yt_xt_mu(xt):
    return xt


def p_yt_xt_R(xt):
    ''' Return covariance matric of Gaussian PDF for measurement yt given xt.'''

    return numpy.diag([gps_cov, gps_cov, gps_cov, gps_cov / util.speedOfLight])


def build_filter(info):
    global filt
    if info.receiver_position is None:
        # We bootstrap the filter by using the receiver's first fix for out initial pdf
        return

    rp = info.receiver_position
    mean = numpy.array([rp.X, rp.Y, rp.Z, 0])
    # Assume independence, we can do better than this but it's only the initial state
    cov = numpy.diag([gps_cov, gps_cov, gps_cov, gps_cov / util.speedOfLight])
    init_pdf = pybayes.pdfs.GaussPdf(mean, cov)

    p_xt_xtp = pybayes.pdfs.GaussCPdf(4, 4, p_xt_xtp_mu, p_xt_xtp_R)
    p_yt_xt = pybayes.pdfs.GaussCPdf(4, 4, p_yt_xt_mu, p_yt_xt_R)

    filt = pybayes.filters.ParticleFilter(n, init_pdf, p_xt_xtp, p_yt_xt)


def do_filter(info):
    if filt is None:
        build_filter(info)

    p = info.receiver_position
    filt.bayes(numpy.array([p.X, p.Y, p.Z, 0]))
    info.filtered_position = filt.posterior().mean()


# ---
pylab.figure()
pylab.ion()
pylab.show()
pylab.hold(False)
d = []
i = None
while True:
    msg = dev.receive_message(ignore_eof=opts.follow)
    if msg is None:
        break

    try:
        name = msg.name()
    except ublox.UBloxError as e:
        continue

    msg.unpack()
    satinfo.add_message(msg)

    # TODO: Fix this code block.
    """
    satinfo.filtered_position isn't declared for the instantiation of that class (SatelliteData)
      There are other positions, which are of class util.PosVector - which also has a custom __add__ method
      This __add__ method requires another PosVector with X, Y, and Z components, so there is potential that
        the list i should be a PosVector instead, and we use another position from satinfo.
    """
    if name == 'NAV_POSECEF':
        if i is None:
            i = [msg.ecefX * 0.01, msg.ecefY * 0.01, msg.ecefZ * 0.01, 0]
        do_filter(satinfo)
        d.append(satinfo.filtered_position - i)
        pylab.plot(d)
        pylab.draw()
