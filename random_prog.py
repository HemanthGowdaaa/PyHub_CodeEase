a=[]
import random
for i in range(5):
    a.append(random.randint(1,1000000))
print(a)
a.sort()
print(a)
random.shuffle(a)
print(a)
toss=["heads","tails"]

print(random.choice(toss))
