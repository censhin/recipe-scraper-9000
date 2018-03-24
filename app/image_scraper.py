import re
from urllib import request

from bs4 import BeautifulSoup


allrecipes_pattern = r"https://images.media-allrecipes.com/userphotos/560x315/\d+\.jpg"
foodnetwork_pattern = r"//food.fnr.sndimg.com/content/dam/images/food/fullset/.*\.jpeg"
epicurious_pattern = r"https://assets.epicurious.com/photos/\w+/6:4/w_274%2Ch_169/.*\.jpg"

allrecipes_regex = re.compile(allrecipes_pattern)
foodnetwork_regex = re.compile(foodnetwork_pattern)
epicurious_regex = re.compile(epicurious_pattern)


def find_image(url, host, title):
    data = request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    if host == "allrecipes.com":
        return find_allrecipes_image(soup)
    elif host == "foodnetwork.com":
        return find_foodnetwork_image(soup, title)
    elif host == "epicurious.com":
        return find_epicurious_image(soup)


def find_allrecipes_image(soup):
    images = soup.findAll("img", {"src": allrecipes_regex})
    if images != []:
        return images[0].get("src")
    else:
        return ""


def find_foodnetwork_image(soup, title):
    images = soup.findAll("img", {"src": foodnetwork_regex})
    for image in images:
        if title in image.get("alt"):
            return "https:{0}".format(image.get("src", ""))


def find_epicurious_image(soup):
    images = soup.findAll("img", {"srcset": epicurious_regex})
    return images[0].get("srcset").replace("w_274%2Ch_169", "w_620%2Ch_413")


def download_image(filename, url):
    if url is "" or url == None:
        return
    path = "{0}/{1}".format("images", filename)
    request.urlretrieve(url, path)
