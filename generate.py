#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import random
import sys
with open ("logs.txt","w") as file:
    file.write("Generate (1):\n")
    A = random.randint(-10, 10)
    file.write("A=" +str(A)+"\n\n")
print (A)