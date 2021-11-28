import json

# from python to json

pdata = {
  "ii" : 1,
  "ss" : "str",
  "obj" : {
    "f1" : "field1",
    "f2" : "filed2",
  },
  "arrs": ["a", "b", "c"]
}

jdata = json.dumps(pdata)
print(type(pdata))
print(type(jdata))
print(jdata)

jdata2 = '''{
  "a" : "av",
  "b" : "bv"
}'''

pdata2 = json.loads(jdata2)
print(type(jdata2))
print(type(pdata2))
print(pdata2)


pdata3 = json.load(open("data.json"))
print(pdata3)