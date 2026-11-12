# Chunking

Et lille eksempel på, hvordan man deler en tekst op i chunks, fx før den lægges i en vektordatabase til RAG. Eksemplet bruger [LangChain](https://python.langchain.com/docs/concepts/text_splitters/).

Hver fil er én måde at chunke på:

- `fixed.py` skærer teksten i stykker af fast længde med lidt overlap (`CharacterTextSplitter`).
- `sentences.py` deler først ved afsnit, så ved linjer og til sidst ved sætninger, så den så vidt muligt ikke klipper midt i en sætning (`RecursiveCharacterTextSplitter`).
- `sections.py` deler ved Markdown-overskrifter, så hvert emne bliver sin egen chunk. Overskrifterne gemmes som metadata på hver chunk. Er et afsnit for langt, deles det yderligere (`MarkdownHeaderTextSplitter`).

`sections.py` giver de bedste chunks til AI.

## Fordele og ulemper

### Fast længde (`fixed.py`)

Fordele:
- Den er meget enkel og hurtig.
- Alle chunks er lige store, så det er nemt at styre, hvor meget der sendes til modellen.
- Den virker på al slags tekst, også tekst uden struktur.

Ulemper:
- Den klipper midt i ord og sætninger.
- En chunk kan blande to emner sammen.
- Overlappet gemmer den samme tekst flere gange.

### Sætninger (`sentences.py`)

Fordele:
- Den holder så vidt muligt sætningerne hele, så hver chunk er nemmere at forstå.
- Den kræver ingen struktur i dokumentet.

Ulemper:
- Den ved ikke, hvor ét emne slutter, og det næste begynder.
- Chunks kan blive meget forskellige i størrelse, og en overskrift kan ende som sin egen chunk uden indhold.
- Den splitter forkert ved forkortelser som "fx." og "bl.a.".

### Overskrifter (`sections.py`)

Fordele:
- Hver chunk handler om ét emne.
- Overskrifterne følger med som metadata, så de kan bruges til søgning og filtrering.
- Når AI'en svarer, kan man se, hvilket afsnit svaret kommer fra.

Ulemper:
- Den kræver, at dokumentet er skrevet i Markdown med overskrifter.
- Afsnit kan være meget forskellige i længde, så lange afsnit skal deles yderligere, og korte afsnit giver små chunks med lidt indhold.

## Kør

```
pip install langchain-text-splitters
python fixed.py
python sentences.py
python sections.py
```

Alle filer læser `dokument.md` fra samme mappe.