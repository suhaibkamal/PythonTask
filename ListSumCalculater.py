# def sum(x):
#     if x > 0:
#         return x + sum(x - 1)
#     else:
#         return 0


def sum(x):
    return int(x * (x + 1) / 2)


inputList = []
sumList = []


def countSumList(x):
    for i in x:
        sumList.append(sum(i))


def getListNumbers():
    s = input("write finish to end...\n")
    while s != 'finish':
        try:
            inputList.append(eval(s))
            s = input()
        except:
            s = input("the value you entered can't be cast to int \n")


getListNumbers()
countSumList(inputList)

print(sumList)
