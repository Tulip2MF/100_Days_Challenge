name1 = input("Write your name: ").lower()
name2 = input("Write other person's name: ").lower()
joinedName = name1 + name2


def loveCounter(countParameter):
    count1 = 0
    for i in countParameter:
        count1 += joinedName.count(i)
    return count1


trueCount = loveCounter("true")
loveCount = loveCounter("love")

percentage= int((str(trueCount) + str(loveCount)))

if percentage<10 or percentage>90:
    print(f"Your Percentage is {percentage}, you go together like coke and mentos")
if percentage < 50 and percentage > 40:
    print(f"Your Percentage is {percentage}, you are alright together")
else:
    print(f"Your Percentage is {percentage}")


