from turtle import down


good_credit=True
price=1000000
if good_credit:
    pricex=price-10000
    print("price after giving 10%",pricex)
else:
    pricey= price-20000
    print("price after giving 20%",pricey)
print('orginal price',price)



orginal_price=1000000
has_good_credit=True

if has_good_credit:
    down_payment=0.1*orginal_price
else:
    down_payment=1.2*orginal_price
print(f"down payment is ${down_payment}")
