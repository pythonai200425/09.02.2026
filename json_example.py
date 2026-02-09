
import json

resp = '{"x": 1, "y": [1,2], "ok": true}'
dict1 = json.loads(resp)
print(dict1)
print(type(dict1))
st1 = json.dumps(dict1)
print(st1)
print(type(st1))