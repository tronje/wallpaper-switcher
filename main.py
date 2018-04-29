#!/usr/bin/env python


import os
import subprocess


USER = subprocess.check_output(["whoami"]).decode().strip()
WPDIR = f"/tmp/{USER}/wallpaper-switcher/"
WPFILE = WPDIR + "current_wallpaper"
LOGFILE = WPDIR + "log"

WP_PREFIX = f"/home/{USER}/pics/wallpapers/solar_system/"

WALLPAPERS = [
    WP_PREFIX + "earth.png",
    WP_PREFIX + "jupiter.png",
    WP_PREFIX + "mars.png",
    WP_PREFIX + "mercury.png",
    WP_PREFIX + "moon.png",
    WP_PREFIX + "neptune.png",
    WP_PREFIX + "pluto.png",
    WP_PREFIX + "saturn.png",
    # WP_PREFIX + "sun.png",
    WP_PREFIX + "uranus.png",
    WP_PREFIX + "venus.png",
]


def init():
    if not os.path.isdir(WPDIR):
        os.mkdir(WPDIR)

    if not os.path.exists(WPFILE):
        f = open(WPFILE, "w")
        f.close()

    if not os.path.exists(LOGFILE):
        f = open(LOGFILE, "w")
        f.close()


def current_wallpaper():
    wallpaper = None

    with open(WPFILE, "r") as f:
        wallpaper = f.readline()

    return wallpaper.strip()


def set_wallpaper(path):
    return_code = subprocess.call(["feh", "--bg-scale", path])

    if return_code != 0:
        with open(LOGFILE, "a") as f:
            f.write(f"Failed to set wallpaper, feh return code: {return_code}")
        return

    with open(WPFILE, "w") as f:
        f.write(path)


def next_wallpaper():
    try:
        curr_idx = WALLPAPERS.index(current_wallpaper())
    except ValueError:
        import random
        curr_idx = random.randint(0, len(WALLPAPERS) - 1)

    next = None

    try:
        next = WALLPAPERS[curr_idx + 1]
    except IndexError:
        next = WALLPAPERS[0]

    return next


if __name__ == "__main__":
    init()
    set_wallpaper(next_wallpaper())
