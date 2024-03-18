import os

changelog_path = "BetterDiscord/CHANGELOG.md"
bdversion_path = "bdversion.txt"

def attempt_BD_install():
    if is_there_update() == True:
        print("Installing BetterDiscord...")
        install_bd()
    else:
        print("No BetterDiscord update")

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
    
    print("Updating bdversion.txt...")
    os.chdir("..")
    rewrite_bdversion(get_vers(changelog_path))
    print("Updated!")
    
def is_there_update():
    if os.path.exists("BetterDiscord") == False: # not installed
        return True
    
    version = get_vers(changelog_path)
    if cmpr_versions(version) == True: # if equal
        return False # no update
    else:
        return True
                
def cmpr_versions(version): 
    if os.path.exists(bdversion_path) == False:
        return False
    
    with open(bdversion_path, "r") as f:
        if f.read() == version:
            return True
    return False

def rewrite_bdversion(version): # fix file
    with open(bdversion_path, "w") as f:
        f.truncate(0)
        f.write(version)
        print(version)
        
def get_vers(path):
    with open(path, "r") as f:
        for line in f:
            if "## " in line and "###" not in line:
                return line