
#bruteforce

def twoSum(nums, target):
       for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i] + nums[j] == target and i!=j:
                x = [i,j]
                return x
        
n = int(input("Enter number of elements : "))
nums=[]
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    nums.append(ele) 
print(nums,'nums')
target = int(input('enter target'))
print(target,'target')
print(twoSum(nums,target))
