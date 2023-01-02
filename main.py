import pygame
import sys
import numpy as np

pygame.init()
#Parameter
BREITE = 600
HOEHE = 600
LINIENBREITE = 15
BRETTREIHEN = 3
BRETTSPALTEN = 3
KREIS_RADIUS = 60
KREIS_BREITE = 15
SCHRAEGSTRICH_BREITE = 25
SCHRAEGSTRICH_FARBE = (66, 66, 66)
SPACE = 55

##rgb: red, green, blue
RED = (255, 0, 0)
Hintergrungfarbe = (28, 170, 156)
LINIE_Farbe = (23, 145, 135)
KREIS_FARBE = (239, 231, 200)

#Einstellungen des Bildschirms
screen = pygame.display.set_mode( (BREITE, HOEHE) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(Hintergrungfarbe)

#Brett
brett = np.zeros( (BRETTREIHEN, BRETTSPALTEN) )
#print(brett)

def gewinner_pruefen(spieler):
    #vertikaler Gewinner pruefen
    for spalte in range(BRETTSPALTEN):
        if brett[0][spalte] == spieler and brett[1][spalte] == spieler and brett[2][spalte] == spieler:
            vertikale_gewinn_linie_zeichnen(spalte, spieler)
            return True

    #horizontaler Gewinner pruefen
    for reihe in range(BRETTREIHEN):
        if brett[reihe][0] == spieler and brett[reihe][1] == spieler and brett[reihe][2] == spieler:
            horizontale_gewinn_linie_zeichnen(reihe, spieler)
            return True

    #asc diagonaller Gewinner pruefen
    if brett[2][0] == spieler and brett[1][1] == spieler and brett[0][2] == spieler:
        diagonalle_asc_gewinn_linie_zeichnen(spieler)
        return True

    # dsc diagonaller Gewinner pruefen
    if brett[0][0] == spieler and brett[1][1] == spieler and brett[2][2] == spieler:
        diagonalle_dsc_gewinn_linie_zeichnen(spieler)
        return True

    return False

def vertikale_gewinn_linie_zeichnen(spalte, spieler):
    posX = spalte * 200 + 100

    if spieler == 1:
        farbe  = KREIS_FARBE
    elif spieler == 2:
        farbe = SCHRAEGSTRICH_FARBE

    pygame.draw.line( screen, farbe, (posX, 15), (posX, HOEHE - 15), 15)
def horizontale_gewinn_linie_zeichnen(reihe, spieler):
    posY = reihe * 200 + 100

    if spieler == 1:
        farbe = KREIS_FARBE
    elif spieler == 2:
        farbe = SCHRAEGSTRICH_FARBE

    pygame.draw.line(screen, farbe, (15, posY), (BREITE - 15, posY), 15)
def diagonalle_asc_gewinn_linie_zeichnen(spieler):
    if spieler == 1:
        farbe = KREIS_FARBE
    elif spieler == 2:
        farbe = SCHRAEGSTRICH_FARBE

    pygame.draw.line(screen, farbe, (15, HOEHE - 15), (BREITE - 15, 15), 15)
def diagonalle_dsc_gewinn_linie_zeichnen(spieler):
    if spieler == 1:
        farbe = KREIS_FARBE
    elif spieler == 2:
        farbe = SCHRAEGSTRICH_FARBE

    pygame.draw.line(screen, farbe, (15, 15), (BREITE - 15, HOEHE - 15), 15)
def restart():
    screen.fill( Hintergrungfarbe )
    linien_zeichen()
    for reihe in range(BRETTREIHEN):
        for spalte in range(BRETTSPALTEN):
            brett[reihe][spalte] = 0

def linien_zeichen():
    #1.horizontale Linie
    pygame.draw.line( screen, LINIE_Farbe, (0, 200), (600, 200), LINIENBREITE)
    # 2.horizontale Linie
    pygame.draw.line(screen, LINIE_Farbe, (0, 400), (600, 400), LINIENBREITE)
    # 1.vertikale Linie
    pygame.draw.line(screen, LINIE_Farbe, (200, 0), (200, 600), LINIENBREITE)
    # 2.vertikale Linie
    pygame.draw.line(screen, LINIE_Farbe, (400, 0), (400, 600), LINIENBREITE)

def figuren_zeichnen():
    for reihe in range(BRETTREIHEN):
        for spalte in range(BRETTSPALTEN):
            if brett[reihe] [spalte] == 1:
                pygame.draw.circle(screen, KREIS_FARBE, (int( spalte * 200 + 200 / 2 ), int( reihe *200 + 200 / 2)), KREIS_RADIUS,KREIS_BREITE)
            elif brett [reihe] [spalte] == 2:
                pygame.draw.line(screen, SCHRAEGSTRICH_FARBE, (spalte * 200 + SPACE, reihe * 200 + 200 - SPACE), (spalte * 200 + 200 - SPACE, reihe * 200 + SPACE), SCHRAEGSTRICH_BREITE)
                pygame.draw.line(screen, SCHRAEGSTRICH_FARBE, (spalte * 200 + SPACE, reihe * 200 + SPACE), (spalte * 200 + 200 - SPACE, reihe * 200 + 200 - SPACE), SCHRAEGSTRICH_BREITE)
def kaestchen_kennzeichnen(reihe, spalte, spieler):
    brett [reihe][spalte] = spieler

def verfuegbare_kaestchen(reihe, spalte):
    return brett[reihe] [spalte] == 0
#    if brett[reihe] [spalte] == 0:
#        return True
#    else:
#        return False

def ob_brett_voll():
    for reihe in range(BRETTREIHEN):
        for spalte in range(BRETTSPALTEN):
            if brett[reihe][spalte] == 0:
                return False
    return True
# False
#print(ob_brett_voll())
# alle Kaestchen kennzeichnen
#for reihe in range(BRETTREIHEN):
#    for spalte in range(BRETTSPALTEN):
#        kaestchen_kennzeichnen(reihe, spalte, 1)
# Brett ist voll
#print(ob_brett_voll())

linien_zeichen()

spieler = 1
game_over = False

#Schleife für Bildschierm
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            ##print(mouseX)
            ##print(mouseY)

            mouse_click_reihe = int(mouseY //200)
            mouse_click_spalte = int(mouseX // 200)

            #print(mouse_click_reihe)
            #print(mouse_click_spalte)

            if verfuegbare_kaestchen(mouse_click_reihe, mouse_click_spalte):
                if spieler == 1:
                    kaestchen_kennzeichnen(mouse_click_reihe, mouse_click_spalte, 1)
                    if gewinner_pruefen(spieler):
                        game_over = True
                    spieler = 2

                elif spieler == 2:
                    kaestchen_kennzeichnen(mouse_click_reihe, mouse_click_spalte, 2)
                    if gewinner_pruefen(spieler):
                        game_over = True
                    spieler = 1

                figuren_zeichnen()
#                print(brett)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

    pygame.display.update()

