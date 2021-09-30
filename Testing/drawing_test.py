# 'for Loops' - when you know how many times to Loop
# 'while Loop' - Loop until a condition.
for i in range(10, -1, -1):
    print(i)

# Running total like the camel in desert miles
# Don't put total in the loop

total = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    total += new_number

print("The total is", total)

# while loop
i = 10
while i >= 0:
    print(i)
    i -+ 1



def count_up(start, end):
    for cur_number in range(start, end + 1):
        print(cur_number)

count_up(5, 10)

