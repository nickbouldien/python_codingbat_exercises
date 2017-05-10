def lone_sum(a,b,c):

    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c



def lucky_sum(a,b,c):
    if a == 13 or b == 13 or c ==13:
        if a == 13:
            return 0
        elif b == 13:
            return a
        else:
            return a + b
    else:
        return a + b + c


def no_teen_sum(a, b, c):
    #
    #
