from bdb import Breakpoint

print("Two Sum")
nums=[3, 1, 4, 10, 77, 44]
target=33
found_output=[]
run=True
for index in range(len(nums)):
    print("***index: ",index)
    if run:
        for num in nums:
            print("num: ", num)
            print(f"nums[{index}]: ", nums[index])
            if num + nums[index] == target:
                found_output.append(num)
                found_output.append(nums[index])
                run=False
                break


print(found_output)


