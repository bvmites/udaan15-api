__author__ = 'alay'

from src.basehandler import BaseHandler
import os.path
import couch

class EventsRegistrationHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render(self.root + '/templates/form.html')

    def post(self, *args, **kwargs):
        try:
            data = dict()
            data['name'] = self.get_argument('name')
            data['department'] = self.get_argument('department')
            data['description'] = self.get_argument('description')
            data['prize'] = self.get_argument('prize')
            manager1 = dict(name=self.get_argument('manager1-name'), number=self.get_argument('manager1-phone'), email=self.get_argument('manager1-email'))
            manager2 = dict(name=self.get_argument('manager2-name'), number=self.get_argument('manager2-phone'), email=self.get_argument('manager2-email'))
            manager3 = dict(name=self.get_argument('manager3-name'), number=self.get_argument('manager3-phone'), email=self.get_argument('manager3-email'))
            manager4 = dict(name=self.get_argument('manager4-name'), number=self.get_argument('manager4-phone'), email=self.get_argument('manager4-email'))
            data['manager'] = [manager1, manager2, manager3, manager4]
            data['fees'] = self.get_argument('fees')
            data['numberOfParticipants'] = self.get_argument('participants')
            str(data['name']).replace(' ', '-')
            if self.get_argument('type') is 'Tech':
                db_name = 'tech'
            else:
                db_name = 'non-tech'
            db = couch.BlockingCouch(db_name, "http://admin:admin@127.0.0.1:5984")
            db.save_doc(data)
            self.send_error(200)
        except Exception as error:
            print(error)
            self.send_error(400)

