#import re: Loads Python’s regular expression module.

#text = "The quick brown fox": This is the string you're searching in.

#pattern = r"brown": The pattern you're looking for. r"" means it's a raw string, so backslashes are treated literally.

#re.search(pattern, text): Searches for the first match of the pattern in the text.

#search.group(): Returns the matched string if found.

import re

text = "The quick brown fox"
pattern = r"quick"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")