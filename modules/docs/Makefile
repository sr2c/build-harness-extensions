
## Generate documentation for an Ansible collection or role
docs/ansible.md: $(wildcard defaults/*.yml handlers/*.yml playbooks/*.yml roles/*/meta/main.yml tasks/*.yml vars/*.yml)
	@echo "<!-- markdownlint-disable -->" > $@
	/usr/bin/env python3 $(BUILD_HARNESS_EXTENSIONS_PATH)/modules/docs/ansible-doc.py >> $@
	@echo "<!-- markdownlint-enable -->" >> $@
