num = int(input())
mid = num//2
strr = ""
for i  in range(1,mid+1):
    strr = ""
    for x in range(mid-i+1):
        strr += " "
    for y in range(1,i+i):
        strr += "*"
    print(strr)

strr = ""
for i in range(num):
    strr += "*"
    
print(strr)

for i  in range(mid,0,-1):
    strr = ""
    for x in range(mid-i+1):
        strr += " "
    for y in range(1,i+i):
        strr += "*"
    print(strr)