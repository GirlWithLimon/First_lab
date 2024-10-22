#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import sys
A=int(input("Write number: "))
A=A**2
print("A^2=",A)
res=open("output.txt",'w')
res.write(str(A))
res.close()
sys.stderr=open('errors.txt','w')