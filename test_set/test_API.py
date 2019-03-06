from Cam import Cam
from API import send_img_from_cam
import pytest


def test_send_img():
    cam = Cam()
    assert send_img_from_cam(cam).status_code == 200
