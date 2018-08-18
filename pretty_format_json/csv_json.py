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

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .format import pretty_print
from data_process.io_csv import process_row_generator, new_csv_reader


def to_csv(data):
    f = StringIO()
    fields = list(data[0])
    process_row_generator(fields, iter(data), f, keep_open=True)
    return f.getvalue()


def from_csv(text):
    with new_csv_reader(StringIO(text)) as csv:
        return list(csv)


def get_target_type_from_text(text):
    if text.strip()[0] in "{[":
        return "csv"
    return "json"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--type", help="type of target output, csv and json are allowed"
    )

    args = parser.parse_args()
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
