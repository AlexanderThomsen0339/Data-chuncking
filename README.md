# Chunking

Et lille eksempel på, hvordan man deler en tekst op i chunks, fx før den lægges i en vektordatabase til RAG.

Hver fil er én måde at chunke på:

- `fixed.py` skærer teksten i stykker af fast længde med lidt overlap, så en pointe ikke forsvinder ved snittet.
- `sentences.py` samler hele sætninger, indtil chunken er fuld. Den klipper ikke midt i en sætning.
- `sections.py` deler teksten ved overskrifter, så hvert emne bliver sin egen chunk. Overskriften kommer med i hver chunk, så modellen ved, hvad teksten handler om. Er et afsnit for langt, deles det yderligere efter sætninger.

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
- Hver chunk består af hele sætninger, så teksten er nemmere at læse og forstå.
- Den er stadig simpel og kræver ingen struktur i dokumentet.

Ulemper:
- Den ved ikke, hvor ét emne slutter, og det næste begynder, så emner kan stadig blive blandet.
- Chunks kan blive meget forskellige i størrelse.
- Den splitter forkert ved forkortelser som "fx." og "bl.a.".

### Overskrifter (`sections.py`)

Fordele:
- Hver chunk handler om ét emne.
- Overskriften kommer med som kontekst, hvilket giver bedre søgeresultater.
- Når AI'en svarer, kan man se, hvilket afsnit svaret kommer fra.

Ulemper:
- Den kræver, at dokumentet har overskrifter.
- Det er svært at genkende overskrifter sikkert i almindelig tekst. Markdown eller HTML er nemmere at arbejde med.
- Afsnit kan være meget forskellige i længde, så lange afsnit skal deles yderligere, og korte afsnit giver små chunks med lidt indhold.

## Kør

Alle filer læser `dokument.txt` fra samme mappe:

```
python fixed.py
python sentences.py
python sections.py
```

Der bruges kun Pythons standardbibliotek.