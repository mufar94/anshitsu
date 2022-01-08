import os

from anshitsu import retouch
from PIL import Image


def test_noise_by_rgb():
    image = Image.open(
        os.path.join(".", "tests", "pic", "dog.jpg"),
    )
    rt = retouch.Retouch(image=image, noise=10.0)
    pict = rt.process()
    assert pict.mode == "RGB"


def test_noise_by_grayscale():
    image = Image.open(
        os.path.join(".", "tests", "pic", "tokyo_station.jpg"),
    )
    rt = retouch.Retouch(image=image, noise=10.0)
    pict = rt.process()
    assert pict.mode == "L"


def test_noise_by_rgba():
    image = Image.open(
        os.path.join(".", "tests", "pic", "nullpo.png"),
    )
    rt = retouch.Retouch(image=image, noise=10.0)
    pict = rt.process()
    assert pict.mode == "RGB"


def test_noise_by_grayscale_with_alpha():
    image = Image.open(
        os.path.join(".", "tests", "pic", "test.png"),
    )
    rt = retouch.Retouch(image=image, noise=10.0)
    pict = rt.process()
    assert pict.mode == "L"
