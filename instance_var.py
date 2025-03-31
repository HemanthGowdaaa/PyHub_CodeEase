class demo:
    def __init__(self):
        self.a =10
        self.b=20
        
    def disp(self):
        print(self.a)
        print(self.b)
        self.c=30
        self.d=40
        print(self.e)
     
d1 = demo()
print(d1.a)
print(d1.b)

d1.e=50
d1.f = 60
# print(d1.e)

d1.disp()



# a=10
# b=10
# c=10
# print(id(a))
# print(id(b))
# print(type(a))
# print(id(a))
# print(id(b))
# print(id(c))
# d=20
# e=20
# f=20
# print(d)
# print(e)
# print(f)
# print(id(d))
# print(id(e))
# print(id(f))
# print(a is d)
# print(e is f)
# print(c is f)
# print(a,"\n",b,"\n",c,"\n",d)
# print(a,b,c,d)
