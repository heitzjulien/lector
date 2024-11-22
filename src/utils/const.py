from openai import OpenAI

LLM = "llama3.2"
FILE_NAME = "MARCUS_AURELIUS.pdf"

PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

CLIENT = OpenAI(
    base_url='http://ollama:11434/v1',
    api_key=LLM
)
