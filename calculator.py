print("welcome dear patron,choose your numbers and opearations")
num1 = float(input("1....enter the first number: "))
num2 = float(input("2....enter the second number: "))
operation = input("3....choose your operation from +,-,*,/: ")
if operation == "+":
    result = num1 + num2
    print("Answer=", result)

elif operation == "-":
        result = num1 - num2
        print("Answer=", result)

elif operation =="*":
            result = num1 * num2
            print("Answer=", result)

elif  operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Answer=", result)
    else:
        print("Error: Division of zero is not defined.")
else:
    print("Invalid operation. Please choose from +,-,* or /")



while True:
    choice = input("Another calculation? (YES/NO): ")
    if choice == "YES":
        num1 = float(input("1....enter the first number:"))
        num2 = float(input("2....enter the second number:"))
        operation = input("3....choose your operation from +,-,*,/:")
        if operation == "+":
            result = num1 + num2 
            print("Answer=", result)
        elif operation == "-":
            result = num1 - num2 
            print("Answer=", result)
        elif operation == "*":
            result = num1 * num2
            print("Answer=", result)
        elif operation =="/":
            if num2 != 0:
                result = num1 / num2
                print("Answer=", result)
            else:
                print("Error: Division of zero is not defined.")
        else:
            print("Invalid operation. Please choose from +,-,* or /")
    elif choice == "NO":
        print("THANKYOU")
        
        break
    
    


    else:
        print("INVALID CHOICE. PLEASE CHOOSE YES/NO.")


            

        
