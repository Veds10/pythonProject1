f=open("ved.txt")
#print(f.tell()) # f.tell tells us where is the pointer
print(f.readline(),end="") #compulsary print for read fun
#print(f.tell())
f.seek(50) #it starts to read from that given no
print(f.readline(),end="")
#print(f.tell())
print(f.readline())
#print(f.tell())
print(f.readline())
#print(f.tell())
f.close()

# readline reads individual one one line
# and readlines read all the lines