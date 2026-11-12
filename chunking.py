import re


def chunk_fixed(text, size=200, overlap=40):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunks.append(text[i:i + size])
    return chunks


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


text = open("dokument.txt", encoding="utf-8").read()

for i, c in enumerate(chunk_sentences(text)):
    print(i, c)