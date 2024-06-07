import file_uploader_2
from minio import Minio
import logger
import utils

class Backup:
    def __init__(self, curr_path):
        self.config = utils.load_config(curr_path)
        self.curr_log = utils.load_log()
        self.dir_path = self.config["dir_path"]

        logger.write_log(f"Backup to {self.config['bucket_name']} started")

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

        upload = file_uploader_2.FileUploader(client, self.config)
        upload.file_browser(self.dir_path, 0)

        logger.write_log(f"Backup to {self.config['bucket_name']} completed!")
        client.fput_object(self.config["bucket_name"], "test_logging.txt", "test_logging.txt")
        client.fput_object(self.config["bucket_name"], "configfile.txt", curr_path)


    
