# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#This creates a web service located off 
# http://localhost/python-web/
#
# To shutdown the server you will need to
# restart the kernel

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
port = 9010

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

    

# <codecell>

main()

# <codecell>

