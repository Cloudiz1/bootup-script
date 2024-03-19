from bs4 import BeautifulSoup
import requests

url = "https://github.com/BetterDiscord/BetterDiscord/releases"
def get_vers():
    req = requests.get(url)
    
    soup = BeautifulSoup(req.text, "html.parser")

    for child in soup.descendants:
        if child.name == "a" and "BetterDiscord v" in child.text:
            return child.text
    
print(get_vers())