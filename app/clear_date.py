__author__ = 'alay'

import couch

localhost = "http://admin:admin@127.0.0.1:5984/"
db_name = 'tech_'

map_function = dict(map="function(doc){emit(doc.name, doc.manager)}")

client = couch.BlockingCouch(db_name, 'http://admin:admin@127.0.0.1:5984/')
docs = client.temp_view(map_function)
docs = docs['rows']
