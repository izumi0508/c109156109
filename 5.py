inpu = int(input("請輸入階層值:"))
i = 1
ans = 1

while inpu >= ans:
    ans *= i
    i += 1

print("超過M為:"+str(inpu)+"的最小階層N值為:"+str(i-1))