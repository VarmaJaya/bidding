import os
is_continue = True
total = {}

def bid(n, b):
    total[n] = b

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while is_continue:
    name = input("Please enter your name: ")
    price = int(input("Please bid your price :$ "))
    bid(n=name, b=price)

    new_entry = input("Are there any other bidders? 'yes' or 'no': ").lower()
    if new_entry == "no":
        is_continue = False
    clear_console()
highest_value = 0
new_name = ""
for item in total:
    if total[item] > highest_value:
        highest_value = total[item]
        item = new_name
print(f"The winner is {name} wih bid of {highest_value}$.")




