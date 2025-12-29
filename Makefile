# Makefile for Django + uv + ruff + pytest

# Default environment variables
PYTHON := uv run python
MANAGE := $(PYTHON) src/manage.py
COMPOSE_FILE=deployment/local/docker-compose.yml
ENV_FILE=.env

# --- Dependency management ---
.PHONY: install
install:
	uv sync

.PHONY: upgrade
upgrade:
	uv sync --upgrade

# --- Code quality ---
.PHONY: lint_fix
lint_fix:
	uv run ruff check . --fix

.PHONY:
lint:
	uv run ruff check .

.PHONY: format_fix
format_fix:
	uv run ruff format .

.PHONY: format
format:
	uv run ruff format --check .

# --- Tests ---
.PHONY: test
test:
	uv run pytest -v --ds=project_name.settings

.PHONY: test-watch
test-watch:
	uv run pytest -v --ds=project_name.settings --maxfail=1 --ff

# --- Django management ---
.PHONY: run
run-django:
	$(MANAGE) runserver

run-uvicorn:
	$(PYTHON) src/run_uvicorn.py

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

.PHONY: shell
shell:
	$(MANAGE) shell

# --- Utilities ---
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf *.egg-info

# --- Docker Compose ---
.PHONY: up
up:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d

.PHONY: down
down:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down

.PHONY: logs
logs:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) logs -f

.PHONY: ps
ps:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) ps