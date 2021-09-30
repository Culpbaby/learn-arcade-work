import random

for i in range(20):
    my_number = random.randrange(5)
    if my_number == 0:
        print("Dragon!")
    else:
        print("No dragon.")
