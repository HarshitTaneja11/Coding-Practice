# AND = both conditons must be true
# OR = at least one condition must be true
# NOT = inverts  the condition

temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Event is cancelled :(")
else:
    print("Event will be held")