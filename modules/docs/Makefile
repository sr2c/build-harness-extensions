
## Generate documentation for an Ansible collection or role
docs/ansible.md: $(wildcard defaults/*.yml handlers/*.yml playbooks/*.yml roles/*/meta/main.yml tasks/*.yml vars/*.yml)
	@echo "<!-- markdownlint-disable -->" > $@
	/usr/bin/env python3 $(BUILD_HARNESS_EXTENSIONS_PATH)/modules/docs/ansible-doc.py >> $@
	@echo "<!-- markdownlint-enable -->" >> $@

## Generate documentation for a Terraform module, splitting out inputs relating to cloudposse/label/null
docs/terraform-split.md: docs/terraform.md
	/usr/bin/env python3 $(BUILD_HARNESS_EXTENSIONS_PATH)/modules/docs/terraform-split.py > $@
