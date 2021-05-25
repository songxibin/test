import argparse
import sys
import random
from pathlib import Path


def test_list(args):
    parser = argparse.ArgumentParser(description='Returns hive list for python')
    # parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args(args)
    input_data = random.choice(["a", "b"])
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as output_path:
        output_path.write('{}'.format(input_data))


if __name__ == '__main__':

    test_list(sys.argv[1:])
