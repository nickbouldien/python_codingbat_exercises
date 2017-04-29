def double_char(string):
    arr = []
    for i in range(len(string)):
        arr.append(string[i]*2)
    return ''.join(arr)


def count_hi(string):
    return string.count("hi")

def cat_dog(string):
    cat = string.count('cat')
    dog = string.count('dog')
    if dog == cat:
        return True
    else:
        return False

def count_code(string):
    dog = string.count('code')



def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    else:
        return False

def xyz_there(string):
    string2 = 'xyz'
    period = '.'
    a = string.find(string2) # should give index
    if string[a-1] == period:
        return False
    else:
        return True



def xyz_there(string):
    string2 = 'xyz'
    period = '.'
    a = string.find(string2) # should give index
    if string[a-1] == period:
      return False
    else:
      return True









##
