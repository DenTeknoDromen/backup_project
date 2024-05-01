from write_files import write_log, write_config
from read_files import load_config, load_log
from file_uploader import FileUploader
from minio import Minio
class Backup:
    def __init__(self):
        self.config = load_config()
        self.file_path = self.config["dir_path"]

        try:
            client = Minio(f"{self.config['endpoint']}:{self.config['port']}",
                            secure=False,
                            access_key=self.config["access_key"],
                            secret_key=self.config["secret_key"])
        except Exception as e:
            print("Connection to server failed")
        
        # Creates bucket of if it does not exists
        # if client.bucket_exists(self.config["bucket_name"]) is False:
        #     client.make_bucket(self.config["bucket_name"])
        
        self.curr_log = load_log()
        self.last_backup = self.curr_log[0].split(": ")[1][:-1]
        upload = FileUploader(client, self.config)
        upload.file_browser()
        

        #file_uploader(self.config)
        #write_log("log.txt", self.curr_log)
        #write_config("config.txt", self.config)
