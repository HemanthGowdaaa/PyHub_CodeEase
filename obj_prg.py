class demo:
    def __init__(myself):
        myself.a=10
        myself.b=20
        print(myself.a)
       
     
    def disp(myself):
        print(myself.a)
        print(myself.b)
        
d1 = demo()
print(d1.a)
print(d1.b)
print(d1)
d2=d1
print(d2)
print(id(d1))
print(id(d2))
d1.disp()
print(d1 is d2)
