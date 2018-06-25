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


def get_text(fp):
    if fp:
        return open(fp).read()
    else:
        return sys.stdin.read()


def parse_text(text):
    text = '\n'.join(x.strip() for x in text.split('\n'))
    text = text.replace('true', 'True').replace('false', 'False').replace(
        'null', 'None').replace('nil', 'None')
    # print(text)
    if not text:
        return None

    py_obj = ast.literal_eval(text)
    return py_obj


def pretty_print(data):
    indent = int(os.getenv('JSON_INDENT', 2))
    print(json.dumps(data, indent=indent, ensure_ascii=False))


def main():
    fp = None
    if len(sys.argv) > 1:
        fp = sys.argv[1]

    text = get_text(fp)
    pretty_print(parse_text(text))


if __name__ == "__main__":
    main()
