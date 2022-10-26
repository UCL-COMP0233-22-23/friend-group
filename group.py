import json

mydata = {'key': ['value1', 'value2'], 
          'key2': {'key4':'value3'}}

json.dumps(mydata)
with open('mylife.json', 'r') as json_file:
    my_data_as_string = json_file.read()
mydata = json.loads(my_data_as_string)
mydata['somekey']
print(json.dumps(mydata, indent=4))



