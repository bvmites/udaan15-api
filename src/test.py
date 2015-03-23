__author__ = 'alay'

from src.basehandler import BaseHandler

class TestHandler(BaseHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument('name')
        print(name)
        print(str(self.request))
        self.message = name

        self.send_error(200)

    def post(self, *args, **kwargs):
        test = self.get_argument('name')
        self.write('name = ' + test)