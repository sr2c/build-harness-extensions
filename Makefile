SHELL := /bin/bash

export DEFAULT_HELP_TARGET ?= help/all
export README_TEMPLATE_FILE ?= templates/README.md.gotmpl

# List of targets the `readme` target should call before generating the readme
export README_DEPS ?= docs/targets.md

-include $(shell curl -sSL -o .build-harness-ext "https://gitlab.com/sr2c/build-harness-extensions/-/raw/main/Makefile.bootstrap"; echo .build-harness-ext)
