# Python data types
from PIL.ImImagePlugin import number

# Numeric Types
# Integer examples
x = 42
y = -10
print("Integer examples:")
print("x =", x)
print("y =", y)

# Float examples
a = 3.14
b = -0.001
print("\nFloat examples:")
print("a =", a)
print("b =", b)

# Complex examples
c = 3 + 4j
d = 2 - 3j
print("\nComplex examples:")
print("c =", c)
print("d =", d)

# Sequence Types
# String examples
name = "Alice"
message = 'Hello, World!'
print("\nString examples:")
print("name =", name)
print("message =", message)

# List examples
fruits = ['apple', 'banana', 'cherry']
body = ["Eyes", "Head", "Leg"]
numbers = [1, 2, 3, 4, 6, 5, 4]
print("\nList examples:")
print("fruits =", fruits)
print("body =", body)
print("numbers =", numbers)                     # Print full list
print(f"First element: {numbers[0]}")           # From start index
print(f"Last element: {numbers[-1]}")           # From last index
print(f"From to: {numbers[1:4]}")               # From start x to start y (excluded last)
print(f"From to negative: {numbers[1:-2]}")     # From start x to last y (excluded last)
print(f"Count: {len(numbers)}")
print(f"Repeated '4' times: {numbers.count(4)}")
numbers.append(89)                              # Add object y in last
numbers.insert(2, 90)           # Insert at index x object y
print(f"Updated list: {numbers}")
numbers.remove(1)                               # Remove form index (works from 1)
print(f"Updated list: {numbers}")


# Tuple examples
point = (2, 3)
person = ('Alice', 25, 'Engineer')
print("\nTuple examples:")
print("point =", point)
print("person =", person)

# Mapping Type
# Dictionary examples
person_dict = {'name': 'Alice', 'age': 25, 'occupation': 'Engineer'}
grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
print("\nDictionary examples:")
print("person_dict =", person_dict)
print("grades =", grades)

# Set Types
# Set examples
colors = {'red', 'green', 'blue', 'green'}
unique_numbers = {1, 2, 3, 4, 5}
print("\nSet examples:")
print("colors =", colors)
print("unique_numbers =", unique_numbers)

# Frozenset examples
immutable_colors = frozenset({'red', 'green', 'blue'})
print("\nFrozenset example:")
print("immutable_colors =", immutable_colors)

# Boolean Type
# Boolean examples
is_student = True
has_paid = False
print("\nBoolean examples:")
print("is_student =", is_student)
print("has_paid =", has_paid)

# Binary Types
# Bytes examples
data = b'Hello'
print("\nBytes example:")
print("data =", data)

# Bytearray examples
mutable_data = bytearray(b'Hello')
print("\nBytearray example:")
print("mutable_data =", mutable_data)

# Memoryview examples
view = memoryview(b'Hello')
print("\nMemoryview example:")
print("view =", view)

# Special Data Type
# NoneType example
result = None
print("\nNoneType example:")
print("result =", result)

# Instructions to Run the Script
## 1. **Create a new file**: Open your text editor or IDE and create a new file named `data_types_example.py`.
## 2. **Copy and Paste**: Copy the code provided above and paste it into the newly created file.
## 3. **Save the file**: Save the file to ensure all changes are stored.
## 4. **Run the script**: Open a terminal or command prompt, navigate to the directory where the file is saved, and run the script using the following command:
''' 
    # bash
    python data_types_example.py
'''