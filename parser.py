# --*-- coding:utf-8 --*--
# Time: 2020/7/28 15:58
# Author: chuanman.yu
# Email: 1165358716@qq.com
# File: test.py
# Software: PyCharm

import argparse
import sys
import json
from pathlib import Path


def flat(list_data):
    result = []
    for i in list_data:
        if isinstance(i, list):
            result.extend(flat(i))
        else:
            result.append(i)
    return result


def test_list(args):
    parser = argparse.ArgumentParser(description='Returns hive list for python')
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args(args)
    input_data = json.loads(args.input)
    result = flat(input_data)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as output_path:
        output_path.write('{}'.format(json.dumps(result))


if __name__ == '__main__':

    test_list(sys.argv[1:])
