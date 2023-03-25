'''When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3'''


def two_small_numbers(arr):

    arr.sort()
    return arr[0],arr[1]

obj = two_small_numbers([198,3,4,9,10,9,2])
print(obj)


