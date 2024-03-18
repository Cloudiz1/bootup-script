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
        os.rmdir("BetterDiscord")
        
    sync_cmd("git clone https://github.com/BetterDiscord/BetterDiscord.git")
    os.chdir("BetterDiscord")
    sync_cmd("npm install -g pnpm")
    sync_cmd("pnpm install")
    sync_cmd("pnpm build")
    sync_cmd("pnpm inject")
    print("Success!")
    
def is_there_update():
    if os.path.exists("BetterDiscord") == False: # not installed
        return True

    os.chdir("BetterDiscord")
    
    with open("CHANGELOG.md", "r") as f:
        for line in f:
            if "## " in line and "###" not in line: # get version
                if cmpr_versions(line) == True: # if equal
                    return False # no update
                else:
                    rewrite_bdversion(line)
                    return True
                
def cmpr_versions(version): 
    if os.path.exists("../bdversions.txt") == False:
        return False
    
    with open("../bdversions.txt", "r") as f:
        if f.read() == version:
            return True
    return False

def rewrite_bdversion(version): # fix file
    with open("../bdversions.txt", "w") as f:
        f.truncate(0)
        f.write(version)
        print(version)
        
def attempt_BD_install():
    if is_there_update() == True:
        print("Installing BetterDiscord...")
        install_bd()
    else:
        print("No BetterDiscord update")