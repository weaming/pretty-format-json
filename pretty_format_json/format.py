#!/usr/bin/env python3
# coding: utf-8
"""
Author       : weaming
Created Time : 2018-06-25 17:07:30

Pretty print json contains python style coments, string literal.
"""
import os
import sys
import json
import ast
from collections import OrderedDict

try:
    from commands import getstatusoutput as get_status_output
except ImportError:
    from subprocess import getstatusoutput as get_status_output

DEBUG = os.getenv('DEBUG')


def get_text(fp):
    if fp:
        return open(fp).read()
    else:
        return sys.stdin.read()


def parse_text(text):
    text = '\n'.join(x.strip() for x in text.split('\n'))
    text = text.replace('true', 'True').replace('false', 'False').replace(
        'null', 'None').replace('nil', 'None')
    if DEBUG:
        print(text)
    if not text:
        return None

    py_obj = ast.literal_eval(text)
    return py_obj


def eval_node(text):
    if "'" in text:
        eval_text = 'node -e "console.log(JSON.stringify({}))"'.format(text)
    else:
        eval_text = "node -e 'console.log(JSON.stringify({}))'".format(text)

    if DEBUG:
        print("NODE: shell command")
        print(eval_text)

    code, output = get_status_output(eval_text)
    if DEBUG:
        print(code)
        print(output)
    if code == 0:
        return output

    return text


def pretty_print(data):
    indent = int(os.getenv('JSON_INDENT', 2))
    data = to_ordered_dict(data)
    print(json.dumps(data, indent=indent, ensure_ascii=False))


def asign(a, b):
    for k in sorted(a.keys()):
        v = a[k]
        if isinstance(v, dict):
            v = to_ordered_dict(v)
        elif isinstance(v, list):
            v = list(map(to_ordered_dict, v))

        b[k] = v


def to_ordered_dict(data):
    # ignore non dict data
    if not isinstance(data, dict):
        return data

    rv = OrderedDict()

    asign(data, rv)
    return rv


def main():
    fp = None
    if len(sys.argv) > 1:
        fp = sys.argv[1]

    text = get_text(fp)
    text = eval_node(text)
    pretty_print(parse_text(text))


if __name__ == "__main__":
    main()
