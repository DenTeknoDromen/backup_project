from json import loads

# Loads dictionary with settings from jsonfile
def load_config(curr_path):
    curr_path = curr_path   # "./config.json"
    try:
        with open(curr_path, "r") as f:
            file_content = f.read()
            return loads(file_content)
    except FileNotFoundError:
        with open(curr_path, "x"):
            print("Error, config file not found\nNew file created")
    except Exception as e:
        print("Unkown file content")

# Loads log
def load_log():
    curr_path = "./log.txt"
    try:
        with open(curr_path, "r") as f:
            curr_log = f.readlines()
            return curr_log
    except FileNotFoundError:
        with open(curr_path, "x"):
            print("Error, log file not found\nNew file created")
    except Exception as e:
        print("Unkown file content(log)")
