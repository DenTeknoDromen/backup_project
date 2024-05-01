from datetime import datetime
from json import dumps

def write_log(curr_log):
    curr_date = datetime.now().isoformat(timespec="minutes")
    curr_date = curr_date.replace("T", " ")
    curr_log[0] = f"Last backup: {curr_date}\n"
    with open("log.txt", "w") as f:
        f.writelines(curr_log)

def write_config(file_path, curr_config):
    json_str = dumps(curr_config)
    with open(file_path, "w") as f:
        f.write(json_str)

def log_backup(output_str, curr_config):
    curr_date = datetime.now().isoformat(timespec="minutes")
    curr_date = curr_date.replace("T", " ")
    curr_config["last_backup"] = curr_date
    write_log(output_str, curr_date)
    write_config(curr_config)

        
