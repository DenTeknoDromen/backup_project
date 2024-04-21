from minio import Minio
from datetime import datetime
import os

def main():
    client = Minio("127.0.0.1:9000",
                secure=False,
                access_key="minioadmin",
                secret_key="minioadmin")
    
    # client.make_bucket("testbucket")
    
    source_file = "test_dir/test_2.txt"
    bucket_name = "backup"
    destination_file = "bajs/test_2.txt"

    #client.make_bucket("temp")
    client.fput_object(bucket_name, destination_file, source_file)
    print(source_file, "Successfully uploaded as object", destination_file, "to bucket", bucket_name)

dir_path = "test_dir"
def file_browser(dir_path, depth):
    test_dir = os.scandir(dir_path)
    # print(f"{("m" * (depth - 1))}>>>> {dir_path}")
    print("\t" * (depth) + dir_path)
    for file in test_dir:
        name = file.name
        unix_time = file.stat().st_mtime
        date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
        date = date.replace("T", " ")

        if file.is_dir():
            #print(file.name + " Last modified: " + date)
            file_browser(dir_path + "/" + name, depth + 1)
        else:
            print("\t" * (depth + 1) + file.name + " Last modified: " + date)

file_browser(dir_path, -1)
if __name__ == "__main__":
    main()
