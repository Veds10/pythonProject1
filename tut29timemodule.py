# import time # its nothing but the multithreading
from time import *

initial=time()

i=0
while(i<=45):
    print("namaste")
    sleep(1)
    i+=1

print(time()-initial)

initial2=time()
for k in range(45):
    print("hello everyone")

print(time()-initial2)

# localtime=asctime(time.localtime(time()))
print(localtime)

