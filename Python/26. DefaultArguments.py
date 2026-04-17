# A default value for certain parameters
# default is used when that argument is omitted, it makes your functions more flexible, reduces # of args
# 1. positional, 2. default, 3.keyword, 4.arbitrary

def net_price(list_price, discount = 0.1, tax = 0.05):
    return list_price * (1-discount) * (1+tax)

print(net_price(500))
print(net_price(500,0.2)) #if we enter a argument then the default value is changed only for that function call


#-----------------------------------------------------------------------------

import time

def count(end, start = 0): # default arguments should always be after non default arguments
    for x in range(start, end+1):
        print(x)
        time.sleep(1) # to add a delay of 1 second
    print("DONE!!")

# count(3)
count(10,1)

 