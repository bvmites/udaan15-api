__author__ = 'alay'

import couch
import uuid

LOCALHOST = "http://admin:admin@127.0.0.1:5984/"

db = couch.BlockingCouch(db_name="departments", couch_url=LOCALHOST)
docs = db.view('get_departments', 'Drawer')
docs = docs['rows']

# for doc in docs:
#     doc = dict(doc)
#     doc.pop('id')
#     print(doc)

a = [doc.pop('id') for doc in docs]

db = couch.BlockingCouch(db_name="tech", couch_url=LOCALHOST)


for doc in docs:
    new_doc = dict()
    new_doc['department'] = doc['value']
    new_doc['name'] = uuid.uuid4().hex[0:6]
    new_doc['description'] = uuid.uuid4().hex
    new_doc['managers'] = list()
    for i in range(0,4):
        new_doc['managers'].append(uuid.uuid4().hex[0:8])
    new_doc['fee'] = str(uuid.uuid4().int)[0:2]
    new_doc['prize'] = str(uuid.uuid4().int)[0:2]
    new_doc['numberOfParticipants'] = str(uuid.uuid4().int)[0:1]
    db.save_doc(new_doc)