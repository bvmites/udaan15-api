__author__ = 'alay'

from app.basehandler import BaseHandler
from app.asynchandledoc import AsyncHandleDoc


class NonTechHandler(BaseHandler):
    def get(self, *args, **kwargs):
        slugs = str(self.request.uri).lstrip('/').rstrip('/').split('/')
        slugs.remove('api')
        slugs.remove('nontech')
        number_of_slugs = slugs.__len__()
        if number_of_slugs == 1:
            if 'all' in slugs:
                db = AsyncHandleDoc('non-tech')
                db.get_query()
                yield db.run_query()
                self.message = list()
                if db.length() == 0:
                    self.send_error(404)
                else:
                    for doc in db.doc:
                        del doc['value']['_id']
                        del doc['value']['_rev']
                        self.message.append(doc['value'])
                    self.send_error(200)
            else:
                query_dict = dict(name=slugs[0])
                db = AsyncHandleDoc('non-tech', query_dict)
                db.get_query()
                yield db.run_query()
                db.get_data()
                if db.length() == 0:
                    self.send_error(404)
                else:
                    self.message = db.doc[0]['value']
                    self.send_error(200)
        else:
            self.send_error(400)