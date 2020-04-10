import pygame as pg

XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

TTT = [[None] * 3, [None] * 3, [None] * 3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
