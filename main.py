import os
import threading
import time
from queue import Queue
from pynput import keyboard

T_REX = "🦖"
CACTUS = "🌵"
ROAD = " \u0332"
SPACE = " "
STRIP_LENGTH = 80

def cls():
    os.system('clear')

def on_press(key):
    try:
        if key == keyboard.Key.space:
            queue.put(True)
        elif key == keyboard.Key.esc:
            print("Quitting...")
            return False
    except AttributeError:
        pass

def animation_thread(queue):
    jump = False
    cactus_position = STRIP_LENGTH
    dinosaur_position = 0

    cls()

    while True:
        if not queue.empty():
            jump = queue.get()  # Get the latest position from the queue
            if jump:
                print(f"{dinosaur_position * SPACE}{T_REX}")
                print(f"{STRIP_LENGTH * SPACE}")
                dinosaur_position += 1
                cactus_position -= 1
                time.sleep(0.5)
                continue

        if cactus_position < 0:
            cactus_position = STRIP_LENGTH 
        if dinosaur_position > STRIP_LENGTH:
            dinosaur_position = 0

        if dinosaur_position < cactus_position:
            print(f"{STRIP_LENGTH * SPACE}")
            print(f"{dinosaur_position * ROAD}{T_REX}{(cactus_position - dinosaur_position) * ROAD}{CACTUS}{(STRIP_LENGTH - cactus_position) * ROAD}")
        elif dinosaur_position > cactus_position:
            print(f"{STRIP_LENGTH * SPACE}")
            print(f"{cactus_position * ROAD}{CACTUS}{(dinosaur_position - cactus_position) * ROAD}{T_REX}{(STRIP_LENGTH - dinosaur_position) * ROAD}")
        elif dinosaur_position == cactus_position:
            print(f"{(STRIP_LENGTH - dinosaur_position) * SPACE}{CACTUS}")
            print(f"{dinosaur_position * ROAD}{T_REX}{(STRIP_LENGTH - dinosaur_position) * ROAD}")

        cactus_position -= 1
        dinosaur_position += 1
        time.sleep(0.5)
        cls()

if __name__ == "__main__":
    print("Press arrow keys to move. Press 'Esc' to quit.")

    # Create a thread-safe queue to pass information between threads
    queue = Queue()

    # Start animation thread
    animation_thread = threading.Thread(target=animation_thread, args=(queue,))
    animation_thread.daemon = True
    animation_thread.start()

    # Create the input listener thread
    input_thread = keyboard.Listener(on_press=on_press)

    # Start the input thread
    input_thread.start()

    # Wait for animation thread to finish (which never happens)
    input_thread.join()
