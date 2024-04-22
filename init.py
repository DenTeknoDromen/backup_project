import json
from datetime import datetime
from write_log import write_log

class Backup:
    def __init__(self) -> None:
        self.config = self.load_config()

        self.endpoint = self.config["endpoint"]
        self.port = self.config["port"]
        self.access_key = self.config["access_key"]
        self.secret_key = self.config["secret_key"]
        self.bucket_name = self.config["bucket_name"]
        self.dir_path = self.config["dir_path"]

        self.curr_log = self.load_log()
        self.last_backup = self.curr_log[0].split(": ")[1][:-1]

        write_log("log.txt", self.curr_log)

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                file_content = f.read()
                return json.loads(file_content)
        except Exception as e:
            print("Error, config file not found")

    def load_log(self):
        try:
            with open("log.txt", "r") as f:
                curr_log = f.readlines()
                return curr_log
        except Exception as e:
            print("Error, log file not found")

curr_backup = Backup()
print("END")