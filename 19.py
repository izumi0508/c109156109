i = int(input("組數為:"))
inpu = []
for x in range(i):
    inp = input("第"+str(x+1)+"組:")
    mid = inp.find(' ')
    ans = int(inp[:mid])*250 + int(inp[mid+1:])*175
    inpu.append(ans)

for y in range(i):
    print("第"+str(y+1)+"組應收費用:"+str(inpu[y]))