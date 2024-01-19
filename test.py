import time
import pygame
time_hrs, time_min, time_sec = input(
    " Enter time in following way (Hours,Minutes,Seconds) to start timer :").split(",")


def sound_fix_to_Stop_byctrlandc(sound_file):
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nAlarm stopped.\n Stopping the sound.\n Exiting Program...")
                pygame.mixer.music.stop()
                break
    except pygame.error as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.quit()


def idk(time_hrs, time_min, time_sec):
    if (int(time_min) >= 60 or int(time_sec) >= 60):
        print("Invalid Time . Exiting Program")
    else:
        timemain = int(time_hrs)*3600+int(time_min)*60+int(time_sec)
        while (timemain != 0):
            x = time.strftime("%H:%M:%S", time.gmtime(timemain))
            print(f"Time remaining {x}", end="\r")
            time.sleep(1)
            timemain -= 1
    print("Timer ends")
    print("Alarm sound starting ...")
    # you could replace with ur file path
    file = "backintime.mp3"
    sound_fix_to_Stop_byctrlandc(file)


idk(time_hrs, time_min, time_sec)
