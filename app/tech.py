__author__ = 'alay'


from app.basehandler import BaseHandler
from app.handledoc import HandleDoc


class TechHandler(BaseHandler):
    def get(self, *args, **kwargs):
        slugs = str(self.request.uri).lstrip('/').rstrip('/').split('/')
        slugs.remove('api')
        slugs.remove('tech')
        number_of_slugs = slugs.__len__()
        if number_of_slugs == 0:
            self.send_error(400)
        elif number_of_slugs == 1:
            if "departments" in slugs:
                db = HandleDoc('departments')
                db.get_view('get_departments', 'Drawer')
                for item in db.doc:
                    del  item['id']
                    item['alias'] = item['value']
                    item['name'] = item['key']
                    del item['key']
                    del item['value']
                self.message = db.doc
                self.send_error(200)
            elif "all" in slugs:
                db = HandleDoc('tech')
                db.get_query()
                db.run_query()
                db.get_data()
                self.message = db.doc
                self.send_error(200)
            else:
                query_dict = dict(department=slugs.pop())
                db = HandleDoc('tech', query_dict)
                db.get_query()
                db.run_query()
                db.get_data()
                if db.length() == 0:
                    self.send_error(404)
                else:
                    self.message = list()
                    for doc in db.doc:
                        self.message.append(doc['value']['name'])
                    self.send_error(200)
        elif number_of_slugs == 2:
            query_dict = dict(department=slugs[0], name=slugs[1])
            db = HandleDoc('tech', query_dict)
            db.get_query()
            db.run_query()
            db.get_data()
            if db.length() == 0:
                self.send_error(404)
            else:
                self.message = db.doc[0]['value']
                self.send_error(200)
        else:
            self.send_error(400)