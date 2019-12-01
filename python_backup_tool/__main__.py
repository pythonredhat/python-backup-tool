from .Rsyncer import Rsyncer
from .config import *
import yaml

def main():
    with open('/usr/bin/backup/config.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    process = Rsyncer(cfg['source_dir'], cfg['destination_dir'], cfg['destination_ip'], cfg['rsync_user'])
    process.confirm_dir_exists()
    process.confirm_ssh_connection()
    process.rsync_incremental()

if __name__ == "__main__":
    main()