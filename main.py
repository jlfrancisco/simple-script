import sys 

from actions_toolkit import core

def printhello():
    print("Hello")

def calculate(a, b):
    return int(a)+int(b)

if __name__=="__main__":
    arg1, arg2 = sys.argv[1:3]
    #printhello()
    print(f"result={calculate(arg1, arg2)}")
    core.set_output("result", calculate(arg1, arg2))
