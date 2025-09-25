"""Тестовий файл для ознайомлення з правилами форматування і оформлення коду згідно з PEP 8"""

import string
import time

SHIFT = 3
PI = 3.14


def print_time(flag: bool) -> None:
    """Виводить поточний час, якщо flag == True."""
    if flag:
        print(time.ctime())


def main() -> None:
    """Головна функція для кодування та декодування тексту."""
    choice_mode = input("Would you like to encode or decode? ")
    word = input("Please enter text: ")

    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""

    if choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = (letters.index(letter) + SHIFT) % len(letters)
                encoded += letters[x]

    elif choice_mode == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = (letters.index(letter) - SHIFT) % len(letters)
                encoded += letters[x]

    print(encoded)
    print(word)


if __name__ == "__main__":
    main()
