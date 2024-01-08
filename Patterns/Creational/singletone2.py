class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class LogManager(Singleton):
    def __init__(self):
        super(LogManager, self).__init__()
        self.log_entries = []

    def log(self, message):
        self.log_entries.append(message)

    def get_logs(self):
        return self.log_entries

# Example of using the logging manager

# Create an instance of the logging manager
log_manager = LogManager()

# Log some messages
log_manager.log("Error: File not found")
log_manager.log("Info: Application started")
log_manager.log("Warning: Low disk space")


# Example of using the logging manager in different parts of the code

# In module A
log_manager_A = LogManager()
log_manager_A.log("Debug: Module A initialized")

# In module B
log_manager_B = LogManager()
log_manager_B.log("Info: Module B started")

# In module C
log_manager_C = LogManager()
log_manager_C.log("Warning: Module C has a potential issue")

# Retrieve and print all logs
all_logs = log_manager.get_logs()
print("All Logs:")
for log in all_logs:
    print(log)