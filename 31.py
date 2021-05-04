data = []
chi = int(input("國文:"))
data.append(chi)
eng = int(input("英文:"))
data.append(eng)
mat = int(input("微積分:"))
data.append(mat)
spo = int(input("體育:"))
data.append(spo)
pro = int(input("程式設計:"))
data.append(pro)
print("平均分數:"+str(sum(data)/5))
ind = max(data)
scrach = data.index(ind)
if scrach == 0:
    print("最高分科目:國文"+str(max(data))+"分")
elif scrach == 1:
    print("最高分科目:英文"+str(max(data))+"分")
elif scrach == 2:
    print("最高分科目:微積分"+str(max(data))+"分")
elif scrach == 3:
    print("最高分科目:體育"+str(max(data))+"分")
elif scrach == 4:
    print("最高分科目:程式設計"+str(max(data))+"分")

ind = min(data)
scrach = data.index(ind)
if scrach == 0:
    print("最低分科目:國文"+str(min(data))+"分")
elif scrach == 1:
    print("最低分科目:英文"+str(min(data))+"分")
elif scrach == 2:
    print("最低分科目:微積分"+str(min(data))+"分")
elif scrach == 3:
    print("最低分科目:體育"+str(min(data))+"分")
elif scrach == 4:
    print("最低分科目:程式設計"+str(min(data))+"分")
