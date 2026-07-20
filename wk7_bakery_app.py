# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: __Sheyla Ixtbalan________________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: _______baked goods__________________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Bakery:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_price(self, price):
        if price < 0:
            print("no")
        else:
            self.price = price
    def deliver(self):
        print(f"Delivering your {self.name}!")


# TICKET 3: The price guard

#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)

#   PREDICT what happens: ____the code will break and say no because the price is below zero__________
#   Paste the message you see here: ____no__________


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class Drink(Bakery):
    def deliver(self):
        print(f"Your {self.name} is on the way!")
bakery = Bakery("cake", 3.00)
drink = Drink("soda", 2.00)

bakery.deliver()
drink.deliver()



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______________


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: _it will show "cake" and the price

item1 = Bakery("cake", 3.00)
item2 = Bakery("cookie", 2.00)
item3 = Bakery("croissant", 3.50)
item4 = Bakery("drink", 2.50)


print(item1.name)
print(item2.name)
print(item3.name)
print(item4.name)
print(item1.price)
print(item2.price)
print(item3.price)
print(item4.price)
print(item1.deliver())
print(item2.deliver())
print(item3.deliver())
print(item4.deliver())
print(total := item1.price + item2.price + item3.price + item4.price)

# Predicted output: "cake", "cookie", "croissant"
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
        print(f"{item.name} added!")
    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total += item.price
        print(f"Total: ${total}")


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {"1": item1, "2": item2, "3": item3, "4": item4}
cart = Cart()



# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________

while True:
    choice = input("Pick an item by number (1-4) or type 'done' to finish: ")
    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
    else:
        print("Invalid choice.")

cart.checkout()


# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
