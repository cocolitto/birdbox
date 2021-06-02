
import os
from datetime import datetime

DIR_STORE_ROOT = "/home/pi/images"

CAMERAS = {
    "front" : "/dev/video0",
    "rear"  : "/dev/video2"
}


def capture_command(name, dev):
    return f"fswebcam --no-banner --resolution=1280x720 --device={dev} {name}.jpg"


def capture_image(name, dev, dir):
    time_stamp = datetime.now().strftime("%F-%H-%M-%S")
    cli_cmd = capture_command(f"{dir}/{name}-{time_stamp}", dev)
    print("Capture: ", cli_cmd )
    capture_process = os.popen(cli_cmd)
    capture_log = capture_process.read()
    #print("Capture image: ")
    #print(capture_log)

if __name__ == "__main__":

    ## INIT
    if not os.path.exists(DIR_STORE_ROOT):
        print(f"Create directory '{DIR_STORE_ROOT}'")
        os.mkdir(DIR_STORE_ROOT)



    ## RECORDING
    dir_store = None
    day_label = None

    if True: # GPIO TRIGGER
        day_label = datetime.now().strftime("%F")


        if dir_store != day_label:
            dir_store = day_label

            if not os.path.exists(f"{DIR_STORE_ROOT}/{dir_store}"):
                print(f"Create directory '{DIR_STORE_ROOT}/{dir_store}'")
                os.mkdir(f"{DIR_STORE_ROOT}/{dir_store}")

        for camera in CAMERAS:
            capture_image(camera, CAMERAS[camera], f"{DIR_STORE_ROOT}/{dir_store}")


        # Take Picture

        # Store Image
