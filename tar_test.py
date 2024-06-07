import os.path
import tarfile

def make_tarfile(dir_path, name):
    output_name = "temp/" + name + ".tar"
    with tarfile.open(output_name, 'w:bz2') as tar:
        tar.add(dir_path)

#make_tarfile("test_dir")