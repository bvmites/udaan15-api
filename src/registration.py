__author__ = 'alay'

from src.basehandler import BaseHandler
import os.path


class EventsRegistrationHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render(self.root + '/templates/events_registration.html')

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name')
            department = self.get_argument('department')
            event_type = self.get_argument('type')
            description = self.get_argument('description')
            time = self.get_argument('time')
            prize = self.get_argument('prize')
            manager1 = [self.get_argument('manager1-name'), self.get_argument('manager1-phone'), self.get_argument('manager1-email')]
            manager2 = [self.get_argument('manager2-name'), self.get_argument('manager2-phone'), self.get_argument('manager2-email')]
            manager3 = [self.get_argument('manager3-name'), self.get_argument('manager3-phone'), self.get_argument('manager3-email')]
            manager4 = [self.get_argument('manager4-name'), self.get_argument('manager4-phone'), self.get_argument('manager4-email')]
            fees = self.get_argument('fees')
            participants = self.get_argument('participants')
            print(name, department, event_type, description, time, prize, fees, manager1, manager2, manager3, manager4)
            self.send_error(200)
        except Exception as error:
            self.send_error(400)

