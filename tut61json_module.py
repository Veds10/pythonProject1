# java script object notation

# Json.load() kisi bhi file object ko as an argument leta hai jabki json.loads kisi bhi string ko as an argument leta hai..
# sort_keys parameter data k key: value pairs ko sort krne ke kam ata hai

import json

data='{"var1":"harry","var2":"65"}'
# print(data) # it will print the whole elements

parsed=json.loads(data)
print(parsed["var1"]) # it will print the specific values of keys eg like dictonary  it will give you the value for the key we searched

 #u can direct print as data to get elements but diffe betw them is they cant print specific values of  keys

# data2= {
#      "1":"one",
#      "colours":["pink","blue","white"],
#      "cars":("bmw","audi"),
#      "isbad":False
#  }
#
# comp=json.dumps(data2) # jasondumps is use to convert py code into javascript code
# print(comp)


# 1-Jason.load :- Ye ek json file (javascript) file kay documents ko  read karta hai or usko python may convert karta hai .
# 2- sort key parameters in dumps:-
# Ye ek True or False parameters leta hai or
# If we gives parameters True:
#         Answer will be in alphabetical           order.
# If we gives parameters as False:
#            Answer will be in as it is form.
