op_list = []

def zero(aux=None):
    global op_list
    if op_list == []:
        op_list.append(0)
    else:
        op_list.append(0)
        res = operate()
        return res


def one(aux=None):
    global op_list
    if op_list == []:
        op_list.append(1)
    else:
        op_list.append(1)
        res = operate()
        return res


def two(aux=None):
    global op_list
    if op_list == []:
        op_list.append(2)
    else:
        op_list.append(2)
        res = operate()
        return res


def three(aux=None):
    global op_list
    if op_list == []:
        op_list.append(3)
    else:
        op_list.append(3)
        res = operate()
        return res


def four(aux=None):
    global op_list
    if op_list == []:
        op_list.append(4)
    else:
        op_list.append(4)
        res = operate()
        return res


def five(aux=None):
    global op_list
    if op_list == []:
        op_list.append(5)
    else:
        op_list.append(5)
        res = operate()
        return res


def six(aux=None):
    global op_list
    if op_list == []:
        op_list.append(6)
    else:
        op_list.append(6)
        res = operate()
        return res


def seven(aux=None):
    global op_list
    if op_list == []:
        op_list.append(7)
    else:
        op_list.append(7)
        res = operate()
        return res


def eight(aux=None):
    global op_list
    if op_list == []:
        op_list.append(8)
    else:
        op_list.append(8)
        res = operate()
        return res


def nine(aux=None):
    global op_list
    if op_list == []:
        op_list.append(9)
    else:
        op_list.append(9)
        res = operate()
        return res


def plus(aux=None):
    global op_list
    op_list.append("+")


def minus(aux=None):
    global op_list
    op_list.append("-")


def times(aux=None):
    global op_list
    op_list.append("*")


def divided_by(aux=None):
    global op_list
    op_list.append("/")


def operate():
    global op_list
    ans = 0
    if op_list[1] == "+":
        ans = op_list[2]+op_list[0]
    if op_list[1] == "-":
        ans = op_list[2]-op_list[0]
    if op_list[1] == "*":
        ans = op_list[2]*op_list[0]
    if op_list[1] == "/":
        ans = op_list[2]//op_list[0]
    op_list = []
    return ans


x = three(times(two()))
y = four(plus(nine()))
z = six(divided_by(one()))
a = eight(minus(nine()))
print(x, y, z, a)
