from .Rsyncer import Rsyncer

def main():
    process = Rsyncer("/opt/django_developer_portfolio", "/opt/django_developer_portfolio", "/tmp/backup")
    process.confirm()

if __name__ == "__main__":
    main()