import os
from datetime import datetime

#test_dir = os.scandir("test_dir")

# for file in temp:
#     unix_time = file.stat().st_mtime
#     date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
#     date = date.replace("T", " ")
#     print(file.name + " Last modified: " + date)

dir_path = "test_dir"
def file_browser(dir_path, depth):
    test_dir = os.scandir(dir_path)
    # print(f"{("m" * (depth - 1))}>>>> {dir_path}")
    #print("---" * (depth) + dir_path)
    for file in test_dir:
        name = file.name
        unix_time = file.stat().st_mtime
        date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
        date = date.replace("T", " ")
        print("|", end="")

        if file.is_dir():
            print("---" * (depth) + name)
            file_browser(dir_path + "/" + name, depth + 1)
            print("|")
        else:
            print("    " * (depth), end="")
            if depth>0:
                print("|", end="")
            print("---" + file.name + " Last modified: " + date)

file_browser(dir_path, 1)
