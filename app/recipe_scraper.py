import json

from recipe_scrapers import scrape_me

from image_scraper import download_image


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


def get_filename(recipe_dict):
    return recipe_dict.get("title", "unknown").lower().replace(" ", "-")


def write_to_file(recipe_dict):
    directory = "data"
    filename = get_filename(recipe_dict)
    path = "{0}/{1}.json".format(directory, filename)
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dict))


def main():
    recipes = get_recipes()
    for recipe in recipes:
        scrape = scrape_me(recipe)
        recipe_dict = recipe_to_dict(scrape)
        write_to_file(recipe_dict)
        download_image(get_filename(recipe_dict))


if __name__ == "__main__":
    main()
