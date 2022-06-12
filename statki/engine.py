import random


class Ship:
    def __init__(self, size):
        self.row = random.randrange(0,9)
        self.col = random.randrange(0, 9)
        self.size = size
        self.orientation = random.choice(["h", "v"])
        self.indexes = self.get_indexes()

    def get_indexes(self):
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i * 10 for i in range(self.size)]


class Player:
    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100)] #U - unknown
        self.place_ship([5, 4, 3, 2, 1])
        indexes_list = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in indexes_list for index in sublist]


    def checkIfPossible(self, ship):
        #check if placement is possible
        placement_possible = True
        for i in ship.indexes:
            if i >= 100:
                placement_possible = False
                break
            #avoid snake behavior
            new_row = i//10
            new_col = i%10
            if new_row != ship.row and new_col != ship.column:
                placement_possible = False
            #avoid intersect
            for ship in self.ships:
                if i in ship.indexes:
                    placement_possible = False
                    break
        return placement_possible

    def place_ship(self, sizes):
        for s in sizes:
            placed = False
            while not placed:
                sh = Ship(s)
                placement_possible = True
                for i in sh.indexes:
                    if i >= 100:
                        placement_possible = False
                        break
                    # avoid snake behavior
                    new_row = i // 10
                    new_col = i % 10
                    if new_row != sh.row and new_col != sh.col:
                        placement_possible = False
                    # avoid intersect
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            placement_possible = False
                            break
                if placement_possible:
                    self.ships.append(sh)
                    placed = True


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player1_turn = True
        self.over = False
        self.result = None

    def make_move(self, i):
        player = self.player1 if self.player1_turn else self.player2
        opponent = self.player2 if self.player1_turn else self.player1
        hit = False
        # set misses M and hits H
        if i in opponent.indexes:
            player.search[i] = "H"
            hit = True
            #check if ship is sunk
            for ship in opponent.ships:
                sunk = True
                for i in ship.indexes:
                    if player.search[i] == "U":
                        sunk = False
                        break
                if sunk:
                    for i in ship.indexes:
                        player.search[i] = "S"
        else:
            player.search[i] = "M"

        #check if game over
        game_over = True
        for i in opponent.indexes:
            if player.search[i] == "U":
                game_over = False
        self.over = game_over
        self.result = 1 if self.player1_turn else 2
        if not hit:
            self.player1_turn = not self.player1_turn