
TERRAFORM_MODULES_TEMPLATES_DIR := "$(BUILD_HARNESS_EXTENSIONS_PATH)/templates/python"

## Initialise a Terraform module with templates
tfmodule/init:
	@([ -f .gitlab-ci.yml ] && echo ".gitlab-ci.yml already exists") || true
	@[ -f .gitlab-ci.yml ] || cp $(TERRAFORM_MODULE_TEMPLATES_DIR)/.gitlab-ci.yml .gitlab-ci.yml
	@([ -f .tflint.hcl ] && echo ".tflint.hcl already exists") || true
	@[ -f .tflint.hcl ] || cp $(TERRAFORM_MODULE_TEMPLATES_DIR)/.tflint.hcl .tflint.hcl
