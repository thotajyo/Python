#Basic Structure of a Conditional Statement
#if condition:
    # code block to run if condition is True
#elif another_condition:
    # code block if first is False but this is True
#else:
    # code block if none of the above are True
age = 18

if age >= 18:
    print("You are an adult.")

age = 15
if age >= 18:
    print("youre an adult.")
else:
    print("Youre not an adult")