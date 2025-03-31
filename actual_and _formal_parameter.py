class demo:
    def swap(self, x,y):
        temp = x
        x=y
        y=temp
        return x,y
d = demo()
a = 10
b=20 
print(a)
print(b)
a,b=d.swap(a,b)
print("after swaping")
print(a)
print(b)