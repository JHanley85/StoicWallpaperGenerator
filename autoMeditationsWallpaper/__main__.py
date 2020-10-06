import ctypes
from pathlib import Path
from autoMeditationsWallpaper.textSlicer import find_lines

def main():


    find_lines()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(Path("sample-out.png").resolve()),0)
