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

## Audyt filmów po uwadze użytkownika

Kryteria: film ma być po polsku, nie może mieć tonu bajki lub materiału przedszkolnego, ma być przydatny dla wychowawcy albo starszej młodzieży oraz powinien prowadzić do konkretnego nagrania, nie do ogólnej strony lub playlisty.

Wnioski:

- Do wymiany zakwalifikowano materiały zbyt dziecięce: film o „języku żyrafy” z przedszkola, materiały Fundacji Uniwersytet Dzieci przy tematach dla starszej młodzieży oraz ekologiczne filmy oparte na bajkowej narracji.
- Do wymiany zakwalifikowano linki, które nie były konkretnym filmem: ogólna strona ZPE, kurs NASK, strona ORE z cyklem filmów, playlisty YouTube i artykuł zamiast wideo.
- Zostawiono materiały eksperckie i szkoleniowe po polsku, jeżeli były wystarczająco dojrzałe dla nauczyciela: m.in. CEO, FDDS, SWPS, ORE, PAH, Akademia NFZ, Centralny Dom Technologii.

Wdrożone podmiany:

- Komunikacja: materiał dla klas 5-8 zastąpiono rozmową SWPS o NVC.
- Odpowiedzialność w szkole: film dziecięcy zastąpiono rozmową CEO o roli wychowawcy.
- Wolontariat: animację PAH zastąpiono materiałem NIW o wolontariacie.
- Zdrowie: film dziecięcy o ekranach przed snem zastąpiono materiałem o śnie jako fundamencie zdrowia i nauki.
- Stres: niedostępny lub problematyczny link zastąpiono warsztatem o radzeniu sobie ze stresem.
- Edukacja zdrowotna: stronę ogólną ZPE zastąpiono konkretną wideolekcją o zdrowym stylu życia.
- Fake news: stronę kursu zastąpiono konkretnym odcinkiem o dezinformacji.
- Potrzeby i trudności: film przedszkolny o żyrafie zastąpiono wystąpieniem Marshalla Rosenberga z polskimi napisami.
- Doradztwo zawodowe: ogólne strony i playlistę zastąpiono konkretnymi filmami ORE oraz webinarem o oczekiwaniach pracodawców.
- Uczenie się i projekt: ogólną stronę ZPE, playlisty i artykuł zastąpiono konkretnymi filmami o wiarygodności źródeł, metodzie projektu, informacji zwrotnej i edukacji przyszłości.
- Ekologia: bajkowe animacje i ogólne strony zastąpiono webinarami, rozmowami eksperckimi i reportażem z sortowni odpadów.

## Źródła audytu

- Oficjalna strona Szkoły Mistrzów: https://www.szkolamistrzow.info/
- Logo użyte przez oficjalną stronę: https://www.szkolamistrzow.info/orze%C5%82%20bez%20t%C5%82a.png
- WHO: adolescent mental health: https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health
- UODO: https://uodo.gov.pl/
- Safer Internet: materiały edukacyjne: https://www.saferinternet.pl/menu/materialy-edukacyjne.html
- FDDS: Przemoc rówieśnicza: https://edukacja.fdds.pl/course/view.php?id=902
- ORE: cykl filmów „Drogi Zawodowe”: https://doradztwo.ore.edu.pl/cykl-filmow-drogi-zawodowe/
- CNVC: czym jest NVC: https://www.cnvc.org/pl/learn/what-is-nvc

## Walidacja techniczna

- `python3 tools/generate_lessons_site.py`
- `git diff --check`
- lokalny parser linków HTML
- Playwright: root i przykładowa lekcja na desktopie oraz mobile
- Metadane YouTube sprawdzone przez publiczny endpoint oEmbed dla nowych linków.
