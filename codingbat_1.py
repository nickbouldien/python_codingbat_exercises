
#gmail
#ca


# warm ups:

def sleep_in(weekday, vacation):
    if weekday == False or  vacation == True:
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True # in trouble
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False

def diff21(n):
    if n > 21:
        return 2*(abs(n-21))
    else:
        return abs(n-21)


def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False


def makes10(a,b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False

def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <=10:
        return True
    else:
        return False

# def pos_neg(a,b,negative):
#
#     if


























#
