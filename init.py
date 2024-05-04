from write_files import log_backup
from read_files import load_config, load_log
from file_uploader import FileUploader
from minio import Minio
class Backup:
    def __init__(self, curr_path):
        self.config = load_config(curr_path)
        self.curr_log = load_log()
        self.dir_path = self.config["dir_path"]

        self.curr_log.insert(0, f"Backup to {self.config['bucket_name']} started\n")

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

        upload = FileUploader(client, self.config)
        upload.file_browser(self.dir_path, 0)

        self.curr_log = upload.get_log() + self.curr_log
        log_backup(self.curr_log, self.config)


    
