.DEFAULT_GOAL=help
.PHONY: ci clean coverage dev help install lint setup test dbuild drun dstop

ci: install lint typecheck test ## Run CI locally
	@true

clean: ## Remove temporary artifacts
	@bin/clean

coverage: ## View test coverage report
	@open tests/coverage/html/index.html

dev: setup install ## Run the application in dev mode
	@uv run fastapi dev --port 3000 src/main.py

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

setup: ## Install uv and required Python version
	@bin/setup

test: install ## Run unit tests
	@printf "\033[35;1m==> Pytest\033[0m\n"
	@uv run pytest

typecheck: install ## Run typechecker
	@printf "\033[35;1m==> Typecheck\033[0m\n"
	@uv run ty check

dbuild: ## Build a docker image of the project
	@docker build --no-cache -t highlights .

drun: dbuild ## Start the API server in a container
	@docker run --rm -d --name highlights -p 3000:3000 highlights
	@printf "\033[32;1mHighlights server is now running\033[0m\n"

dstop: ## Shut down the running container
	@docker stop -t 0 highlights
