import argparse
import sys
import time

from services import ask_question, setup_pdf


def main():
    parser = argparse.ArgumentParser(description='PDF-based RAG system')
    parser.add_argument('--mode', '-m',
                        choices=['setup', 'ask', 'ask-no-rag'],
                        help='Operation mode')
    parser.add_argument('--question', '-q',
                        type=str,
                        help='Question to ask (required for ask modes)')
    parser.add_argument('--temperature', '-t',
                        type=float,
                        help='LLM temperature (0.0 to 1.0)')

    if len(sys.argv) == 1:
        while True:
            time.sleep(1)
        return

    args = parser.parse_args()
    llm_params = {}

    if args.temperature is not None:
        llm_params['temperature'] = args.temperature

    if args.mode == 'setup':
        setup_pdf()

    elif args.mode == 'ask':
        if not args.question:
            raise ValueError("Question is required for ask mode")
        response = ask_question(args.question, use_rag=True, llm_params=llm_params)
        print(f"\nAssistant: {response}")

    elif args.mode == 'ask-no-rag':
        if not args.question:
            raise ValueError("Question is required for ask-no-rag mode")
        response = ask_question(args.question, use_rag=False)
        print(f"\nAssistant: {response}")


if __name__ == "__main__":
    main()
