# class claculator:
#     def __init__(self):
#         self.x=10
#         self.y=20

#     def disp(self):
#             a=100
#             b=200
#             c=a+b
#             print(c)
#             return c

# c1 = claculator()
# print(claculator().x)
# print(c1.y)
# print(c1.disp())

# class claculator:
#     def __init__(self):
#         self.x=10
#         self.y=20
        
#     def disp(self,a,b):
#             c=a+b
#             return c

# c1 = claculator()
# print(claculator().x)
# print(c1.y)
# n1=10
# n2=20
# q=c1.disp(n1,n2)
# print(q)

class calculator:
    def __init__(self):
        self.a=10
        self.b=20
    def disp(self,x,y):
        z=x+y
        return z
c1 = calculator()
print(c1.a)
print(c1.b)
ref = c1.disp(100,200)
print(ref)