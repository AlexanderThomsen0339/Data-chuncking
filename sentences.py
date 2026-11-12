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

# Her er et eksempel på, hvordan man kan bruge Langchain til at opdele tekst i mindre bidder baseret på sætninger:

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " "],
    chunk_size=200,
    chunk_overlap=0,
    keep_separator="end",
)

text = open("dokument.md", encoding="utf-8").read()

for i, c in enumerate(splitter.split_text(text)):
    print(f"--- chunk {i} ---\n{c}\n")