# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def increment_num(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = arr[i] + 1
    return arr

obj  = increment_num([1,2,4])
print(obj)
