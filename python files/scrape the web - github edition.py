import requests
from bs4 import BeautifulSoup as bs

githubUser = input("Input Github username: ")
url = f"https://github.com/{githubUser}"
r = requests.get(url)
soup = bs(r.content, "html.parser")
profileImage = soup.find("img", {"alt": "View "+githubUser+"'s full-sized avatar"})["src"]
print(profileImage)