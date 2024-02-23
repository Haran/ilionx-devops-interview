.DEFAULT_GOAL := info
SHELL := /usr/bin/bash

# Process all recipes in the current file looking for targets and comments with two hashtags
# parsing them into nicely formatted table
.PHONY: info
info:
	@grep -E '(^[/\.a-zA-Z_\-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/' && echo ""

.PHONY: venv-check
venv-check:
	@if [[ $$VIRTUAL_ENV = "" ]]; then\
		echo "ERROR: not running in venv";\
		exit 1;\
	fi

##
## Development shortcuts
.PHONY: freeze
freeze: venv-check ## Freeze current dependencies to requirements.txt
	pip freeze > requirements.txt

.PHONY: lint
lint: venv-check ## Check syntax against lint rules
	-@flake8 -v .

.PHONY: test
test: venv-check ## Run unit tests with coverage
	@coverage run -m pytest
	@coverage report -m

.PHONY: build
build: venv-check ## Compile
	 pyinstaller --onefile --clean ./main.py
