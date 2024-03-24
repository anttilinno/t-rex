import os
import time

T_REX = "🦖"
CACTUS = "🌵"
ROAD = " \u0332"
SPACE = " "
STRIP_LENGTH = 81

def cls():
    os.system('clear')

cls()
cactus_position = STRIP_LENGTH

while True:
    if cactus_position < 0:
        cactus_position = STRIP_LENGTH 

    print(f"{STRIP_LENGTH * SPACE}")
    print(f"{cactus_position * ROAD}{CACTUS}")
    cactus_position -= 1
    time.sleep(0.1)
    cls()
