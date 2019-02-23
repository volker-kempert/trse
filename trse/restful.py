# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api

import logging
logger = logging.getLogger('trse_rest')
logger.setLevel(logging.DEBUG)


app = Flask(__name__)
api = Api(app)

serial_lines = {}

class SerialLine(Resource):
    def put(self, sl_id):
        logger.info('Put Serial')
        serial_lines[sl_id] = request.form['data']
        return { sl_id: serial_lines[sl_id] }

api.add_resource(SerialLine, '/serial/<int:sl_id>')

class SerialLines(Resource):
    def get(self):
        logger.info('Get Serial Lines:')
        return serial_lines

api.add_resource(SerialLines, '/serials')


##############################################################################
from twisted.internet import reactor


def prepare_serving_wsgi():
    reactor_args = {}

    def run_twisted_wsgi():
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = Site(resource)
        reactor.listenTCP(5000, site)

    if app.debug:
        # Disable twisted signal handlers in development only.
        reactor_args['installSignalHandlers'] = 0
        # Turn on auto reload.
        import werkzeug.serving
        run_twisted_wsgi = werkzeug.serving.run_with_reloader(run_twisted_wsgi)

    logger.info("start wsgi")
    run_twisted_wsgi()
    return reactor_args


if __name__ == '__main__':
    # app.run(debug=True)  ## the classical way
    reactor_args = prepare_serving_wsgi()
    reactor.run(**reactor_args)


