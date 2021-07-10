import ctypes
import os
import time

# Virtual-Key Code for Pause and Play Media Key "https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes"
VK_MEDIA_PLAY_PAUSE = 0xB3

# Time Between Window Check
delay = 1

# Loading User32.dll for the Media Keys
dll_user32 = ctypes.WinDLL("user32.dll")


def tasklist_window(name):
    return os.popen("tasklist /nh /fo:csv /fi \"WINDOWTITLE eq {}\"".format(name)).read()


while True:
    check_ad = [tasklist_window("Advertisement"),
                tasklist_window("Spotify")]

    if "Spotify.exe" in check_ad[0] or "Spotify.exe" in check_ad[1]:
        print("###########################")
        print("Spotify Advertisement Found")
        os.system("taskkill /IM Spotify.exe")
        print("Process Killed")
        print("Waiting 1 Seconds for Spotify to Launch")
        time.sleep(1)
        os.system(
            "powershell Start-Process {}\Spotify\Spotify.exe -WindowStyle Minimized".format(os.getenv('appdata')))
        print("Spotify Launched")
        # !IMPORTANT! Change This Value if The Program Dont Auto Play The Music, it is the Delay Between The Launch of Spotify And When The Program Press The Media Play Pause Key. !IMPORTANT!
        time.sleep(1)
        # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-keybd_event
        dll_user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 1, 0)
        print("Music Started")
        print("###########################")

    time.sleep(float(delay))
