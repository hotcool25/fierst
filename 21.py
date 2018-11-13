money = int(input("Введіть суму в копійках: "))
m = money
coins = 0
while (money != 0):

    if (money - 25 >= 0):
        money -= 25

    elif (money - 10 >= 0):
        money -= 10

    elif (money - 5 >= 0):
        money -= 5
        #coins =
    elif (money - 1 >= 0):
        money -= 1

    else:
        money -= 1

    coins += 1
print("How much change is owed?")
print(m)
print(coins)