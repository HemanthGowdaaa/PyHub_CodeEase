class demo:
    def disp(self,x=11,y=22,z=33):
        print(x)
        print(y)
        print(z)
        print()

        
d = demo()
a=10
b=20
c=30
d.disp(a,b)
d.disp(a,b,c)
d.disp()
d.disp(a)
d.disp(b)
d.disp(c)
d.disp(z=c)
d.disp(y=b)
d.disp(x=a)