import bs4
import requests

# If we want search "python 3"
# https://imgur.com/search?q=python%203.8

# These 2 following vars could be read by cmdline or user input, but not
# the purpose in this chapter
keySearch = "python 3"
maxMatches = 10


urlSearch = "https://imgur.com/search?q=" + keySearch

# Get html of imgur research
print(f"searching {keySearch}")
res = requests.get(urlSearch)
res.raise_for_status()
print("Connected to", res.url)
imgur_soup = bs4.BeautifulSoup(res.text, "html.parser")


results = imgur_soup.find_all("a", class_="image-list-link")
limit = len(results) if len(results) < maxMatches else maxMatches
for i in range(limit):
    urlResultImg = "https:" + results[i].img["src"]

    # download the img
    res = requests.get(urlResultImg)
    res.raise_for_status()

    # save img
    f = open(f"{i}_{keySearch}.jpg", "wb")
    print(f"{i}_downloading {keySearch}.jpg")
    for chunk in res.iter_content(100000):
        f.write(chunk)
    f.close()
