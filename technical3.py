nums = [1, 5, 7, -1, 5]
target = 6
count = 0


for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if i < j and target == nums[i] + nums[j]:
            count +=1
                
print(f'Count of pairs: {count}')