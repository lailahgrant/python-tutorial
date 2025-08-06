#create function
def get_number():
    while True: 
        operand = input("Number 1: ")
        try:
            operand = float(operand)
            break
        except:
            print("Invalid input operand")

    return operand



while True: 
    operand2 = input("Number 2: ")
    try:
        operand2 = float(operand2)
        break
    except:
        print("Invalid input operand")

sign = input("Sign: ")
    
result = 0
if sign == "+":
    result = float(operand) + float(operand)
elif sign == "-":
    result = float(operand) - float(operand)
elif sign == "/":
    if float(operand2) != 0:
        result = float(operand) / float(operand2)
    else:
        print("Division by Zero.") #type a custom error
elif sign == "*":
        result = float(operand) * float(operand2)

print(result)




