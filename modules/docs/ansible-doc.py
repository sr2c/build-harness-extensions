#!/usr/bin/env python3

import glob
import os
import re
from typing import Any, Dict, List

import yaml

RE_VARIABLE_LINE = re.compile(r".*#\s*\@var\s+([^:]+):\s+([^#]*)#\s*(.*)\s*")
RE_TAG_LINE = re.compile(r".*#\s*\@tag\s+([^#]+)#\s*(.*)\s*")

ROLE_FILE_PATTERNS = [
    "defaults/**/*.yml",
    "handlers/**/*.yml",
    "tasks/**/*.yml",
    "vars/**/*.yml",
]


def find_all_role_files() -> List[str]:
    files = []
    for pattern in ROLE_FILE_PATTERNS:
        files.extend(glob.glob(pattern, recursive=True))
    return files


class AnsibleRole:
    tags: Dict
    vars: Dict

    def __init__(self):
        self.tags = {}
        self.vars = {}

    def parse(self):
        for filename in find_all_role_files():
            self._parse_file(filename)

    def _parse_file(self, filename: str) -> None:
        with open(filename) as handle:
            lines = handle.readlines()
            for line in lines:
                self._parse_line(line)

    def _parse_line(self, line: str) -> None:
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


def document_role():
    role = AnsibleRole()
    role.parse()

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
        print()

    if role.tags:
        print("## Role Tags")
        print()
        print("| Tag Name     | Description  |")
        print("| ------------ | ------------ |")
        tag_names = sorted(role.tags.keys())
        for tag_name in tag_names:
            print(f"| {tag_name} | {role.tags[tag_name][0]} |")
        print()


class AnsibleCollection:
    galaxy: Dict[str, Any]
    roles: Dict[str, str]
    playbooks: Dict[str, str]

    def __init__(self):
        self.galaxy = yaml.safe_load(open("galaxy.yml"))
        self.roles = {}
        self.playbooks = {}

    def discover_roles(self):
        for role_metadata_filename in glob.glob("roles/*/meta/main.yml"):
            filename_parts = role_metadata_filename.split("/")
            role_metadata = yaml.safe_load(open(role_metadata_filename))
            description = role_metadata["galaxy_info"]["description"]
            self.roles[f"{self.galaxy['namespace']}.{self.galaxy['name']}.{filename_parts[1]}"] = description

    def discover_playbooks(self):
        for playbook_metadata_filename in glob.glob("playbooks/*.yml"):
            playbook_name = playbook_metadata_filename.split("/")[1][:-4]
            playbook = yaml.safe_load(open(playbook_metadata_filename))
            description = "*TODO*"
            try:
                description = playbook[0]["name"]
            except (IndexError, KeyError):
                pass
            self.playbooks[f"{self.galaxy['namespace']}.{self.galaxy['name']}.{playbook_name}"] = description


def document_collection():
    collection = AnsibleCollection()
    collection.discover_roles()
    collection.discover_playbooks()

    if collection.roles:
        print("## Roles")
        print()
        print("| Role Name    | Description  |")
        print("| ------------ | ------------ |")
        role_names = sorted(collection.roles.keys())
        for role_name in role_names:
            print(f"| [{role_name}](./roles/{role_name}) | {collection.roles[role_name]} |")
        print()

    if collection.playbooks:
        print("## Playbooks")
        print()
        print("| Playbook Name    | Description  |")
        print("| ---------------- | ------------ |")
        playbook_names = sorted(collection.playbooks.keys())
        for playbook_name in playbook_names:
            print(f"| [{playbook_name}](./playbooks/{playbook_name}.yml) | {collection.playbooks[playbook_name]} |")
        print()


if __name__ == "__main__":
    if os.path.isfile("tasks/main.yml"):
        document_role()
    elif os.path.isfile("galaxy.yml"):
        document_collection()
    else:
        raise RuntimeError("This isn't a role or a collection so I don't know how to document it.")
