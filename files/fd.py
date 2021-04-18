f=open("sample","r")
for lines in f:
    words=lines.rstrip("\n").split(" ")
    print(words)