import os
from updatebd import *

# check and launch spicetify
os.system("spicetify update")
os.system('start Spotify:')

# check and launch discord
attempt_BD_install()
os.system('start Discord:')

input("Press enter to finish.")