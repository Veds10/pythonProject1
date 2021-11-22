
"""
f=open("ved.txt","w")  #write
f.write("you are too good")
f.close()

f=open("ved.txt","a")
a=f.write("you are too good \n") # append
print(a) #f.write returns no of char
f.close()

"""
# handle read and write both(where read will display on screen and write will add whatever you want in txt file

f=open("ved.txt","r+")
print(f.read())
f.write("hello everyone")
f.close()






