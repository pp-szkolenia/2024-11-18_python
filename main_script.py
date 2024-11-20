import re  # regular expressions


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

. ^ $ * + ? { } [ ] \ | ( )
- _ = /

253-234-623
321-555-4321
5135-2446-1533

123.555.1234
123*555*1234
'''

r"""
## Znaki specjalne
```
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
```
"""


def find_pattners(pattern, text_to_search):
    pattern = re.compile(pattern)
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)


# find_pattners(".", text_to_search)
# find_pattners(r"\D", text_to_search)
# find_pattners(r"\w", text_to_search)

# find_pattners(r"\.", text_to_search)
# find_pattners(r"\\", text_to_search)
find_pattners(r"3\.5", text_to_search)
