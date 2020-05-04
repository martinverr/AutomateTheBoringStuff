# link verification: given a URL, try to download every page linked
# and show the broken one (404 error)

import requests
import bs4


def isValidLink(url):
    if requests.get(url).status_code == 404:
        return False
    else:
        return True


givenURL = "https://automatetheboringstuff.com/"

# Get the home page
res = requests.get(givenURL)
try:
    res.raise_for_status()
except Exception:
    print("Cannot reach given URL")

# Get the a tag soup elements of the home page
home_soup = bs4.BeautifulSoup(res.text, "html.parser")
allAelement = home_soup.find_all("a")
print("Found", len(allAelement), "links")

# Try to connect to the links in those <a> elements
for Aelement in allAelement:
    try:
        link = Aelement["href"]
        if not (link.startswith("www") or link.startswith("http")):
            link = givenURL + link
    except Exception:
        print("Found a link doesn't have a 'href' tag")
        break

    if not isValidLink(link):
        print("Found", link, "not valid(404 Error)")
