import math
import random

# --- Basic math operations ---
def add(a, b):  # Addition
    return a + b

def subtract(a, b):  # Subtraction
    return a - b

def multiply(a, b):  # Multiplication
    return a * b

def divide(a, b):  # Division (with zero check)
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def modulo(a, b):  # Modulo (remainder)
    return a % b 

def power(a, b):  # Exponentiation
    return a ** b

def absolute_value(a):  # Absolute value
    return abs(a)

def floor_division(a, b):  # Integer division (floor division)
    return a // b

def square_root(a):  # Square root with error handling
    if a < 0:
        return "Error: Negative number"
    return round(math.sqrt(a), 2)

# --- Binary operations ---
def binary_or(a, b):  # Binary OR
    return int(a) | int(b)

def binary_and(a, b):  # Binary AND
    return int(a) & int(b)

def binary_xor(a, b):  # Binary XOR
    return int(a) ^ int(b)

def binary_not_and(a, b):  # Binary NOT AND (~a & b)
    return ~int(a) & int(b)


# --- Comparisons and averages ---
def average(a, b):  # Average of two numbers
    return (a + b) / 2

def less_or_equal(a, b):  # Less than or equal
    return a <= b

def greater_or_equal(a, b):  # Greater than or equal
    return a >= b

def greater_than(a, b):  # Greater than
    return a > b

def less_than(a, b):  # Less than
    return a < b

# --- Practice quiz function ---
def practice_quiz():
    score = 0
    total = int(input("How many exercises do you want to do? "))

    for i in range(total):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operator = random.choice(["+", "-", "*", "/"]) 
        
        # Calculate correct answer based on operator
        if operator == "+":
            correct_answer = a + b
        elif operator == "-":
            correct_answer = a - b
        elif operator == "*":
            correct_answer = a * b
        elif operator == "/":
            while b == 0:  # Prevent division by zero
                b = random.randint(1, 20)
            correct_answer = round(a / b, 2)

        # Ask user for answer
        answer = input(f"{a} {operator} {b} = ")

        try:
            # Check if answer is correct (with tolerance for decimals)
            if abs(float(answer) - correct_answer) < 0.01:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer is {correct_answer}")
        except:
            print(f"Invalid input. Correct answer was {correct_answer}")

    print(f"\nFinal score: {score}/{total}")

# --- Main program loop ---
while True:
    print(" MATHEMATICAL MULTI-TOOL PROGRAM ")
    print("\n--- Options ---:") 
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")
    print("%. Modulo")
    print("**. Power")
    print("//. Floor division")
    print("sqrt. Square root")
    print("abs. Absolute value")
    print("3. Average")
    print("OR. Binary OR")
    print("AND. Binary AND")
    print("XOR. Binary XOR")
    print("~. Binary NOT AND (~a & b)")
    print("<=. Less or equal")
    print(">=. Greater or equal")
    print(">. Greater")
    print("<. Less")
    print("7. Practice quiz with +-*/")
    print("exit. Exit program\n")
    
    choice = input("Enter operation: ").strip()  
    
    if choice == "exit":  # Exit condition
        print("Program terminated. Thanks for using it!")
        break
    
    try:  # Error handling for invalid input
        if choice == "7":
            practice_quiz()
            continue

        # Operations that need only 1 number
        if choice in ["sqrt", "abs"]:
            a = float(input("Enter number: "))
            if choice == "sqrt":
                print("Result:", square_root(a))
            else:
                print("Result:", absolute_value(a))
            continue

        # For all other operations, ask for 2 numbers
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))
        
        if choice == "+":
            print("Result:", add(a, b))
            
        elif choice == "-":
            print("Result:", subtract(a, b))
            
        elif choice == "*":
            print("Result:", multiply(a, b))
            
        elif choice == "/":
            print("Result:", divide(a, b))
            
        elif choice == "%":
            print("Result:", modulo(a, b))
            
        elif choice == "**":
            print("Result:", power(a, b))
            
        elif choice == "//":
            print("Result:", floor_division(a, b))
            
        elif choice.upper() == "OR":
            print("Result:", binary_or(a, b))
            
        elif choice.upper() == "AND":
            print("Result:", binary_and(a, b))
            
        elif choice.upper() == "XOR":
            print("Result:", binary_xor(a, b))
            
        elif choice == "~":
            print("Result:", binary_not_and(a, b))
            
        elif choice == "3":
            print("Result:", average(a, b))
            
        elif choice == "<=":
            print("Result:", less_or_equal(a, b))
            
        elif choice == ">=":
            print("Result:", greater_or_equal(a, b))
            
        elif choice == ">":
            print("Result:", greater_than(a, b))
            
        elif choice == "<":
            print("Result:", less_than(a, b))
            
        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: You must enter a numeric value.")  
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.") 
    except Exception as e:
        print("An unexpected error occurred:", e)
