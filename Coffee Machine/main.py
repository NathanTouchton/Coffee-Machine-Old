MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Program Requirements:
    # 1: Print report
    # 2: Check if RESOURCES are sufficient
    # 3: Process coins.
    # 4: Check if transaction was successful

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

USER_DRINK_CHOICE = input("What would you like? (espresso/latte/cappuccino): ").lower()
QUARTERS = int(input("How many quarters? "))
DIMES = int(input("How many dimes? "))
NICKELS = int(input("How many nickels? "))
PENNIES = int(input("How many pennies? "))

QUARTERS_MATH = QUARTERS * .25
DIMES_MATH = DIMES * .1
NICKELS_MATH = NICKELS * .05
PENNIES_MATH = PENNIES * .01

TOTAL_CALCULATION = QUARTERS_MATH + DIMES_MATH + NICKELS_MATH + PENNIES_MATH

# TODO 2: Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows 
    # the current resource values. e.g.  
    # Water: 100ml 
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

def report():
    for item in RESOURCES:
        print(item + ": " + str(RESOURCES[item]))
if USER_DRINK_CHOICE == "report":
    report()

# TODO 3: Check RESOURCES sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # RESOURCES to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.

def dispense(drink):
    for item in RESOURCES:
        if RESOURCES[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there's not enough {item}. You've been refunded. Please try again later.")
            return
    drink_cost = MENU[drink]["cost"]
    if TOTAL_CALCULATION < drink_cost:
        print(f"Sorry, you gave ${TOTAL_CALCULATION}, but the total is ${drink_cost}. Your money has been returned. Please try again when you have enough.")
    elif TOTAL_CALCULATION > drink_cost:
        change = TOTAL_CALCULATION - drink_cost
        print(f"Here is ${round(change, 2)} in change. Enjoy your coffee!")
    elif TOTAL_CALCULATION == drink_cost:
        print("Enjoy your cofee!")
    

dispense(USER_DRINK_CHOICE)

# TODO 4: Process coins. ----- Done in lines 49-54.
    # a. If there are sufficient RESOURCES to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 5: Check transaction successful? ----- Done in dispense function
    # a. Check that the user has inserted enough money to purchase the drink they selected.
    # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    # program should say “Sorry that's not enough money. Money refunded.”
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
    # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
    # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    # places.

# TODO 6: Make Coffee.
    # a. If the transaction is successful and there are enough RESOURCES to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine RESOURCES.

    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0

    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.50

    # b. Once all RESOURCES have been deducted, tell the user “Here is your latte. Enjoy!”. If
    # latte was their choice of drink.

def ingredients_check(drink):
    for i in MENU[drink]["ingredients"]:
        ingredient_requirement = MENU[drink]["ingredients"][i]
        ingredient_amount = RESOURCES[i]
        if ingredient_requirement > ingredient_amount:
            print(f"Sorry, there's not enough {i}. Please try again later.")
            return
