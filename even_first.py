# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def even_first(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            elem = arr[i]
            arr.remove(arr[i])
            arr.append(elem)
    return arr
obj = even_first([7, 3, 5, 6, 4, 10, 3, 2])
print(obj)