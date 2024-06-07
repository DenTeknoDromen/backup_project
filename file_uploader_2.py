from minio import Minio
from datetime import datetime
#from init import Backup
from tar_test import make_tarfile
from os import scandir, remove

class FileUploader():       
    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.log = []
        self.curr_date = datetime.now().isoformat(timespec="minutes")
        self.curr_date = self.curr_date.replace("T", " ")
        #super().__init__()  # Name of config and log file should be passed as parameters
#        config = self.config
        # client = Minio(f"{config['endpoint']}:{config['port']}",
        #                 secure=False,
        #                 access_key=config["access_key"],
        #                 secret_key=config["secret_key"])
    

    #bucket_name = Backup.bucket_name
    #dir_path = Backup.dir_path

    # Checks if current file has been changed since last backup
    def get_log(self):
        return self.log

    def check_last_modified(self, last_modified):
        last_backup = datetime.fromisoformat(self.config["last_backup"])
        last_modified = datetime.fromisoformat(last_modified)
        if last_modified >= last_backup:
            return True
        else:
            return False
    
    # Creates a string for print output
    def get_printline(self, file_info, depth):
        output = "|"
        output += ("    " * depth)
        if depth > 0:
            output += "|"
        output += "---"
        output += file_info
        return output        

    # Rcursive method that goes through every file in directory and uploads to endpoint
    def file_browser(self, dir_path, depth):
        dir = scandir(dir_path)
        temp = scandir("temp/")

        for file in dir:
            name = file.name
            unix_time = file.stat().st_mtime
            date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
            date = date.replace("T", " ")

            print(self.get_printline(f"{name}, Last modified: {date}", depth))

            if file.is_dir() and self.check_last_modified(date):
                make_tarfile(f"{dir_path}/{name}", name)
                self.client.fput_object(self.config["bucket_name"], name + ".tar", f"temp/{name}.tar")
                remove(f"temp/{name}.tar")



if __name__ == "__main__":
    #curr_backup = Backup()
    #file_uploader = FileUploader
    #file_uploader.file_browser(-1)
    upload = FileUploader()
    upload.file_browser(upload.file_path, 0)
    # print(check_last_modified("2024-04-21"))
