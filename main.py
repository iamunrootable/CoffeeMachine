import sys

# Constants
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


def coffee_machine():

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    def check_resources(drink):
        requirements = MENU[drink]['ingredients']
        out_of_stock = []
        for resource, requirement in requirements.items():
            if requirement > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                out_of_stock.append(resource)
                break
            else:
                resources[resource] -= requirement

        if not out_of_stock:
            return True
        else:
            return False

    def check_coins(drink):
        print("Please insert coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickels = float(input("How many nickels?: ")) * 0.5
        pennies = float(input("How many pennies?: ")) * 0.1
        total = round(quarters + dimes + nickels + pennies, 2)

        cost = MENU[drink]["cost"]
        if total < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif total > cost:
            change = round(total - cost, 2)
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {drink} ☕ Enjoy!")
            resources["money"] += (total - change)
            check_passed = True
            return True
        else:
            resources["money"] += total
            print(f"Here is your {drink} ☕ Enjoy!")
            check_passed = True
            return True

    closed_shop = False
    while not closed_shop:
        drink_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        accepted_drinks = ["espresso", "latte", "cappuccino"]
        if drink_order == "off":
            print("Coffee machine powered off.")
            closed_shop = True
        elif drink_order == "report":
            for k, v in resources.items():
                if k == "money":
                    print(f"{k.title()}: ${v:.2f}")
                elif k == "coffee":
                    print(f"{k.title()}: {v}g")
                else:
                    print(f"{k.title()}: {v}ml")
        elif drink_order not in accepted_drinks:
            print(f"Error: drink order {drink_order} not on the menu.")
        elif check_resources(drink_order):
            check_coins(drink_order)

coffee_machine()

