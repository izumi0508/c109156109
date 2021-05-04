num = int(input())
data = []
for i in range(num):
    data.append(int(input()))
    data.append(int(input()))
    data.append(int(input()))
    data.append(int(input()))

for i in range(0,num*4,4):
    if data[i+1]/data[i] == data[i+2]/data[i+1]:
        if data[i+3]/data[i+2] == data[i+2]/data[i+1]:
            ans = data[i+3]*(data[i+1]/data[i])
            print(str(data[i])+" "+str(data[i+1])+" "+str(data[i+2])+" "+str(data[i+3])+" "+str(int(ans)))
            print("此為等比數列")
    elif data[i+1]-data[i] == data[i+2]-data[i+1]:
        if data[i+3]-data[i+2] == data[i+2]-data[i+1]:
            ans = data[i+3]+(data[i+1]-data[i])
            print(str(data[i])+" "+str(data[i+1])+" "+str(data[i+2])+" "+str(data[i+3])+" "+str(ans))
            print("此為等差數列")
