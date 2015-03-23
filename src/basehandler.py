__author__ = 'alay'

from tornado.web import RequestHandler
from os.path import dirname
import traceback
import json
import pickle


def getTimestamp():
    try:
        with open("timestamp.pickle", "rb") as timestamp:
            return pickle.load(timestamp)
    except IOError as error:
        return None

class BaseHandler(RequestHandler):

    timestamp = None
    root = dirname(__file__).rstrip('/src')
    localhost = 'http://admin:admin@127.0.0.1:5984/'

    def initialize(self):
        self.message = ''

    def write_error(self, status_code, **kwargs):
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header('Content-Type', 'application/json')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        else:
            if self.message == '':
                self.message = self._reason
            response = dict()
            response['status'] = str(status_code)
            response['message'] = self.message
            self.set_header('Content-Type', 'application/json')
            self.finish(json.dumps(response))