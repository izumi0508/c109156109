inpu = input("輸入一字元為:")
mid = len(inpu)//2
i=0
while True:
    if i > mid :
        print("YES")
        break
    a = inpu[mid-i-1:mid-i]
    b = inpu[mid+i+1:mid+i+2]
    if a == b:
        i += 1
    else:
        print("NO")
        break
