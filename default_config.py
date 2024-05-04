from write_files import write_config

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