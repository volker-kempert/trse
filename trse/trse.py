# -*- coding: utf-8 -*-

"""Main module."""
import sys
import logging

logger = logging.getLogger('trse_service')
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from twisted.internet import reactor
from restful import prepare_serving_wsgi
from ser import serial_init

def hello():
    logger.info('Hello from the reactor loop!')


class Countdown(object):

    counter = 5

    def __init__(self, rate=1):
        self._rate = rate

    def count(self):
        if self.counter == 0:
            # reactor.stop()
            pass
        else:
            logger.info( '..{}'.format(self.counter) )
            self.counter -= self._rate
            reactor.callLater(1, self.count)



def main():


    reactor.callWhenRunning(hello)
    reactor.callWhenRunning(Countdown().count)

    reactor_args = {}
    reactor_args = prepare_serving_wsgi()
    serial_init()
    reactor.run(**reactor_args)


if __name__ == "__main__":
    logger.info('Starting main')
    sys.exit(main())  # pragma: no cover
