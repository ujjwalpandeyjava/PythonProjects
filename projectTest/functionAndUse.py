def sumNum(a, b):
    return a+ b

print(sumNum(1, 3))
print(sumNum(13, 3))


print(sum([4, 32]))         # one in-built function

# Can take any numbers of arguments and provides average
def average(*args):
    if not args:
        return None  # or raise an exception
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))  # Output: 3.0
print(average(10, 20, 30))  # Output: 20.0