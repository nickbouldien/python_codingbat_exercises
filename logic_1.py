

def cigar_party(cigars, is_weekend):
    if is_weekend == True:
        if cigars >= 40:
            return True
        else:
            return False
    else:
        if (cigars >=40 and cigars <=60):
            return True
        else:
            return False


def date_fashion(you, date):
    if you <=2  or date <= 2:
        # if you >= 8 or date >= 8:
        #     return 2
        # else:
            return 0
    elif you >=8 or date >= 8:
        return 2
    else:
        return 1


def squirrel_play(temp, is_summer):
    if is_summer == True:
        if temp >= 60 and temp <= 100:
            return True
        else:
            return False
    else:
        if temp >= 60 and temp <= 90:
            return True
        else:
            return False


def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        if speed >=66 and speed <=85:
            return 1
        elif speed <= 65:
            return 0
        else:
            return 2
    else:
        if speed >=61 and speed <=80:
            return 1
        elif speed <= 60:
            return 0
        else:
            return 2


def sorta_sum(a, b):
    if (a + b) >= 10 and (a + b) <= 19:
        return 20
    else:
        return (a + b)


def alarm_clock(day, vacation):
    if vacation == True:
        if day in range(1,6):
            return "10:00"
        else: # sab/dom
            return "off"
    else: # not on vacation
        if day in range(1,6):
            return "7:00"
        else: # sab/dom
            return "10:00"



def in1to10(n, outside_mode):
    if outside_mode == True:
        if n not in range(2,10):
            return True
        else:
            return False
    else:
        if n in range(1,11):
            return True
        else:
            return False


# def near_ten(num):
#     if (num % 10 < 12 or num % 10 > 8 ) or (num % 5 < 12 or num % 5 > 8) or (num % 2 < 12 or num % 2 >8) or (num % 1 < 12 or num % 1 > 8):
#         return True
#     else:
#         return False
#
# def near_ten(num):
#     if (num % 10 < 2) or (num % 5 < 2) or (num % 2 < 2) or (num % 1 < 2):
#         return True
#     else:
#         return False


# in javascript

# // yes I think you're overthinking it! Here's my interpretation:
# function nick(num){
#   return (num % 10 <= 2 || num % 10 >= 8);
# }
#
# // test function
# for (var i = 0; i < 50; i++){
#   console.log("num: " + i + "- result: " + nick(i));
# }

def near_ten(num):
    return (num %10 <= 2 or num % 10 >= 8)



def love6(a, b):
    if a == 6 or b == 6:
        return True
    elif abs(a - b) == 6 or abs(b-a) == 6:
        return True
    elif a + b == 6:
        return True
    else:
        return False




#
