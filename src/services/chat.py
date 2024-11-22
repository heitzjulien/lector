import torch
import ollama

from typing import List
from utils import RESET_COLOR, CYAN, CLIENT, LLM, SYSTEM_MESSAGE, DEFAULT_LLM_PARAMS
from services.setup import setup_rag


def get_relevant_context(query: str, vault_embeddings: torch.Tensor, vault_content: List[str], top_k: int = 3) -> List[
    str]:
    """Get the most relevant context passages for a query."""
    if vault_embeddings.nelement() == 0:
        return []

    # Get embeddings for the query
    query_embedding = ollama.embeddings(model='mxbai-embed-large', prompt=query)["embedding"]

    # Calculate similarity scores
    cos_scores = torch.cosine_similarity(torch.tensor(query_embedding).unsqueeze(0), vault_embeddings)

    # Get top_k most relevant passages
    top_k = min(top_k, len(cos_scores))
    top_indices = torch.topk(cos_scores, k=top_k)[1].tolist()

    return [vault_content[idx].strip() for idx in top_indices]


def ask_question(question: str, use_rag: bool = True, llm_params: dict = None) -> str:
    """Ask a question to the LLM with or without RAG"""
    conversation_history: List[dict] = []

    if use_rag:
        vault_embeddings, vault_content = setup_rag()
        response = chat_with_llm(
            query=question,
            system_message=SYSTEM_MESSAGE,
            vault_embeddings=vault_embeddings,
            vault_content=vault_content,
            conversation_history=conversation_history,
            llm_params=llm_params
        )
    else:
        response = chat_with_llm(
            query=question,
            system_message=SYSTEM_MESSAGE,
            vault_embeddings=torch.tensor([]),
            vault_content=[],
            conversation_history=conversation_history,
            llm_params=llm_params
        )

    return response


def chat_with_llm(query: str,
                  system_message: str,
                  vault_embeddings: torch.Tensor,
                  vault_content: List[str],
                  conversation_history: List[dict],
                  model: str = LLM,
                  llm_params: dict = None) -> str:
    """Main chat function with RAG capabilities."""
    conversation_history.append({"role": "user", "content": query})

    relevant_context = get_relevant_context(query, vault_embeddings, vault_content)

    params = DEFAULT_LLM_PARAMS.copy()
    if llm_params:
        params.update(llm_params)

    if relevant_context:
        context_str = "\n".join(relevant_context)
        print(f"{CYAN}Context from documents:\n{context_str}{RESET_COLOR}")

    if relevant_context:
        query_with_context = f"{query}\n\nRelevant Context:\n{context_str}"
        conversation_history[-1]["content"] = query_with_context

    messages = [
        {"role": "system", "content": system_message},
        *conversation_history
    ]

    response = CLIENT.chat.completions.create(
        model=model,
        messages=messages,
        **params
    )

    # Add assistant's response to conversation history
    assistant_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response
