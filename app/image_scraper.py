import re
from urllib import request

from bs4 import BeautifulSoup


allrecipes_pattern = r"https://images.media-allrecipes.com/userphotos/560x315/\d+\.jpg"
allrecipes_regex = re.compile(allrecipes_pattern)


def find_image(url):
    data = request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    images = soup.findAll("img", {"src": allrecipes_regex})
    return images[0]["src"]


def download_image(filename, url):
    directory = "images"
    path = "{0}/{1}.jpg".format(directory, filename)
    request.urlretrieve(url, path)


def main():
    image = find_image("https://www.allrecipes.com/recipe/8358/apple-cake-iv/")
    download_image("test", image)


if __name__ == "__main__":
    main()
