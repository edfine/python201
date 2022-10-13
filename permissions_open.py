import os

def permissions_open(filename):
    print(f'I am going to change the permissions of {filename}!')
    return os.chmod(filename, 0o777)
