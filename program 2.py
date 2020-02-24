def special_larger(x,y):
    xf = int(str(x)+str(y))
    yf = int(str(y)+str(x))
    if xf >yf:
        return True
    else:
        return False
def get_largest_num(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if not special_larger(nums[i],nums[j]):
                nums[i],nums[j] = nums[j],nums[i]
    y = [str(a) for a in nums]
    str_y = "".join(y)
    return int(str_y)    
nums=list(map(int,input("enter").split()))
print(get_largest_num(nums))               