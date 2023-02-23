import os
import sys


PATH = os.path.dirname(__file__)


def main(a, b):
    return a * b


if __name__ == "__main__":
    sys.exit(main(1, 2))
