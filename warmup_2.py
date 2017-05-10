
def string_times(string, n):
  return string * n


def front_times(string, n):
  front = string[0:3]
  if len(string) <= 3:
      return string * n
  else:
      return front * n



def string_bits(string):
    newString = ''
    for char in range(len(string)):
        if char % 2 == 0:
            #print(string[char])
            newString = newString + string[char]
            #print(newString)
    return newString



def string_splosion(string):
    arr = []
    for ind in range(len(string)):
        print(string[ind])
        #arr.push()


def last2(string):









def array123(nums):

    for num in nums:
        if num 










def string_match(a,b):
    total = 0
    for char in range(len(a)):
        if a[char:char+2] == b[char:char+2]:
            total += 1
    return total

        #
