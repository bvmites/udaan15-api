__author__ = 'alay'


from src import registration
from src.basehandler import BaseHandler
from src.test import TestHandler
from src.tech import TechHandler
from src.nontech import NonTechHandler
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


serverIP = "172.31.39.221"


app = Application(handlers=[
    (r'/api/registration/events', registration.EventsRegistrationHandler),
    (r'/api/tech(.*)', TechHandler),
    (r'/api/nontech(.*)', NonTechHandler),
    (r'/api/test', TestHandler),
])

server = HTTPServer(app)
server.listen(8000, address=serverIP)
ioLoop = IOLoop.instance().start()
