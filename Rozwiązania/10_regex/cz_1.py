import re


text = r"""To jest przykładowy tekst do ćwiczeń z wyrażeń regularnych! #regex

Email: user@example.com
Telefon: 123-456-789

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 42 In hac habitasse platea dictumst. @SpecialChar

Data: 2023-11-04
https://www.example.com

Znaki specjalne: !@#$%^&*()

(123) 456-7890

#regex #python #learningRegex
"""


def find_pattners(pattern, text_to_search):
    pattern = re.compile(pattern)
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)


# find_pattners(r"\d", text)
# find_pattners(r"\d{2,4}", text)
# find_pattners(r"#\w+", text)
find_pattners(r"\d{4}-\d{2}-\d{2}", text)

