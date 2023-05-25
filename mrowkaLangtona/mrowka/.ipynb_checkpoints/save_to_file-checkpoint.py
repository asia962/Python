"""Moduł służacy do zapisywania wyników działa programu do pliku"""
import tkinter

def save_picture(board, size):
    """Funkcja przedstawiająca wyniki działania programu w graficznym interfejsie (z wykorzystaniem biblioteki tkiner)"""
    #otwieram główne okno aplikacji
    root = tkinter.Tk()
    #ustalam rozmiar okna
    window_size = 400
    #tworzę kontrolkę canvas, która służy do rysowania po niej elementów graficznych. 
    canvas = tkinter.Canvas(root, width=window_size, height=window_size)
    #podppinanie kontrolki pod okno
    canvas.pack()
    #tworzę zmienną s która  określa rozmiar pojedynczych kwadracików w stworzonym oknie
    s = window_size / size
    #pętla przechodzi po kolejnych elementrach tablicy i jeśli natrafi na 1, tworzy czarny kwadracik, w miejscu wyznaczonym przez współrzędne
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            color = "white" if field == 0 else "black"
            canvas.create_rectangle(
                s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
            )
    #zapisanie wyniku do pliku
    canvas.postscript(file="picture.eps")   
 
   #uruchomienie głównej pętli 
    root.mainloop()

def save_text(name, moves, black, white):
    """Fukcja zapisujące podstawe informacje na temat działania programu do pliku txt"""
    #otwarcie pliku
    file = open(name, 'wt')
    #zapisywanie do pliku
    file.writelines("Wynik działania progamu Mrówka Langtona: \n")
    file.writelines(f"Mrówka wykonała {moves} kroków! \n")
    file.writelines(f"Końcowa liczba czarnych pól to: {black} a białych:  {white} ")
    #zamknięcie pliku
    file.close()