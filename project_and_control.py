import glob
import random
import os
import datetime

beamer_activated = True
activate_beamer_cmd = "vcgencmd display_power 1"
deactivate_beamer_cmd = "vcgencmd display_power 0"
time_management = True

while True:

    # play random video
    rand_elem = random.choice (glob.glob('raspi_video_gen_player/videos/*.mp4'))
    os.system("omxplayer " + rand_elem)

    if time_management:
        # projector time management
        timestamp = datetime.datetime.now().time()
        if (timestamp.hour >= 15) or (timestamp.hour <= 1): 
            if(beamer_activated == False):
                os.system(activate_beamer_cmd)
                beamer_activated = True
        else:
            if(beamer_activated == True):
                os.system(deactivate_beamer_cmd)
                beamer_activated = False