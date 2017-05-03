
def string_times(string, n):
  return string * n


def front_times(string, n):
  front = string[0:3]
  if len(string) <= 3:
      return string * n
  else:
      return front * n


def string_bits(string):
    for char in range(len(string)):
        if char % 2 == 0:
            print(string[char])


def string_splosion(string):
    arr = []
    for ind in range(len(string)):
        print(string[ind])
        #arr.push()


def last2(string):



def string_match(a,b):
    total = 0
    for char in range(len(a)):
        if a[char:char+2] == b[char:char+2]:
            total += 1
    return total

        #
