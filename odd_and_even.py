num = int(input("Enter the number :"))
even_num = 0
odd_num = 0
while num != 0:
    digit = num % 2
    if digit == 0:
        even_num = even_num +1
    else:
        odd_num = odd_num + 1
    num = num // 10


print("Even number count is ",even_num)
print("Odd number count is ",odd_num)


