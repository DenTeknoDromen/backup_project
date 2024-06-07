from minio import Minio
from datetime import datetime
import tarfile
from os import scandir, remove
import logger

def make_tarfile(self, dir_path, name):
    output_name = "temp/" + name + ".tar"
    with tarfile.open(output_name, 'w:bz2') as tar:
        tar.add(dir_path)   

class FileUploader():       
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check_last_modified(self, last_modified):
        last_backup = datetime.fromisoformat(self.config["last_backup"])
        last_modified = datetime.fromisoformat(last_modified)
        if last_modified >= last_backup:
            return True
        else:
            return False      

    # Rcursive method that goes through every file in directory and uploads to endpoint
    def file_browser(self, dir_path):
        dir = scandir(dir_path)

        for file in dir:
            name = file.name
            unix_time = file.stat().st_mtime
            date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
            date = date.replace("T", " ")

            if file.is_dir() and self.check_last_modified(date):
                make_tarfile(f"{dir_path}/{name}", name)
                self.client.fput_object(self.config["bucket_name"], name + ".tar", f"temp/{name}.tar")
                remove(f"temp/{name}.tar")
                logger.write_log(f"{dir_path}/{name} copied to {self.config['bucket_name']}")  
