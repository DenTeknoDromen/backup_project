from datetime import datetime
from json import dumps

def write_log(curr_log):    
    with open("log.txt", "w") as f:
        f.writelines(curr_log)

def write_config(curr_config):
    json_str = dumps(curr_config, indent=0)
    with open("config.json", "w") as f:
        f.write(json_str)

def log_backup(output_str, curr_config):
    curr_date = datetime.now().isoformat(timespec="minutes")
    curr_date = curr_date.replace("T", " ")
    output_str.insert(0, f"{curr_date} - Backup to {curr_config['bucket_name']} completed!\n")
    curr_config['last_backup'] = curr_date
    write_log(output_str)
    write_config(curr_config)

        
