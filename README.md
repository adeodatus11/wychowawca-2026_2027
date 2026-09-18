# Plan pracy wychowawczo-profilaktycznej 2026/2027

Publiczna strona z materiałami dla wychowawców ZSZ5 na rok szkolny 2026/2027.

## Aktualna wersja

- źródło tematów: `Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx`,
- liczba tematów: 35,
- format: strona główna z aktualnościami oraz osobna strona HTML dla każdej lekcji,
- wejście do strony: `index.html`,
- plan pracy: `plan-pracy-wychowawczo-profilaktycznej.html`,
- baza wiedzy: `baza-wiedzy.html` (poradniki o integracji klasy, reagowaniu na trudne zachowania i wspieraniu ucznia w spektrum autyzmu),
- krótkie adresy lekcji: `lekcje/01.html`, `lekcje/02.html` itd.,
- dodatkowa prezentacja startowa: `spotkanie-z-uczniami-1-wrzesnia-2026.html`,
- wersja dokumentu do teczki wychowawcy: `wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html` z pobieraniem pliku Word,
- zebranie z rodzicami: link do artykułu SharePoint oraz plik `wytyczne_zebr_rodz_4wrz2026_ost.docx` do pobrania,
- lokalny wykaz podziałów na grupy: `wykaz-podzialow-grup.html`,
- Tydzień o Przeciwdziałaniu Przemocy Rówieśniczej: `tydzien-przeciwdzialania-przemocy-rowiesniczej.html`
  wraz z pakietem plików MEN w `materialy/tydzien-przeciwdzialania-przemocy-rowiesniczej/`.

## Strona główna

`index.html` pełni teraz funkcję strony aktualności dla wychowawców. Zawiera bieżące komunikaty, skróty do planu pracy i bazy wiedzy oraz archiwum wpisów.

## Zawartość lekcji

Każda lekcja zawiera cel, przewidywane rezultaty, przygotowanie nauczyciela, przebieg 30 minut, ćwiczenie, sekcję `Co musi wybrzmieć`, dowód realizacji, źródła rozszerzające i film albo inspirację wideo dla nauczyciela.

## Prezentacja 1 września 2026

Strona zawiera dodatkową prezentację do przeprowadzenia spotkania wychowawcy z uczniami 1 września 2026 r. Prezentacja działa w przeglądarce, obsługuje kliknięcie w slajd, strzałki, spację i tryb pełnoekranowy. Przed właściwą prezentacją znajduje się osobny wstęp z notatkami dla wychowawcy.

## Wytyczne do teczki wychowawcy

Strona zawiera także dokument `Wytyczne na spotkanie z uczniami 1 września - wersja do teczki wychowawców`, odtworzony bezpośrednio z pliku Word. Oryginał `.docx` jest dostępny do pobrania z poziomu strony.

## Tydzień o Przeciwdziałaniu Przemocy Rówieśniczej

Artykuł w aktualnościach opisuje ogólnopolską inicjatywę MEN, podaje terminy obu tygodni (w szkołach — przeciwdziałanie przemocy rówieśniczej, w przedszkolach — budowanie relacji) i zbiera materiały dla uczniów w wieku 14–18 lat. Baza wiedzy prowadzi do niego samym linkiem, bez osobnego kafelka z przyciskiem.

Pliki z pakietu MEN są zapisane lokalnie w katalogu `materialy/tydzien-przeciwdzialania-przemocy-rowiesniczej/`: bank dobrych praktyk (DOCX), scenariusz lekcji „Młode Głowy” dla klas ponadpodstawowych, cztery e-booki dla nastolatków, ścieżki pomocy dla ucznia i rodzica, listy Minister Edukacji oraz plakaty.

Artykuł zawiera też propozycje wprowadzenia tematu na języku polskim, WOS, informatyce, wychowaniu fizycznym i przedmiotach zawodowych, z linkami do gotowych lekcji na ZPE.

Termin edycji 2025 (29 września – 3 października) pochodzi z listów Minister Edukacji dołączonych do pakietu. Termin edycji 2026 wymaga potwierdzenia na stronie MEN i jest tak oznaczony w artykule.

## Wytyczne na zebranie z rodzicami

Strona zawiera wpis z linkiem do artykułu SharePoint o zebraniu z rodzicami 4 września 2026 r. oraz udostępnia oryginalny plik `.docx` do pobrania.

## Generowanie

Stronę generuje skrypt:

```bash
python tools/generate_lessons_site.py
```

Przed publikacją generator sprawdza zgodność listy 35 tematów z plikiem DOCX, jeśli dostępna jest biblioteka `python-docx`.
