#!/usr/bin/env python
import os, sys
from gevent import monkey; monkey.patch_all()
from gevent import wsgi
from wsgi import application

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(BASE_DIR)
# set spawn=None for memcache
wsgi.WSGIServer((sys.argv[1], int(sys.argv[2])), application).serve_forever()
