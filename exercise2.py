#House price = 300000
#if buyer has good credit = 10% downpayment
#otherwish = 28% > need to pay
House_price = 300000
credit = (input("your creadit\n")
downpayment = 0

if credit == "Good":
    print("Good credit entitled 10 persen downpayment")
    downpayment = house_price*0.1
    print("downpayment are"+str(downpayment))

elif credit =="NotGood":
    print("Not Good credit entitled 28 persen downpayment")
    downpayment = house_price*2.8
    print("downpayment are"+str(downpayment))
else:
    print("Try again")