import math  # Math library
running = True  # Keep application running

print("# Methods list #")
print("Mulitiplcation -> * \nAddition -> + \nSubtract -> - \nDivide -> / \nFloor-division -> // \nModulus -> % \nExponentiation -> **  \nisGreaterThan -> > \nisLessThan -> < \n\n")
while running == True:
    try:
        num1 = float(input("Number-1 >> "))
        method = str(input("Method >> "))       # Enter numbers/method
        num2 = float(input("Number-2 >> "))


        def Calculate(num1, method, num2):  # Function does all the math
            try:
                if method == "*":
                    return num1 * num2
                elif method == "+":
                    return num1 + num2
                elif method == "-":
                    return num1 - num2
                elif method == "/":
                    return num1 / num2
                elif method == "//":
                    return num1 // num2
                elif method == "%":
                    return num1 % num2
                elif method == ">":
                    return num1 > num2
                elif method == "<":
                    return num1 < num2
                elif method == "**":
                    return num1 ** num2

            except ZeroDivisionError:
                print("0 Division error") # Handle divide by 0 error
            except OverflowError:
                print("Math equation was too large") # Just in case .-.

        output = Calculate(num1, method, num2)
        outputStr = "{0} {1} {2} => {3}"
        if output == None:
            print("Unexpected output. Try again with a valid equation/method") # Checks if there is any calculation made and if output is nil then give error
        else:
            print(outputStr.format(num1, method, num2, output))


    except ValueError:
        print("Must be number")
    except KeyboardInterrupt:
        validation = input("\nAre you sure you want to exit? (Y/N) ") # Making sure you want to exit
        if validation.lower() == "y":
            running = False # Closes program
            break
        elif validation.lower() == "n":
            pass
        else:
            print("Invalid option")