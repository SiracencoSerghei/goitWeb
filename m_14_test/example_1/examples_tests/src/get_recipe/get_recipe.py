import pathlib
import sys

project_root = (
    pathlib.Path(__file__).resolve().parents[1]
)  # Go two levels up to reach the project root
sys.path.append(str(project_root))

def get_recipe(path, search_id):
    result = None
    with open(path, "r") as f:
        for line in f:
            (id, name, *recipes) = line.strip().split(",")
            if id == search_id:
                result = {"id": id, "name": name, "ingredients": recipes}
    return result


if __name__ == '__main__':
    # Get the absolute path of the current script's directory
    script_directory = pathlib.Path(__file__).parent.resolve()
    print(f"Script directory: {script_directory}")

    # Construct the absolute path to the ingredients.csv file
    ingredients_file = script_directory / "ingredients.csv"
    print(f"Ingredients file: {ingredients_file}")

    # Call get_recipe with the absolute file path
    result = get_recipe(ingredients_file, "60b90c1c13067a15887e1ae1")
    print(result)
