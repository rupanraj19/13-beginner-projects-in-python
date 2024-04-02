# Binary search (divide and find)
# function that takes a list and target parameters
# multiple variables : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while start <= end:
        print(f"Steps: {steps}, list: {list[start:end+1]}")
        steps += 1
        middle = (start + end) // 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            start = middle + 1
            middle = (start + end) // 2
        elif list[middle] > target:
            end = middle - 1
            middle = (start + end) // 2

    return -1 # The function returns -1 if the target element is not found in the given list.

mylist = [1,2,3,4,5,6,7,8,9,0]
target = 4

binary_search(mylist, target)


