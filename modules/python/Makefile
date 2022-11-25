
PYTHON_TEMPLATES_DIR := "$(BUILD_HARNESS_EXTENSIONS_PATH)/templates/python"

## Run bandit to detect security issues
python/bandit: python/deps
	pip install --quiet bandit
	bandit -c bandit.yml -r .

## Install base dependencies with pip (from requirements.txt)
python/deps: python/deps/base

python/deps/base:
	pip install -r requirements.txt

## Install all dependencies with pip (from base and requirements-*.txt)
python/deps/all: requirements.txt requirements-*.txt
	for file in $^; do \
		pip install --quiet -r $${file}; \
	done

## List available extra dependency sets
python/deps/list: requirements-*.txt
	@for file in $^; do \
		echo $${file} | sed -e 's/^requirements-//' -e 's/.txt$$//'; \
	done

## Install extra dependencies with pip (from requirements-%.txt)
python/deps/%:
	([ -f requirements-$(word 3,$(subst /, ,$@)).txt ] && \
		pip install --quiet -r requirements-$(word 3,$(subst /, ,$@)).txt) || true

## Initialise a Python project with templates
python/init:
	@([ -f .gitignore ] && echo ".gitignore already exists") || true
	@[ -f .gitignore ] || cp $(PYTHON_TEMPLATES_DIR)/gitignore .gitignore
	@([ -f .gitlab-ci.yml ] && echo ".gitlab-ci.yml already exists") || true
	@[ -f .gitlab-ci.yml ] || cp $(PYTHON_TEMPLATES_DIR)/gitlab-ci.yml .gitlab-ci.yml
	@([ -f bandit.yml ] && echo "bandit.yml already exists") || true
	@[ -f bandit.yml ] || cp $(PYTHON_TEMPLATES_DIR)/bandit.yml bandit.yml
	@([ -f mypy.ini ] && echo "mypy.ini already exists") || true
	@[ -f mypy.ini ] || cp $(PYTHON_TEMPLATES_DIR)/mypy.ini mypy.ini

## Run mypy to detect type issues
python/mypy: python/deps python/deps/types
	pip install --quiet mypy
	mypy .
