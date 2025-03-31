str1="rama"
str2="sita"
str3="ravana"
str4="rama"
str5="rama"
str6="sita"
str7="ravana"
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))
print(id(str7))

print(ord("a"))
print(chr(59))
print(chr(104))
# print("enter a input")
# s = input()
# ord = ord(s)
# print(ord)\

print(ord("A"))
s = input("input char : ")
# s="hgvnKH"
for i in s:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i, end="")
        
    else:
        print(ord(i))
        
        print(chr(ord(i) - 32), end="")

# print("enter a string ")
# str2= input()
# i = 0
# newstr1 = ""
# newstr2=""
# while(i < len(str2)):
#     data= str2[i]
#     if 65 <= ord(data) >= 90:
#         newstr1+=data
#     else:
#         newstr2 +=data
#     i+=1
# print(newstr1)
# print(newstr2)
        
















