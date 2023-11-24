fp=open("demo.txt",mode="r")
chars=0
lines=0
words=0
for l in fp:
    lines+=1
    l=l.strip("\n")
    chars+=len(l)
    lst=l.split()
    words+=len(lst)
fp.close()
print("Number of lines: ",lines)
print("Number of words: ",words)
print("Number of characters: ",chars)
