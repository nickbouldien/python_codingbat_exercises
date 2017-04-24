def hello_name(name):
    return "Hello " + name + "!"


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return "<" + tag + ">" + word +"</" + tag + ">"

def make_out_word(out, word):
    a = out[:2]
    b = out[2:]
    return a + word + b

def extra_end(string):
    #a = string[-1:-3:-1]
    a = string[-1]
    b = string[-2]
    return (b+a)*3


def first_two(string):
    if len(string) >= 2:
        return string[:2]
    else:
        return string


def first_half(string):
    a = len(string)
    b = int(round(a /2))
    return string[:b]


def without_end(string):
    string = string[1:]
    return string[:-1]


def combo_string(a,b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


def non_start(a, b):
    a = a[1:]
    b = b[1:]
    return a + b


def left2(string):
    return string[2:] + string[:2]



#
