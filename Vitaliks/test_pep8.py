import string
import os
import math, time
# по одному імпорту на рядок
shift = 3
PI= 3.14
# треба пропуски з обох боків навколо =
def PrintTime(x):   # не PrintTime а  print_time
    if x == True:   #Не рекомендується порівнювати з True/False напряму → if x:
        print( time.ctime( ) )  #Лишні пробіли всередині дужок
        return

def main ():   #лишній пробіл перед дужками
    Choice_mode = input("would you like to encode or decode?")
    # не Choice_mode a choice_mode

    word = input("Please enter text")
    LETTERS = string.ascii_letters + string.punctuation + string.digits

    encoded = ""

    if Choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                x = LETTERS.index(letter) + shift
                encoded = encoded + LETTERS[x]
                y=x + 5   #відсутні пробіли навколо "="

    if Choice_mode == "decode":
        for letter in word:
            if letter == " ":
                encoded=encoded+" "   #відсутні пробіли навколо = і +
            else:
                x = LETTERS.index(letter)- shift  #відсутній пробіл навколо -
                encoded=encoded+ LETTERS[x]   #відсутні пробіли навколо = і +, та пробіл після + зайвий
                y= x - 5   #відсутній пробіл перед =

    print(encoded)
    print(Word)   #має бути word а не Word

if __name__ == '__main__':  #потрібно __main__ а не '__main__'
    main()
