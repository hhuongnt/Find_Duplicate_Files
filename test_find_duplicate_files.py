#!/usr/bin/env python3
from argparse import ArgumentParser
from os import walk
from os.path import islink, abspath, join


def parse_arguments():
    """
    Parse command-line into argument
    """
    parser = ArgumentParser(description='Find Duplicate Files')
    parser.add_argument('--path', '-p', help='insert directory path')
    return parser.parse_args()


def scan_files(path):
    """

    """
    list_files = []
    for root, dirs, files in walk(path, topdown=False):
        for f in files:
            if not islink(f):
                list_files.append(join(root,abspath(f)))
    return list_files


path = parse_arguments().path
list_files = scan_files(path)
print (list_files)
