from sentences import chunk_sentences


def is_heading(line):
    return 0 < len(line) < 40 and not line.endswith((".", "!", "?"))


def chunk_sections(text, max_len=500):
    sections, heading, body = [], "", []

    for line in text.splitlines():
        line = line.strip()
        if is_heading(line):
            if body:
                sections.append((heading, " ".join(body)))
            heading, body = line, []
        elif line:
            body.append(line)

    if body:
        sections.append((heading, " ".join(body)))

    chunks = []
    for heading, body in sections:
        for part in chunk_sentences(body, max_len):
            chunks.append(f"{heading}\n{part}")
    return chunks


if __name__ == "__main__":
    text = open("dokument.txt", encoding="utf-8").read()

    for i, c in enumerate(chunk_sections(text)):
        print(f"--- chunk {i} ---\n{c}\n")

# Her er et eksempel på, hvordan man kan bruge Langchain til at opdele tekst i mindre bidder baseret på sektioner:

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

headers = MarkdownHeaderTextSplitter([("#", "titel"), ("##", "afsnit")])
sizer = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

text = open("dokument.md", encoding="utf-8").read()
chunks = sizer.split_documents(headers.split_text(text))

for i, c in enumerate(chunks):
    print(f"--- chunk {i} ---\n{c.metadata}\n{c.page_content}\n")