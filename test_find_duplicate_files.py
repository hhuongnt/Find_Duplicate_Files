#!/usr/bin/env python3
from argparse import ArgumentParser
from os import walk
from os.path import islink, join, getsize, abspath, expanduser
from hashlib import md5


def parse_arguments():
    """
    Parse command-line into argument
    """
    parser = ArgumentParser(description='Find Duplicate Files')
    parser.add_argument('--path', '-p', help='insert directory path')
    return parser.parse_args()


def scan_files(path):
    """
    Returns a flat list of files (scanned recursively) from the specified path.
    @parameters:
    path: the absolute path need to be scanned.
    """
    file_path_names = []
    for root, dirs, files in walk(path):
        for f in files:

            # check symbolic link
            if not islink(f):
                file_path_names.append(join(abspath(root), f))
    return file_path_names


def group_files_by_size(file_path_names):
    """
    Returns a list of groups (with at least two files) which have the same size.
    @parameters:
    file_path_names: list of file names in the specified path.
    """
    groups_file_size = {}
    for path in file_path_names:
        file_size = getsize(path)

        # ignore empty files
        if file_size:

            # if key already exists
            if file_size in groups_file_size.keys():
                groups_file_size[file_size].append(path)

            # if key not exists
            else:
                groups_file_size[file_size] = [path]
    return [group for group in groups_file_size.values() if len(group)>1]


def get_file_checksum(file_path_name):
    """
    Generate a Hash Value for a File using md5.
    @parameters:
    file_path_name: name of file content need to be hash.
    """
    with open(file_path_name, 'rb') as f:
        return md5(f.read()).hexdigest()


def group_files_by_checksum(file_path_names):
    """
    Returns a list of groups that contain duplicate files using hash value.
    @parameters:
    file_path_names: file names in the specified path.
    """
    groups_checksum = {}
    for file_path_name in file_path_names:
        hash_value = get_file_checksum(file_path_name)

        # if key already exists
        if hash_value in groups_checksum.keys():
            groups_checksum[hash_value].append(file_path_name)

        # if key not exists
        else:
            groups_checksum[hash_value] = [file_path_name]
    return groups_checksum.values()


def find_duplicate_files(file_path_names):
    """

    """


path = parse_arguments().path
list_files = scan_files(path)
print (list_files)
groups_size = group_files_by_size(list_files)
print (groups_size)
