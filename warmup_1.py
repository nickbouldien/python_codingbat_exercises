
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

def sum_double(a, b):
    if a == b:
        return 2*(a + b)
    else:
        return a + b

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

def pos_neg(a,b,negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if a > 0 and b < 0:
            return True
        elif a < 0 and b > 0:
            return True
        else:
            return False

def not_string(str):

    if str[0:3] == "not":
        return str
    else:
        return "not " + str


def missing_char(string, n):
    lister = list(string)
    #print(lister)
    del lister[n]
    #"".join(lister)
    return ("".join(lister))

#missing_char("nick",2)

def front_back(string):
  if len(string) == 1:
    return string
  elif len(string) == 2:
    return string[1] + string[0]
  else:
    return string[-1:] + string[1:-1] + string[:1]

# def front_back(string):
#     final = ""
#     final = final + string[len(string)-1] + string[1:len(string)-1] + string[0]
#     return final


def front3(string):
    final = ""
    final = final + string[0:3]*3
    return final


















#
