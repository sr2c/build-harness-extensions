
TERRAFORM_MODULE_TEMPLATES_DIR := $(BUILD_HARNESS_EXTENSIONS_PATH)/templates/terraform-module
TERRAFORM_MODULE_TEMPLATES_DOTFILES := $(filter-out .,$(filter-out ..,$(notdir $(wildcard $(TERRAFORM_MODULE_TEMPLATES_DIR)/.*))))
TERRAFORM_MODULE_TEMPLATES_FILES := $(wildcard $(TERRAFORM_MODULE_TEMPLATES_DIR)/*) $(TERRAFORM_MODULE_TEMPLATES_DOTFILES)

## Initialise a Terraform module with templates
tfmodule/init:
	@for FILE in $(TERRAFORM_MODULE_TEMPLATES_FILES); do \
		([ -f $$FILE ] && echo "$$FILE already exists") || true; \
		[ -f $$FILE ] || cp $(TERRAFORM_MODULE_TEMPLATES_DIR)/$$FILE $$FILE; \
	done

