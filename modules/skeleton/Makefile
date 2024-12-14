
## Initialise a new Terraform/OpenTofu module project with template files
skeleton/tf: depends/curl
	mkdir -p test
	touch test/.gitkeep
	curl https://gitlab.com/guardianproject-ops/templates/terraform-module-template/-/archive/main/terraform-module-template-main.tar.gz \
		| tar --strip-components 1 -zxvkf - terraform-module-template-main/{main,outputs,variables,versions}.tf \
			terraform-module-template-main/README.yaml terraform-module-template-main/LICENSE
