import os
import sys
from argparse import ArgumentParser
import main

working_directory = os.path.dirname(os.path.abspath(__file__))
if working_directory not in sys.path:
    sys.path.append(working_directory)

if __name__ == "__main__":
    main.main()