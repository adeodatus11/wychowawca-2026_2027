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
- wykaz podziałów na grupy (stała zakładka w menu): `wykaz-podzialow-grup.html`,
- nauczyciele uczący w oddziałach (stała zakładka w menu): `nauczyciele-w-oddzialach.html`
  z danymi w `nauczyciele-w-oddzialach-dane.js` (oba wykazy generuje `tools/build_nauczyciele_w_oddzialach.py`),
- Tydzień o Przeciwdziałaniu Przemocy Rówieśniczej: `tydzien-przeciwdzialania-przemocy-rowiesniczej.html`
  wraz z pakietem plików MEN w `materialy/tydzien-przeciwdzialania-przemocy-rowiesniczej/`,
- standardy postępowania w kryzysie samobójczym: `kryzys-samobojczy-standardy-dla-nauczycieli.html`
  wraz z obiema wersjami PDF w `materialy/standardy-postepowania-kryzys-samobojczy/`,
- OdFiltruj Rzeczywistość (PZU i Universal Music Polska): `odfiltruj-rzeczywistosc.html`
  wraz ze scenariuszem lekcji i plakatem konkursu w `materialy/odfiltruj-rzeczywistosc/`.

## Strona główna

`index.html` to strona startowa wychowawcy. Na górze są stałe narzędzia: wybór „Mojej klasy” (zapamiętywany w przeglądarce) oraz kafelki do podziałów na grupy, nauczycieli w oddziałach, planu pracy i bazy wiedzy. Pod nimi są aktualności, a w bocznej kolumnie link do wklejenia w dzienniku, przydatne strony i lista wszystkich wpisów.

## Nauczyciele w oddziałach i podziały na grupy

Obie strony (`nauczyciele-w-oddzialach.html` i `wykaz-podzialow-grup.html`) korzystają z jednego źródła: arkusza `dane/zestawienie-nauczycieli-oddzialy.xlsx` (zestawienie z planu lekcji aSc). Zmiany względem arkusza wpisuje się w `dane/korekty-nauczycieli-oddzialow.csv` (kolumny `oddzial;przedmiot;grupa;nauczyciel`, nauczyciel w formacie „Nazwisko Imię”). Wiersze korekty zastępują wszystkie wiersze arkusza dla tej samej pary oddział + przedmiot. Nauczycieli nauczania indywidualnego (nie ma go w planie lekcji) wpisuje się w `dane/nauczanie-indywidualne.csv` (kolumny `oddzial;przedmiot;nauczyciel`); strona nauczycieli pokazuje ich w osobnej tabeli „Nauczanie indywidualne” i oznacza takie klasy znacznikiem NI, a na podziały na grupy nie mają wpływu. Po zmianie arkusza lub korekt uruchom `python3 tools/build_nauczyciele_w_oddzialach.py` — skrypt zapisze `nauczyciele-w-oddzialach-dane.js` i podmieni dane w `wykaz-podzialow-grup.html`.

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

Artykuł podaje termin w roku szkolnym 2026/2027: 28 września – 2 października 2026 r. Pakiet materiałów pochodzi z pierwszej edycji akcji (29 września – 3 października 2025 r.) i pozostaje aktualny.

## Standardy postępowania w kryzysie samobójczym

Poradnik `kryzys-samobojczy-standardy-dla-nauczycieli.html` streszcza materiał Instytutu Psychiatrii i Neurologii w Warszawie „Standardy postępowania dla nauczycieli w kontakcie z osobami w kryzysie samobójczym, po próbie samobójczej i w żałobie po śmierci samobójczej” (opracowanie: Małgorzata Łuba, konsultacja: Lucyna Kicińska).

Artykuł zawiera trzy kroki pierwszej pomocy emocjonalnej (ZAUWAŻ — POROZMAWIAJ — DZIAŁAJ) w formie tabel „co robić / czego nie robić”, listę sygnałów ostrzegawczych, zestawienie błędnych przekonań z rzetelną wiedzą, zasady współpracy z opiekunami prawnymi, postępowanie po próbie samobójczej ucznia i po śmierci samobójczej oraz wykaz bezpłatnych telefonów pomocowych.

Oryginalne pliki są zapisane w `materialy/standardy-postepowania-kryzys-samobojczy/`: wersja skrócona (karty do wydruku) i wersja rozszerzona (pełne opracowanie z bibliografią). Wpis o materiale jest w aktualnościach, a kafelek z przyciskiem — w bazie wiedzy.

## OdFiltruj Rzeczywistość

Artykuł `odfiltruj-rzeczywistosc.html` opisuje projekt edukacyjny PZU i Universal Music Polska, będący częścią kampanii społecznej „OdFiltruj Rzeczywistość”. Streszcza scenariusz godziny wychowawczej dla szkół ponadpodstawowych „Po drugiej stronie szkła tak wiele jesteś wart” (2 godziny lekcyjne, teledyski bryskiej, Zuzy Jabłońskiej i Daniela Godsona, karta pracy o samoocenie) oraz zasady konkursu dla uczniów trwającego do 31 października 2026 r.

Oryginalny plik scenariusza jest zapisany w `materialy/odfiltruj-rzeczywistosc/`, a jego ostatnia strona — plakat konkursu — także jako osobny plik PDF do wydruku. Wpis jest w aktualnościach, a link do artykułu — w bazie wiedzy.

## Wytyczne na zebranie z rodzicami

Strona zawiera wpis z linkiem do artykułu SharePoint o zebraniu z rodzicami 4 września 2026 r. oraz udostępnia oryginalny plik `.docx` do pobrania.

## Generowanie

Stronę generuje skrypt:

```bash
python tools/generate_lessons_site.py
```

Przed publikacją generator sprawdza zgodność listy 35 tematów z plikiem DOCX, jeśli dostępna jest biblioteka `python-docx`.
