import configparser
from pathlib import Path
import logging

package_name = "hw-07"
logger = logging.getLogger(package_name)


def read_config() -> str:
    file_config = (
        Path(__file__).parent.parent.parent.joinpath(".config").joinpath("config.ini")
    )
    if not file_config.exists():
        logger.error(f"CONFIG NOT FOUND {file_config}")
        return None

    config = configparser.ConfigParser()
    config.read(file_config)
    if "DB" not in config.sections():
        logger.error("CONFIG READ ERROR SECTION [DB]")
        return False
    section_db = config["DB"]
    host = section_db.get("host")
    port = section_db.get("port")
    database_name = section_db.get("db_name")
    username = section_db.get("username")
    password = section_db.get("password")
    uri = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
    return uri
