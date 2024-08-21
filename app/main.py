from os import scandir
from init import Backup
import logger as logger
import utils as utils

# Scans directory /configfiles for json files
# Files must end with "config.json" to be vaild
# Creates a default config file if none exists
config_dir = scandir("./configfiles/")
check = False
for files in config_dir:
    if files.name.endswith("config.json"):
        curr_backup = Backup(files.path)
        check = True
if check == False:
    utils.create_default_config()
    logger.write_log("No config file found, creating new one")
