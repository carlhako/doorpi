globalVar = 0
print(globalVar)

def fun1():
    fun2()

def fun2():
    global globalVar
    print(globalVar)
    globalVar = 1

fun1()
