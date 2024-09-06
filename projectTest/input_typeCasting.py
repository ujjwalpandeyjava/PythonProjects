from datetime import datetime

# Print statement
print('Single quote')
print("Double quote can print ' too")
arr = [1, 2, 4, 6, 9]
print(f'With variables quote {arr}\n')
for num in arr:
    print(num)
print("\n")
for num in arr:
    print(num, end="\n") # Same as above
print("\n")
for num in arr:
    print(num, end=" ")
print("\n")
for num in arr:
    print(num, end="+")
print("\n")



# Take input from user
userName = input("\nEnter your name: ")  # return string
print(f"user name: >>{userName}<<")

userAge= input("What is you date of birth: ")
# int(userAge) is called type casting
print(f"Your are approx {datetime.now().year - int(userAge)} years old")
print(f"Your are approx in float {datetime.now().year - float(userAge)} years old")


## calculation
val1 = input("Enter number 1: ")
val2 = input("Enter number 2: ")
print(f"sum as float: {int(val1) + float(val2)}")