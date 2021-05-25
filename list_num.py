import argparse
import sys
import json
from pathlib import Path


def test_list(args):
    parser = argparse.ArgumentParser(description='Returns list for python')
    parser.add_argument("--input", type=int, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args(args)
    list = []
    for i in range(0,args.input):
        list.append(i)
    result = str(list)
    input_data = json.loads(result)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as output_path:
        output_path.write('{}'.format(json.dumps(input_data)))


if __name__ == '__main__':

    test_list(sys.argv[1:])
