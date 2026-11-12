# Chunking

Et lille eksempel på, hvordan man deler en tekst op i chunks, fx før den lægges i en vektordatabase til RAG.

Hver fil er én måde at chunke på:

- `fixed.py` skærer teksten i stykker af fast længde med lidt overlap, så en pointe ikke forsvinder ved snittet.
- `sentences.py` samler hele sætninger, indtil chunken er fuld. Den klipper ikke midt i en sætning.
- `sections.py` deler teksten ved overskrifter, så hvert emne bliver sin egen chunk. Overskriften kommer med i hver chunk, så modellen ved, hvad teksten handler om. Er et afsnit for langt, deles det yderligere efter sætninger.

`sections.py` giver de bedste chunks til AI.

## Kør

Alle filer læser `dokument.txt` fra samme mappe:

```
python fixed.py
python sentences.py
python sections.py
```

Der bruges kun Pythons standardbibliotek.