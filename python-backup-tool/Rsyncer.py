import os
import sys
from .config import *


class Rsyncer():
    def __init__(self, os_dir, source, destination):
        self.os_dir = os_dir
        self.source = source
        self.destination = destination

    def confirm(self):
        if not os.path.exists(self.os_dir):
            print(f"{self.os_dir} does not exist")
            sys.exit(1)
        else:
            print(f"Confirmed {self.os_dir} does exist, beginning rsync process...")

 #   def rsync(source, destination):

if __name__ == "__main__":
    process = Rsyncer("/opt/django_developer_portfolio", "/opt/django_developer_portfolio", "/tmp/backup")
    process.confirm()

'''
workflow
1) confirm directory exists to backup
2) take that directory and do an incremental rsync to remote directory
3) progress bar?

extra:
1) add logger
2) add exceptions
3) unit tests
4) monitoring
'''