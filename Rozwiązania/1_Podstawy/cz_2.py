text = ("Skopiuj treść tego zadania i przypisz do nowo utworzonej zmiennej text. Następnie"
        " utwórz kilka nowych zmiennych: text_lower, text_upper, text_capitalize oraz"
        "text_title, do których przypiszesz odpowiednio przekształconą zmienną"
        " text i wyprintuj je.")

text_lower = text.lower()
text_upper = text.upper()
text_capitalize = text.capitalize()
text_title = text.title()

half_text = text[:int(len(text)/2)]
print(half_text)

my_input = input("Input any text: ")

print(f"Powyższy tekst posiada {len(my_input)} znaków")
