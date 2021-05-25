import argparse
import os
import sys
from pathlib import Path
import json


def main(args):
    parser = argparse.ArgumentParser(description='Returns sum of two arguments')
    parser.add_argument("--read_name", type=str, required=True) # List Item
    args = parser.parse_args(args)
    print("images:zjr123/read_op:test")
    # Path(args.read_path).parent.mkdir(parents=True, exist_ok=True)
    path = json.loads(args.read_name) # string to list
    # path = args.read_name
    print(path)
    for i in path:
        with open(i, 'r') as f:
            text = f.read()
            print(text)
            print(str(i))
            f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
