__author__ = 'alay'


from app.basehandler import BaseHandler
from app.asynchandledoc import AsyncHandleDoc
from tornado.gen import coroutine


class CulturalHandler(BaseHandler):

    @coroutine
    def get(self, *args, **kwargs):
        client = AsyncHandleDoc('cultural')
        client.get_query()
        yield client.run_query()
        client.get_data()
        self.message = list()
        for data in client.doc:
            self.message.append(data['value'])
        self.send_error(200)