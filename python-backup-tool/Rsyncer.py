import os
import sys
from .config import *
import logging
import time
import paramiko

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="./logs/rsync.log")


class Rsyncer():
    def __init__(self, source_dir, destination_dir, destination_ip, rsync_user):
        self.source_dir = source_dir
        self.destination = destination_dir
        self.destination_ip = destination_ip
        self.rsync_user = rsync_user 
        
    def confirm_dir_exists(self):
        if not os.path.exists(self.source_dir):
            print(f"{self.source_dir} does not exist")
            logging.debug(f"{self.source_dir} does not exist")
            sys.exit(1)
        else:
            print(f"Confirmed {self.source_dir} does exist, beginning rsync process...")
            logging.debug(f"Confirmed {self.source_dir} does exist, beginning rsync process...")

    def confirm_ssh_connection(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.connect({self.destination_ip}, {self.rsync_user})
            print(f"Connection to {self.destination_ip} worked")
            logging.debug(f"Connection to {self.destination_ip} worked")
        except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
            logging.error(f"ssh connection failed!!!")
            logging.exception(e)
            print(f"ssh connection failed!!!!")
            print(e)
        finally:
            ssh.close()

   #confirm ssh connection
   # def confirm_rsync_connection(self):

    def rsync_incremental(self):
        try:
            start_time = time.time()
            os.system(f"rsync -avr -e 'ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null' --delete {self.source_dir} {self.rsync_user}@{self.destination_ip}:{self.destination}")
            print("Rsync process completed in %s seconds!" % (time.time() - start_time))
            logging.debug("Rsync process completed in %s seconds!" % (time.time() - start_time))
        except Exception as e:
            logging.error(f"Rsync process failed!")
            logging.exception(e)
            print(f"Rsync process failed!")
            print(e)
            sys.exit(1)

    


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