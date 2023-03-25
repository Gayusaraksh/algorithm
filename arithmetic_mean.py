'''Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]'''


def arithmetic_mean(arr):
    result = 0
    for i in arr:
        result = result + i
    res1 = result/len(arr)
    for j in arr:
        if j < res1:
            print(j)
obj = arithmetic_mean([0,2,4,5,6,7,8,9,3,1])
