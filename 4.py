X = int(input("X軸座標:"))
Y = int(input("Y軸座標:"))

if X == 0 & Y == 0:
    print("該點位於原點")
elif (X == 0) & (Y > 0):
    print("該點位於上半平面Y軸上，離原點距離為根號"+str(Y*Y))
elif (X == 0) & (Y < 0):
    print("該點位於下半平面Y軸上，離原點距離為根號"+str(Y*Y))
elif (X < 0) & (Y == 0):
    print("該點位於左半平面X軸上，離原點距離為根號"+str(X*X))
elif (X > 0) & (Y == 0):
    print("該點位於右半平面X軸上，離原點距離為根號"+str(X*X))
elif (X > 0) & (Y > 0):
    print("該點位於第一象限，離原點距離為根號"+str(X*X+Y*Y))
elif (X > 0) & (Y < 0):
    print("該點位於第二象限，離原點距離為根號"+str(X*X+Y*Y))
elif (X < 0) & (Y < 0):
    print("該點位於第三象限，離原點距離為根號"+str(X*X+Y*Y))
elif (X < 0) & (Y < 0):
    print("該點位於第四象限，離原點距離為根號"+str(X*X+Y*Y))