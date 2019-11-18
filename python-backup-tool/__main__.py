from .Rsyncer import Rsyncer
from .config import *

def main():
    process = Rsyncer("/opt/django_developer_portfolio", "/opt/django_developer_portfolio", "/tmp/backup")
    process.confirm_dir_exists()

if __name__ == "__main__":
    main()