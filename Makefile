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
.PHONY: pull pull-models build setup ask ask-demo ask-no-rag ask-no-rag-demo demo demo-no-rag

pull: ## Pull LLM model into Ollama container (usage: make pull MODEL=llama3.2)
	$(INFO) "Pulling $(MODEL) model into Ollama..."
	$(COMPOSE) exec ollama ollama pull $(MODEL)
	$(SUCCESS) "$(MODEL) model pulled successfully"

pull-models:
	$(COMPOSE) exec ollama ollama pull mxbai-embed-large
	$(COMPOSE) exec ollama ollama pull llama3.2

build: ## Build and start all services
	$(INFO) "Building and starting services..."
	$(COMPOSE) up --build -d
	$(SUCCESS) "Services built and started"
	$(INFO) "Ollama API available at: http://localhost:11434"

setup: ## Setup the PDF document
	$(COMPOSE) exec app python src/app.py -m setup

ask: ## Ask a question using RAG (usage: make ask q="your question")
	$(COMPOSE) exec app python src/app.py -m ask -q "$(q)"

ask-demo: ## Ask a demo question
	$(MAKE) ask q="What is the meaning of life according to Marcus Aurelius?"

ask-no-rag: ## Ask a question without RAG (usage: make ask-no-rag q="your question")
	$(COMPOSE) exec app python src/app.py -m ask-no-rag -q "$(q)"

ask-no-rag-demo: ## Ask a demo question without RAG
	$(MAKE) ask-no-rag q="En quelles années l'équipe de France a gagné la Coupe du Monde ?"

demo: build pull-models setup ask-demo

demo-no-rag: build pull-models ask-no-rag-demo

##@ Utilities
.PHONY: status
status: ## Check the status of Docker containers
	$(COMPOSE) ps

.DEFAULT_GOAL := help