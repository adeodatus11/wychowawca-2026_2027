# Audyt strony i wdrożone poprawki

Data audytu: 21 sierpnia 2026 r.

## Zakres

- Treści: wykrycie powtórzeń, języka szablonowego i ogólników.
- Prawdziwość: sprawdzenie ryzykownych twierdzeń, szczególnie w obszarach AI, zdrowia psychicznego, danych osobowych, przemocy i pierwszej pomocy.
- Wizualnie: desktop i telefon, czytelność, brak poziomego przewijania, działanie filtrów.
- Użyteczność: łatwość wejścia w lekcję, sensowna kolejność treści, widoczność logo i zasobów.

## Ustalenia

- Strona potrzebowała wyraźnego brandingu szkoły. Dodano oficjalny znak orła ZSZ5 i tekst „Szkoła Mistrzów”.
- W nagłówku głównym było za dużo opisowego, powtarzalnego tekstu. Skrócono go do informacji praktycznej dla wychowawcy.
- Miesięczne nagłówki były przeciążone listą obszarów. Zostawiono miesiąc i liczbę lekcji; obszar jest widoczny na kartach.
- W przygotowaniu nauczyciela pojawiały się zbyt ogólne instrukcje. Zmieniono je na konkret: przeczytaj opis, przygotuj pytanie startowe, pracuj na przykładach fikcyjnych, ustal dowód realizacji.
- Na telefonie zasoby boczne pojawiały się przed właściwą treścią lekcji. Zmieniono kolejność: najpierw treść, potem film i źródła.
- Nie znaleziono treści jawnie sprzecznych z podstawową wiedzą naukową, ale utrzymano ostrożny język przy zdrowiu psychicznym, AI, danych osobowych i przemocy.

## Wdrożenia

- Dodano `assets/logo-orzel-zsz5.png` oraz kopię do folderu publikacyjnego `strona_html/assets/`.
- Dodano pasek brandu do strony głównej i wszystkich lekcji.
- Poprawiono tekst hero oraz metrykę: zamiast „1 osobny URL na lekcję” jest „7 miesięcy”.
- Usunięto przeciążające opisy obszarów z nagłówków miesięcy.
- Poprawiono przygotowanie nauczyciela.
- Zmieniono układ mobilny lekcji: treść przed materiałami bocznymi.
- Zweryfikowano lokalne linki, obecność logo, komplet 35 lekcji oraz brak poziomego przewijania.

## Źródła audytu

- Oficjalna strona Szkoły Mistrzów: https://www.szkolamistrzow.info/
- Logo użyte przez oficjalną stronę: https://www.szkolamistrzow.info/orze%C5%82%20bez%20t%C5%82a.png
- WHO: adolescent mental health: https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health
- UODO: https://uodo.gov.pl/
- Safer Internet: materiały edukacyjne: https://www.saferinternet.pl/menu/materialy-edukacyjne.html
- FDDS: Przemoc rówieśnicza: https://edukacja.fdds.pl/course/view.php?id=902

## Walidacja techniczna

- `python3 tools/generate_lessons_site.py`
- `git diff --check`
- lokalny parser linków HTML
- Playwright: root i przykładowa lekcja na desktopie oraz mobile
