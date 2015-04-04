__author__ = 'alay'


from app import registration
from app.test import TestHandler
from app.tech import TechHandler
from app.basehandler import BaseHandler
from app.nontech import NonTechHandler
from app.cultural import CulturalHandler
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import StaticFileHandler

# serverIP = "172.31.40.214"
serverIP = "192.168.1.3"

app = Application(handlers=[
    (r'/api/registration/events', registration.EventsRegistrationHandler),
    (r'/api/tech(.*)', TechHandler),
    (r'/api/cultural/all', CulturalHandler),
    (r'/api/nontech(.*)', NonTechHandler),
    (r'/api/schedule/(.*)', StaticFileHandler, dict(path=BaseHandler.root + '/public')),
    (r'/api/test', TestHandler)
])

server = HTTPServer(app)
server.listen(8000, address=serverIP)
ioLoop = IOLoop.instance().start()
