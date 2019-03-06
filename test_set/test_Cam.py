from Cam import Cam
from numpy import ndarray
import pytest


def test_cam_get_image():
    cam = Cam()
    assert type(cam.get_image()) == ndarray
