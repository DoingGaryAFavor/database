import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('PUT', '/1/roles/TcF4HNVUpM', json.dumps({
       "users": {
         "__op": "AddRelation",
         "objects": [
            {
             "__type": "Pointer",
             "className": "_User",
             "objectId": "FEmYz6cXSa"
            }
         ]
       }
     }), {
       "X-Parse-Application-Id": "aOa7pfDy6GLtckl4cYBEMCnkBW9NyDLZ7ta4FVoI",
       "X-Parse-Master-Key": "opsRRqIsbUBYWUWyaGXYmvCJnezmnnSPbPMUBNV8",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result