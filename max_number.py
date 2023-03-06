n1 = int( input("Enter the number n1: ") )
n2 = int( input("Enter the number n2: ") )
n3 = int( input("Enter the number n3: ") )



if n1 > n2 and n1 > n3:
    print("Result is :",n1)
elif n2 > n3 and n2 > n1:
    print("Result is :",n2)
else:
    print("Result is :",n3)