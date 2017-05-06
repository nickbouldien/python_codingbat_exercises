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


####
def sum67(nums):
    total = 0

    for num in nums:
        total = total + num
        if num == 6:
            pass

    return total
