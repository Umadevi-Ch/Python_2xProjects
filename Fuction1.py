def sayhello(name='User'):
    print("Hello", name)
    print("Good Morning")

def add(fn, sn):
    result = fn + sn
    print('Result ' + str(result))

def getSum(*x):
    result = 0
    for a in x:
        result += a
    print("Result :", result)

sayhello("rafique")
getSum(25, 5, 33)