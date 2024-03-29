# Sample code: REPLACE with project code.
import os
import sys

from api.text_processor import TextWriter
from version_tooling import VERSION


def main():
    """
    Top-level method executed at application runtime.
    """
    w = TextWriter()
    w.out("Hello World!")
    w.out(VERSION)
    print("EXITING!")
    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
