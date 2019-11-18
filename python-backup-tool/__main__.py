from .Rsyncer import Rsyncer
from .config import *

def main():
    process = Rsyncer(source_dir, destination_dir, destination_ip, rsync_user)
    process.confirm_dir_exists()
    process.rsync()

if __name__ == "__main__":
    main()