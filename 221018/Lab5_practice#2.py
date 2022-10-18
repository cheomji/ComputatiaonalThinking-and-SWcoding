from stack import *
from stack import isEmpty
from stack import push
from stack import getstack

def printStack():
    for i in st:
        print(i, end=' ')

def add(a, b):
    return a+b
def sub(a, b):
    return b-a
def mul(a, b):
    return a*b
def div(a, b):
    return b//a

operator = ['+', '-', '*', '/', '-']
func = [add, sub, mul, div]
postfix = input()
postfix = postfix.split()

st = getstack()
for item in postfix:
    if item in operator:
        if isEmpty(st):
            pass
        op2 = int(pop(st))
        if isEmpty(st):
            pass
        op1 = int(pop(st))
        if item == '+': push(st, op1+op2)
        elif item == '-': push(st, op1-op2)
        elif item == '*': push(st, op1*op2)
        elif item == '/': push(st, op1//op2)
    else:
        push(st, int(item))
