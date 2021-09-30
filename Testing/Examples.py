def sum_two_numbers(a, b):
    result = a + b
    return result
sum_two_numbers(3, 2)

# Slope finder
def calculate_line_slope(x1, y1, x2, y2):
    m=(y2-y1)/(x2-x1)
    result = m
    return result

calculate_line_slope(2, 3, 4, 5)


# Write your code here

def compare_values(a, b):
    if a < b:
        return("less")
    elif a > b:
        return("greater")
    else:
        return("equal")

compare_values(5, 6)

def simpson_check(a):
    if a == simpson:
        return("Match")
    else:
        return("No match")


simpson_check(simpson)


