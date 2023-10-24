from cnns.utils import init_logger
from cnns import connect

APP_NAME = "cnns"
lg = init_logger(APP_NAME)


def main():
    connect.main()


if __name__ == "__main__":
    main()
