import pickle

#pickling a python object
# cars=["bmw","audi","maryti","nano"]
# file="mycar.pkl"
# fileobj= open(file,"wb") #wb=write binary mode
# pickle.dump(cars,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,"rb") # read binary mode
mycar=pickle.load(fileobj)
print(mycar)

# pickle.loads() = This function takes a byte string as argument.
# pickle.load() = This function takes a  file-like object as argument.
#
# This was the same analogy you can take from json.load() and json.loads()
