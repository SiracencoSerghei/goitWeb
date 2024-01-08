import logging

# Налаштування форматування для файлового обробника
file_log_format = "{asctime} [{levelname}] {name} {funcName:15}({lineno}) - {message}"
file_formatter = logging.Formatter(file_log_format, style="{")
file_handler = logging.FileHandler("app.logs")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Налаштування форматування для консольного обробника
console_log_format = "[{levelname}] {message}"
console_formatter = logging.Formatter(console_log_format, style="{")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

# Створення і налаштування логгера
logger = logging.getLogger("my_logger")
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Налаштування іншого формату для окремого обробника
other_console_log_format = "[{levelname}] {name} - {message}"
other_console_formatter = logging.Formatter(other_console_log_format, style="{")
other_console_handler = logging.StreamHandler()
other_console_handler.setLevel(logging.WARNING)
other_console_handler.setFormatter(other_console_formatter)

# Додавання окремого обробника з іншим форматом до логгера
logger.addHandler(other_console_handler)


def process_data(data):
    try:
        result = data / 0  # Генерувати ділення на нуль для демонстрації помилки
    except Exception as e:
        logger.error(f"Error processing data: {e}", exc_info=True)
        # За допомогою exc_info=True виводимо деталі стеку в лог


if __name__ == "__main__":
    logger.info("Starting the application.")
    data_to_process = 42
    logger.debug(f"Processing data: {data_to_process}")
    process_data(data_to_process)
    logger.warning("This is a warning message.")
    logger.info("Shutting down the application.")
