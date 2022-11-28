TMP ?= /tmp
TFLINT ?= $(BUILD_HARNESS_PATH)/vendor/tflint
TFLINT_VERSION ?= 0.43.0
TFLINT_URL ?= https://github.com/terraform-linters/tflint/releases/download/v$(TFLINT_VERSION)/tflint_$(OS)_$(BUILD_HARNESS_ARCH).zip

## Alias for tflint/{install,init,run}
tflint: tflint/install tflint/init tflint/run
	@exit 0

## Install terraform
tflint/install:
	@[ -x $(TFLINT) ] || ( \
		echo "Installing TFLint $(TFLINT_VERSION) ($(OS)) from $(TFLINT_URL)" && \
		curl '-#' -fL -o $(TMP)/tflint.zip $(TFLINT_URL) && \
		unzip -q -d $(TMP)/ $(TMP)/tflint.zip && \
		mv $(TMP)/tflint $(TFLINT) && \
		rm -f $(TMP)/tflint.zip \
		)
	$(TFLINT) -v

## Initialise tflint
tflint/init:
	$(TFLINT) --init

## Run tflint
tflint/run:
	@$(TFLINT) --module