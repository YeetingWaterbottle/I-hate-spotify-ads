import ctypes
import os
import time

# Virtual-Key Code for Pause and Play Media Key "https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes"
VK_MEDIA_PLAY_PAUSE = 0xB3

WM_CLOSE = 0x10

# Time Between Window Check
delay = 1.0


def find_ad(name):
    return ctypes.windll.user32.FindWindowW(None, name)


while True:
    list_of_ad = [find_ad("Advertisement"),
                  find_ad("Spotify")]

    for title in list_of_ad:
        if title != 0:
            ctypes.windll.user32.PostMessageW(title, WM_CLOSE, 0, 0)
            time.sleep(1)
            os.popen(
                "start /min {}\Spotify\Spotify.exe".format(os.getenv('appdata')))
            # !IMPORTANT! Change This Value if The Program Dont Auto Play The Music, it is the Delay Between The Launch of Spotify And When The Program Press The Media Play Pause Key. !IMPORTANT!
            time.sleep(1)

            # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-keybd_event
            ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 1, 0)

    print("No ads")

    time.sleep(float(delay))
