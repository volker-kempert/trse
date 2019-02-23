# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('trse_serial')
logger.setLevel(logging.DEBUG)

from twisted.protocols.basic import LineReceiver
from twisted.protocols.basic import LineReceiver

from twisted.internet import reactor
from twisted.internet.serialport import SerialPort


class EchoProtocol(LineReceiver):
    """Wait for specific amount of data.
       Regardless of success, closes connection timeout seconds after opening.
    """
    def __init__(self, port, timeout):
        self._timeout = timeout

    def dataReceived(self, data):
        # write all the data twice char by char :-)
        # TODO use other methods of line receiver
        # TODO inject output channel
        logger.info('Data received: ' + repr(data))
        self.transport.write(data)
        self.transport.write(data)
        self.transport.flushOutput()

    def connectionMade(self):
        logger.info('Connection made.')
        reactor.callLater(self._timeout, self.transport.loseConnection, 'timeout')

    def connectionLost(self, reason):
        logger.info('Connection lost. ' + str(reason))


def serial_init(port='/dev/ttyUSB0', baudrate=115200):
    logging.debug('About to open port {0}'.format(port))
    s = SerialPort(EchoProtocol(port,1000), port, reactor, baudrate=baudrate)
    s.write('\r\nHello ...\r\n'.encode('utf8'))
