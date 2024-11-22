# Lector 📚

Lector is a RAG (Retrieval-Augmented Generation) system that enables interaction with PDF documents using Large Language Models (LLMs). The current implementation uses Marcus Aurelius' writings as a knowledge base.

## Key Features ✨

- Natural interaction with PDF documents
- RAG system for accurate contextual responses
- Support for different language models via Ollama
- Flexible model parameters
- Intuitive command-line interface

## Technologies 🛠

| Category | Technologies |
|----------|-------------|
| Core | Python 3.13 |
| Containerization | Docker, Docker Compose |
| LLM | Ollama |
| Embeddings | PyTorch, mxbai-embed-large |
| Text Generation | llama3.2 |

## Installation ⚙️

### Prerequisites

- Docker and Docker Compose
- Make
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/heitzjulien/lector.git
   cd lector
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```

### Configuration

Available environment variables:

```ini
# LLM Parameters
# LLM Parameters
DEFAULT_TEMPERATURE=0.7    # Controls response creativity (0.0-1.0)
MAX_TOKENS=2000           # Maximum response length
TOP_P=1.0                 # Nucleus sampling parameter
FREQUENCY_PENALTY=0       # Controls repetition
PRESENCE_PENALTY=0        # Controls topic diversity

# Model and Data Configuration
LLM_MODEL=llama3.2        # Default LLM model
PDF_FILE_NAME=MARCUS_AURELIUS.pdf
GDRIVE_URL=URL_GOOGLE_DRIVE
```

## Quick Start 🚀

### Complete Demo
```bash
# With RAG
make demo

# Without RAG
make demo-no-rag
```

The `demo` command automatically:
1. Builds the containers
2. Pulls the required models
3. Sets up the PDF document
4. Runs an example question

## Available Commands 📝

### Setup Commands
```bash
# Build containers
make build

# Pull the required models
make pull MODEL=mxbai-embed-large
make pull MODEL=llama3.2

# Setup PDF document
make setup
```

### Interaction Commands
```bash
# Ask a question using RAG
make ask q="What did Marcus Aurelius say about virtue?"

# Ask a question without RAG
make ask-no-rag q="Who was Marcus Aurelius?"

# Ask with custom temperature
make ask q="Your question" t=0.2
```

### Utility Commands
```bash
# Show help
make help

# Check container status
make status
```

## Parameter Guide 🎛

### Temperature (0.0-1.0)

Temperature affects response style:

| Range | Response Style | Recommended Use |
|-------|----------------|-----------------|
| 0.1-0.3 | Factual & Precise | Technical questions, definitions |
| 0.4-0.7 | Balanced | General use |
| 0.8-1.0 | Creative | Creative content generation |

Examples:
```bash
# Factual response
make ask q="What are the main principles in Marcus Aurelius' writings?" t=0.1

# Creative response
make ask q="Write a poem about Marcus Aurelius' philosophy" t=0.8
```

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for details.