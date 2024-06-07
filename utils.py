from datetime import datetime
from json import dumps, loads

def get_currdate():
    curr_date = datetime.now().isoformat(timespec="minutes")
    curr_date = curr_date.replace("T", " ")
    return curr_date

def write_config(curr_config):
    curr_config['last_backup'] = get_currdate
    json_str = dumps(curr_config, indent=0)
    with open("config.json", "w") as f:
        f.write(json_str)

def load_config(curr_path):
    curr_path = curr_path   # "./config.json"
    try:
        with open(curr_path, "r") as f:
            file_content = f.read()
            return loads(file_content)
    except Exception as e:
        print("Unkown file content")

def create_default_config():
    default =   {
                "endpoint": "127.0.0.1",
                "port": "9000",
                "access_key": "minioadmin",
                "secret_key": "minioadmin",
                "bucket_name": "backup",
                "dir_path": "test_dir",
                "last_backup": "1995-11-25"
                }
    write_config(default)