__author__ = 'alay'


from app import registration
from app.basehandler import BaseHandler
from app.test import TestHandler
from app.tech import TechHandler
from app.nontech import NonTechHandler
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.web import StaticFileHandler

# serverIP = "172.31.39.221"
serverIP = "127.0.0.1"


app = Application(handlers=[
    (r'/api/registration/events', registration.EventsRegistrationHandler),
    (r'/api/tech(.*)', TechHandler),
    (r'/api/nontech(.*)', NonTechHandler),
    (r'/api/test', TestHandler)
])

server = HTTPServer(app)
server.listen(8000, address=serverIP)
ioLoop = IOLoop.instance().start()
