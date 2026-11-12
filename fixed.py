def chunk_fixed(text, size=200, overlap=40):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunks.append(text[i:i + size])
    return chunks


if __name__ == "__main__":
    text = open("dokument.txt", encoding="utf-8").read()

    for i, c in enumerate(chunk_fixed(text)):
        print(f"--- chunk {i} ---\n{c}\n")