import os
import sys
from .config import *


class Rsyncer():
    def __init__(self, source_dir, destination_dir, destination_ip, rsync_user):
        self.source_dir = source_dir
        self.destination = destination_dir
        self.destination_ip = destination_ip
        self.rsync_user = rsync_user 
        
    def confirm_dir_exists(self):
        if not os.path.exists(self.source_dir):
            print(f"{self.source_dir} does not exist")
            sys.exit(1)
        else:
            print(f"Confirmed {self.source_dir} does exist, beginning rsync process...")

   # def confirm_rsync_connection(self):

    def rsync_incremental(self):
        os.system(f"rsync -avr -e 'ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null' --delete {self.source_dir} {self.rsync_user}@{self.destination_ip}:{self.destination}")

if __name__ == "__main__":
    process = Rsyncer("/opt/django_developer_portfolio", "/opt/django_developer_portfolio", "/tmp/backup")
    process.confirm_dir_exists()

'''
workflow
1) confirm directory exists to backup
2) confirm an rsync connection can be made
2) take that directory and do an incremental rsync to remote directory
3) have option to do full rsync
3) progress bar?
last) confirm it is done

extra:
1) add logger
2) add exceptions
3) unit tests
4) monitoring
'''