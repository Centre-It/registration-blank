#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from web import app
from werkzeug.contrib.fixers import LighttpdCGIRootFix


if __name__ == '__main__':
    app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
    WSGIServer(app).run()