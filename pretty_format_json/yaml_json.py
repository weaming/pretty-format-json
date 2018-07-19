#!/usr/local/bin/python3
# coding: utf-8
"""
Author       : weaming
Created Time : 2018-07-19 03:24:06
Prerequisites:
    pip3 install pyyaml
    pip3 install pretty-format-json

Yaml and JSON converter
"""
import sys
import argparse
import json

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from .format import pretty_print


def to_yaml(data):
    return dump(
        data, Dumper=Dumper, default_flow_style=False, allow_unicode=True)


def from_yaml(stream):
    return load(stream, Loader=Loader)


def get_target_type_from_text(text):
    if text.strip()[0] in '{[':
        return 'yaml'
    return 'json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--type',
        help="type of target output, yaml and json are allowed")

    args = parser.parse_args()
    text = sys.stdin.read()

    t = args.type or get_target_type_from_text(text)
    if t == 'yaml':
        try:
            data = json.loads(text)
        except ValueError as e:
            print(e)
            sys.exit(1)

        y = to_yaml(data)
        print(y)

    elif t == 'json':
        pretty_print(from_yaml(text))


if __name__ == '__main__':
    main()
