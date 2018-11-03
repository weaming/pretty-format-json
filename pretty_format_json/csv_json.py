#!/usr/local/bin/python3
# coding: utf-8
"""
Author       : weaming
Created Time : 2018-07-19 03:24:06

CSV and JSON converter
"""
import sys
import argparse
import json
import io
from . import *

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .format import pretty_print
from data_process.io_csv import process_row_generator, read_csv

is_py2 = sys.version_info[0] == 2


def to_csv(data):
    if is_py2:
        fuck = lambda x: x.encode("utf8")
    else:
        fuck = lambda x: x
    data = [{fuck(k): fuck(v) for k, v in row.items()} for row in data]
    f = StringIO()
    fields = sorted(data[0]) if is_py2 else list(data[0])
    process_row_generator(fields, iter(data), f, keep_open=True)
    return f.getvalue()


def from_csv(text):
    return read_csv(StringIO(text))


def get_target_type_from_text(text):
    text = text.strip()
    if text and text[0] in "{[":
        return "csv"
    return "json"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--type", help="type of target output, csv and json are allowed"
    )
    parser.add_argument(
        "-v", "--version", default=False, action="store_true", help="print version"
    )

    args = parser.parse_args()
    if args.version:
        print(version)
        sys.exit(0)

    text = sys.stdin.read()

    t = args.type or get_target_type_from_text(text)
    if t == "csv":
        try:
            data = json.loads(text)
        except ValueError as e:
            print(e)
            sys.exit(1)

        y = to_csv(data)
        print(y)

    elif t == "json":
        pretty_print(from_csv(text))


if __name__ == "__main__":
    main()
