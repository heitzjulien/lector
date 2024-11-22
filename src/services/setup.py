import torch
import ollama
import os
from typing import List, Tuple

from services import download_from_gdrive, convert_pdf_to_text
from utils import FILE_NAME, NEON_GREEN, RESET_COLOR, GDRIVE_URL


def setup_pdf():
    """Initialize PDF document"""
    print("Downloading file...")
    url = GDRIVE_URL
    downloaded_file = download_from_gdrive(url, FILE_NAME)
    print(f"File downloaded: {downloaded_file}")

    print("Converting PDF to text...")
    convert_pdf_to_text()
    print("Conversion successful")


def setup_rag() -> Tuple[torch.Tensor, List[str]]:
    """Setup the RAG system by loading content and generating embeddings."""
    print(f"{NEON_GREEN}Initializing RAG system...{RESET_COLOR}")

    vault_content = []
    if os.path.exists("vault.txt"):
        with open("vault.txt", "r", encoding='utf-8') as vault_file:
            vault_content = vault_file.readlines()

    print(f"{NEON_GREEN}Generating embeddings...{RESET_COLOR}")
    vault_embeddings = []
    for content in vault_content:
        response = ollama.embeddings(model='mxbai-embed-large', prompt=content)
        vault_embeddings.append(response["embedding"])

    return torch.tensor(vault_embeddings), vault_content
