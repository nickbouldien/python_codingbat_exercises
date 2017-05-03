def first_last6(nums):
    return True if nums[0] == 6 or nums[-1]== 6 else False


def same_first_last(nums):
    return True if len(nums) >=1 and nums[0] == nums[-1] else False

def make_pi():
    return [3,1,4]


def common_end(a,b):
    return True if a[0] == b[0] or a[-1] == b[-1] else False

def sum3(nums):
    total = 0
    for num in nums:
        total += num
    return total

def rotate_left3(nums):
    final = [0,0,0]
    final[0] = nums[1]
    final[1] = nums[2]
    final[2] = nums[0]
    return final

def reverse3(nums):
    final = [0,0,0]
    final[0] = nums[2]
    final[1] = nums[1]
    final[2] = nums[0]
    return final

def max_end3(nums):

    if nums[0] > nums[-1]:
        nums[1] = nums[0]
        nums[2] = nums[0]
    else:
        nums[0] = nums[-1]
        nums[1] = nums[-1]
