from art_calculator import logo
def multiplication(number1,number2):
        multiplication_result = number1 * number2
        return multiplication_result

division = lambda first_number,second_number: first_number/ second_number
def addition(number1, number2):
    addition_result = number1 + number2
    return addition_result
def subtraction(number1,number2):
    subtraction_result = number1 - number2
    return subtraction_result




print(logo,"\n\n")
first_number = int(input("Give the first number: "))
operation_dictionary = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
}



while True:
    operation = input("What operation to perform?\n'+' for addition\n'-' for subtraction\n'*' for multiplication\n'/' for division\n Operator: ")
    second_number = int(input("Give the second number: "))
    calculation = operation_dictionary[operation]
    result = calculation(first_number,second_number)
    print(f"The result\n{first_number} {operation} {second_number} = {result}")
    first_number = result
    try_again = input("Press 'N' if you want to exit or any other key to continue: ").lower()
    if try_again == 'n':
        break



