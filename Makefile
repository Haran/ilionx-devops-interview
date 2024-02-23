SHELL=/usr/bin/env bash
.DEFAULT_GOAL := info

# Process all recipes in the current file looking for targets and comments with two hashtags
# parsing them into nicely formatted table
.PHONY: info
info:
	@grep -E '(^[/\.a-zA-Z_\-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/' && echo ""

.PHONY: install-docker
install-docker: ## Install DockerCE, make it run with vagrant user, enable autostart
	ansible-playbook -c local -i localhost, docker-playbook.yml

.PHONY: helloworld
helloworld: ## Compile helloworld application, pack it to docker and run in container
	ansible-playbook -c local -i localhost, helloworld-playbook.yml
