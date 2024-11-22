COMPOSE = docker compose
MODEL ?= llama3.2

YELLOW = \033[33m
RED = \033[31m
GREEN = \033[32m
BLUE = \033[34m
NC = \033[0m # No Color
INFO = @echo "$(BLUE)➜$(NC)"
SUCCESS = @echo "$(GREEN)✔$(NC)"
WARNING = @echo "$(YELLOW)⚠$(NC)"

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }' $(MAKEFILE_LIST)

##@ Development
.PHONY: pull-llm build status

pull: ## Pull LLM model into Ollama container (usage: make pull MODEL=llama3.2)
	$(INFO) "Pulling $(MODEL) model into Ollama..."
	$(COMPOSE) exec ollama ollama pull $(MODEL)
	$(SUCCESS) "$(MODEL) model pulled successfully"

build: ## Build and start all services
	$(INFO) "Building and starting services..."
	$(COMPOSE) up --build -d
	$(SUCCESS) "Services built and started"
	$(INFO) "Ollama API available at: http://localhost:11434"

question: ## Ask a question to the LLM
	$(WARNING) "This command is not implemented yet"

##@ Utilities
status: ## Check the status of Docker containers
	$(COMPOSE) ps

.DEFAULT_GOAL := help