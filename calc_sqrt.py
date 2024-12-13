#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import sys
import math
C = float(sys.stdin.readline())
if C > 0:
            C = math.sqrt(C)
            print(C)
else:
            print("Error, C<0")

with open("output.txt", "w") as file:
            file.write(str(C))

with open("logs.txt", "a") as file:
            if C > 0:
                file.write("calc_sqrt (3):\n")
                file.write("C=" + str(C) + "\n\n")
            else:
                file.write("calc_sqrt (3):\n")
                file.write("Error! C<0\n\n")





