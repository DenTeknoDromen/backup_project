from minio import Minio
import file_uploader_2 as file_uploader_2
import logger as logger
import utils as utils


class Backup:
    def __init__(self, curr_path):
        self.config = utils.load_config(curr_path)
        self.dir_path = self.config["dir_path"]

        logger.write_log(f"Backup to {self.config['bucket_name']} started")

        try:
            client = Minio(f"{self.config['endpoint']}:{self.config['port']}",
                           secure=False,
                           access_key=self.config["access_key"],
                           secret_key=self.config["secret_key"])

        except Exception as e:
            print("Connection to server failed")

        # Creates bucket of if it does not exists
        true_bucket = client.bucket_exists(bucket_name=self.config["bucket_name"])
            # print("stop")
        if true_bucket != True:
            client.make_bucket(self.config["bucket_name"])

        upload = file_uploader_2.FileUploader(client, self.config)
        upload.file_browser(self.dir_path)

        utils.write_config(self.config)

        client.fput_object(
            self.config["bucket_name"], "_" + logger.get_logname(), "test_logging.txt")
        client.fput_object(
            self.config["bucket_name"], "_configfile.txt", curr_path)
        
        logger.write_log(
            f"Backup to bucket: {self.config['bucket_name']} completed!\n")

