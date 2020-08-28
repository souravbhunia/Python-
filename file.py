with open("kk.txt","r") as f:
        content=f.read()
        print("   ")
        print(content)
        print("  ")

fileptr=open("kk.txt","a") 
fileptr.write(" Python has an easy syntax and user-friendly interaction")
content=fileptr.readlines()
print(content)
for i in fileptr:
    print(i)
fileptr.close()