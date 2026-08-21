# Plan pracy wychowawczo-profilaktycznej 2026/2027

Publiczna strona z materiałami dla wychowawców ZSZ5 na rok szkolny 2026/2027.

## Aktualna wersja

- źródło tematów: `Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx`,
- liczba tematów: 35,
- format: osobna strona HTML dla każdej lekcji,
- wejście do strony: `materialy_lekcje_wychowawcze_2026_2027/strona_html/index.html`.

## Zawartość lekcji

Każda lekcja zawiera cel, przewidywane rezultaty, przygotowanie nauczyciela, przebieg 30 minut, ćwiczenie, sekcję `Co musi wybrzmieć`, dowód realizacji, źródła rozszerzające i film albo inspirację wideo dla nauczyciela.

## Generowanie

Stronę generuje skrypt:

```bash
python tools/generate_lessons_site.py
```

Przed publikacją generator sprawdza zgodność listy 35 tematów z plikiem DOCX, jeśli dostępna jest biblioteka `python-docx`.
