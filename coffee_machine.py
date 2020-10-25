water = 400
milk = 540
coffee_beans = 120
money = 550
disposable_cups = 9

def change_qty(water2,milk2,coffee_beans2,disposable_cups2,money2):
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money
    water -= water2
    milk -= milk2
    coffee_beans -= coffee_beans2
    disposable_cups -= disposable_cups2
    money += money2

def print_status():
    print(f'''The coffee machine now has:
    {water} ml of water
    {milk} ml  of milk
    {coffee_beans} g of coffee beans
    {disposable_cups} disposable cups
    ${money} of money''')


def check_cups():
    if disposable_cups < 1:
        print("Sorry, not enough disposable cups!")

def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()
    if coffee_type == "3":
        check_cups()
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif coffee_beans < 12:
            print("Sorry, not enough coffee beans!")
        else:
            print('I have enough resources, making you a coffee!')
            change_qty(200, 100, 12, 1, 6)
    elif coffee_type == "2":
        check_cups()
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif coffee_beans < 20:
            print('Sorry, not enough coffee beans!')
        else:
            print("I have enough resources, making you a coffee!")
            change_qty(350, 75, 20, 1, 7)
    elif coffee_type == "1":
        check_cups()

        if water < 250:
            print("Sorry, not enough water!")
        elif coffee_beans < 16:
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            change_qty(250, 0, 16, 1, 4)

    elif coffee_type == "back":
        main()
    else:
        pass

def fill():
    print("Write how many ml of water do you want to add:")
    given_water = int(input())
    print("Write how many ml of milk do you want to add:")
    given_milk = int(input())
    print("Write how many grams of coffee do you want to add:")
    given_coffee = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    given_cups = int(input())
    change_qty(-given_water, -given_milk, -given_coffee, -given_cups, 0)


def take():
    print(f"I gave you ${money}")
    change_qty(0, 0, 0, 0, -money)

def main():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            print_status()
        elif action == "exit":
            exit()

main()