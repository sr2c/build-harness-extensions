.PHONY: docker/push

## Push $DOCKER_IMAGE_NAME
docker/push:
	$(call assert-set,DOCKER)
	$(call assert-set,DOCKER_IMAGE_NAME)
	"$(DOCKER)" push $(DOCKER_IMAGE_NAME)


## When in Gitlab CI, login to the current repo's container registry
docker/login/gitlab:
	$(call assert-set,CI_REGISTRY_PASSWORD)
	$(call assert-set,CI_REGISTRY)
	$(call assert-set,CI_REGISTRY_USER)
	@echo "${CI_REGISTRY_PASSWORD}" | echo docker login ${CI_REGISTRY} -u ${CI_REGISTRY_USER} --password-stdin
