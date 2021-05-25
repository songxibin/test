import argparse
import os
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Returns sum of two arguments')
    parser.add_argument("--read_name", type=str, required=True)
    args = parser.parse_args(args)
    print("start to read...")
    # Path(args.read_path).parent.mkdir(parents=True, exist_ok=True)
    path = args.read_name
    print(path)
    with open(path, 'r') as f:
        text = f.read()
        print(text)
        f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
