q = 10

for i in range(1, q + 1):
    print("*" * i)

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

while x != y:
    print("x and y are not equal.")
    x = int(input("Enter a new value for x: "))
    y = int(input("Enter a new value for y: "))

print("x and y are now equal.")


