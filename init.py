from write_files import log_backup
from read_files import load_config, load_log
from file_uploader import FileUploader
from minio import Minio
class Backup:
    def __init__(self):
        self.config = load_config()
        self.curr_log = load_log()
        self.dir_path = self.config["dir_path"]

        try:
            client = Minio(f"{self.config['endpoint']}:{self.config['port']}",
                            secure=False,
                            access_key=self.config["access_key"],
                            secret_key=self.config["secret_key"])
            
            # Creates bucket of if it does not exists
            # if client.bucket_exists(self.config["bucket_name"]) is False:
            #     client.make_bucket(self.config["bucket_name"])            
            
        except Exception as e:
            print("Connection to server failed")
        
        #self.last_backup = self.curr_log[0].split(": ")[1][:-1]

        upload = FileUploader(client, self.config)
        upload.file_browser(self.dir_path, 0)

        self.curr_log = upload.get_log() + self.curr_log
        log_backup(self.curr_log, self.config)
        

        #file_uploader(self.config)
        #write_log("log.txt", self.curr_log)
        #write_config("config.txt", self.config)

if __name__== "__main__":
    curr_backup = Backup()
