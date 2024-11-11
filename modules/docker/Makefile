.PHONY: docker/push

## Push $DOCKER_IMAGE_NAME
docker/push:
	$(call assert-set,DOCKER)
	$(call assert-set,DOCKER_IMAGE_NAME)
	"$(DOCKER)" push $(DOCKER_IMAGE_NAME)

