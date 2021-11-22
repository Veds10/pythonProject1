#strings slicing
"""
mystr = "happy birthday to you"
print(mystr[0]) # it will give single letter

mystr = "happy birthday to you"
print(mystr[0:21]) # it will cut word that you want

print(len(mystr))

print(mystr[0:21:2]) #it will skip the char
"""

#functions

mystr = "happybirthdaytoyou"
print(mystr.isalnum())

mystr = "happy birthday to you"
print(mystr.isalnum())

print(mystr.endswith("ou"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("you","i"))
print(mystr.find("birthday"))
print(mystr.lower())
print(mystr.upper())


