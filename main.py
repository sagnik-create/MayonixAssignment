import sys
import time
from embeddings.embedding_service import EmbeddingService
from utils.similarity import get_top_k_similar
from data.messages import MESSAGES
from colorama import Fore, Style, init

init(autoreset=True)

def colorize(score):
    if score > 0.6:
        return Fore.GREEN
    elif score > 0.3:
        return Fore.YELLOW
    else:
        return Fore.RED

def parse_topk(args, max_k, default=3):
    if "--topk" in args:
        try:
            idx = args.index("--topk")
            k = int(args[idx + 1])
            if k < 1:
                raise ValueError
            return min(k, max_k)
        except (ValueError, IndexError):
            print("❌ Invalid value for --topk. Example usage: --topk 5")
            sys.exit(1)
    return default

def main():
    args = sys.argv[1:]

    # Get query
    if len(args) > 0:
        query = args[0]
    else:
        query = input("Enter your message: ").strip()

    if not query:
        print("❌ Input cannot be empty")
        return

    messages_text = [msg for msg, _ in MESSAGES]

    # Parse top-k from CLI
    k = parse_topk(args, max_k=len(messages_text), default=3)

    embedder = EmbeddingService()
    embedder.fit(messages_text)

    start = time.time()
    message_embeddings = embedder.embed(messages_text)
    query_embedding = embedder.embed([query])

    results = get_top_k_similar(query_embedding, message_embeddings, messages_text, k=k)
    end = time.time()

    print(f"\nTop {k} Similar Messages:\n")
    for i, res in enumerate(results, 1):
        score_pct = round(res["score"] * 100, 2)
        color = colorize(res["score"])
        print(f"{i}. {color}[Score: {score_pct}%]{Style.RESET_ALL} \"{res['message']}\"")

    print(f"\n⏱ Execution Time: {round(end - start, 5)} seconds")

if __name__ == "__main__":
    main()
