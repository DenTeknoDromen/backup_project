import json
from datetime import datetime
from write_log import write_log

class Backup:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()

        # self.endpoint = self.config["endpoint"]
        # self.port = self.config["port"]
        # self.access_key = self.config["access_key"]
        # self.secret_key = self.config["secret_key"]
        # self.bucket_name = self.config["bucket_name"]
        # self.dir_path = self.config["dir_path"]

        self.curr_log = self.load_log()
        self.last_backup = self.curr_log[0].split(": ")[1][:-1]

        #file_uploader(self.config)
        write_log("log.txt", self.curr_log)

    # Loads dictionary with settings from jsonfile
    def load_config(self):
        curr_path = self.file_path + "config.json"
        try:
            with open(curr_path, "r") as f:
                file_content = f.read()
                return json.loads(file_content)
        except FileNotFoundError:
            with open(curr_path, "x"):
                print("Error, config file not found\nNew file created")
        except Exception as e:
            print("Unkown file content")

    # Loads log
    def load_log(self):
        curr_path = self.file_path + "log.txt"
        try:
            with open(curr_path, "r") as f:
                curr_log = f.readlines()
                return curr_log
        except FileNotFoundError:
            with open(curr_path, "x"):
                print("Error, log file not found\nNew file created")
        except Exception as e:
            print("Unkown file content(log)")

#curr_backup = Backup()
#print("END")