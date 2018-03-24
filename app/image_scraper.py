import re
from urllib import request

from bs4 import BeautifulSoup


allrecipes_pattern = r"https://images.media-allrecipes.com/userphotos/560x315/\d+\.jpg"
foodnetwork_pattern = r"//food.fnr.sndimg.com/content/dam/images/food/fullset/.*\.jpeg"

allrecipes_regex = re.compile(allrecipes_pattern)
foodnetwork_regex = re.compile(foodnetwork_pattern)


def find_image(url, host, title):
    data = request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    if host == "allrecipes.com":
        return find_allrecipes_image(soup)
    elif host == "foodnetwork.com":
        return find_foodnetwork_image(soup, title)


def find_allrecipes_image(soup):
    images = soup.findAll("img", {"src": allrecipes_regex})
    return images[0]["src"]


def find_foodnetwork_image(soup, title):
    images = soup.findAll("img", {"src": foodnetwork_regex})
    for image in images:
        if title in image.get("alt"):
            return "https:{0}".format(image.get("src", ""))


def download_image(filename, url):
    path = "{0}/{1}".format("images", filename)
    request.urlretrieve(url, path)
