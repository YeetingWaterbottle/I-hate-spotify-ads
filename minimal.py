import keyboard
import os
import time

delay = 1

while True:
    check_if_running = os.popen(
        "tasklist /NH /FO:CSV /FI \"IMAGENAME eq Spotify.exe\"").read()
    check_if_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Advertisement\"").read()
    check_if_another_ad_exist = os.popen(
        "tasklist /NH /FO:CSV /FI \"WINDOWTITLE eq Spotify\"").read()

    if "Spotify.exe" in check_if_ad_exist or "Spotify.exe" in check_if_another_ad_exist:
        os.system("taskkill /IM Spotify.exe")
        time.sleep(1)
        os.system(
            "start /MIN C:\\Users\\{}\\AppData\\Roaming\\Spotify\\Spotify.exe".format(os.getlogin()))
        time.sleep(0.5)
        keyboard.press_and_release('play/pause media')

    time.sleep(float(delay))
