def terminal1():
    print("Go to terminal 1")
    mainfunc()
def termnal2():
    print("Go to terminal 2")
    mainfunc()
def terminal3():
    print("Go to terminal 3")
    mainfunc()
def mainfunc():
    response=input("your fight:domestic/budget/international")
    if response=="budget":
        terminal1()
    elif response=="domestic":
        termnal2()
    elif response=="international":
        terminal3()
mainfunc()