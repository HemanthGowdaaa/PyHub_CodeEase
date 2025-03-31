class student:
    def __init__(self,sname,sage,susn,sadd):
        self.name=sname
        self.age = sage
        self.usn = susn
        self.add = sadd
        print(self.name,self.age,self.usn,self.add)
        
s1 = student("hima",22,"1ew21cs060","bengaluru")
s2 = student("adi",17,"1ew21cs007","kengeri")
print(s1.name)
print(s1.usn)
print(s1.age)
print(s1.add)