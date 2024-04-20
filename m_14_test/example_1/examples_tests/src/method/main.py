import json
import pathlib
import sys

project_root = (
    pathlib.Path(__file__).resolve().parents[1]
)  # Go two levels up to reach the project root
sys.path.append(str(project_root))


def write_contacts_to_file(filename, contacts):
    try:
        with open(filename, "w") as file:
            json.dump({"contacts": contacts}, file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while writing to file '{filename}': {e}")


def read_contacts_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = json.load(file)
            print(content)
        return content.get("contacts")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{filename}': {e}")
        return None
    except Exception as e:
        print(f"An error occurred while reading file '{filename}': {e}")
        return None
if __name__ == "__main__":
    # Get the absolute path of the current script's directory
    script_directory = pathlib.Path(__file__).parent.resolve()
    print(f"Script directory: {script_directory}")

    # Construct the absolute path to the ingredients.csv file
    contacts_file = script_directory / "contacts.json"
    print(f"Ingredients file: {contacts_file}")

    # Example data
    contacts = [
        {"name": "John Doe", "phone": "123456789"},
        {"name": "Jane Smith", "phone": "987654321"}
    ]
    # Write contacts to a JSON file
    write_contacts_to_file(contacts_file, contacts)

    # Read contacts from the JSON file
    read_contacts = read_contacts_from_file(contacts_file)
    print("Contacts read from file:")
    print(read_contacts)
