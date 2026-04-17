# Keyword Argumemt = an argument preceded by an identifier, helps with readability, order does not matter 

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr.", first="Harshit", last="Taneja")
hello("Hello", title="Ms.", first="Prisha", last="Acharya") #postional argument should never follow keyword argument


print("1", "2", "3", sep="->") #"sep=" is a built in keyword argument for the print function

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+1", area=561, first=480, last=9580)
print(phone_num)