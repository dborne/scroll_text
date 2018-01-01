"""
For drawing 4 pixel high, scrolling text on the Adafruit NeoPixel FeatherWing
"""

import machine
import neopixel
from time import sleep
from os import urandom

GREEN =     (0, 5, 0)
RED =       (5, 0, 0)
BLUE =      (0, 0, 5)
YELLOW =    (6, 5, 0)
PINK =      (3, 1, 1)
BABY_BLUE = (0, 1, 3)
ORANGE =    (6, 2, 0)
PURPLE =    (4, 0, 6)

COLORS = [GREEN, RED, BLUE, YELLOW, PINK,
          BABY_BLUE, ORANGE, PURPLE]


def rand():
    """ get a random number from 0 to 255 """
    return ord(urandom(1))


def randrange(start, end):
    """ get a random number from 'start' to 'end' """
    return int(rand()/(256/(end-start))) + start


def choice(seq):
    """ get a random item from 'seq' """
    return seq[randrange(0, len(seq))]


# 'key': ([<pixels to light on the featherwing>], <width of character>)
letters = {
    'A': ([1,2,8,11,16,17,18,19,24,27], 4),
    'B': ([0,1,2,8,9,10,11,16,19,24,25,26], 4),
    'C': ([1,2,3,8,16,25,26,27], 4),
    'D': ([0,1,2,8,11,16,19,24,25,26], 4),
    'E': ([0,1,2,3,8,16,17,18,24,25,26,27], 4),
    'F': ([0,1,2,3,8,16,17,24], 4),
    'G': ([1,2,3,8,16,18,19,25,26,27], 4),
    'H': ([0,3,8,11,16,17,18,19,24,27], 4),
    'I': ([0,1,2,9,17,24,25,26], 3),
    'J': ([1,2,3,11,16,19,25,26], 4),
    'K': ([0,3,8,10,16,17,18,19,24,27], 4),
    'L': ([0,8,16,24,25,26], 3),
    'M': ([0,1,3,4,8,10,12,16,20,24,28], 5),
    'N': ([0,3,8,9,11,16,18,19,24,27], 4),
    'O': ([1,2,8,11,16,19,25,26], 4),
    'P': ([0,1,2,8,11,16,17,18,24], 4),
    'Q': ([1,2,8,11,16,18,19,25,26,27], 4),
    'R': ([0,1,2,8,11,16,17,18,24,27], 4),
    'S': ([1,2,3,8,9,18,19,24,25,26], 4),
    'T': ([0,1,2,9,17,25], 3),
    'U': ([0,3,8,11,16,19,25,26], 4),
    'V': ([0,3,8,11,16,18,24,25], 4),
    'W': ([0,4,8,12,16,18,20,24,25,27,28], 5),
    'X': ([0,3,8,11,17,18,24,27], 4),
    'Y': ([0,2,8,10,17,25], 3),
    'Z': ([0,1,2,3,10,17,24,25,26,27], 4),
    'a': ([9,16,18,25,26], 3),
    'b': ([0,8,9,16,18,24,25], 3),
    'c': ([9,10,16,25,26], 3),
    'd': ([2,9,10,16,18,25,26], 3),
    'e': ([1,8,9,10,16,25], 3),
    'f': ([1,8,16,17,24], 2),
    'g': ([0,1,8,9,10,18,25], 3),
    'h': ([0,8,16,17,18,24,26], 3),
    'i': ([0,16,24], 1),
    'j': ([8,9,10,18,24,25], 3),
    'k': ([0,8,10,16,17,24,26], 3),
    'l': ([0,8,16,25], 2),
    'm': ([8,9,11,16,18,20,24,28], 5),
    'n': ([8,9,16,18,24,26], 3),
    'o': ([9,16,18,25], 3),
    'p': ([0,1,8,10,16,17,24], 3),
    'q': ([1,2,8,10,17,18,26], 3),
    'r': ([8,9,16,24], 2),
    's': ([9,10,17,24,25], 3),
    't': ([1,8,9,10,17,25], 3),
    'u': ([8,10,16,18,24,25,26], 3),
    'v': ([8,10,16,18,25], 3),
    'w': ([8,12,16,18,20,25,27], 5),
    'x': ([8,10,17,24,26], 3),
    'y': ([8,10,17,24], 3),
    'z': ([8,9,17,25,26], 3),
    ' ': ([], 1),
    '1': ([1,8,9,17,25], 2),
    '2': ([0,1,2,10,11,16,17,24,25,26,27], 4),
    '3': ([0,1,2,3,10,19,24,25,26], 4),
    '4': ([0,8,10,16,17,18,19,26], 4),
    '5': ([0,1,2,3,8,9,18,19,24,25,26], 4),
    '6': ([1,2,8,16,17,18,19,24,25,26,27], 4),
    '7': ([0,1,2,3,11,18,25], 4),
    '8': ([1,2,8,9,10,11,16,19,24,25,26,27], 4),
    '9': ([0,1,2,3,8,9,10,11,19,25,26], 4),
    '0': ([1,2,8,10,11,16,17,19,25,26], 4),
    '.': ([24], 1),
    ',': ([17,24], 2),
    ':': ([0,16], 1),
    ';': ([1,17,24], 2),
    '!': ([0,8,24], 1),
    '?': ([0,1,2,3,10,11,26], 4),
    '"': ([0,2,8,10], 3),
    "'": ([0,8], 1),
    '-': ([16,17,18], 3),
    '+': ([9,16,17,18,25], 3),
    '*': ([0,2,9,16,18], 3),
    '/': ([3,10,17,24], 4),
    '(': ([1,8,16,25], 2),
    ')': ([0,9,17,24], 2),
    '=': ([8,9,10,24,25,26], 3),
    '[': ([0,1,8,16,24,25], 2),
    ']': ([0,1,9,17,24,25], 2),
    '{': ([1,2,8,17,25,26], 3),
    '}': ([0,1,10,17,24,25], 3),
    '@': ([1,2,3,8,10,11,16,25,26,27], 4),
    }


def draw_letter(letter, pos, np, color):
    """
    Draw letter offset horizontally by <pos> on the FeatherWing
    """
    for point in letter:
        for r in [range(0,8), range(8,16), range(16,24), range(24,32)]:
            if (point in r) and (point + pos in r):
                np[point + pos] = color


def scroll_text(text, np, speed=10, color=None):
    """
    Do the scrolling
    
    Pop letters off the string and move them across the screen till they're
    off the left side.
    
    Randomly color each letter if no color is given.
    """
    text = list(text)
    screen = []  # Letters on the screen
    while text or screen:
        if screen:
            if (screen[0]['pos'] + screen[0]['data'][1]) <= 0:
                # letter falls off left side
                screen.pop(0)
            if text and ((screen[-1]['pos'] + screen[-1]['data'][1]) < 9):
                # rightmost letter is all the way on the screen,
                # add another letter if any are left
                screen.append({'data': letters[text.pop(0)], 
                               'pos': 9, 
                               'color': color or choice(COLORS)})
        else:  # nothing on the screen yet
            screen.append({'data': letters[text.pop(0)], 
                           'pos': 9, 
                           'color': color or choice(COLORS)})
        for letter in screen:  # draw the screen
            draw_letter(letter['data'][0], letter['pos'], np, letter['color'])
            letter['pos'] -= 1  # scroll to the left
        np.write() 
        np.fill([0,0,0])
        sleep(.2/speed)


if __name__ == '__main__':
    np = neopixel.NeoPixel(machine.Pin(15), 32)
    scroll_text('Text to scroll goes here.', np)
