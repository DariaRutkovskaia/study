MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def get_order_info(coffee):
    wanted_coffee = MENU[coffee]
    return wanted_coffee


def report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def check_resourses(dict_o, dict_r):
    key_list = list(dict_o.keys())
    for i in key_list:
        if dict_o[i] > dict_r[i]:
            print(f"Sorry there is not enough {i}")
            coffeemaker()


def take_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def make_a_coffee(dict_o, dict_r):
    global choice
    print(f"Here is your {choice} ☕️. Enjoy!")
    key_list = list(dict_o.keys())
    for i in key_list:
        dict_r[i] = dict_r[i] - dict_o[i]


def coffeemaker():
    global choice, money
    turned_on = True
    while turned_on:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choice == "report":
            report()
            coffeemaker()
        elif choice == "off":
            print("I'm turning off!! See ya!!")
            return not turned_on

        customers_coffee = get_order_info(choice)
        composition = customers_coffee['ingredients']
        check_resourses(composition, resources)
        summ = take_money()
        cost = customers_coffee["cost"]
        if cost > summ:
            print("Sorry that's not enough money. Money refunded.")
            coffeemaker()
        else:
            money += cost
            change = summ - cost
            print(f"Here is ${change} in change.")
            make_a_coffee(composition, resources)


coffeemaker()
