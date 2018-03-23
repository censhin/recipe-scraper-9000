import json

from recipe_scrapers import scrape_me


def set_recipe_values(scrape):
    recipe = {
        "title": "",
        "totalTime": "",
        "ingredients": "",
        "instructions": ""
    }
    recipe["title"] = scrape.title()
    recipe["totalTime"] = scrape.total_time()
    recipe["ingredients"] = scrape.ingredients()
    recipe["instructions"] = scrape.instructions()
    return recipe


def write_to_file(recipe):
    with open("data/test.json", "w") as f:
        f.write(json.dumps(recipe))


def main():
    scrape = scrape_me("https://www.allrecipes.com/recipe/8358/apple-cake-iv/")
    recipe = set_recipe_values(scrape)
    write_to_file(recipe)


if __name__ == "__main__":
    main()
