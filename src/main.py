import os
from updatebd import *

# check for updates
attempt_BD_install()
os.system("spicetify update")

os.system('start Spotify:')
os.system('start Discord:')