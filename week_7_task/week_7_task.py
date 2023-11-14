items = ['pizza £7.30', 'pie £3.45', 'burger £4.50', 'chips £2.00', 'onion rings £2.30', 'drink £1.50']
print("this is the menu")
for x in items:

    print(x)
order = []
# the [] is used here so that the order prints out as a list 
total = 0.00
ordering = True
while ordering == True:

    print("enter the item you want to purchase")
    item = input().lower()
    if item == "pizza":
        order.append(items[0])
# the .apppend is used to add an item to the list
        total += 7.30
    if item == "pie":
        order.append(items[1])
        total += 3.45
    if item == "burger":
        order.append(items[2])
        total += 4.50
    if item == "chips":
        order.append(items[3])
        total += 2.00
    if item == "onion rings":
        order.append(items[4])
        total += 2.30
    if item == "drink":
        order.append(items[5])
        total += 1.50
    if item == "finish":
        break 
print("your order is ")
for x in order:
    print(x)
print(f"your total is {total}")
