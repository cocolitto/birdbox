import time
from gpiozero import  Button


trigger_in = Button("BOARD11")
trigger_out = Button("BOARD12")


if __name__ == "__main__":

    while True:
        if trigger_in.is_pressed:
            print("Bird flies in.")
            time.sleep(0.5)

        if trigger_out.is_pressed:
            print("Bird flies out.")
            time.sleep(0.5)