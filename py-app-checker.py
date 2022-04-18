import datetime
import time
import sys


class Pycheck:

    def __init__(self, base_dangerous_words, testing_file):
        self.base_dangerous_words = base_dangerous_words
        self.testing_file = testing_file

    def save_log(self):
        pass

    def show_dangerous_words(self):
        with open(self.base_dangerous_words, 'r') as dangerous_words:
            print('**********\nZakazane slowa: \n')
            for word in dangerous_words:
                print(word)
            print('**********')

    def py_check(self):
        pass

    def add_dangerous_word(self):
        with open(self.base_dangerous_words, 'a') as dangerous_words:
            word = input('Podaj nowe slowo do zakazania: ')
            if word not in dangerous_words:
                print(word, file=dangerous_words)
                print(f'Slowo {word} zostalo dodane do slownika')
            else:
                print('Podane slowo jest juz w slowniku slow zakazanych')

    def remove_dangerous_word(self):
        with open(self.base_dangerous_words, 'w') as dangerous_words:
            word = input('Podaj slowo do usuniecia z listy slow zakazanych: ')
            if word in dangerous_words:
                print(word, file=dangerous_words)
                print(f'Slowo {word} zostalo usuniete ze slownika')
            else:
                print('Podane slowo nie istnieje w slowniku slow zakazanych')

pychecker = Pycheck('dangerous_words.txt', 'testing_file.py')

while True:
    try:
        print('Wprowadz 1 aby wyswietlic liste slow zakazanych.')
        print('Wprowadz 2 aby sprawdzic czy program zawiera slowa zakazane.')
        print('Wprowadz 3 aby dodac slowo zakazane do slownika.')
        print('Wprowadz 4 aby usunac slowo zakazane ze slownika.')
        print('Wprowadz 5 aby zamknac program.')
        print()

        user_choice = int(input('Wybierz opcje: >>> '))

        if user_choice == 1:
            pychecker.show_dangerous_words()
        elif user_choice == 2:
            pychecker.py_check()
        elif user_choice == 3:
            pychecker.add_dangerous_word()
        elif user_choice == 4:
            pychecker.remove_dangerous_word()
        elif user_choice == 5:
            sys.exit()
        else:
            print('Wprowadzona wartosc jest spoza przedzialu 1 - 4.')
    except Exception as error:
        print(f'Bledny wybor, kod bledu: {error}')