__author__ = 'alay'

from couch import AsyncCouch
from tornado.gen import coroutine
from tornado.gen import Future


class AsyncHandleDoc():

    def __init__(self, db_name, input_doc=None, url='http://admin:admin@127.0.0.1:5984/'):
        self.input_doc = input_doc
        self.url = url
        self.db_name = db_name
        self.client = AsyncCouch(self.db_name, self.url)
        self.query_string = ""
        self.doc = Future
        self.func_name = ''
        self.view_doc_name = ''
        self.view_name = ''

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

    @coroutine
    def run_query(self):
        view = dict(map=self.query_string, reduce=None)
        try:
            self.doc = yield self.client.temp_view(view)
            self.doc = self.doc['rows']
        except Exception as error:
            print(str(error))

    @coroutine
    def get_view(self, doc_name, view_name):
        self.doc = yield self.client.view(doc_name, view_name)
        self.doc = self.doc['rows']

    def get_data(self):
        for doc in self.doc:
            del doc['id']
            del doc['value']['_id']
            del doc['value']['_rev']

    def length(self):
        return self.doc.__len__()

    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    a = AsyncHandleDoc("departments")
    a.run_get_view('get_departments', 'Drawer')
    print(a.doc)
