#Description: Calculator project for the primary school children, with a scope to enhance for advanced calculations.

#Calculator layout
print("My Awesome Calculator")
print("+---------------------+")
print("+ |+| |-| |*| |/| |^| |avg| +")
print("+     |Numbers' game|       +")
print("+        Calculate          +")
print("       \\\\\\\\ ^--^ \\\\\\\\     ")
print()
print()

#Calculator instructions
print("My Awesome Calculator that includes")
print("1. Addition (+). Please input + when prompted")
print("2. Subtraction (-). Please input - when prompted")
print("3. Multiplication (*). Please input * when prompted")
print("4. Division (/). Please input / when prompted")
print("5. Exponentiation (^). Please input ^ when prompted")
print("6. Average (avg). Please input avg when prompted")
print("7. Memory Store (ms). Please input ms when prompted")
print("8. Memory Recall (mr). Please input mr when prompted")
    
# Function to calculate average. The input string is splitted into a list of strings and extra spaces are removed by strip method
def calculate_average():
    list_numbers = input("Enter a list of numbers separated by commas or spaces: ")
    try:
        numbers = [float(num.strip()) for num in list_numbers.replace(',', ' ').split()]
    except ValueError:
        print("The values entered are not valid numbers. Please try again.")
        return
    
    # To return the calculated average up to three decimal places
    avg = sum(numbers) / len(numbers)
    print(f"The average of {' , '.join(map(str, numbers))} is {avg:.3f}")
    return avg  
    
# Function to perform mathematical operations
def perform_operation(operation, first_number, second_number, last_result):
    if operation == "+":
        return first_number + second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "/":
        if second_number == 0:
            return ("Infinity")
        else: #result up to three decimal places
            return (f"{first_number/second_number:.3f}")
    elif operation == "^":
        return (f"The result of the {first_number} to the power of {second_number} is {first_number ** second_number}")
    elif operation == "mr":  # Memory recall operation
        print(f"Value {last_result} is recalled") # Recall the value stored in memory
    else:
        return "Invalid operation"
        
# Main program loop
last_result = None  # Variable to store the result of the last calculation
memory_value = None  # Variable to store the memory value
while True:
    operation = input("\nEnter which mathematical calculation you would like to perform?: ")
    
    #Check if the mathematical operation is one of the listed ones
    if operation not in ['+', '*', '-', '/', '^', 'avg', 'mr', 'ms']:  # Added 'ms' for memory store
        print("Not a valid mathematical calculation")
        continue
    
    if operation == 'avg':
        last_result = calculate_average()
    elif operation == 'ms':  # Memory store operation
        memory_value = last_result  # Store the last result in memory
        print(f"Value {last_result} is stored in memory")
    else: #Prompting for values
        first_number = input("Enter the first number: ")
        second_number = input("Enter the second number: ") 
        
        try:#Convert first_number and second_number to floats and check if they are valid numbers
            first_number = float(first_number)
            second_number = float(second_number)
        except ValueError:
            print("One or both values entered are not valid numbers. Please try again.")
            continue
        
        last_result = perform_operation(operation, first_number, second_number, last_result)
        print(f"The result of the operation is: {last_result}")
    
    #Ask if the user wants to continue and while Loop until valid input is provided
    while True:
        more_calculation = input("\nWould you like to continue with another calculation? (yes/no): ")
        if more_calculation.lower() == 'yes':
            break  # Exit the loop and continue with the next calculation
        elif more_calculation.lower() == 'no':
            print("Thank you, see you later!") # Exit the loop and end the program
            break
        else:
            print ("Invalid output. Please enter 'yes' or 'no.'")
            continue
    if more_calculation.lower() == 'no':
        break
    
    
#Print a smiley and a sustainability message at the end of the output
print(":-)")
print()
print()
print("Save water, save environment.")
    
