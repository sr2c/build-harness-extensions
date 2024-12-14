SHELL := /bin/bash

export DEFAULT_HELP_TARGET := help/all

export README_TEMPLATE_REPO_ORG := "sr2c"
export README_TEMPLATE_FILE := templates/README.md.gotmpl
export README_DEPS := docs/targets.md

export BUILD_HARNESS_EXT_ORG ?= sr2c
export BUILD_HARNESS_EXT_PROJECT ?= build-harness-extensions
export BUILD_HARNESS_EXT_BRANCH ?= main

# Resolves BUILD_HARNESS_EXTENSIONS_PATH to BUILD_HARNESS_EXTENSIONS_PATH_LOCAL when BUILD_HARNESS_EXTENSIONS_PATH does not exist
BUILD_HARNESS_EXTENSIONS_PATH ?= $(shell until [ -d "$(BUILD_HARNESS_EXT_PROJECT)" ] || [ "`pwd`" == '/' ]; do cd ..; done; pwd)/$(BUILD_HARNESS_EXT_PROJECT)
BUILD_HARNESS_EXTENSIONS_PATH_LOCAL := $(PWD)/$(BUILD_HARNESS_EXT_PROJECT)
export BUILD_HARNESS_EXTENSIONS_PATH := $(or $(wildcard $(BUILD_HARNESS_EXTENSIONS_PATH)),$(BUILD_HARNESS_EXTENSIONS_PATH_LOCAL))

export EXT_INTERACTIVE := $(shell [ -t 0 ] && echo 1 || echo 0)

-include $(shell curl -sSL -o .build-harness "https://cloudposse.tools/build-harness"; echo .build-harness)

.PHONY: .init
init::
	ln -sn "$$(pwd)" build-harness-extensions