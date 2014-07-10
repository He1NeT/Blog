#!/usr/bin/env python
import os,sys
 
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

DEBUG = True
BASE_SETTINGS = 'settings'

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", BASE_SETTINGS)
 
def main(host, port):
    tornado.options.parse_command_line()
    wsgi_app = tornado.wsgi.WSGIContainer(
         django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application([
        ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ],
        debug=DEBUG)
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(port, address=host) 
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == '__main__':
    if len(sys.argv)  > 1:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        main('127.0.0.1', 8002)