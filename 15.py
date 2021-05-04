inpu = input("輸入一組四位數字為:")
a = (int(inpu[0])+7)%10
b = (int(inpu[1])+7)%10
c = (int(inpu[2])+7)%10
d = (int(inpu[3])+7)%10
e = a
a = c 
c = e
e = b
b = d
d = e
print("輸出加密後的數字為:"+str(a)+str(b)+str(c)+str(d))