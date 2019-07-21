# 1.define the price of an apple
price_str=float(input("Please input apple price:"))

# 2.select an apple
weight_str=float(input("Please input apple weight:"))

# 3.calculator cost
money=weight_str*price_str

# 4.ouput total price
print("apple price %3f $/kg, buy %f kg, need to pay %3f" %(price_str,weight_str,money))
