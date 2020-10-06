import ctypes
import os

from autoMeditationsWallpaper.textSlicer import findLines2


def main():
    findLines2()
    ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\Lord of Eight peaks\\PycharmProjects\\wallpaperChanger\\sample-out.png",0)
