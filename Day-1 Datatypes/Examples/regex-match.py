import re

text = "The quick brown fox"

# match
m = re.match("quick", text)
print("Match:", m)  # None

# search
s = re.search("quick", text)
print("Search:", s.group())  # "quick"

#Use match() when you're checking if a string starts with a pattern (e.g., validating input).

#Use search() when you're looking for a pattern anywhere in the string (e.g., scanning logs, parsing text).