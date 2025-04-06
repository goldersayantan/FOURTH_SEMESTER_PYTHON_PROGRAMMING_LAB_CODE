def twosum(nums, target):
    my_lst = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == target:
                my_lst.append(i)
                print(my_lst)
                my_lst = []
            elif nums[i] + nums[j] == target:
                my_lst.append(i)
                my_lst.append(j)
                print(my_lst)
                my_lst = []


nums = [0, 4, 3, 0]
target = 0
twosum(nums, target)
