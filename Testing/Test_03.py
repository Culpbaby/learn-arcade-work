

my_list = [4, 2, 56, 2, 0]

biggest_number = 0
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)


def get_smallest(x):
    odds = []
    for i in x:
        if i < 2 != 0:
            odds.append(i)
    return min(odds)