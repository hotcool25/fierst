question = "How much change is owed? "
coins = 0

while (True):
    money = float(input("Oh hai! " + question))
    if (money < 0):
        money = float(input(question))
    else:
        break

# Step Two: Convert to change.
money = int(round(money * 100, 2))

# Step Three: Get the change
while (money != 0):
    # The goal is to get the fewest coins as possible.
     if (money - 50 >= 0):
        money -= 50
     elif (money - 25 >= 0):
        money -= 25
     elif (money - 10 >= 0):
        money -= 10
     elif (money - 5 >= 0):
        money -= 5
     elif (money - 2 >= 0):
        money -= 2
     else:
        money -= 1

     coins += 1

# Step Four: Print the change
print(coins)
