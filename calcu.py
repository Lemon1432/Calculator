try:

       cmd = int(input("""
Enter 1 for Usual Addition Calculations
Enter 2 for Usual Subtraction Calculations
Enter 3 for Usual Multiplication Calculations
Enter 4 for Usual Division Calculations
>>> """))

except ValueError:
    print("You have entered an invalid input. Please try again.")

else:
    
    print()

    if cmd == 1:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 + num2)

    if cmd == 2:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 - num2)

    if cmd == 3:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 * num2)

    if cmd == 4:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 / num2)                    

       
            

            
        
