.DEFAULT_GOAL=help
.PHONY: check clean dev help install lint setup test

ci: install lint test ## Run CI locally
	@true

clean: ## Remove temporary artifacts
	@bin/clean

dev: setup install ## Run the Flask application in dev mode
	@uv run flask --app src run --debug

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; \
	printf "\nCommands:\n\033[35m\033[0m"} /^[$$()% a-zA-Z_-]+:.*?##/ { \
	printf "  \033[35;1m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { \
	printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: ## Install dependencies and update the environment
	@uv sync

lint: install ## Run lint and format checks
	@printf "\033[35;1m==> Lint\033[0m\n"
	@uv run ruff check

setup: ## Setup the project
	@bin/setup

test: install ## Run unit tests
	@printf "\033[35;1m==> Pytest\033[0m\n"
	@uv run pytest
