# Plan pracy wychowawczo-profilaktycznej 2026/2027

Publiczna strona z materiałami dla wychowawców ZSZ5 na rok szkolny 2026/2027.

## Aktualna wersja

- źródło tematów: `Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx`,
- liczba tematów: 35,
- format: osobna strona HTML dla każdej lekcji,
- wejście do strony: `index.html`,
- krótkie adresy lekcji: `lekcje/01.html`, `lekcje/02.html` itd.,
- dodatkowa prezentacja startowa: `spotkanie-z-uczniami-1-wrzesnia-2026.html`,
- wersja dokumentu do teczki wychowawcy: `wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html` z pobieraniem pliku Word.

## Zawartość lekcji

Każda lekcja zawiera cel, przewidywane rezultaty, przygotowanie nauczyciela, przebieg 30 minut, ćwiczenie, sekcję `Co musi wybrzmieć`, dowód realizacji, źródła rozszerzające i film albo inspirację wideo dla nauczyciela.

## Prezentacja 1 września 2026

Strona zawiera dodatkową prezentację do przeprowadzenia spotkania wychowawcy z uczniami 1 września 2026 r. Prezentacja działa w przeglądarce, obsługuje kliknięcie w slajd, strzałki, spację i tryb pełnoekranowy. Przed właściwą prezentacją znajduje się osobny wstęp z notatkami dla wychowawcy.

## Wytyczne do teczki wychowawcy

Strona zawiera także dokument `Wytyczne na spotkanie z uczniami 1 września - wersja do teczki wychowawców`, odtworzony bezpośrednio z pliku Word. Oryginał `.docx` jest dostępny do pobrania z poziomu strony.

## Generowanie

Stronę generuje skrypt:

```bash
python tools/generate_lessons_site.py
```

Przed publikacją generator sprawdza zgodność listy 35 tematów z plikiem DOCX, jeśli dostępna jest biblioteka `python-docx`.
