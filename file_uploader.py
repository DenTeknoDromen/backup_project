from minio import Minio
from datetime import datetime
#from init import Backup
from os import scandir

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

        for file in dir:
            name = file.name
            unix_time = file.stat().st_mtime
            date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
            date = date.replace("T", " ")

            print(self.get_printline(f"{name}, Last modified: {date}", depth))

            if file.is_dir() and self.check_last_modified(date):
                self.file_browser(f"{dir_path}/{name}", depth + 1)
            elif self.check_last_modified(date):
                self.log.append(f"{self.curr_date} - {dir_path}/{name} copied to {self.config['bucket_name']}\n")        
                #self.client.fput_object(
                #self.bucket_name, f"{file_path}/{name}", f"{file_path}/{name}")           p   


if __name__ == "__main__":
    #curr_backup = Backup()
    #file_uploader = FileUploader
    #file_uploader.file_browser(-1)
    upload = FileUploader()
    upload.file_browser(upload.file_path, 0)
    # print(check_last_modified("2024-04-21"))
