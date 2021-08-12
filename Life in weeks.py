currentAge = int(input("What is your current age?\n"))
remainingYears = 90-currentAge
remainingWeeks = remainingYears*52
remainingDays = remainingYears*365
print(f"You have {remainingYears} years or {remainingWeeks} weeks or {remainingDays} days to live")

#print the week bubble

for i in range(remainingYears):
    print("\n")
    for j in range(52):
        print("O",end="")