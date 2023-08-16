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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def process_coins():
    print("Please insert coins:")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)
    return total / 100


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


def coffee_machine():
    restart = True
    while restart:
        user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_order == "report":
            for item, amount in resources.items():
                print(f"{item.capitalize()}: {amount}")
        elif user_order in MENU:
            drink_ingredients = MENU[user_order]["ingredients"]

            # Check if there's enough water to make the selected drink
            if (
                "water" in drink_ingredients
                and drink_ingredients["water"] > resources["water"]
            ):
                print("Insufficient water. Please refill the water reservoir.")
                continue

            cost = MENU[user_order]["cost"]
            payment = process_coins()

            if payment < cost:
                print("Insufficient funds. Money refunded.")
            else:
                change = payment - cost
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_order}. Enjoy!")

                make_coffee(user_order)
                resources["money"] += cost
        else:
            print("Invalid choice. Please choose a valid drink.")

        restart = input("Do you want to order again? (yes/no): ").lower() == "yes"


coffee_machine()
