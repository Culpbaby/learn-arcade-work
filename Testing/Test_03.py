x = "0123456789"

print("x=", x)
print("x[0]=", x[0])
print("x[1]=", x[1])
print("x[4]=", x[4])

# Up to but not including
print("x[:5]=", x[:5])
print("x[5:]=", x[5:])

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end="%")



plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x += 1
    c2 = chr(x)
    print(c2, end="")

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
print()
for c in encrypted_text:
    x = ord(c)
    x -= 1
    c2 = chr(x)
    print(c2, end="")


my_list = [4, 2, 56, 2, 0]

biggest_number = 0
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)
