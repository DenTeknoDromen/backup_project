from os import scandir
from init import Backup
import logger

config_dir = scandir("./configfiles/")
check = 0
for files in config_dir:
    if files.name.endswith("config.json"):
        curr_backup = Backup(files.path)
        check += 1
if check == 0:
    create_default_config()
    logger.write_log("No config file found, creating new one")