"""
===================
Item                    Price
——————————————————
Apples                  0.4
Pears                    0.5
Cantaloupes           1.92
====================
"""

newitem = input()
newprice = input()

item2price = [
    ["Apples", 0.4],
    ["Pears", 0.5],
    ["Cantaloupes", 1.92],
    [newitem, newprice]
]

print("====================")
print("Item\tPrice")
print("——————————————————")

for item, price in item2price:
    print(item, "\t", price)

print("====================")
