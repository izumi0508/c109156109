num = int(input("測試的資料量:"))
inpu = []
index = 0
for i in range(num):
    blood = input()
    inpu.append(blood[:blood.find(' ')])
    print(blood[:blood.find(' ')])
    trans = blood[blood.find(' ')+1:]
    inpu.append(trans[:trans.find(' ')])
    print(trans[:trans.find(' ')])    
    blood = trans[trans.find(' ')+1:] 
    inpu.append(blood)
    print(blood)

for i in range(num):
    dad = inpu[index]
    index +=1
    mom = inpu[index]
    index += 1
    kid = inpu[index]
    index += 1
    if (dad == "O")&(mom == "O"):
        if kid == "O" :
            print("YES")
        else :
            print("IMPOSSIBLE")
    elif (dad == "A")&(mom == "A"):
        if (kid == "O") | (kid == "A"):
            print("YES")
        else :
            print("IMPOSSIBLE")
    elif (dad == "B")&(mom == "B"):
        if (kid == "O") | (kid == "B"):
            print("YES")
        else :
            print("IMPOSSIBLE")
    elif (dad == "AB")&(mom == "AB"):
        if kid == "O":
            print("IMPOSSIBLE")
        else :
            print("YES")
    elif dad == "O":
        if mom == "A":
            if (kid == "O")|(kid == "A"):
                print("YES")
            else :
                print("IMPOSSIBLE")
        elif mom == "B":
            if (kid == "O")|(kid == "B"):
                print("YES")
            else :
                print("IMPOSSIBLE")
        elif mom == "AB":
            if (kid == "A")|(kid == "B"):
                print("YES")
            else :
                print("IMPOSSIBLE")
    elif mom == "O":
        if dad == "A":
            if (kid == "O")|(kid == "A"):
                print("YES")
            else :
                print("IMPOSSIBLE")
        elif dad == "B":
            if (kid == "O")|(kid == "B"):
                print("YES")
            else :
                print("IMPOSSIBLE")
        elif dad == "AB":
            if (kid == "A")|(kid == "B"):
                print("YES")
            else :
                print("IMPOSSIBLE")
    elif dad == "A":
        if mom == "B":
                print("YES")
        elif mom == "AB":
            if kid == "O":
                print("IMPOSSIBLE")
            else :
                print("YES")
    elif mom == "A":
        if dad == "B":
                print("YES")
        elif dad == "AB":
            if kid == "O":
                print("IMPOSSIBLE")
            else :
                print("YES")    
    elif dad == "B":
        if mom == "AB":
            if kid == "O":
                print("IMPOSSIBLE")
            else :
                print("YES")
    elif mom == "B":
        if dad == "AB":
            if kid == "O":
                print("IMPOSSIBLE")
            else :
                print("YES")
