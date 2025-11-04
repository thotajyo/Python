#Swapping variables (Pythonic way)
a = 1
b = 2
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)

#Constants (by naming convention, though not enforced)
PI = 3.14159        # All uppercase indicates a constant
GRAVITY = 9.8
print("PI:", PI, "Gravity:", GRAVITY)


#Using variables in expressions
radius = 5
area = PI * radius ** 2   # Using a variable in calculation
print("Area of circle:", area)

first_name = "jyo"
last_name = "thota"

full_name = first_name + " " + last_name
print(full_name)