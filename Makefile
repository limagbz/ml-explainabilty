.DEFAULT_GOAL := help
SHELL := /bin/bash

########################################################################################
# Setup Project & Dependencies                                                  	   #
########################################################################################
.PHONY: clean requirements setup

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Synchronize Python Dependencies
requirements:
	uv sync

## Initial Setup
setup: requirements
	uv run -- pre-commit install
	sudo apt install openjdk-21-jdk -y

########################################################################################
# Tools										                                           #
########################################################################################
.PHONY: notebook spark-ui

notebook: ## Open a Jupyter Notebook
	uv run -- jupyter lab

spark-ui: ## Show Spark
	@echo "Spark UI: http://localhost:4040/"

########################################################################################
# Format, Lint & Tests						                                           #
########################################################################################
.PHONY: format lint pre-commit test type-check

## Format code
format:
	uv run -- ruff format

## Lint code
lint:
	uv run -- ruff check

## Pre-commit
pre-commit:
	uv run -- pre-commit run --all-files

## Unit testing
test:
	uv run -- pytest

## Type Checking
type-check:
	uv run -- ty check

########################################################################################
# Self Documenting Commands                                                     	   #
########################################################################################
.PHONY: help

help:
	@echo
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) == Darwin && echo '--no-init --raw-control-chars')
	@echo
