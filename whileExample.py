"""
order = []
order = input("What would you like to order? (Q to Quit)")

while (order.upper() 1 = 'Q' ):
    #find the order and add it to the list is it exists
    #see if the customer wants to order anything else
"""    
"""
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
"""

orders = [];

alive = True;
while(alive):
    order = input("order apa ? (Q untuk quit)");
    if order.upper() == 'Q':
        alive = False;
    else:
        orders.append(order);
print(orders);