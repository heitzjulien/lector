import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

LLM = os.getenv("LLM_MODEL", "llama3.2")
FILE_NAME = os.getenv("PDF_FILE_NAME", "MARCUS_AURELIUS.pdf")
GDRIVE_URL = os.getenv("GDRIVE_URL")

PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

CLIENT = OpenAI(
    base_url='http://ollama:11434/v1',
    api_key=LLM
)

# LLM prompt
SYSTEM_MESSAGE = """You are a helpful AI assistant. When providing answers:
- Use the provided context when relevant
- Be concise and clear
- If you're not sure about something, say so
- If the context doesn't help answer the question, use your general knowledge"""

# LLM parameters
DEFAULT_LLM_PARAMS = {
    "temperature": float(os.getenv("DEFAULT_TEMPERATURE", 0.7)),
    "max_tokens": int(os.getenv("MAX_TOKENS", 2000)),
    "top_p": float(os.getenv("TOP_P", 1.0)),
    "frequency_penalty": float(os.getenv("FREQUENCY_PENALTY", 0)),
    "presence_penalty": float(os.getenv("PRESENCE_PENALTY", 0))
}