
"""Moduł służacy do pobierania danych od użytkownika"""
import os

def get_date():
    """Pobieranie danych od użytkownika z uwzględnieniem obsługi wyjątków"""

    #sprawdzenie czy użytkownik wprowadził poprawne dane
    while True:
        try:
            moves = int(input("Podaj ilośc kroków jaką ma wykonac mrówka: "))
            if moves > 0:
                #jeżeli użytkownik wprowadził dane w odpowiedniej formie(int) oraz podana liczba jest większa od zera wychodzimy z pętli
                break
            else:
                print("Wpowadzona wartość nie może być ujemna. Wprowadź liczbę całkowita dodatnią")
        except ValueError:
            print("Podałeś nieprawidłową formę danych. Wprowadź liczbę całkowitą")


    while True:
        try:
            size = int(input("Podaj wymiar planszy (a x a) po której ma poruszać się mrówka: "))
            if size > 0:
                break
            else:
                print("Wpowadzona wartość nie może być ujemna. Wprowadź liczbę całkowita dodatnią")
        except ValueError:
            print("Podałeś nieprawidłową formę danych. Wprowadź liczbę całkowitą")


    while True:
        try:
            wait = int(input("Podaj okres przerwy pomiędzy wyświetlaniem kolejnych kroków mrówki (ms): "))
            if wait >= 0:
                break
            else:
                print("Wpowadzona wartość nie może być ujemna. Wprowadź liczbę całkowita dodatnią")
        except ValueError:
            print("Podałeś nieprawidłową formę danych. Wprowadź liczbę całkowitą")



    name = input('Podaj nazwę pliku do którego zostaną zapisane wyniki działania programu np result.txt: ')
    while True:
        #spradzamy czy plikl o podanej nazwie już nie istnieje
        if os.path.exists(name):
            print(f"Plik {name} istnieje.")
            name = input('Podaj inną nazwę: ')
        # Jeśli użytkownik nie poda nazwy pliku, to ustawiona jest wartość domyślna
        elif name == '':
           name = 'result.txt'
        else:
            break

    return moves, size, wait, name