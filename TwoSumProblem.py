def twoSum(nums, target):
    index_found = []
    cur_index = 0
    for _ in nums[cur_index:]:
        current_num = nums[cur_index]
        second_index = cur_index + 1
        for val1 in nums[cur_index + 1:]:
            # print(cur_index, current_num, val1, second_index, target)
            if current_num + val1 == target:
                index_found.append(cur_index)
                index_found.append(second_index)
                return index_found
            second_index += 1
        cur_index += 1


class Solution:
    print(twoSum([2, 7, 11, 15], 22))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))
    print(twoSum([3, 3, 7], 10))
