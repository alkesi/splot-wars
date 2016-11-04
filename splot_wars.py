import numpy as np
import random as rndm
import sys
import time
import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0, 0, 0)

pygame.init()

def main_array(no_play, test_round):
    #if in testing, no_play has to equal to 0
    #creates the main array
    x = np.zeros([20, 20], dtype=np.int8)
    if no_play == 2 and test_round == 1:
        #2 zones that have randomly generated splots
        x[0:4, 0:4] = random_splot_generator(x[0:4, 0:4], 1)
        x[16:20, 16:20] = random_splot_generator(x[16:20, 16:20], 2)
    print(x)
    return x

def test_player_count(playno, test_round):
    if playno > 4:
        print("ERROR: There cannot be more than 4 players")
    if playno == 2 and test_round == 1:
        print("Initiating Test Round...")
    else:
        print("Initiating game for", playno, "player(s)")




def random_splot_generator(array, p):
    for i in array:
        for j in range(len(i)):
            r = rndm.random()
            if r > 0.7:
                i[j] = p
    return array


def main_spreading(array, play_count):
    arr_copy = np.copy(array)
    r,s = array.shape
    for i in range(r):
        for j in range(s):
            if array[i,j] == 0:
                a, b = border_control(r-1, i)
                c, d = border_control(r-1, j)
                x = array[a:b, c:d]
                if x.sum() == 0:
                    continue
                counted_colors = count_colors(x, play_count)
                arr_copy[i, j] = calc_spreading(counted_colors)
    return arr_copy


def calc_spreading(counted_colors):
    acc = 0
    for i in range(len(counted_colors)):
        counted_colors[i] += acc
        acc = counted_colors[i]
    rand_no = rndm.random()*acc
    for j in range(len(counted_colors)):
        if rand_no < counted_colors[j]:
            return j


def border_control(r, centre):
    if centre == 0:
        x = 0
    else:
        x = centre-1
    if centre == r:
        y = r
    else:
        y = centre+2
    return (x,y)

def count_colors(array, play_count):
    lst = [0]*(play_count+1)
    for i in range(len(array)):
        for j in range(len(array[0])):
            # Lasketaan kuinka monta samanarvoista solua on taulukossa
            lst[array[i][j]] += 1
    #lst[0] = 0
    return lst


def end_state(array, colors):
    x = 0
    y = 0
    r,s = array.shape
    for h in range(1,colors+1):
        hcount = 0
        for i in range(r):
            for j in range(s):
                if array[i,j] == h:
                    hcount += 1
        if x < hcount:
            x = hcount
            y = h
        print("pelaaja", h,":", hcount)
    print("pelaaja", y, "voitti pistemäärällä", x)



def find_zero(array):
    res = 0
    r,s = array.shape
    for i in range(r):
        for j in range(s):
            if array[i,j] == 0:
                res = 1
    return res


def game_loop():
    no_players = int(input("How many players are going to play? "))
    test_round = 0
    if no_players == 0:
        no_players = 2
        test_round = 1
    test_player_count(no_players, test_round)
    array = main_array(no_players, test_round)
    end = find_zero(array)
    draw(array, no_players)
    while end != 0:
        draw(array, no_players)
        array = main_spreading(array, no_players)
        print()
        print(array)
        end = find_zero(array)
        time.sleep(1)
    end_state(array, no_players)


# Here starts PyGame code.

def draw(array, player_count):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    r,s = array.shape
    colors = {1:red, 2:blue, 3:green, 4:darkBlue}
    for i in range(r):
        for j in range(s):
            for k in range(1, player_count+1):
                pygame.event.get()
                pygame.draw.rect(screen, black, (i*TILE_WIDTH,j*TILE_WIDTH,TILE_WIDTH,TILE_WIDTH), 3)
                if array[i][j] == k :
                    pygame.draw.rect(screen, colors[k], (i * TILE_WIDTH, j * TILE_WIDTH, TILE_WIDTH, TILE_WIDTH), 0)
    pygame.display.flip()

infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_h
TILE_WIDTH = SCREEN_WIDTH / 20
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.HWSURFACE)



game_loop()
