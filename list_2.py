def count_evens(nums):
  a = []
  for num in nums:
    if num % 2 == 0:
      a.append(num)
  return len(a)



def big_diff(nums):
    a = min(nums)
    b = max(nums)
    return b-a


def centered_average(nums):
    a = min(nums)
    b = max(nums)
    nums.remove(a)
    nums.remove(b)
    return reduce(lambda x, y: x+y, nums) / len(nums)


###
def sum13(nums):
  arr = []
  sum = 0
  if len(nums) == 0:
      return 0
  else:
      for i,num in enumerate(nums):
        if num == 13:
          #print(i)
          pass
      elif nums[i+1] == 13:
          pass
        else:
          sum += num
  return sum




def has22(nums):
    #for i,num in enumerate(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            #arr = True
            return True
    return False


def sum67(nums):
    total = 0
    a = nums.index(6)
    b = nums.index(7)
    #
    # for i in range(0:a):
    #     total = total + nums[i]
    # for j in range(b:len(nums)):
    #     total = total + nums[j]

    while i<a:
        total = total + nums[i]
        i += 1
    for j, num in enumerate(nums, start=b):
        total += nums[j]

    return total


def sum67(nums):
    total = 0

    try:
      a = nums.index(6)
      print(a)
      b = nums.index(7)
      print(b)
    except:
      return 0
    #
    # for i in range(0:a):
    #     total = total + nums[i]
    # for j in range(b:len(nums)):
    #     total = total + nums[j]
    i=0
    while i<a:
        total = total + nums[i]
        i += 1
    for j, num in enumerate(nums, start=b):
        total += nums[j]

    return total


#sum67([1, 2, 2])
sum67([1, 2, 2, 6, 99, 99, 7])
#sum67([1, 1, 6, 7, 2])













##
