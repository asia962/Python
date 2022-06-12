import pygame
from engine import *

pygame.init()
pygame.display.set_caption('Battleship game')
pygame.font.init()
myfont = pygame.font.SysFont("fresansttf", 100)

play = True
pause = False

B_SIZE = 35
MARGIN_H = B_SIZE * 4
MARGIN_V = B_SIZE
WIDTH = B_SIZE * 10 * 2 + MARGIN_H
HEIGHT = B_SIZE * 10 * 2 + MARGIN_V
GREY = (40, 50, 60)
WHITE = (255, 250, 250)
GREEN = (50, 200, 150)
RED = (250, 50, 100)
BLUE = (50, 150, 200)
ORANGE = (250, 140, 20)
COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED}
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_grid(player, left=0, top=0, search=False):
    for i in range(100):
        x = left + i % 10 * B_SIZE
        y = top + i // 10 * B_SIZE
        square = pygame.Rect(x, y, B_SIZE, B_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, 3)
        if search:
            x += B_SIZE // 2
            y += B_SIZE // 2
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], (x, y), radius=B_SIZE // 4)


def draw_ships(player, left=0, top=0):
    for ship in player.ships:
        x = left + ship.col * B_SIZE
        y = top + ship.row * B_SIZE
        IMAGE_POSITION = (x, y)
        if ship.orientation == 'h':
            if ship.size == 5:
                ship_image = pygame.image.load("images\AircraftCarrier.png")
            elif ship.size == 4:
                ship_image = pygame.image.load("images\BattleShip.png")
            elif ship.size == 3:
                ship_image = pygame.image.load("images\Cruiser.png")
            elif ship.size == 2:
                ship_image = pygame.image.load("images\Submarine.png")
            else:
                ship_image = pygame.image.load("images\PatrolBoat.png")
            width = ship.size * B_SIZE
            height = B_SIZE
            IMAGE_SIZE = (width, height)
            ship_image = pygame.transform.scale(ship_image, IMAGE_SIZE)
        else:
            if ship.size == 5:
                ship_image = pygame.image.load("images\AircraftCarrierV.png")
            elif ship.size == 4:
                ship_image = pygame.image.load("images\BattleShipV.png")
            elif ship.size == 3:
                ship_image = pygame.image.load("images\CruiserV.png")
            elif ship.size == 2:
                ship_image = pygame.image.load("images\SubmarineV.png")
            else:
                ship_image = pygame.image.load("images\PatrolBoatV.png")
            width = B_SIZE
            height = ship.size * B_SIZE
            IMAGE_SIZE = (width, height)
            ship_image = pygame.transform.scale(ship_image, IMAGE_SIZE)
            #ship_image = pygame.transform.rotate(ship_image, 180)
        SCREEN.blit(ship_image, IMAGE_POSITION)


game = Game()

while play:
    for event in pygame.event.get():
        # if we close window
        if event.type == pygame.QUIT:
            play = False
        #if user click on mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if not game.over and game.player1_turn and x < B_SIZE*10 and y < B_SIZE*10:
                row = y//B_SIZE
                col = x//B_SIZE
                index = row * 10 + col
                game.make_move(index)
            elif not game.over and not game.player1_turn and x > WIDTH - B_SIZE*10 and y >B_SIZE*10 + MARGIN_V:
                row = (y - B_SIZE*10 - MARGIN_V)//B_SIZE
                col = (x - B_SIZE*10 - MARGIN_H)//B_SIZE
                index = row * 10 + col
                game.make_move(index)

        if event.type == pygame.KEYDOWN:
            # if excape close window
            if event.key == pygame.K_ESCAPE:
                play = False
            #restart
            if event.key == pygame.K_RETURN:
                game = Game()

    SCREEN.fill(GREY)
    # search grid
    draw_grid(game.player1, search=True)
    draw_grid(game.player2, search=True, left=(WIDTH - MARGIN_H) // 2 + MARGIN_H, top=(HEIGHT - MARGIN_V) // 2 + MARGIN_V)

    # position grif
    draw_grid(game.player1, (WIDTH - MARGIN_H) // 2 + MARGIN_H)
    draw_grid(game.player2, top=(HEIGHT - MARGIN_V) // 2 + MARGIN_V)

    draw_ships(game.player1, top=(HEIGHT - MARGIN_V) // 2 + MARGIN_V)
    draw_ships(game.player2, left=(WIDTH - MARGIN_H) // 2 + MARGIN_H)


    if game.over:
        text = "Player " + str(game.result) + " wins!"
        textbox = myfont.render(text, False, GREY, WHITE)
        SCREEN.blit(textbox, (WIDTH//2 - 240, HEIGHT//2 - 50))
    pygame.display.flip()
