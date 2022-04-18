import datetime
import time
import sys

def save_log(msg, other = None):
    with open('logs.txt', 'a') as logs:
        dt = datetime.datetime.now()
        print(dt, msg, other, file=logs)

class Pycheck:

    def __init__(self, base_dangerous_words, testing_file):
        self.base_dangerous_words = base_dangerous_words
        self.testing_file = testing_file

    def show_dangerous_words(self):
        with open(self.base_dangerous_words, 'r') as dangerous_words:
            print('**********\nZakazane slowa: \n')
            for word in dangerous_words:
                print(word)
            print('**********')
        save_log('Wyswietlono liste slow zakazanych z pliku: ', self.base_dangerous_words)

    def py_check(self):
        try:
            with open(self.base_dangerous_words, 'r') as dangerous_words_checking:
                testing_file_2 = open(self.testing_file).read()
                testing_file_2 = testing_file_2.split()
                # testing_file_2 = testing_file_2.split()
                for anyword in testing_file_2:    
                    if anyword in dangerous_words_checking:
                        print('Program jest dla Ciebie szkodliwy')
                    else:
                        print('Program OK!')
        except Exception as error:
            print('Cos poszlo nie tak: >>> ', error)
        save_log('Sprawdzono plik: ', self.testing_file)

    def add_dangerous_word(self):
        try:    
            with open(self.base_dangerous_words, 'a') as dangerous_words:
                dangerous_words_2 = open(self.base_dangerous_words)
                dangerous_words_2 = dangerous_words_2.read()
                dangerous_words_2 = dangerous_words_2.split()

                word = str(input('Podaj nowe slowo do zakazania: '))
                if word not in dangerous_words_2:
                    print(f'Dodano slowo {word}')
                    print(word, file=dangerous_words)
                else:
                    print('To slowo juz jest w slowniku')
        except Exception as error:
            print('Wystapil blad: ', error)
        save_log(f'Dodano nowe slowo zakazane do slownika: {self.base_dangerous_words} pod kluczem: {word}')

    def remove_dangerous_word(self):
        with open(self.base_dangerous_words, 'r') as dangerous_words:
            word = input('Podaj slowo do usuniecia z listy slow zakazanych: ')
            if word in dangerous_words:
                # print(word, file=dangerous_words)
                print(f'Slowo {word} zostalo usuniete ze slownika // na razie trwa budowa tego etapu')
            else:
                print('Podane slowo nie istnieje w slowniku slow zakazanych')

try:
    pathway_dangerous_words = input('Podaj sciezke do pliku z lista slow zakazanych: >>> ')
    pathway_testing_file = input('Podaj sciezke do pliku ktory chcesz przetestowac: >>> ')
except Exception as error:
    print('Wykryto problem: ', error)

pychecker = Pycheck(pathway_dangerous_words, pathway_testing_file)

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
            save_log('Wybrano opcje: ', user_choice)
        elif user_choice == 2:
            pychecker.py_check()
            save_log('Wybrano opcje: ', user_choice)
        elif user_choice == 3:
            pychecker.add_dangerous_word()
            save_log('Wybrano opcje: ', user_choice)
        elif user_choice == 4:
            pychecker.remove_dangerous_word()
            save_log('Wybrano opcje: ', user_choice)
        elif user_choice == 5:
            save_log('Wybrano opcje: ', user_choice)
            sys.exit()
        else:
            print('Wprowadzona wartosc jest spoza przedzialu 1 - 4.')
            save_log('Wybrano opcje: ', user_choice)
    except Exception as error:
        print(f'Bledny wybor, kod bledu: {error}')
        save_log('Wystapil blad na etapie MENU: ', error)