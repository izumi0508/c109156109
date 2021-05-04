inpu = int(input("輸入一正整數:"))
if (inpu % 11 == 0)&(inpu % 2 == 0)&(inpu % 5 != 0)&(inpu % 7 != 0):
    print(str(inpu)+"為新公倍數?:Yes")
else:
    print(str(inpu)+"為新公倍數?:No")