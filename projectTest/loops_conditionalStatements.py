# We can use _ in a number for better code readability and it works fine too eg: 1000000 == 10_00_000

# if else
print("if else")
temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not hot outside.")

# if else if
print("\nif else if")
grade = 85
if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
else:
    print("You failed.")

# for loop
print("\nfor loop")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# while loop
print("\nwhile loop")
count = 0
while count < 5:
    print(count)
    count += 1

# break statement
print("\nbreak statement")
for i in range(1_0):
    if i == 5:  # Don't print after as 5 comes
        break
    print(i)


# continue statement
print("\ncontinue statement")
for i in range(10):
    if i % 2 == 0:  # print only odd
        continue
    print(i)

# print x numbers of time
noOfTimes = 3
print(noOfTimes * "Ujjwal-")