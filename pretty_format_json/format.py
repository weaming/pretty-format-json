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
import re
import datetime
from collections import OrderedDict

try:
    from commands import getstatusoutput as get_status_output
except ImportError:
    from subprocess import getstatusoutput as get_status_output

DEBUG = os.getenv("DEBUG")
FORCE_SORT = os.getenv("FORCE_SORT")


def get_text(fp):
    if fp:
        return open(fp).read()
    else:
        return sys.stdin.read()


def parse_text(text):
    text = "\n".join(x.strip() for x in text.split("\n"))
    text = (
        text.replace("true", "True").replace("false", "False").replace(
            "null", "None"
        ).replace("nil", "None")
    )
    if DEBUG:
        print(text)
    if not text:
        return None

    py_obj = ast.literal_eval(text)
    return py_obj


def eval_in_nodejs(text):
    if "'" in text:
        eval_text = 'node -e "console.log(JSON.stringify({}))"'.format(text)
    else:
        eval_text = "node -e 'console.log(JSON.stringify({}))'".format(text)

    if DEBUG:
        print("NODE: shell command")
        print(eval_text)

    try:
        code, output = get_status_output(eval_text)
    except:
        if DEBUG:
            raise
        else:
            return text

    if DEBUG:
        print(code)
        print(output)
    if code == 0:
        return output

    return text


def pretty_print(data):
    def json_serializer(obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            if isinstance(obj, datetime.date):
                fmt = os.getenv("DATE_FORMAT")
                if fmt:
                    return obj.strftime(fmt)
            if isinstance(obj, datetime.datetime):
                fmt = os.getenv("DATETIME_FORMAT")
                if fmt:
                    return obj.strftime(fmt)
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))

    indent = int(os.getenv("JSON_INDENT", 2))
    data = to_ordered_dict(data)
    print(
        json.dumps(
            data, indent=indent, ensure_ascii=False, default=json_serializer
        )
    )


def asign(a, b):
    for k in sorted(a.keys()):
        v = a[k]
        if isinstance(v, dict):
            v = to_ordered_dict(v)
        elif isinstance(v, list):
            v = list(map(to_ordered_dict, v))

        b[k] = v


def to_ordered_dict(data):
    # parse list
    if isinstance(data, (tuple, list)):
        return list(map(to_ordered_dict, data))

    # do not process other types
    if not isinstance(data, dict):
        return data

    # ordered already
    if isinstance(data, OrderedDict):
        if not FORCE_SORT:
            return data

    # sort dict
    rv = OrderedDict()
    asign(data, rv)
    return rv


def main():
    fp = None
    if len(sys.argv) > 1:
        fp = sys.argv[1]

    text = get_text(fp)
    if re.search(r'\)\s*,', text):
        text = text.replace('false', 'False').replace('true', 'True')
        text = json.dumps(ast.literal_eval(text), ensure_ascii=False)
    else:
        text = eval_in_nodejs(text)
    pretty_print(parse_text(text))


if __name__ == "__main__":
    main()
