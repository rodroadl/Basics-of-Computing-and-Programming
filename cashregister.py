first = float(input("Enter price of the first Item: "))
second = float(input("Enter price of the second Item: "))
club_card = input("Does customer have a club card? (Y/N): ")
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

base_price = '%2.2f' % (first + second)

if(first > second):
    if(club_card == "y" or club_card == "Y"):
        price_after_discounts = (first + second * 0.5) * 0.9
    else:
        price_after_discounts = first + second * 0.5
else:
    if(club_card == "y" or club_card == "Y"):
        price_after_discounts = (second + first * 0.5) * 0.9
    else:
        price_after_discounts = second + first * 0.5

total_price = round(price_after_discounts * (1 + tax_rate * 0.01), 2)
price_after_discounts = '%2.2f' % price_after_discounts

print("Base price =", base_price)
print("Price after discounts =", price_after_discounts)
print("Total price =", total_price)
