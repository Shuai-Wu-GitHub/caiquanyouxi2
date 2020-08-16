import random
A = random.randint(1,3)
B = random.randint(1,3)
print(A,B)
if A == 1 and B==1:
    print("石头平局")
elif A == 1 and B == 2:
    print("石头VS剪刀，石头胜")
elif A == 1 and B == 3:
    print("石头VS布，布胜")
elif A == 2 and B == 2:
    print("剪刀平局")
elif A == 2 and B == 1:
    print("剪刀VS石头，石头胜")
elif A == 2 and B == 3:
    print("剪刀VS布，布胜")
elif A == 3 and B == 3:
    print("布VS布，平局")
elif A == 3 and B == 1:
    print("布VS石头，石头胜")
elif A == 3 and B == 2:
    print("布VS剪刀，剪刀胜")
