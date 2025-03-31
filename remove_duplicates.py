words = "Rama is Rama is a good boy"
words=[i for i in words.split(" ")]
ans=""
for i in words:
    if i not in ans:
        if ans == "":
            ans+=i
        else:
            ans+=" "+i
print(ans)