import argparse
import os
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Returns sum of two arguments')
    parser.add_argument("--name", type=str, required=True)
    parser.add_argument("--name_out", type=str, required=True)
    args = parser.parse_args(args)
    path_pre = '/data/'
    if not os.path.exists(path_pre):
        os.makedirs(path_pre)
    path = '{}{}'.format(path_pre, args.name)
    print("Start to read...")
    print('path:', path)

    with open(path, 'w') as f:
        f.write('test!test')
        print("successful write..")

        f.close()
    name_out = args.name_out
    Path(name_out).parent.mkdir(parents=True, exist_ok=True)
    with open(name_out, 'w') as output_f:
        output_f.write(path)


if __name__ == '__main__':
    main(sys.argv[1:])
