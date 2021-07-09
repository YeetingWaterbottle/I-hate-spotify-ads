import ctypes
import os
import time

# Virtual-Key Code for Pause and Play Media Key "https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes"
VK_MEDIA_PLAY_PAUSE = 0xB3

delay = 1  # Time Between Window Check
# Loading User32.dll for the Media Keys
dll_user32 = ctypes.WinDLL("user32.dll")
running_seconds, running_minutes, stopped_seconds, stopped_minutes = 0, 0, 0, 0

while True:
    # poop code below
    check_if_running = os.popen(
        "tasklist /NH /FO:CSV /FI \"IMAGENAME eq Spotify.exe\"").read()
    check_if_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Advertisement\"").read()
    check_if_another_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Spotify\"").read()
    # poop code above

    if "Spotify.exe" in check_if_ad_exist or "Spotify.exe" in check_if_another_ad_exist:
        print("###########################")
        print("Spotify Advertisement Found")
        os.system("taskkill /IM Spotify.exe")
        print("Process Killed")
        print("Waiting 1 Seconds for Spotify to Launch")
        time.sleep(1)
        os.system(
            "powershell Start-Process {}\Spotify\Spotify.exe -WindowStyle Minimized".format(os.getenv('appdata')))
        print("Spotify Launched")
        time.sleep(0.5)
        # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-keybd_event
        dll_user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 1, 0)
        print("Music Started")
        print("###########################")

    elif "Spotify.exe" in check_if_running:
        running_seconds += 1
        if running_seconds >= 60:
            running_minutes += 1
            running_seconds -= 60
        print("Running, no Advertisement Found. {}m {}s".format(
            running_minutes, running_seconds))

    elif "Spotify.exe" not in check_if_running:
        stopped_seconds += 1
        if stopped_seconds >= 60:
            stopped_minutes += 1
            stopped_seconds -= 60
        print("Spotify is not Running. {}m {}s".format(
            stopped_minutes, stopped_seconds))

    time.sleep(float(delay))
