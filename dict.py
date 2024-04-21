import json

dict = {"endpoint": "127.0.0.1:",
        "port":"9000",
        "access_key": "minioadmin", 
        "secret_key": "minioadmin",
        "bucket_name": "backup",
        }

config = json.dumps(dict, indent=0)
with open("config.json", "w") as f:
    f.write(config)