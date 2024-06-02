import os

def sync_cmd(command):
    print(command)
    if os.system(command) == 0:
        return True
    else:
        print("Error")
        return False

def install_bd():
    if os.path.exists("BetterDiscord") == True:
        os.system('rmdir /S /Q "{}"'.format("BetterDiscord")) 
        
    sync_cmd("git clone https://github.com/BetterDiscord/BetterDiscord.git")
    os.chdir("BetterDiscord")
    sync_cmd("npm install -g pnpm")
    sync_cmd("pnpm install")
    sync_cmd("pnpm build")
    sync_cmd("pnpm inject")
    print("Success!")