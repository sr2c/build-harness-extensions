#!/usr/bin/env python3

import glob
import re
from typing import Dict

ANSIBLE_FILE_PATTERNS = [
    "defaults/**/*.yml",
    "handlers/**/*.yml",
    "tasks/**/*.yml",
    "vars/**/*.yml",
]

RE_VARIABLE_LINE = re.compile(r".*#\s*\@var\s+([^:]+):\s+([^#]*)#\s*(.*)\s*")
RE_TAG_LINE = re.compile(r".*#\s*\@tag\s+([^#]+)#\s*(.*)\s*")


class AnsibleRole:
    tags: Dict
    vars: Dict

    def __init__(self):
        self.tags = {}
        self.vars = {}

    def parse_file(self, filename):
        with open(filename) as handle:
            lines = handle.readlines()
            for line in lines:
                self._parse_line(line)

    def _parse_line(self, line):
        if matches := RE_VARIABLE_LINE.match(line):
            var_name, var_default, var_description = matches.groups()
            var_name = var_name.strip()
            var_default = var_default.strip()
            var_description = var_description.strip()
            if var_name in self.vars:
                raise RuntimeError(f"Duplicate definition for variable {var_name}")
            self.vars[var_name] = (var_default, var_description)
        elif matches := RE_TAG_LINE.match(line):
            tag_name, tag_description = matches.groups()
            tag_name = tag_name.strip()
            tag_description = tag_description.strip()
            if tag_name in self.tags:
                raise RuntimeError(f"Duplicate definition for tag {tag_name}")
            self.tags[tag_name] = tag_description


def find_all_ansible_filenames():
    files = []
    for pattern in ANSIBLE_FILE_PATTERNS:
        files.extend(glob.glob(pattern, recursive=True))
    return files


if __name__ == "__main__":
    ansible_filenames = find_all_ansible_filenames()
    role = AnsibleRole()
    for filename in ansible_filenames:
        role.parse_file(filename)

    if role.vars:
        print("## Role Variables")
        print()
        print("| Variable     | Default Value  | Description  |")
        print("| ------------ | -------------- | ------------ |")
        var_names = sorted(role.vars.keys())
        for var_name in var_names:
            var_default = role.vars[var_name][0]
            if var_default == "REQUIRED":
                var_default = "**REQUIRED**"
            elif var_default == "":
                var_default = "~"
            else:
                var_default = f"`{var_default}`"
            print(f"| {var_name} | {var_default} | {role.vars[var_name][1]} |")

    if role.tags:
        print("## Role Tags")
        print()
        print("| Tag Name     | Description  |")
        print("| ------------ | ------------ |")
        tag_names = sorted(role.tags.keys())
        for tag_name in tag_names:
            print(f"| {tag_name} | {role.tags[tag_name][0]} |")
