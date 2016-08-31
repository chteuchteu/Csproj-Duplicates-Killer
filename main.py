#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re


parser = argparse.ArgumentParser(description='csproj duplicates killer')
parser.add_argument('csproj_path')
args = parser.parse_args()

csproj_path = args.csproj_path
if not os.path.isfile(csproj_path):
    print('Could not find {}'.format(csproj_path))
    sys.exit(1)

with open(csproj_path, 'r') as fh:
    lines = [line.rstrip(os.linesep) for line in fh]

# Remove duplicates entries in lines
line_regex = re.compile('\s*<Content Include="(.*)" \/>')

new_lines = []
for line in lines:
    # Check if it matches what we're looking for
    if line_regex.match(line):
        if line in new_lines:
            # This line already is in new_lines, just skip it
            print('Found duplicate {}'.format(line))
            continue

    new_lines.append(line)

csproj_newpath = csproj_path + '.new'
try:
    with open(csproj_newpath, 'w') as fh:
        fh.truncate()

        for line in new_lines:
            fh.write(str(line) + '\n')

        print('Successfully removed {} duplicates lines'.format(len(lines) - len(new_lines)))
        print('Result csproj has been written to "{}". Please review changes and update "{}".'.format(
            os.path.basename(csproj_newpath), os.path.basename(csproj_path)
        ))
except PermissionError:
    print('Could not write csproj file {}'.format(os.path.basename(csproj_newpath)))
    print('This is usually a permission error')

    if os.path.isfile(csproj_newpath):
        print('{} already exists: it is write-protected?'.format(os.path.basename(csproj_newpath)))
