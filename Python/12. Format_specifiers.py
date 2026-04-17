#format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:.2f}") #to round of to 2 decimal places
print(f"price 2 is {price2:10}") #prints the value after 10 spaces
print(f"price 3 is {price3:010}") # 0 padding

#left justify
print(f"price 1 is ${price1:<10}") 
print(f"price 2 is {price2:<10}") 
print(f"price 3 is {price3:<10}") 

#right justify
print(f"price 1 is ${price1:>10}") 
print(f"price 2 is {price2:>10}") 
print(f"price 3 is {price3:>10}") 

#center align
print(f"price 1 is ${price1:^10}") 
print(f"price 2 is {price2:^10}") 
print(f"price 3 is {price3:^10}") 

#like this we have many flags (+,',', -, <, >, ^)