from os import scandir
from init import Backup
from default_config import create_default_config

curr_dir = scandir("./")
check = 0
for files in curr_dir:
    if files.name.endswith("config.json"):
        curr_backup = Backup(files.path)
        check += 1
if check == 0:
    create_default_config()