# Building a calculator using if and else

print("My captain calculator")
print(" 1.Add\t", "2.Subtract\n", "3.Multiply\t", "4.Divide\n", "5.Square root\t", "6.Squares")
choice = int(input("Enter a option from (1-6) :\n"))

if choice == 1:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a + b
    print("Sum = ", c)
elif choice == 2:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a - b
    print("Difference = ", c)
elif choice == 3:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a * b
    print("Product = ", c)
elif choice == 4:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a / b
    print("Quotient = ", c)
elif choice == 5:
    a = int(input("Enter a number: "))
    b = a ** 0.5
    print("Square root [{}] =  ".format(a), b)
elif choice == 6:
    a = int(input("Enter a number: "))
    b = a * a
    print("Square of [{}] = ".format(a), b)
else:
    print(" Please select the correct option ")



