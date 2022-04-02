#calculator using function

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

print("my captain calculator")

print(" 1.Add\t", "2.Subtract\n", "3.multiply\t", "4.Divide\n")

condition = True

while condition:
    choice = int(input("select one operation from(1-4): \n"))
    if choice < 5:
        number1 = int(input("Enter A: "))
        number2 = int(input("Enter B: "))

        if choice == 1:
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == 2:
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == 3:
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == 4:
            print(number1, "/", number2, "=", divide(number1, number2))

        conditon_check = input("Do you want to do another calculation(yes/no): ")
        
        if conditon_check == "yes":
            condition = True
        else:
            condition = False


    else:
        print("Select correct option")
