# Switch statement - alternative to using multiple if elif statements


def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:  # Default case
            return "Not a valid day"


print(day_of_week(1))
print(day_of_week(3))
print(day_of_week("W"))
