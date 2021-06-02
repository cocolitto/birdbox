import time
import os
from datetime import datetime

import camera_test as cmt
from gpiozero import  Button

trigger_in = Button("BOARD11")
trigger_out = Button("BOARD12")

CAMERAS = {
    "front" : "/dev/video0",
    "rear"  : "/dev/video2"
}

if __name__ == "__main__":
    ## INIT
    if not os.path.exists(cmt.DIR_STORE_ROOT):
        print(f"Create directory '{cmt.DIR_STORE_ROOT}'")
        os.mkdir(cmt.DIR_STORE_ROOT)


    ## RECORDING
    dir_store = None
    day_label = None

    while True:
        if trigger_in.is_pressed: # GPIO TRIGGER
            time.sleep(1)

            day_label = datetime.now().strftime("%F")

            if dir_store != day_label:
                dir_store = day_label

                if not os.path.exists(f"{cmt.DIR_STORE_ROOT}/{dir_store}"):
                    print(f"Create directory '{cmt.DIR_STORE_ROOT}/{dir_store}'")
                    os.mkdir(f"{cmt.DIR_STORE_ROOT}/{dir_store}")

            for camera in CAMERAS:
                cmt.capture_image(camera, CAMERAS[camera], f"{cmt.DIR_STORE_ROOT}/{dir_store}")