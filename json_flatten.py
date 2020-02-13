import json
string = ""
def flatten_json(nested_json):
    out = {} 
  
    def flatten(x, name =''): 
        if type(x) is dict: 
            for a in x: 
                flatten(x[a], name + a + '_') 
        else: 
            out[name[:-1]] = x 
    flatten(nested_json)  
    return out
#from json_flatten import flatten
for _ in range(int(input())):
    obj = input()
    data =json.loads(obj)
    flat_data=flatten_json(data)
    final = json.dumps(flat_data)
    print(final)
    #print(flatten_json(obj))
