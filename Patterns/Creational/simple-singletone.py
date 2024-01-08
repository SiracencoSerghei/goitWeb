import json

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class ConfigurationManager(Singleton):
    def __init__(self):
        super(ConfigurationManager, self).__init__()
        self.config_data = {}

    def load_config(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            print(f"Warning: File '{file_path}' not found. Using default configuration.")
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON format in '{file_path}'. Using default configuration.")

    def get_config_value(self, key):
        return self.config_data.get(key, None)

# Example of using the configuration manager

# Create an instance of the configuration manager
config_manager = ConfigurationManager()

# Load configuration settings from a file
config_manager.load_config('config.json')

# Access configuration settings
api_key_value = config_manager.get_config_value('api_key')
print(api_key_value)

