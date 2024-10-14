SHELL := /bin/bash

export DEFAULT_HELP_TARGET := help/all

export README_TEMPLATE_REPO_ORG := "sr2c"
export README_TEMPLATE_FILE := templates/README.md.gotmpl
export README_DEPS := docs/targets.md

-include $(shell curl -sSL -o .build-harness "https://cloudposse.tools/build-harness"; echo .build-harness)

.PHONY: .init
init::
	ln -sn "$$(pwd)" build-harness-extensions