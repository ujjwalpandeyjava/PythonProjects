from oops.Student import Student

s1 = Student()
print(s1)
print(s1.f_name)
print(s1.l_name)

s1.f_name = "UP - "
s1.l_name = "Ujjwal Pandey ji"
print("\nAfter update...")
print(s1.f_name + s1.l_name)