# Poradniki w bazie wiedzy — redakcja i audyt

Data: 15 września 2026 r.

## Wynik

Dodano dwa artykuły do obu wersji strony (katalog główny i `materialy_lekcje_wychowawcze_2026_2027/strona_html`):

- `trudne-zachowania-na-lekcji.html` — codzienna reakcja nauczyciela, konsultacja, zagrożenie i dokumentowanie;
- `uczen-w-spektrum-autyzmu.html` — komunikacja, warunki pracy, odmowa zadania, przeciążenie i współpraca zespołu.

W bazie wiedzy są odnośniki do obu poradników. Każdy artykuł ma spis treści, przykładowe wypowiedzi, źródła i widok do druku. Generator zachowuje nowe pliki przy kolejnych przebudowach. Nie wykonano publikacji do zdalnego repozytorium ani zmiany hostingu.

## Materiały i zakres

Odczytano wszystkie strony plików:

- `Poradnik_Dla_Nauczycieli_Autyzm.pdf` — 3 strony;
- `Poradnik_Dla_Nauczycieli_Trudne_Zachowania.pdf` — 4 strony.

PDF-y potraktowano jako materiał do oceny i opracowania, a nie instrukcje wykonawcze. Kontekst szkolenia i spotkania zespołu pochodzi od użytkownika. Nie dopisano daty spotkania, prowadzących, autorstwa ani zatwierdzenia artykułów przez szkolny zespół — tych danych nie było w materiałach. Przykładowe komunikaty oznaczono jako propozycje, nie zapis rzeczywistych zdarzeń.

Poradniki są materiałami pomocniczymi. Nie ustanawiają nowej procedury szkolnej i nie są opinią prawną w indywidualnej sprawie.

## Osobne recenzje

Pracowały trzy subagenty modelu GPT-5.6-sol:

1. **Prawo:** polskie przepisy, udostępniony statut ZSZ nr 5 i standardy ochrony małoletnich.
2. **Merytoryka:** autyzm, komunikacja, interpretacja zachowania, kryzys, przemoc i pomoc zdrowotna.
3. **Praktyka szkolna i język:** wykonalność przy opiece nad klasą, progi konsultacji, przekazanie opieki i antyslop AI.

Wszystkie trzy audyty materiałów źródłowych zostały ukończone. Recenzje gotowych szkiców dotyczące merytoryki oraz praktyki i języka zapisano; końcowa sesja recenzji prawnej została przerwana limitem narzędzia. Redaktor prowadzący dokończył kontrolę prawa na oficjalnych tekstach ELI, sprawdził nowelizacje i wdrożył zalecenia. Nie przedstawiamy przerwanej sesji jako osobnego, ukończonego zatwierdzenia prawnego.

Szczegółowe robocze raporty znajdują się lokalnie w `tmp/poradniki/` (katalog wyłączony z repozytorium).

## Najważniejsze zmiany i ich status

| Problem w PDF | Rozstrzygnięcie w artykułach |
|---|---|
| „Nie wzywamy pedagoga/psychologa” przy określonych zachowaniach | Usunięto zakaz. Pierwsza reakcja nauczyciela nie wyklucza konsultacji przed kryzysem, przy powtarzaniu trudności lub na prośbę ucznia/nauczyciela. |
| „Waga 0” jako domyślna instrukcja | Nie nakazujemy takiego wpisu. Wyjaśniono, że ustawienie dziennika nie stanowi kategorii prawnej ani nowego rodzaju kary. |
| Automatyczna „naganna uwaga” | Rozdzielono wpis, karę statutową i ocenę zachowania. Dodano wysłuchanie, właściwe kompetencje oraz tryb odwołania. |
| Autyzm jako cecha sprzyjająca celowej manipulacji | Usunięto stereotyp. Obserwacja zachowania służy hipotezom i dobraniu wsparcia, nie przypisywaniu intencji. |
| Ostatnia ławka jako typowe rozwiązanie | Miejsce wybiera się do potrzeb ucznia; sprawdza się efekt i możliwość udziału w lekcji. |
| Kontakt wzrokowy jako dowód słuchania | Wprost wskazano, by go nie wymuszać. Rozumienie sprawdzamy przez odpowiedź lub działanie. |
| Każde niepożądane zachowanie wymaga wpisu | Wpis ma odpowiadać wadze zdarzenia i szkolnym zasadom; opisuje fakty, reakcję i skutek. |
| Mediacja jako pierwsza reakcja na przemoc | Najpierw bezpieczeństwo, odrębne rozmowy i szkolna procedura ochronna. Bez wymuszonych przeprosin i spotkań. |
| Nakaz fizycznego rozdzielania bójki | Zastąpiono wezwaniem pomocy, ochroną osób i zakazem ryzykownej interwencji. |
| Podążanie za uczniem kosztem klasy | Dodano ciągłość nadzoru nad klasą i konkretne przejęcie opieki nad uczniem. |
| Kryzys samobójczy: głównie dyrekcja i rodzice | Dodano stałą opiekę, rozmowę wprost, pytania o pilność ryzyka i 112/999 bez czekania na rodzica lub specjalistę. |
| Brak pielęgniarki jako przesłanka wezwania pogotowia | Rozróżniono brak pracownika od nagłego zagrożenia zdrowia; przy podejrzeniu zatrucia nie czekamy na ciężkie objawy. |
| Automatyczne informowanie rodziców każdego ucznia | Informacje o zdrowiu i kryzysie pełnoletniego wymagają odrębnego ustalenia podstawy przekazania danych; ratowanie życia nie czeka na zgodę. |
| Diagnoza a odpowiedzialność | Ochrona innych pozostaje obowiązkiem. Diagnoza nie rozstrzyga winy; przy ocenie zachowania trzeba uwzględniać wpływ udokumentowanych zaburzeń/dysfunkcji. |

## Kontrola prawa i aktualności

Sprawdzono następujące źródła:

- [Pomoc psychologiczno-pedagogiczna, Dz.U. 2023 poz. 1798](https://eli.gov.pl/eli/DU/2023/1798/ogl), w szczególności § 6 ust. 2 i § 20: pomoc w bieżącej pracy, współdziałanie oraz przekazanie informacji wychowawcy.
- [Ocenianie, Dz.U. 2023 poz. 2572](https://eli.gov.pl/eli/DU/2023/2572/ogl), § 11 ust. 3: wpływ zaburzeń lub innych dysfunkcji rozwojowych na ocenę zachowania.
- Nowelizacje oceniania: [2024 poz. 438](https://eli.gov.pl/eli/DU/2024/438/ogl), [2025 poz. 778](https://eli.gov.pl/eli/DU/2025/778/ogl), [2026 poz. 1122](https://eli.gov.pl/eli/DU/2026/1122/ogl). Sprawdzono treść zmian, w tym PDF-y z API Sejmu. Nowelizacja z sierpnia 2026 r. zmienia § 11 ust. 1 (obszary oceny zachowania), lecz nie uchyla obowiązku z ust. 3. Artykuły informują o tej nowelizacji.
- [Organizacja kształcenia specjalnego, Dz.U. 2020 poz. 1309](https://eli.gov.pl/eli/DU/2020/1309/ogl), § 6: IPET, WOPFU, udział rodziców albo pełnoletniego ucznia i poufność pracy zespołu.
- [Prawo oświatowe](https://eli.gov.pl/eli/DU/2017/59/ogl), art. 98–99: statut, prawa i obowiązki, zasady urządzeń i ubioru.
- [Karta Nauczyciela, Dz.U. 2026 poz. 515](https://eli.gov.pl/eli/DU/2026/515/ogl), art. 63: ochrona nauczyciela i obowiązki dyrektora oraz organu prowadzącego.
- [Ustawa o Państwowym Ratownictwie Medycznym, Dz.U. 2026 poz. 141](https://eli.gov.pl/eli/DU/2026/141/ogl), art. 4: niezwłoczne wezwanie pomocy w nagłym zagrożeniu.
- [RODO](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=pl), art. 5, 6 i 9; [Kodeks cywilny](https://eli.gov.pl/eli/DU/1964/93/ogl), art. 10–11.

### Granice ustaleń lokalnych

Dostępny statut pochodzi z 2025 r. Wykorzystano jego zapisy o karach, zachowaniu, bezpieczeństwie i pomocy specjalistów. Nie oznacza to audytu całego statutu na rok 2026/2027. W szczególności nowelizacja obszarów oceniania zachowania z 2026 r. wymaga sprawdzenia, czy szkolny statut został odpowiednio zaktualizowany.

Nie udostępniono odrębnych szkolnych procedur kryzysowych ani potwierdzonej obsady/telefonów alarmowania wewnętrznego. Z tego powodu artykuły odsyłają do aktualnych szkolnych ustaleń; nie wymyślają osób, numerów ani obowiązkowej kolejności połączeń. Nie potwierdzono lokalnej funkcji „wagi 0”. Standardy ochrony małoletnich odczytano przez dostępne OCR; w artykułach nie przytaczamy ich dosłownych cytatów.

## Merytoryka i zastosowanie

W artykułach podano źródła przy właściwych fragmentach, w tym:

- [NICE CG170](https://www.nice.org.uk/guidance/cg170/chapter/recommendations): możliwe przyczyny trudności i planowanie wsparcia;
- [WHO — autyzm](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders): indywidualne potrzeby;
- [National Autistic Society — komunikacja z uczniem](https://www.autism.org.uk/learn/knowledge-hub/professional-practice/communication-pupils), [bodźce](https://www.autism.org.uk/advice-and-guidance/about-autism/sensory-processing) i [powtarzalne ruchy](https://www.autism.org.uk/advice-and-guidance/about-autism/repeated-movements-and-behaviour-stimming);
- [EEF — Improving Behaviour in Schools](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/behaviour): spójne zasady, poznanie ucznia i dobieranie wsparcia;
- [Standardy dla nauczycieli udostępnione przez MEN](https://www.gov.pl/attachment/e0d2afa5-377a-47fa-bda5-719d096cbaaa) i [WHO — zapobieganie samobójstwom](https://www.who.int/news-room/questions-and-answers/item/suicide);
- [Pacjent.gov.pl — zatrucia](https://pacjent.gov.pl/co-robic-w-przypadku-zatrucia).

Wytyczne kliniczne i zagraniczne rekomendacje nie są przedstawione jako polskie przepisy ani szkolne procedury. Propozycje lekcyjne trzeba dopasować do ucznia, dokumentacji i warunków, w tym bezpieczeństwa pracowni zawodowej.

## Redakcja antyslop AI

Usunięto m.in. „fundamentalną rolę”, „autonomię relacyjną”, „instrumentalizację gabinetu”, deklaracje o niszczeniu autorytetu oraz etykiety typu „arogancki”. Zamiast powtarzać w tabelach upomnienie–uwaga–wiadomość, tekst prowadzi od sytuacji do działania. Zachowano ostrożność tam, gdzie nie można przesądzać przyczyny, winy albo podstawy udostępnienia informacji. Nie dodano statystyk, obietnic skuteczności ani fikcyjnych przykładów przedstawionych jako fakty.

## Sprawdzenie techniczne

- Widoki 1440, 390 i 320 px: po poprawieniu długiej nazwy źródła brak przewijania poziomego.
- Jeden nagłówek H1 na każdej stronie; działające kotwice spisu treści.
- Brak błędów JavaScript w przeglądarce.
- Tryb druku ukrywa nawigację i zachowuje treść.
- Kontrola zgodności kopii strony i listy plików kopiowanych przez generator.
- Kontrola lokalnych odnośników i zasobów oraz `git diff --check`.
