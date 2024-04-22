from minio import Minio
from datetime import datetime
import os

client = Minio("127.0.0.1:9000",
               secure=False,
               access_key="minioadmin",
               secret_key="minioadmin")

bucket_name = "backup"
dir_path = "test_dir"


def main():
    print("placeholder")


def check_last_modified(last_modified):
    last_backup = datetime.fromisoformat("1995-11-25")
    last_modified = datetime.fromisoformat(last_modified)
    if last_modified >= last_backup:
        return True
    else:
        return False


def file_browser(dir_path, depth):
    dir = os.scandir(dir_path)
    file_path = dir_path

    print("\t" * (depth) + dir_path)

    for file in dir:
        name = file.name
        unix_time = file.stat().st_mtime
        date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
        date = date.replace("T", " ")

        if file.is_dir():
            file_browser(f"{dir_path}/{name}", depth + 1)
        elif check_last_modified(date):
            print("\t" * (depth + 1) + name + " Last modified: " + date)
            client.fput_object(
                bucket_name, f"{file_path}/{name}", f"{file_path}/{name}")


if __name__ == "__main__":
    file_browser(dir_path, -1)
    # print(check_last_modified("2024-04-21"))
