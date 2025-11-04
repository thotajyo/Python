import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text) #re.sub() stands for substitute. It replaces all matches of a pattern in a string with a new value.
print("Modified text:", new_text)