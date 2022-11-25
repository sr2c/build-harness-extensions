
## Install base dependencies with pip (from requirements.txt)
python/deps: python/deps/base

python/deps/base:
	pip install -r requirements.txt

## Install all dependencies with pip (from base and requirements-*.txt)
python/deps/all: requirements.txt requirements-*.txt
	for file in $^; do \
		pip install -r $${file}; \
	done

## List available extra dependency sets
python/deps/list: requirements-*.txt
	@for file in $^; do \
		echo $${file} | sed -e 's/^requirements-//' -e 's/.txt$$//'; \
	done

## Install extra dependencies with pip (from requirements-%.txt)
python/deps/%: requirements-$(word 3,$(subst /, ,$@)).txt
	pip install -r $^
