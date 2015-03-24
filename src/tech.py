__author__ = 'alay'


from src.basehandler import BaseHandler
from src.handledoc import HandleDoc


class TechHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        slugs = str(self.request.uri).lstrip('/').rstrip('/').split('/')
        slugs.remove('api')
        slugs.remove('tech')
        if str(slugs) == '[]':
            db = HandleDoc('departments')
            db.get_view('get_departments', 'Drawer')
            doc = db.doc["rows"]
            for item in doc:
                del item['id']
                item['alias'] = item['value']
                item['name'] = item['key']
                del item['key']
                del item['value']
            self.message = doc
            self.send_error(200)
        elif str(slugs) == "['all']":
            db = HandleDoc('tech')
            db.get_query()
            db.run_query()
            self.message = list()
            for doc in db.doc:
                del doc['value']['_id']
                del doc['value']['_rev']
                self.message.append(doc['value'])
            self.send_error(200)
        else:
            slugs = str(slugs).lstrip("['").rstrip("']")
            query_dict = dict(name=slugs)
            db = HandleDoc('tech', query_dict)
            db.get_query()
            db.run_query()
            if str(db.doc) == '[]':
                self.send_error(404)
            else:
                self.message = list()
                for doc in db.doc:
                    del doc['value']['_id']
                    del doc['value']['_rev']
                    self.message.append(doc['value'])
                self.send_error(200)