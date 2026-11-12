def chunk_fixed(text, size=200, overlap=40):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunks.append(text[i:i + size])
    return chunks


if __name__ == "__main__":
    text = open("dokument.txt", encoding="utf-8").read()

    for i, c in enumerate(chunk_fixed(text)):
        print(f"--- chunk {i} ---\n{c}\n")


# En endnu nemmere måde, som alle bruger i dag er ved brug af Langchain. Her er et eksempel på, hvordan man kan bruge Langchain til at opdele tekst i mindre bidder:

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="", chunk_size=200, chunk_overlap=40)

text = open("dokument.md", encoding="utf-8").read()

for i, c in enumerate(splitter.split_text(text)):
    print(f"--- chunk {i} ---\n{c}\n")