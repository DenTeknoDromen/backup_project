import os
from datetime import datetime

def get_printline(file_info, depth):
    output = "|"
    output += ("    " * depth)
    if depth > 0:
        output += "|"
    output += "---"
    output += file_info
    return output


dir_path = "test_dir"
def file_browser(dir_path, depth):
    test_dir = os.scandir(dir_path)

    for file in test_dir:
        name = file.name
        unix_time = file.stat().st_mtime
        date = datetime.fromtimestamp(unix_time).isoformat(timespec="minutes")
        date = date.replace("T", " ")

        print(get_printline(f"{name}, Last modified: {date}", depth))

        if file.is_dir():
            file_browser(dir_path + "/" + name, depth + 1)
            print("|")


file_browser(dir_path, 0)
