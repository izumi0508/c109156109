inpu = input("輸入月及日為:")

if inpu[0:1] == "12":
    if int(inpu[3:])>21 :
        print("Capricorn")
    else:
        print("Sagittarius")
elif inpu[:2] == "01":
    if int(inpu[3:])>20 :
        print("Aquarius")
    else:
        print("Capricorn")
elif inpu[:2] == "02":
    if int(inpu[3:])>18 :
        print("Pisces")
    else:
         print("Aquarius")
elif inpu[:2] == "03":
    if int(inpu[3:])>20 :
        print("Aries")
    else:
        print("Pisces")
elif inpu[:2] == "04":
    if int(inpu[3:])>20 :
        print("Taurus")
    else:
        print("Aries")
elif inpu[:2] == "05":
    if int(inpu[3:])>21 :
        print("Gemini")
    else:
        print("Taurus")
elif inpu[:2] == "06":
    if int(inpu[3:])>21 :
        print("Cancer")
    else:
        print("Gemini")
elif inpu[:2] == "07":
    if int(inpu[3:])>22 :
        print("Leo")
    else:
        print("Cancer")
elif inpu[:2] == "08":
    if int(inpu[3:])>23 :
        print("Virgo")
    else:
        print("Leo")
elif inpu[:2] == "09":
    if int(inpu[3:])>23 :
        print("Libra")
    else:
        print("Virgo")
elif inpu[:2] == "10":
    if int(inpu[3:])>23 :
        print("Scorpio")
    else:
        print("Libra")
elif inpu[:2] == "11":
    if int(inpu[3:])>22 :
        print("Sagittarius")
    else:
        print("Scorpio")