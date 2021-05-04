inpu = int(input())
if inpu <= 120:
    summer = inpu*2.10
    nonsummer = inpu*2.10
    print("Summer months:"+str(summer))
    print("Non-Summer months:"+str(nonsummer))
elif inpu <= 330:
    summer = 120*2.10+(inpu-120)*3.02
    nonsummer = 120*2.10+(inpu-120)*2.68
    print("Summer months:"+str(summer))
    print("Non-Summer months:"+str(nonsummer))
elif inpu <= 500:
    summer = 120*2.10+210*3.02+(inpu-330)*4.39
    nonsummer = 120*2.10+210*2.68+(inpu-330)*3.61
    print("Summer months:"+str(summer))
    print("Non-Summer months:"+str(nonsummer))
elif inpu <= 700:
    summer = 120*2.10+210*3.02+170*4.39+(inpu-500)*4.97
    nonsummer = 120*2.10+210*2.68+170*3.61+(inpu-500)*4.01
    print("Summer months:"+str(summer))
    print("Non-Summer months:"+str(nonsummer))
else:
    summer = 120*2.10+210*3.02+170*4.39+200*4.97+(inpu-700)*5.63
    nonsummer = 120*2.10+210*2.68+170*3.61+200*4.01+(inpu-700)*4.50
    print("Summer months:"+str(summer))
    print("Non-Summer months:"+str(nonsummer))
