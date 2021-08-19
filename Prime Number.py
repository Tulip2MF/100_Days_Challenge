# This code is to test whether a number is prime or not

def prime_check(number):
    if number <= 1:
        print("Can't say. Please provide a number above 1")
    else:
        for denominator in range(1, round(number / 2)):
            if number % denominator == 0:
                return "Its a prime number"

            else:
                if denominator == round(number / 2):
                    return "It's not a prime number"



user_input = int(input("Give a number to check: "))

output = prime_check(user_input)
print(output)