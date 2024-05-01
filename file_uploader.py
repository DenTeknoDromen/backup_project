from minio import Minio
from datetime import datetime
from init import Backup
import os

class FileUploader(Backup):       
    def __init__(self):
        super().__init__("")
        config = self.config
        client = Minio(f"{config['endpoint']}:{config['port']}",
                        secure=False,
                        access_key=config["access_key"],
                        secret_key=config["secret_key"])
    

    #bucket_name = Backup.bucket_name
    #dir_path = Backup.dir_path

    def check_last_modified(last_modified):
        last_backup = datetime.fromisoformat("1995-11-25")
        last_modified = datetime.fromisoformat(last_modified)
        if last_modified >= last_backup:
            return True
        else:
            return False

    def file_browser(self, dir_path, depth):
        dir = os.scandir(dir_path)
        file_path = dir_path

        print("\t" * (depth) + dir_path)

        for file in dir:
            name = file.name
            unix_time = file.stat().st_mtime
            date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
            date = date.replace("T", " ")

            if file.is_dir() and self.check_last_modified(date):
                self.file_browser(f"{dir_path}/{name}", depth + 1)
            elif self.check_last_modified(date):
                print("\t" * (depth + 1) + name + " Last modified: " + date)
                #self.client.fput_object(
                #self.bucket_name, f"{file_path}/{name}", f"{file_path}/{name}")


if __name__ == "__main__":
    #curr_backup = Backup()
    #file_uploader = FileUploader
    #file_uploader.file_browser(-1)
    upload = FileUploader()
    upload.file_browser(-1)
    # print(check_last_modified("2024-04-21"))
