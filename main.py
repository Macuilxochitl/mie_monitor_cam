from Cam import Cam
from API import send_img_from_cam

if __name__ == "__main__":
    cam = Cam()
    while 1:
        send_img_from_cam(cam)
