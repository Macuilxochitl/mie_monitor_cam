import os
import cv2
from numpy import ndarray
import Config
import time


class Cam(object):

    cap = None

    def __init__(self, cam_index: "index of cam in /dev" = 0):
        resolution = self.max_resolution
        w, h = resolution.split("x")
        w, h = float(w), float(h)

        self.cap = cv2.VideoCapture(cam_index)
        self.cap.set(3, w)
        self.cap.set(4, h)

    @property
    def resolution_list(self) -> list:
        ret = os.popen('''v4l2-ctl --list-formats-ext | egrep "Size: Discrete"''').read().split("\n")[:-1]
        for i in range(len(ret)):
            ret[i] = ret[i][ret[i].find("Discrete ") + 9:]
        ret = list(set(ret))
        return ret

    @property
    def max_resolution(self) -> str:
        resolutions = self.resolution_list
        max_len = -1
        for i in resolutions:
            if len(i) > max_len:
                max_len = len(i)

        max_res = []

        for i in resolutions:
            if len(i) >= max_len:
                max_res.append(i)

        return max(max_res)

    def get_image(self) -> ndarray:
        ret, frame = self.cap.read()
        if not ret:
            print("Get img error.")
            return None
        return frame

    def save_image(self) -> str:
        file_path = Config.tmp_path
        cv2.imwrite(file_path, self.get_image())
        return file_path

    def release(self):
        self.cap.release()
        time.sleep(1)
