def divisionFunction (year,denominator):
    if(year % denominator) == 0:
        return "Yes"
    else:
        return "No"

year=int(input("Type the year: \n"))

divideBy4= divisionFunction(year,4)
divideBy400 = divisionFunction(year,400)
divideBy100 = divisionFunction(year,100)

if divideBy4 == "Yes":
    if divideBy400 == "Yes":
        print("Leap year")
    elif divideBy100 == "Yes":
        print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap year")