import re


def chunk_sentences(text, max_len=200):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, current = [], ""

    for s in sentences:
        if len(current) + len(s) > max_len and current:
            chunks.append(current.strip())
            current = ""
        current += s + " "

    if current:
        chunks.append(current.strip())
    return chunks


if __name__ == "__main__":
    text = open("dokument.txt", encoding="utf-8").read()

    for i, c in enumerate(chunk_sentences(text)):
        print(f"--- chunk {i} ---\n{c}\n")