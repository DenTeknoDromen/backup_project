from datetime import datetime

def write_log(file_path, curr_log):
    curr_date = datetime.now().isoformat(timespec="minutes")
    curr_date = curr_date.replace("T", " ")
    curr_log[0] = f"Last backup: {curr_date}\n"
    with open(file_path, "w") as f:
        f.writelines(curr_log)