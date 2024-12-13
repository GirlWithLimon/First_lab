#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import random
import sys
A=int(sys.stdin.readline())
B=random.randint(-10,10)
if B==0:
    print("Error, B=0")
else:
    C=A/B
    print (C)
with open ("logs.txt","a") as file:
    file.write("calc_ratio (2):\n")
    if B == 0:
        file.write("ERROR! B=0\n\n")
    else:
        file.write("B=" + str(B) + "\n\n")
        file.write("A/B=C="+str(A/B)+"\n")
