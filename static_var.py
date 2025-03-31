class farmer:
    r=2.5
    def __init__(self,p,t):
        self.p=p
        self.t=t
    def kisan_schema(self):
        intrest=(self.p*self.t*farmer.r)/100
        print(intrest)

hemanth = farmer(10000,2)
adithya = farmer(15000,3)
bharath = farmer(30000,4)

hemanth.kisan_schema()
adithya.kisan_schema()
bharath.kisan_schema()

print(f"the interst is : {farmer.r}")
