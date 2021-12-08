
import random 

lottery = random.randint(0, 99)
guess = eval(input("Enter your lottery, pick two digits: "))

lotterydigit1 = lottery // 10
lotterydigit2 = lottery % 10

guessdigit1 = guess // 10
guessdigit2 = guess % 10

print("The lottery number is", lottery)

if guess == lottery:
    print("Exact match, you win £10,000)")
elif (guessdigit2 == lotterydigit1 and guessdigit1 == lotterydigit2):
    print("Matched digits, you win £5,000")
elif (guessdigit1 == lotterydigit1 or guessdigit1 == lotterydigit2 or guessdigit2 == lotterydigit1 or guessdigit2 == lotterydigit2):
    print("One match: you win £1,000")
else:
    print("Sorry, no match :(")
