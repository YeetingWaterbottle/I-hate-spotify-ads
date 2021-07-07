import keyboard
import os
import time

delay = 1
running_seconds, running_minutes, stopped_seconds, stopped_minutes = 0, 0, 0, 0

while True:
    check_if_running = os.popen(
        "tasklist /NH /FO:CSV /FI \"IMAGENAME eq Spotify.exe\"").read()
    check_if_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Advertisement\"").read()
    check_if_another_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Spotify\"").read()

    if "Spotify.exe" in check_if_ad_exist or "Spotify.exe" in check_if_another_ad_exist:
        print("###########################")
        print("Spotify Advertisement Found")
        os.system("taskkill /IM Spotify.exe")
        print("Process Killed")
        print("Waiting 1 Seconds for Spotify to Launch")
        time.sleep(1)
        os.system(
            "start /MIN C:\\Users\\{}\\AppData\\Roaming\\Spotify\\Spotify.exe".format(os.getlogin()))
        print("Spotify Launched")
        time.sleep(0.5)
        keyboard.press_and_release('play/pause media')
        print("Music Started")
        print("###########################")
        running_seconds, running_minutes = 0, 0

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
