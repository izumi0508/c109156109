a = int(input())
b = int(input())
c = int(input())
if a == 0:
    print("0")
elif b*b-4*a*c < 0:
    print("0")
else:
    ans1 = ((b*(-1))+(b*b-(4*a*c))**0.5)/(2*a)
    ans2 = ((b*(-1))-(b*b-(4*a*c))**0.5)/(2*a)
    if ans1 == ans2:
        print(str(ans1))
    else:
        print(str(ans1))
        print(str(ans2))