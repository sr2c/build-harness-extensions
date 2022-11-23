SHELL := /bin/bash

export DEFAULT_HELP_TARGET ?= help/all
export README_TEMPLATE_FILE ?= templates/README.md.gotmpl

-include $(shell curl -sSL -o .build-harness "https://cloudposse.tools/build-harness"; echo .build-harness)
