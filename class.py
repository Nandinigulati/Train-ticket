class programmer:
    company="microsoft"

    def __init__(self,name,product):
        self.name =name
        self.product=product
    
    def getInfo(self):
        print(f"the name of the programmer is {self.name} and the product is {self.product}")
         
n=programmer("nandini","skype")
h=programmer("harry","html")
n.getInfo()
h.getInfo()



