import json

from recipe_scrapers import scrape_me

from image_scraper import download_image
from image_scraper import find_image


def get_recipes():
    recipes = []
    with open("recipes.txt", "r") as f:
        for line in f:
            recipes.append(line.strip("\n"))
    return recipes


def recipe_to_dict(scrape):
    recipe = {
        "title": "",
        "source": "",
        "totalTime": "",
        "ingredients": "",
        "instructions": ""
    }
    recipe["title"] = scrape.title()
    recipe["source"] = scrape.url
    recipe["totalTime"] = scrape.total_time()
    recipe["ingredients"] = scrape.ingredients()
    recipe["instructions"] = scrape.instructions()
    return recipe


def get_file_type(image_url):
    if image_url:
        file_type = image_url[-4:]
        if "jpeg" == file_type:
            return "jpeg"
        elif ".jpg" == file_type:
            return "jpg"
        elif ".png" == file_type:
            return "png"
        else:
            return ""


def get_file_name(recipe_dict):
    return recipe_dict.get("title", "unknown").lower().replace(" ", "-")


def write_to_file(recipe_dict):
    directory = "data"
    filename = get_file_name(recipe_dict)
    path = "{0}/{1}.json".format(directory, filename)
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dict))


def main():
    recipes = get_recipes()
    for recipe in recipes:
        scrape = scrape_me(recipe)
        print("scraping: {0}".format(scrape.title()))
        recipe_dict = recipe_to_dict(scrape)
        write_to_file(recipe_dict)
        image_url = find_image(recipe_dict.get("source"), scrape.host(), recipe_dict.get("title"))
        filename = "{0}.{1}".format(get_file_name(recipe_dict), get_file_type(image_url))
        download_image(filename, image_url)


if __name__ == "__main__":
    main()
