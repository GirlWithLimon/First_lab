#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import sys
import math

def main():
    try:
        C = float(sys.stdin.readline())
        if not C < 0:
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
    except ValueError:
        print("C don`t have value, because B=0")
    except EOFError:
        print("the field is empty")
    except Exception as problem:
        print(problem)
    return
if __name__=="__main__":
    main()


