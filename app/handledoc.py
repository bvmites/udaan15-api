__author__ = 'alay'

from couch import AsyncCouch
from couch import BlockingCouch
from tornado.gen import coroutine
from tornado.ioloop import IOLoop


class HandleDoc():

    def __init__(self, db_name, input_doc=None, url='http://admin:admin@127.0.0.1:5984/'):
        self.input_doc = input_doc
        self.url = url
        self.db_name = db_name
        self.client = BlockingCouch(self.db_name, self.url)
        self.query_string = ""
        self.doc = ''

    def get_query(self):
        self.query_string = 'function(doc)'
        if self.input_doc is None:
            self.query_string += '{'
        else:
            self.query_string += '{ if ('
            for key in self.input_doc:
                self.query_string = self.query_string + "doc." + key + " == '" + self.input_doc[key] + "'" + ' && '
            self.query_string = self.query_string[:-4]
            self.query_string += ') {'
        self.query_string += 'emit(null, doc); }'
        if self.input_doc is not None:
            self.query_string += '}'

    def run_query(self):
        view = dict(map=self.query_string, reduce=None)
        try:
            self.doc = self.client.temp_view(view)['rows']
        except Exception as error:
            print(str(error))
            self.doc = None

    def get_view(self, doc_name, view_name):
        self.doc = self.client.view(doc_name, view_name)['rows']

    def get_data(self):
        for doc in self.doc:
            del doc['id']
            del doc['value']['_id']
            del doc['value']['_rev']

    def length(self):
        return self.doc.__len__()

