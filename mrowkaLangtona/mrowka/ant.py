# import potrzebnych modułów
from pprint import pprint
import numpy as np
import date
import time
import os
import save_to_file


class Array():
    """Klasa Array zawiera metody potrzebne do stworzenia mecierzy po któej będzie poruszać się mrówka"""

    def __init__(self, size):
        """metoda to metoda specjalna, wykonuuje sie za kazdym razem przy tworzeniu obiektu"""
        self.size = size

    def create_board(self):
        """Program tworzący macierz, po ktorej poruszać się będzie mrówka"""
        # funkcja zwraca macierz o podanych wymiarach - do stworzenia macierzy wykorzystuje biblioteke numpy
        return np.zeros(shape=(self.size, self.size))

    def initial_coordinates(self):
        """Metoda wyznaczjąca początkową wartość wspórzędnych (porządkowe polozenie mrowki)"""
        coord = self.size // 2
        return coord

    def clear():
        """Metoda czyszcząca ekran po każdym kroku mrówki"""
        # Jeśli windows, os.name zwraca 'nt'
        if os.name == 'nt':
            # Czyszczenie ekranu w systemie Windows
            os.system('cls')
        else:
            # Czyszczenie ekranu w Linukxie, macOS itd
            os.system('clear')


class Ant():
    """Klasa mrówka zawiera informacje an temat poruszania się mrówki, zmian kolorów pól itp"""

    def __init__(self, board, x, y, wait):
        self.board = board
        self.y = y
        self.x = x
        self.wait = wait
        # ustawiamy poczatkowy kierunek mrówki
        self.coordinates = (0, -1)

    def moves(self):
        """Metoda określająca parametry ruchów mrówki"""
        # tworzy słownik skłądający się z tupli i określający w którą stronę ma poruszyć się mrówka w zależności od tego w jakką stronę jest obecnie obrócona oraz na jakim polu się znajduje
        # kierunek mrówki oznaczony jest w następujący sposób: N(-1,0), E(0, 1), S(1, 0), W(0, -1)
        coord_moves = {
            "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
            "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
        }

        # tworzenie zmiennej która okresla aktualne polozenie mrówki
        field = self.board[self.y][self.x]
        # tworzenie zmiennej która określa kierunek ruchu mrówki - jeżeli pole jest różne od 0 to przypisujemy zmiennej wartość L
        # w przeciwnym wypadku mrówka przypisujemy zmiennej wartość R
        moves = "L" if field else "R"
        # odczytanie przesunięcie mrówki z wcześniej stworzonego słownika
        self.coordinates = coord_moves[moves][self.coordinates]
        # zmiana wartości pola na tkóym zjadowała się mrówka (jeśli było 0 to 1 i na odwrót)
        self.board[self.y][self.x] = 0 if field else 1
        # przesunięcie mrówki o wartość odczytną ze słownika
        self.y = self.y + self.coordinates[0]
        self.x = self.x + self.coordinates[1]

    def show_result(self, moves_number):
        """Pętla służaca do pokazywania kolejnych ruchów mrówki i zmian koloru pól"""
        # iterator pętli
        i = 1
        # Pętla wykonuję się dopóki i jest mniejsze lub równe liczbie ruchów wskazanej przez użtkownika
        while i <= moves_number:
            # Obsługa wyjątków - jeżeli okazałoby się że użytkownik podał zbyt mały rozmiar tablicy w stosunku do ilości
            # ruchów mrówki i mrówka przekroczyła by jej zakres
            try:
                self.moves()
            except IndexError:
                print(
                    "Podana ilość ruchów przekracza wskazany rozmiar tablicy. \nSpróbuj uruchomić program ponownie, deklarującR większy wymiar")
                break
            # czyszczenie ekranu po każdym ruchu
            Array.clear()
            print(f"Krok: {i}")
            print(f"Aktualne wpółrzędne mrówki: {self.x}, {self.y}")
            # w celu lepszej wizualizacja, zamiana każdego pola z numerem 1 na pole zapełnione
            # pętla przechodzi po kolejnych wierszach i polach w każdym wierszu
            for row in board:
                for field in row:
                    print(f"[{'█' if field == 1 else ' '}]", end="")
                print()
                # print(self.board)
            # zatrzymanie widoku na określony czas
            time.sleep(self.wait)
            i += 1

    def number_black_fields():
        """Metoda zliczająca po wykonaniu programu ilość pól czarnych i białych w tablicy"""
        counter = 0
        counter2 = 0
        for row in board:
            for field in row:
                if field == 1:
                    counter += 1
                else:
                    counter2 += 1
        return counter, counter2


# zapisanie do zmiennych danych pobranych od użytkownika
moves, size, wait, name = date.get_date()
# przekształcenie zmiennej z ms na s
wait = float(wait / 100)
# tworzy tablicę klasy Array z wykorzystaniem metody create_board
board = Array(size).create_board()
# tworzy obieky x, y klasy Array przechowujący informacje o współrzędnych
x = Array(size).initial_coordinates()
y = Array(size).initial_coordinates()
# tworzy obiek klasy mrówka
ant1 = Ant(board, x, y, wait)
ant2 = Ant(board, 1, 1, wait)
# wywołuje na obiekcie metodę show_result
#ant1.show_result(moves)
ant2.show_result(moves)
# wywoluje z modulu save_to_file funkcje zapisującą obraz do pliku
save_to_file.save_picture(board, size)
# zapisujemy do zmiennej ilość pól białych i czarnych
black, white = Ant.number_black_fields()
# wywoluje z odulu save_to_file funkcje zapisującą plik tekstowy
save_to_file.save_text(name, moves, black, white)
