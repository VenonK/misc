import requests
from bs4 import BeautifulSoup as bs

redUser = input("Enter their Reddit username: ")
url = f"https://www.reddit.com/user/{redUser}"
headers = {'User-Agent': 'Mozilla/5.0'}  # Adding a user-agent header to mimic a browser request

try:
    req = requests.get(url, headers=headers)
    req.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    soup = bs(req.content, "html.parser")
    profileImage = soup.find("img", {"alt": f"{redUser} u/{redUser} avatar"})
    
    if profileImage and profileImage.has_attr('src'):
        print(profileImage['src'])
    else:
        print("Profile image not found.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")