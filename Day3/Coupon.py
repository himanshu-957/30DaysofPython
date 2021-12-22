# if else/ try except

total = 0
product = {'Soap': 10,'Tea': 25, 'Chips': 15}
discount = {'DIS10':0.10,'DIS20':0.20,'DIS30':0.30}
basket = input("Welcome to XYZ store Press 'y' to proceed: ")
while(basket!='n'):
    if basket == 'y'or's'or't'or'c':
        basket = input("Press 's' for Soap, 't' for Tea, 'c' for Chips, 'n' for checkout: ")
        if basket == 's':
            total = total + product['Soap']
        elif basket == 't':
            total = total + product['Tea']
        elif basket == 'c':
            total = total + product['Chips']
    else:
        if basket != 'n':
            print("Sorry! you have pressed wrong button")
print("Your total amount is {}".format(total))
code = input("Do you have any Coupon Code?(y/n): ")
if code == 'y':
    coupon = input("Please enter the coupon code: ")
    if coupon in discount.keys():
        total = total - total*discount[coupon]
        print("Your total amount after applying coupon code is {}".format(total))
    else:
        print("Sorry! Coupon code you entered is invalid")
        print("Your total amount is {}".format(total))
print("Okay, You can pay the total amount")