class Dad:
    Basketball=1

class Son(Dad):
    dance=1
    Basketball=9
    def isdance(self): #its nothing but the method/function
        return f"yes i dance {self.dance} no of times"

class Grandson(Son):
    dance=6

    def isdance(self):
        return f"yes i dance on dfferent level {self.dance} no of times"
# whatever we give method to find it will 1st find it in self func if its not then 2nd and then 3rd it will go from down to up

farry=Dad()
larry=Son()
harry=Grandson()

print(harry.Basketball)
print(larry.isdance())



