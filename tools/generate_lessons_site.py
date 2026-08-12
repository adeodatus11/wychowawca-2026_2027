from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "materialy_lekcje_wychowawcze_2026_2027"
SCENARIOS = OUT / "scenariusze"
SLIDES = OUT / "prezentacje_md"
SITE = OUT / "strona_html"


SOURCES = [
    {
        "name": "MEN: Podstawowe kierunki realizacji polityki oświatowej państwa w roku szkolnym 2026/2027",
        "url": "https://www.gov.pl/web/edukacja/podstawowe-kierunki-realizacji-polityki-oswiatowej-panstwa-w-roku-szkolnym-20262027",
        "note": "Zweryfikowano 2026-08-10; zgodne z lokalnym plikiem 20260527_Podstawowe_kierunki_2026_2027.pdf.",
    },
    {
        "name": "ZSZ nr 5 we Wrocławiu, strona EduPage",
        "url": "https://zsz5.edupage.org/",
        "note": "Kontakt szkoły, menu, statut, pomoc psychologiczno-pedagogiczna, dziennik.",
    },
    {
        "name": "Szkoła Mistrzów",
        "url": "https://www.szkolamistrzow.info/",
        "note": "Oferta Technikum nr 5, Branżowej Szkoły I stopnia nr 5 i kształcenia zawodowego.",
    },
    {
        "name": "Statut Zespołu Szkół Zawodowych nr 5 we Wrocławiu",
        "url": "https://zsz5.edupage.org/",
        "note": "Tekst jednolity obowiązujący od 16.10.2025; publikowany na stronie szkoły.",
    },
    {
        "name": "VULCAN Baza wiedzy: kartoteki uczniów",
        "url": "https://www.bazawiedzy.vulcan.edu.pl/bazawiedzy.php/show/416",
        "note": "Dane do kartotek mogą wprowadzać m.in. sekretarz, wychowawca i pedagog w określonych modułach.",
    },
    {
        "name": "VULCAN Baza wiedzy: seryjne dane uczniów i opiekunów",
        "url": "https://www.bazawiedzy.vulcan.edu.pl/bazawiedzy.php/show/310",
        "note": "Potwierdza kategorie: dane adresowe i kontaktowe ucznia oraz dane podstawowe, adresowe i kontaktowe rodziców/opiekunów.",
    },
    {
        "name": "Dziennik VULCAN: aktualizacja konta",
        "url": "https://dziennik.vulcan.edu.pl/akz/",
        "note": "Kod jednorazowego dostępu, osobne kody ucznia i rodzica; rodzic ma dostęp m.in. do usprawiedliwiania nieobecności.",
    },
    {
        "name": "Prawo oświatowe, art. 42",
        "url": "https://api.sejm.gov.pl/eli/acts/DU/2017/59/text.html",
        "note": "Niespełnianie obowiązku nauki: nieusprawiedliwiona nieobecność co najmniej 50% dni zajęć w miesiącu.",
    },
    {
        "name": "Ustawa o systemie oświaty, art. 44k",
        "url": "https://api.sejm.gov.pl/eli/acts/DU/2024/750/text.html",
        "note": "Nieklasyfikowanie przy braku podstaw z powodu nieobecności przekraczającej połowę czasu zajęć.",
    },
]


LESSONS = [
    {
        "id": "00",
        "slug": "00_wycieczka_po_zsz5_klasy_pierwsze",
        "title": "Lekcja 0: Nawigacja po ZSZ5",
        "group": "Tylko klasy pierwsze Technikum nr 5 i BS I stopnia nr 5",
        "men": "Adaptacja, bezpieczeństwo, komunikacja szkoła-uczeń-rodzic",
        "purpose": "Uczeń wie, gdzie szukać pomocy i informacji w szkole oraz w kanałach cyfrowych ZSZ5.",
        "outcomes": [
            "wskazuje najważniejsze miejsca w budynku i wie, kiedy z nich korzystać",
            "odróżnia stronę EduPage, stronę Szkoła Mistrzów, Facebook szkoły i Dziennik VULCAN",
            "potrafi wyjaśnić, dlaczego dostęp do Dziennika VULCAN ma uczeń i rodzic",
            "zna podstawową ścieżkę kontaktu: wychowawca, sekretariat, pedagog/psycholog, dyrekcja",
        ],
        "materials": [
            "telefon nauczyciela lub komputer z dostępem do strony zsz5.edupage.org",
            "link do szkolnego Facebooka: https://www.facebook.com/zsz5wro",
            "link do Szkoły Mistrzów: https://www.szkolamistrzow.info/",
            "kartka z trasą spaceru po szkole; numery sal do uzupełnienia lokalnie",
        ],
        "prep": [
            "Sprawdź aktualne miejsca: sekretariat uczniowski, dyrekcja/wicedyrektor, gabinet pedagoga, gabinet psychologa, biblioteka, sale/pracownie zawodowe, tablice informacyjne.",
            "Dopisz aktualne numery sal lub skróty lokalizacyjne na wydruku.",
            "Jeżeli spacer po budynku jest niemożliwy, zrób wariant stacjonarny z mapą słowną i stronami WWW.",
        ],
        "schedule": [
            ("0-3 min", "Start", "Pytanie: gdzie uczeń szuka informacji, gdy nie wie, co zrobić?"),
            ("3-14 min", "Spacer nawigacyjny", "Krótka trasa: wejście/portiernia, sekretariat, tablice, pedagog/psycholog, biblioteka, pracownie."),
            ("14-22 min", "Nawigacja cyfrowa", "Pokaz: EduPage, Szkoła Mistrzów, Facebook, Dziennik VULCAN."),
            ("22-27 min", "Mini-zadanie", "Uczniowie w parach układają 3 scenki: gdzie idę / do kogo piszę / co sprawdzam w dzienniku."),
            ("27-30 min", "Domknięcie", "Każdy zapisuje jedną rzecz, którą sprawdzi dziś w domu z rodzicem/opiekunem."),
        ],
        "key_points": [
            "EduPage to oficjalne źródło dokumentów i komunikatów szkoły.",
            "Szkoła Mistrzów pokazuje ofertę i charakter kształcenia zawodowego.",
            "Facebook jest szybkim kanałem informacji i promocji, ale nie zastępuje dziennika.",
            "Dziennik VULCAN jest podstawowym miejscem komunikacji, frekwencji, ocen i usprawiedliwień.",
            "Rodzic/opiekun powinien mieć własny dostęp, bo konto rodzica ma inne uprawnienia niż konto ucznia.",
        ],
        "activity": "Mapa decyzji: nauczyciel czyta sytuacje, a uczniowie wskazują kanał: budynek, EduPage, Facebook, VULCAN, wychowawca. Przykłady: brak dostępu do dziennika, choroba, praktyki, zmiana planu, potrzeba rozmowy z pedagogiem.",
        "privacy": "Nie zapisujemy loginów ani haseł. Nie fotografujemy dokumentów z danymi osób. W razie problemu z kontem uczeń zgłasza to wychowawcy zgodnie z procedurą szkoły.",
        "assessment": "Na koniec uczeń potrafi w 30 sekund powiedzieć: gdzie znajdzie statut, gdzie sprawdzi frekwencję, do kogo zgłosi problem i dlaczego rodzic potrzebuje dostępu do dziennika.",
        "slides": [
            ("Po co ta lekcja?", ["Dziś uczymy się poruszać po szkole i po jej kanałach informacji.", "Cel: wiedzieć, gdzie i do kogo iść, zanim pojawi się problem."]),
            ("Najważniejsze miejsca", ["Wejście i portiernia", "Sekretariat uczniowski", "Pedagog, psycholog, pomoc PP", "Biblioteka i tablice informacyjne", "Pracownie zawodowe i sale klasowe"]),
            ("Strona szkoły", ["zsz5.edupage.org", "statut, dokumenty, komunikaty", "zakładki dla uczniów i rodziców"]),
            ("Szkoła Mistrzów", ["szkolamistrzow.info", "oferta zawodowa", "dualny charakter kształcenia"]),
            ("Facebook szkoły", ["bieżące życie szkoły", "wydarzenia i sukcesy", "nie zastępuje oficjalnych komunikatów"]),
            ("Dziennik VULCAN", ["oceny, frekwencja, wiadomości", "usprawiedliwienia i kontakt z rodzicem", "uczeń i rodzic potrzebują własnego dostępu"]),
            ("Szybka mapa decyzji", ["Nie wiem, gdzie iść: wychowawca", "Nie mam dostępu do dziennika: wychowawca/procedura szkoły", "Jestem chory: rodzic i usprawiedliwienie", "Mam kryzys: pedagog/psycholog"]),
        ],
    },
    {
        "id": "01",
        "slug": "01_dane_do_dziennika_vulcan",
        "title": "Dane do Dziennika VULCAN: po co je zbieramy i jak je zabezpieczyć",
        "group": "Wszystkie klasy",
        "men": "Współpraca z rodzicami, bezpieczeństwo, organizacja pracy szkoły",
        "purpose": "Uczeń rozumie, jakie dane są potrzebne do kartoteki szkolnej i dlaczego aktualne kontakty są warunkiem realnej współpracy szkoły z domem.",
        "outcomes": [
            "wymienia podstawowe kategorie danych do kartoteki ucznia",
            "rozumie, że dane kontaktowe rodziców/opiekunów muszą być aktualne",
            "wie, że dane wrażliwe i dokumenty przekazuje się tylko bezpiecznym kanałem wskazanym przez szkołę",
            "potrafi przygotować rodzica/opiekuna do uzupełnienia braków",
        ],
        "materials": [
            "lista kontrolna danych do sprawdzenia w domu",
            "bezpieczna koperta lub oficjalny formularz szkoły, jeśli szkoła go stosuje",
            "dostęp nauczyciela do Dziennika VULCAN według uprawnień",
        ],
        "prep": [
            "Zweryfikuj z sekretariatem, które pola są faktycznie brakujące w kartotece oddziału.",
            "Nie wyświetlaj listy uczniów z danymi na projektorze.",
            "Ustal, czy dane mają wrócić przez dziennik, formularz papierowy, sekretariat czy zebranie z rodzicami.",
        ],
        "schedule": [
            ("0-4 min", "Start", "Dlaczego szkoła nie może działać na nieaktualnym numerze telefonu?"),
            ("4-10 min", "Kategorie danych", "Uczeń, adres, rodzice/opiekunowie, kontakty, dane do dokumentacji szkolnej."),
            ("10-18 min", "Lista kontrolna", "Uczniowie zaznaczają, co mają sprawdzić w domu; bez wpisywania danych na forum klasy."),
            ("18-25 min", "Bezpieczeństwo danych", "Co wolno wysłać, czego nie wolno publikować, komu przekazujemy dokumenty."),
            ("25-30 min", "Zadanie domowe", "Uczeń ustala z rodzicem/opiekunem, co trzeba uzupełnić i do kiedy."),
        ],
        "key_points": [
            "Typowe kategorie: imiona i nazwisko ucznia, PESEL lub dokument tożsamości, data i miejsce urodzenia, adres zamieszkania, dane rodziców/opiekunów, adresy i kontakty, adres e-mail do konta dziennika.",
            "VULCAN wskazuje, że kartoteki obejmują dane adresowe i kontaktowe ucznia oraz dane podstawowe, adresowe i kontaktowe rodziców/opiekunów.",
            "Wychowawca nie zbiera danych publicznie. Uczeń ma tylko sprawdzić kompletność i przekazać informację ustalonym kanałem.",
            "Aktualny telefon rodzica ma znaczenie przy frekwencji, wypadku, kryzysie, praktykach i pilnych komunikatach.",
            "Kody dostępu do Dziennika VULCAN są indywidualne; rodzic i uczeń mają osobne konta.",
        ],
        "activity": "Ćwiczenie bez danych osobowych: uczniowie dostają fikcyjną kartotekę z brakami i oznaczają, które braki uniemożliwiają kontakt szkoły z domem. Potem przenoszą wnioski na własną listę do sprawdzenia w domu.",
        "privacy": "Nie zbieramy numerów PESEL, adresów, numerów telefonów ani e-maili w otwartym dokumencie, na tablicy, w grupowym czacie ani w prezentacji. Dane wracają tylko procedurą szkoły.",
        "assessment": "Uczeń oddaje podpisaną przez siebie listę kontrolną: wiem, co mam sprawdzić w domu; nie zawiera ona danych osobowych.",
        "slides": [
            ("Po co kartoteka?", ["kontakt w pilnej sytuacji", "prawidłowe dokumenty szkolne", "frekwencja i usprawiedliwienia", "komunikacja z rodzicem/opiekunem"]),
            ("Kategorie danych", ["dane ucznia", "adres zamieszkania", "rodzice/opiekunowie", "telefony i e-maile", "dane do dokumentacji szkolnej"]),
            ("Dane rodzica/opiekuna", ["imię i nazwisko", "adres, jeśli wymagany", "telefon", "e-mail do konta dziennika", "aktualność kontaktu"]),
            ("Czego nie robimy", ["nie czytamy danych na forum", "nie wpisujemy danych w publiczny formularz", "nie wysyłamy dokumentów na grupę klasy", "nie pokazujemy kartoteki na projektorze"]),
            ("Zadanie", ["sprawdź z rodzicem/opiekunem", "uzupełnij braki ustaloną drogą", "zgłoś problem z dostępem do dziennika"]),
        ],
    },
    {
        "id": "02",
        "slug": "02_statut_zsz5",
        "title": "Statut ZSZ5: gdzie go znaleźć, co reguluje i jak z niego korzystać",
        "group": "Wszystkie klasy",
        "men": "Odpowiedzialność, prawa i obowiązki, współpraca w społeczności szkolnej",
        "purpose": "Uczeń traktuje statut jako praktyczną instrukcję życia szkoły, a nie dokument do przeczytania tylko przy konflikcie.",
        "outcomes": [
            "znajduje statut na stronie szkoły",
            "wyjaśnia, co statut reguluje: prawa, obowiązki, frekwencję, ocenianie, praktyki, pomoc PP",
            "wskazuje najważniejsze paragrafy dotyczące frekwencji i klasyfikacji",
            "wie, że statut obowiązuje uczniów Technikum nr 5 i BS I stopnia nr 5 w ramach ZSZ5",
        ],
        "materials": [
            "link do strony zsz5.edupage.org i zakładki Statut",
            "lokalny tekst statutu z 15.10.2025",
            "wydruk trzech fragmentów: frekwencja, klasyfikacja, praktyki",
        ],
        "prep": [
            "Sprawdź, czy na stronie jest aktualny plik statutu.",
            "Przygotuj 3 krótkie fragmenty bez długiego czytania całego dokumentu.",
            "Zaznacz uczniom, że w razie wątpliwości pracujemy na aktualnym pliku ze strony szkoły.",
        ],
        "schedule": [
            ("0-4 min", "Start", "Gdzie szukać zasad, gdy ktoś mówi: 'tak jest w statucie'?"),
            ("4-9 min", "Jak znaleźć dokument", "Pokaz strony szkoły i zakładki Statut."),
            ("9-18 min", "Co reguluje statut", "Prawa, obowiązki, ocenianie, zachowanie, frekwencja, praktyki, pomoc."),
            ("18-26 min", "Praca na fragmentach", "Grupy rozwiązują 3 przypadki: nieobecność, praktyka, nieklasyfikowanie."),
            ("26-30 min", "Podsumowanie", "Uczeń zapisuje: jeden paragraf, który realnie go dotyczy."),
        ],
        "key_points": [
            "ZSZ5 obejmuje Technikum nr 5, Branżową Szkołę I stopnia nr 5 i Branżową Szkołę II stopnia nr 5.",
            "Statut reguluje organizację szkoły, prawa i obowiązki, ocenianie, frekwencję, praktyczną naukę zawodu, pomoc psychologiczno-pedagogiczną i zadania wychowawcy.",
            "W statucie ZSZ5 frekwencja jest połączona z usprawiedliwianiem, karami porządkowymi, klasyfikacją i promocją.",
            "W BS I praktyki i dzienniczek zajęć praktycznych są elementem obowiązku szkolnego/zawodowego.",
            "Wychowawca ma statutowe zadanie monitorowania frekwencji, rozpoznawania przyczyn nieobecności i pomocy uczniom z brakami.",
        ],
        "activity": "Case study: 'Uczeń był nieobecny przez kilka dni i przynosi usprawiedliwienie po czasie'; 'Uczeń BS I nie dostarcza dzienniczka praktyk'; 'Uczeń ma ponad połowę nieobecności na przedmiocie'. Grupy wskazują, czego trzeba szukać w statucie.",
        "privacy": "Nie omawiamy realnych spraw uczniów z klasy. Przypadki są fikcyjne i służą tylko zrozumieniu zasad.",
        "assessment": "Exit ticket: 'Statut przydaje mi się, gdy...' oraz 'najpierw sprawdzam...'.",
        "slides": [
            ("Statut to instrukcja szkoły", ["nie tylko dokument prawny", "zasady wspólne dla uczniów i nauczycieli", "punkt odniesienia w sporach"]),
            ("Gdzie go znaleźć", ["zsz5.edupage.org", "menu: Statut", "pracujemy na aktualnym pliku ze strony"]),
            ("Co reguluje", ["prawa i obowiązki", "ocenianie i zachowanie", "frekwencję", "praktyki", "pomoc psychologiczno-pedagogiczną"]),
            ("ZSZ5 w statucie", ["Technikum nr 5", "Branżowa Szkoła I stopnia nr 5", "Branżowa Szkoła II stopnia nr 5"]),
            ("Dlaczego frekwencja jest w statucie", ["usprawiedliwienia", "ostrzeżenia i nagany", "klasyfikacja", "promocja", "praktyki zawodowe"]),
        ],
    },
    {
        "id": "03",
        "slug": "03_frekwencja",
        "title": "Frekwencja: obecność jako warunek zaliczenia, bezpieczeństwa i zawodu",
        "group": "Wszystkie klasy",
        "men": "Bezpieczeństwo, odpowiedzialność, zdrowie psychiczne, współpraca z rodzicami",
        "purpose": "Uczeń widzi frekwencję nie jako procent w dzienniku, lecz jako warunek relacji ze szkołą, pracodawcą i własną przyszłością.",
        "outcomes": [
            "wyjaśnia skutki nieusprawiedliwionych nieobecności w ZSZ5",
            "odróżnia chorobę i usprawiedliwienie od unikania szkoły",
            "zna próg ustawowy 50% nieusprawiedliwionej nieobecności w miesiącu dla obowiązku nauki",
            "zna zasadę nieklasyfikowania przy braku podstaw z powodu ponad połowy nieobecności na zajęciach",
            "tworzy osobisty plan naprawy frekwencji lub utrzymania dobrej obecności",
        ],
        "materials": [
            "wydruk progów ze statutu ZSZ5",
            "karta 'plan 7 dni obecności'",
            "przykładowe, fikcyjne raporty frekwencji",
        ],
        "prep": [
            "Nie pokazuj rankingu klasy z nazwiskami.",
            "Przygotuj neutralne przykłady procentów i liczb godzin.",
            "Ustal ścieżkę wsparcia: wychowawca, rodzic, pedagog/psycholog, pracodawca/KSP.",
        ],
        "schedule": [
            ("0-5 min", "Start", "Frekwencja to nie ocena z charakteru, tylko informacja o ryzyku."),
            ("5-12 min", "Konkrety prawne i szkolne", "50% w miesiącu, nieklasyfikowanie, progi statutu ZSZ5."),
            ("12-20 min", "Analiza przypadków", "Trzy fikcyjne sytuacje: choroba, spóźnienia, unikanie praktyk."),
            ("20-27 min", "Plan naprawy", "Uczeń wybiera jeden mikro-krok na 7 dni."),
            ("27-30 min", "Zamknięcie", "Kiedy proszę o pomoc i kogo informuję?"),
        ],
        "key_points": [
            "Prawo oświatowe wskazuje próg co najmniej 50% nieusprawiedliwionej nieobecności w miesiącu jako niespełnianie obowiązku nauki.",
            "Ustawa o systemie oświaty dopuszcza nieklasyfikowanie, gdy brak podstaw do oceny z powodu nieobecności przekraczającej połowę czasu zajęć.",
            "Statut ZSZ5 przewiduje reakcje za godziny nieusprawiedliwione: upomnienie wychowawcy, naganę wychowawcy, naganę dyrektora, a w skrajnych przypadkach skreślenie.",
            "W BS I nieobecność na praktycznej nauce zawodu ma dodatkowe skutki, bo dotyczy także pracodawcy i dzienniczka praktyk.",
            "Frekwencję naprawia się wcześnie: rozmowa, usprawiedliwienia, plan nadrobienia, kontakt z rodzicem/pracodawcą, wsparcie pedagoga lub psychologa.",
        ],
        "activity": "Plan 7 dni: uczniowie wybierają jedną barierę frekwencji i zapisują realistyczny krok: transport, sen, komunikacja z rodzicem, kontakt z wychowawcą, nadrobienie jednego przedmiotu. Karty mogą zostać u ucznia.",
        "privacy": "Nie diagnozujemy publicznie przyczyn nieobecności. Uczniowie nie muszą ujawniać sytuacji rodzinnej, zdrowotnej ani psychicznej.",
        "assessment": "Uczeń tworzy mini-plan: 'jeśli nie mogę być w szkole, robię trzy rzeczy: informuję..., sprawdzam..., nadrabiam...'.",
        "slides": [
            ("Frekwencja to sygnał", ["nie ranking", "nie etykieta", "informacja o ryzyku", "punkt startu do działania"]),
            ("Dlaczego ważna", ["klasyfikacja", "promocja", "praktyki i pracodawca", "bezpieczeństwo", "kontakt z rodzicem"]),
            ("Progi, które trzeba znać", ["50% nieusprawiedliwionej nieobecności w miesiącu", "ponad połowa nieobecności na zajęciach może oznaczać brak klasyfikacji", "statutowe reakcje szkoły"]),
            ("Co robię po nieobecności", ["usprawiedliwienie w terminie", "sprawdzenie zaległości", "kontakt z nauczycielem", "plan nadrobienia"]),
            ("Plan 7 dni", ["jeden problem", "jeden konkretny krok", "jedna osoba do kontaktu", "jedna rzecz do nadrobienia"]),
        ],
    },
]


PRIORITY_LESSONS = [
    (
        "04",
        "04_reforma26_kompas_jutra",
        "Reforma26 i Kompas Jutra: szkoła wymagająca, wspierająca i przyjazna",
        "Wspieranie szkół we wdrażaniu zmian wynikających z Reformy26. Kompas Jutra.",
        "Uczeń rozumie, że reforma nie jest hasłem ministerialnym, tylko zmianą sposobu uczenia się: więcej sensu, wymagań, wsparcia i informacji zwrotnej.",
        ["szkoła może jednocześnie wymagać i wspierać", "uczeń ma wpływ na sposób uczenia się klasy", "informacja zwrotna pomaga poprawić pracę"],
        "Burza faktów: co w naszej klasie pomaga się uczyć, co przeszkadza, czego potrzebujemy od siebie.",
        ["wymagania", "wsparcie", "przyjazna relacja", "odpowiedzialność ucznia", "informacja zwrotna"],
    ),
    (
        "05",
        "05_odpornosc_spoleczna_bezpieczenstwo",
        "Odporność społeczna: patriotyzm, obywatelskość i bezpieczeństwo na co dzień",
        "Szkoła miejscem budowania odporności społecznej; postawy patriotyczne, obywatelskie, prospołeczne i odpowiedzialność za bezpieczeństwo.",
        "Uczeń rozumie, że odporność społeczna zaczyna się od codziennych zachowań: reagowania, informowania, dbania o innych i przestrzegania procedur.",
        ["rozpoznaje sytuacje wymagające reakcji dorosłych", "odróżnia donoszenie od odpowiedzialnego zgłoszenia", "wiąże patriotyzm z troską o wspólnotę"],
        "Drabina reakcji: uczniowie ustawiają sytuacje od 'rozwiązuję sam' do 'natychmiast zgłaszam dorosłemu'.",
        ["wspólnota", "odpowiedzialność", "bezpieczeństwo", "procedury", "pomoc"],
    ),
    (
        "06",
        "06_edukacja_zdrowotna",
        "Edukacja zdrowotna: sen, ruch, jedzenie, pierwsza pomoc i frekwencja",
        "Edukacja zdrowotna; zdrowy styl życia, aktywność ruchowa, zachowania prozdrowotne i pierwsza pomoc.",
        "Uczeń łączy zdrowie z obecnością w szkole, gotowością do pracy i bezpieczeństwem własnym oraz innych.",
        ["wskazuje jeden nawyk zdrowotny wpływający na frekwencję", "zna podstawowy schemat reagowania w sytuacji zagrożenia", "rozumie, że zdrowie to też proszenie o pomoc"],
        "Audit dnia: uczniowie wybierają jeden element do poprawy przez tydzień: sen, śniadanie, ruch, nawodnienie, ograniczenie ekranu przed snem.",
        ["sen", "ruch", "jedzenie", "pierwsza pomoc", "gotowość do nauki"],
    ),
    (
        "07",
        "07_higiena_cyfrowa_ai_zpe",
        "Higiena cyfrowa, AI i krytyczne myślenie",
        "Higiena cyfrowa i aktywność offline; bezpieczeństwo w sieci; krytyczna analiza informacji; odpowiedzialne wykorzystanie AI; ZPE.",
        "Uczeń potrafi nazwać koszt nadmiaru telefonu i wie, jak odpowiedzialnie korzystać z AI bez oddawania swoich danych i myślenia.",
        ["odróżnia pomoc AI od zastępowania własnej pracy", "zna zasadę niewpisywania danych osobowych do publicznych narzędzi", "umie sprawdzić informację w co najmniej dwóch źródłach"],
        "Test informacji: uczniowie dostają krótką tezę i planują, jak ją zweryfikować bez kopiowania pierwszego wyniku.",
        ["telefon", "uwaga", "AI", "RODO", "weryfikacja źródeł"],
    ),
    (
        "08",
        "08_potrzeby_ucznia_wspolpraca_z_rodzicami",
        "Moje potrzeby w szkole: jak prosić o wsparcie i współpracować z rodzicem",
        "Rozpoznawanie potrzeb dzieci i młodzieży; współpraca z rodzicami; pomoc psychologiczno-pedagogiczna i wychowawcza.",
        "Uczeń wie, że trudność szkolna powinna uruchomić rozmowę i wsparcie, a nie samotne znikanie z lekcji.",
        ["nazywa szkolne sytuacje, w których warto poprosić o pomoc", "wie, że pomoc PP jest dobrowolna i nieodpłatna", "potrafi przygotować krótką wiadomość do wychowawcy"],
        "Trzy zdania do wychowawcy: 'Mam trudność z...', 'Potrzebuję...', 'Mogę zrobić pierwszy krok...'.",
        ["potrzeby", "rozmowa", "rodzic", "pedagog", "psycholog"],
    ),
    (
        "09",
        "09_uzaleznienia_przemoc_kryzys",
        "Uzależnienia behawioralne, przemoc rówieśnicza i kryzys psychiczny",
        "Profilaktyka uzależnień behawioralnych i przemocy rówieśniczej; zdrowie psychiczne; reagowanie w kryzysach.",
        "Uczeń rozpoznaje sygnały ryzyka i wie, że szybkie zgłoszenie przemocy lub kryzysu jest działaniem ochronnym.",
        ["odróżnia konflikt od przemocy", "wskazuje przykłady uzależnień behawioralnych", "zna szkolną ścieżkę zgłoszenia kryzysu"],
        "Sygnały i reakcje: uczniowie przypisują sytuacje do reakcji: rozmowa, wsparcie rówieśnicze, wychowawca, pedagog/psycholog, natychmiastowa pomoc dorosłego.",
        ["przemoc", "kryzys", "uzależnienia behawioralne", "zgłoszenie", "wsparcie"],
    ),
    (
        "10",
        "10_doradztwo_zawodowe_ksztalcenie_zawodowe",
        "Decyzje edukacyjno-zawodowe: zawód, praktyki i rynek pracy",
        "Świadome decyzje edukacyjno-zawodowe; doradztwo zawodowe; promocja kształcenia zawodowego; nowa oferta szkół branżowych i techników.",
        "Uczeń widzi związek między frekwencją, praktyką, relacją z pracodawcą i przyszłą ścieżką zawodową.",
        ["łączy obecność z nabywaniem kompetencji zawodowych", "wskazuje źródła informacji o zawodach w ZSZ5", "potrafi nazwać jedną kompetencję do rozwijania w semestrze"],
        "Mapa zawodu: uczniowie wybierają kompetencję zawodową i dopisują, gdzie ją ćwiczą: szkoła, praktyka, dom, projekt.",
        ["zawód", "praktyki", "kompetencje", "pracodawca", "frekwencja"],
    ),
    (
        "11",
        "11_praca_projektowa_ocenianie_ksztaltujace",
        "Ciekawość, projekt i informacja zwrotna",
        "Ciekawość i aktywność poznawcza; interdyscyplinarność; praca projektowa; ocenianie kształtujące i informacja zwrotna.",
        "Uczeń rozumie, że dobra informacja zwrotna i praca projektowa pomagają uczyć się także po błędzie.",
        ["formułuje prosty cel projektu", "odróżnia ocenę od informacji zwrotnej", "umie dać koledze informację: plus, pytanie, propozycja poprawy"],
        "Mini-projekt klasy: wybór problemu szkolnego, szybki cel, kryteria sukcesu i jedna informacja zwrotna w parze.",
        ["ciekawość", "projekt", "cel", "kryteria sukcesu", "informacja zwrotna"],
    ),
]


for pid, slug, title, men, purpose, outcomes, activity, key_points in PRIORITY_LESSONS:
    LESSONS.append(
        {
            "id": pid,
            "slug": slug,
            "title": title,
            "group": "Wszystkie klasy",
            "men": men,
            "purpose": purpose,
            "outcomes": outcomes,
            "materials": [
                "tablica lub wspólny dokument bez danych osobowych",
                "karta pracy z pytaniami do refleksji",
                "fragment priorytetu MEN 2026/2027 w języku ucznia",
            ],
            "prep": [
                "Wybierz przykłady bliskie klasie: technikum, BS I stopnia, praktyki, pracodawca, frekwencja.",
                "Nie używaj realnych spraw uczniów jako studiów przypadku.",
                "Zdecyduj, czy efekt lekcji zostaje w teczce wychowawcy, czy u ucznia.",
            ],
            "schedule": [
                ("0-4 min", "Start", "Jedno pytanie otwierające i szybka diagnoza skojarzeń."),
                ("4-10 min", "Priorytet MEN po ludzku", "Nauczyciel tłumaczy sens priorytetu na przykład z życia szkoły."),
                ("10-21 min", "Ćwiczenie główne", activity),
                ("21-27 min", "Przeniesienie na klasę", "Co z tego wynika dla naszej frekwencji, relacji, praktyk lub bezpieczeństwa?"),
                ("27-30 min", "Zamknięcie", "Exit ticket: jedna decyzja, jedna prośba, jedno pytanie."),
            ],
            "key_points": key_points,
            "activity": activity,
            "privacy": "Uczniowie mogą pracować na przykładach fikcyjnych. Nie ujawniamy danych zdrowotnych, rodzinnych, ocen, sytuacji kryzysowych ani nazwisk.",
            "assessment": "Krótka karta wyjścia: 'rozumiem...', 'mogę zrobić...', 'potrzebuję zapytać...'.",
            "slides": [
                ("Temat", [title, "30 minut rozmowy i konkretu wychowawczego"]),
                ("Priorytet MEN", [men]),
                ("Po co nam to w ZSZ5", [purpose]),
                ("Słowa kluczowe", key_points),
                ("Ćwiczenie", [activity]),
                ("Połączenie z frekwencją", ["obecność daje kontakt", "kontakt daje wsparcie", "wsparcie pomaga utrzymać naukę i praktyki"]),
                ("Wyjście z lekcji", ["jedna decyzja", "jedna prośba", "jedno pytanie"]),
            ],
        }
    )


def md_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def table(rows: list[tuple[str, str, str]]) -> str:
    body = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in rows)
    return "| Czas | Segment | Działanie |\n|---|---|---|\n" + body


def scenario_md(lesson: dict) -> str:
    return f"""# {lesson['title']}

**Grupa:** {lesson['group']}  
**Czas:** 30 minut  
**Powiązanie z priorytetami MEN / pracą szkoły:** {lesson['men']}

## Cel lekcji

{lesson['purpose']}

## Uczeń po lekcji

{md_list(lesson['outcomes'])}

## Materiały

{md_list(lesson['materials'])}

## Przygotowanie wychowawcy

{md_list(lesson['prep'])}

## Przebieg lekcji minuta po minucie

{table(lesson['schedule'])}

## Treści, które trzeba powiedzieć wprost

{md_list(lesson['key_points'])}

## Ćwiczenie główne

{lesson['activity']}

## Notatka dla wychowawcy

- Trzymaj lekcję w tempie: ma być praktyczna, nie wykładowa.
- Zbieraj tylko te informacje, które są potrzebne do działania wychowawczego.
- Gdy pojawia się realny problem ucznia, przenieś rozmowę do trybu indywidualnego.
- Jeżeli temat dotyczy frekwencji, zawsze oddziel chorobę i sytuację kryzysową od nieusprawiedliwionego unikania szkoły.

## Bezpieczeństwo, RODO i dobrostan

{lesson['privacy']}

## Sprawdzenie efektu

{lesson['assessment']}

## Zadanie po lekcji

Uczeń kończy zdanie: `Po tej lekcji wiem, że...` oraz zapisuje jedną rzecz do sprawdzenia, poprawienia albo omówienia z rodzicem/opiekunem, wychowawcą lub pracodawcą.

## Źródła i odniesienia

- MEN, podstawowe kierunki polityki oświatowej 2026/2027.
- Strona ZSZ nr 5 we Wrocławiu: https://zsz5.edupage.org/
- Statut ZSZ5, tekst jednolity obowiązujący od 16.10.2025.
- Dla tematów VULCAN/frekwencji: Baza wiedzy VULCAN oraz aktualne przepisy wskazane w pliku `zrodla.md`.
"""


def slides_md(lesson: dict) -> str:
    slides = []
    for title, bullets in lesson["slides"]:
        slides.append("## " + title + "\n\n" + "\n".join(f"- {b}" for b in bullets))
    notes = f"""## Notatki prowadzącego

- Czas całej lekcji: 30 minut.
- Grupa: {lesson['group']}.
- Nie wpisuj na slajdach danych osobowych ani przykładów pozwalających rozpoznać ucznia.
- Po slajdach przejdź do ćwiczenia głównego: {lesson['activity']}
"""
    return f"# {lesson['title']} - prezentacja MD\n\n" + "\n\n---\n\n".join(slides + [notes])


def readme_md() -> str:
    lesson_rows = "\n".join(
        f"| {lesson['id']} | {lesson['title']} | {lesson['group']} | [scenariusz](scenariusze/{lesson['slug']}.md) | [prezentacja](prezentacje_md/{lesson['slug']}.md) |"
        for lesson in LESSONS
    )
    return f"""# Lekcje wychowawcze ZSZ5 2026/2027

Zestaw zawiera scenariusze 30-minutowych lekcji wychowawczych oraz pliki Markdown pod przyszłe prezentacje.

Lekcja 0 jest przeznaczona wyłącznie dla klas pierwszych. Pozostałe lekcje są przygotowane dla wszystkich klas Technikum nr 5 i Branżowej Szkoły I stopnia nr 5.

## Struktura

| Nr | Lekcja | Grupa | Scenariusz | Prezentacja MD |
|---|---|---|---|---|
{lesson_rows}

## Jak korzystać

1. Otwórz `strona_html/index.html` w przeglądarce.
2. Wybierz lekcję z listy.
3. Skorzystaj ze scenariusza lub z linku do prezentacji MD.
4. Przed użyciem uzupełnij lokalne informacje, szczególnie numery sal, procedurę VULCAN i aktualne osoby kontaktowe.

## Ważne

Materiały nie zbierają danych osobowych. Lekcja o VULCAN zawiera listę kontrolną i zasady bezpieczeństwa, ale właściwy sposób przekazywania danych powinien być potwierdzony z sekretariatem szkoły.
"""


def sources_md() -> str:
    return "# Źródła i weryfikacja\n\n" + "\n\n".join(
        f"## {src['name']}\n\n- URL: {src['url']}\n- Uwagi: {src['note']}" for src in SOURCES
    )


def css() -> str:
    return """
:root {
  --bg: #eef2f5;
  --panel: #ffffff;
  --panel-soft: #f8fafb;
  --ink: #14212b;
  --muted: #607080;
  --line: #d7e0e8;
  --accent: #0b6b5f;
  --accent-2: #dff3ef;
  --blue: #255d9a;
  --blue-soft: #e7f0fb;
  --amber: #9b5b00;
  --amber-soft: #fff2d9;
  --rose: #8d2942;
  --rose-soft: #ffe7ed;
  --shadow: 0 18px 50px rgba(20, 33, 43, .10);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    linear-gradient(90deg, rgba(20, 33, 43, .045) 1px, transparent 1px),
    linear-gradient(180deg, rgba(20, 33, 43, .045) 1px, transparent 1px),
    var(--bg);
  background-size: 28px 28px;
  color: var(--ink);
  line-height: 1.5;
}
a { color: var(--accent); }
button, input, select { font: inherit; }
button:focus-visible, a:focus-visible, input:focus-visible, select:focus-visible {
  outline: 3px solid rgba(37, 93, 154, .28);
  outline-offset: 2px;
}
header {
  padding: 26px clamp(18px, 4vw, 48px) 20px;
  background:
    linear-gradient(135deg, rgba(11, 107, 95, .13), transparent 36%),
    linear-gradient(90deg, #ffffff 0%, #f8fbfd 60%, #eef6f4 100%);
  border-bottom: 1px solid var(--line);
}
.topline {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: flex-start;
  flex-wrap: wrap;
}
.kicker {
  color: var(--accent);
  font-size: .82rem;
  font-weight: 800;
  margin: 0 0 8px;
}
h1 { margin: 0; font-size: clamp(1.8rem, 3vw, 2.75rem); line-height: 1.08; letter-spacing: 0; max-width: 900px; }
.subtitle { max-width: 980px; margin: 12px 0 0; color: var(--muted); font-size: 1rem; }
.badge {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 7px 11px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--accent-2);
  color: var(--accent);
  font-weight: 700;
  white-space: nowrap;
}
.hero-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(150px, 1fr));
  gap: 12px;
  margin-top: 18px;
  max-width: 1100px;
}
.metric {
  min-height: 86px;
  padding: 13px;
  border: 1px solid rgba(215, 224, 232, .9);
  border-radius: 10px;
  background: rgba(255, 255, 255, .72);
  box-shadow: 0 10px 30px rgba(20, 33, 43, .06);
}
.metric strong { display: block; font-size: 1.5rem; line-height: 1; }
.metric span { display: block; margin-top: 7px; color: var(--muted); font-size: .86rem; }
main {
  display: grid;
  grid-template-columns: minmax(290px, 390px) 1fr;
  gap: 20px;
  padding: 20px clamp(18px, 4vw, 48px) 34px;
}
aside, .detail {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: var(--shadow);
}
aside { padding: 14px; align-self: start; position: sticky; top: 14px; }
.panel-title {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}
.panel-title strong { font-size: .96rem; }
.count-pill {
  color: var(--blue);
  background: var(--blue-soft);
  border: 1px solid #c6d9ef;
  border-radius: 999px;
  padding: 4px 8px;
  font-size: .8rem;
  font-weight: 800;
}
.filters { display: grid; gap: 10px; margin-bottom: 12px; }
label { font-weight: 750; font-size: .88rem; }
input, select {
  width: 100%;
  min-height: 42px;
  border: 1px solid var(--line);
  border-radius: 9px;
  padding: 8px 10px;
  background: #fff;
}
.quick-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 4px 0 13px;
}
.chip {
  border: 1px solid var(--line);
  background: #fff;
  color: var(--ink);
  border-radius: 999px;
  min-height: 32px;
  padding: 5px 10px;
  cursor: pointer;
  font-weight: 750;
  font-size: .83rem;
}
.chip.active, .chip:hover { background: var(--accent-2); border-color: #9dcfc6; color: var(--accent); }
.lesson-list { display: grid; gap: 9px; max-height: calc(100dvh - 295px); overflow: auto; padding-right: 2px; }
.lesson-button {
  width: 100%;
  text-align: left;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, #fff, #fbfcfd);
  color: var(--ink);
  border-radius: 10px;
  padding: 11px;
  cursor: pointer;
  position: relative;
  transition: transform .16s ease, border-color .16s ease, box-shadow .16s ease, background .16s ease;
}
.lesson-button::before {
  content: "";
  position: absolute;
  inset: 10px auto 10px 0;
  width: 4px;
  border-radius: 0 5px 5px 0;
  background: var(--accent);
  opacity: .25;
}
.lesson-button:hover, .lesson-button.active {
  border-color: var(--accent);
  background: linear-gradient(180deg, #ffffff, var(--accent-2));
  box-shadow: 0 12px 24px rgba(11, 107, 95, .12);
  transform: translateY(-1px);
}
.lesson-button:active, .chip:active, .actions a:active, .actions button:active, .tab:active { transform: translateY(1px); }
.lesson-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 34px;
  height: 26px;
  border-radius: 7px;
  background: var(--panel-soft);
  border: 1px solid var(--line);
  margin-bottom: 8px;
  font-weight: 850;
}
.lesson-button strong { display: block; font-size: .96rem; line-height: 1.25; padding-left: 2px; }
.lesson-button span { display: block; color: var(--muted); font-size: .82rem; margin-top: 5px; padding-left: 2px; }
.lesson-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 9px; }
.tag {
  display: inline-flex;
  align-items: center;
  min-height: 23px;
  padding: 3px 7px;
  border-radius: 999px;
  font-size: .72rem;
  font-weight: 800;
  background: var(--blue-soft);
  color: var(--blue);
}
.tag.attendance { background: var(--rose-soft); color: var(--rose); }
.tag.first { background: var(--amber-soft); color: var(--amber); }
.detail { min-height: 650px; overflow: hidden; }
.detail-head {
  padding: 24px;
  border-bottom: 1px solid var(--line);
  background:
    linear-gradient(140deg, rgba(11, 107, 95, .11), transparent 45%),
    linear-gradient(90deg, #fbfcfd, #ffffff);
}
.detail-top {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(190px, 260px);
  gap: 18px;
  align-items: start;
}
.lesson-mark {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 5px 10px;
  border-radius: 9px;
  background: var(--ink);
  color: #fff;
  font-weight: 850;
  margin-bottom: 12px;
}
.detail h2 { margin: 0; font-size: clamp(1.45rem, 2.2vw, 2.25rem); line-height: 1.12; max-width: 880px; }
.meta { color: var(--muted); margin: 10px 0 0; }
.focus-card {
  border: 1px solid var(--line);
  border-radius: 12px;
  background: rgba(255, 255, 255, .76);
  padding: 12px;
}
.focus-card strong { display: block; font-size: 1.25rem; }
.focus-card span { color: var(--muted); font-size: .86rem; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
.actions a, .actions button {
  border: 1px solid var(--accent);
  background: var(--accent);
  color: #fff;
  text-decoration: none;
  border-radius: 9px;
  padding: 9px 13px;
  font-weight: 700;
  min-height: 40px;
  cursor: pointer;
  transition: transform .16s ease, box-shadow .16s ease, background .16s ease;
}
.actions a:hover, .actions button:hover { box-shadow: 0 10px 22px rgba(11, 107, 95, .16); }
.actions .secondary { background: #fff; color: var(--accent); }
.tabs {
  display: flex;
  gap: 8px;
  padding: 12px 24px 0;
  background: #fff;
  overflow-x: auto;
}
.tab {
  border: 1px solid var(--line);
  background: #fff;
  color: var(--muted);
  border-radius: 999px;
  min-height: 36px;
  padding: 6px 12px;
  cursor: pointer;
  font-weight: 800;
  white-space: nowrap;
}
.tab.active { color: var(--accent); border-color: #9dcfc6; background: var(--accent-2); }
.content { padding: 22px 24px 26px; display: grid; gap: 18px; }
.section-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}
section, .info-card {
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 16px;
  background: #fff;
}
.info-card.tint { background: var(--panel-soft); }
.info-card.full, .full { grid-column: 1 / -1; }
h3 { margin: 0 0 9px; font-size: 1rem; }
ul { margin: 0; padding-left: 20px; }
.timeline { display: grid; gap: 10px; }
.time-row {
  display: grid;
  grid-template-columns: 92px 150px 1fr;
  gap: 10px;
  padding: 10px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: #fbfcfd;
}
.time { font-weight: 850; color: var(--accent); }
.segment { font-weight: 800; }
.slide-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}
.slide-card {
  min-height: 170px;
  border: 1px solid #cfdbe5;
  border-radius: 12px;
  padding: 16px;
  background:
    linear-gradient(160deg, rgba(37, 93, 154, .10), transparent 45%),
    #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.slide-card h3 { font-size: 1.08rem; margin-bottom: 12px; }
.slide-card li { margin-bottom: 5px; }
.deck-shell {
  display: grid;
  gap: 12px;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px;
  background:
    linear-gradient(135deg, rgba(11, 107, 95, .12), transparent 42%),
    linear-gradient(315deg, rgba(37, 93, 154, .10), transparent 36%),
    #ffffff;
}
.deck-stage {
  aspect-ratio: 16 / 9;
  min-height: 360px;
  border-radius: 14px;
  background:
    linear-gradient(135deg, #10232f 0%, #163f4b 54%, #0b6b5f 100%);
  color: #fff;
  box-shadow: 0 24px 60px rgba(20, 33, 43, .18);
  overflow: hidden;
  position: relative;
}
.deck-stage::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(255,255,255,.07) 1px, transparent 1px),
    linear-gradient(180deg, rgba(255,255,255,.07) 1px, transparent 1px);
  background-size: 44px 44px;
  opacity: .55;
}
.deck-slide {
  position: relative;
  z-index: 1;
  min-height: 100%;
  padding: clamp(28px, 5vw, 64px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.deck-slide small {
  display: inline-flex;
  align-items: center;
  width: max-content;
  min-height: 30px;
  padding: 5px 10px;
  border-radius: 999px;
  background: rgba(255,255,255,.13);
  border: 1px solid rgba(255,255,255,.22);
  font-weight: 850;
}
.deck-slide h3 {
  max-width: 850px;
  margin: 18px 0 18px;
  font-size: clamp(1.9rem, 4vw, 4.5rem);
  line-height: 1.05;
}
.deck-slide ul {
  max-width: 780px;
  display: grid;
  gap: 10px;
  padding-left: 24px;
  font-size: clamp(1.05rem, 1.55vw, 1.55rem);
}
.deck-slide li::marker { color: #8ee1d5; }
.deck-controls {
  display: grid;
  grid-template-columns: auto auto 1fr auto auto auto;
  align-items: center;
  gap: 8px;
}
.deck-btn {
  min-height: 40px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #fff;
  color: var(--ink);
  font-weight: 850;
  padding: 8px 11px;
  cursor: pointer;
}
.deck-btn.primary {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}
.deck-btn:hover { border-color: var(--accent); }
.deck-progress {
  height: 10px;
  border-radius: 999px;
  background: #dce6ee;
  overflow: hidden;
}
.deck-progress span {
  display: block;
  height: 100%;
  width: var(--progress);
  background: linear-gradient(90deg, var(--accent), var(--blue));
}
.deck-help { color: var(--muted); font-size: .88rem; margin: 0; }
.deck-shell:fullscreen {
  width: 100vw;
  height: 100vh;
  border: 0;
  border-radius: 0;
  padding: 18px;
  background: #07141b;
}
.deck-shell:fullscreen .deck-stage {
  height: calc(100vh - 92px);
  min-height: 0;
  aspect-ratio: auto;
}
.deck-shell:fullscreen .deck-slide { padding: clamp(42px, 7vw, 96px); }
.deck-shell:fullscreen .deck-slide h3 { font-size: clamp(3rem, 6vw, 6.6rem); }
.deck-shell:fullscreen .deck-slide ul { font-size: clamp(1.4rem, 2vw, 2.25rem); }
.deck-shell:fullscreen .deck-controls,
.deck-shell:fullscreen .deck-help { color: #d8e8ef; }
.pptx-shell {
  display: grid;
  gap: 12px;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px;
  background:
    linear-gradient(135deg, rgba(11, 107, 95, .12), transparent 42%),
    linear-gradient(315deg, rgba(37, 93, 154, .10), transparent 36%),
    #ffffff;
}
.pptx-frame-wrap {
  aspect-ratio: 16 / 9;
  min-height: 520px;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid #cfdbe5;
  background: #10232f;
  box-shadow: 0 24px 60px rgba(20, 33, 43, .18);
}
.pptx-frame {
  width: 100%;
  height: 100%;
  border: 0;
  background: #ffffff;
}
.pptx-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}
.pptx-note {
  color: var(--muted);
  font-size: .9rem;
  margin: 0;
}
.pptx-shell:fullscreen {
  width: 100vw;
  height: 100vh;
  border: 0;
  border-radius: 0;
  padding: 14px;
  background: #07141b;
}
.pptx-shell:fullscreen .pptx-frame-wrap {
  height: calc(100vh - 74px);
  min-height: 0;
  aspect-ratio: auto;
}
.pptx-shell:fullscreen .pptx-note { color: #d8e8ef; }
.warning {
  border-left: 5px solid var(--amber);
  background: var(--amber-soft);
  padding: 12px 14px;
  border-radius: 8px;
}
.toast {
  position: fixed;
  right: 18px;
  bottom: 18px;
  max-width: min(340px, calc(100vw - 36px));
  padding: 12px 14px;
  border: 1px solid #9dcfc6;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: var(--shadow);
  color: var(--accent);
  font-weight: 800;
  opacity: 0;
  transform: translateY(8px);
  pointer-events: none;
  transition: opacity .2s ease, transform .2s ease;
}
.toast.show { opacity: 1; transform: translateY(0); }
.focus-mode aside { display: none; }
.focus-mode main { grid-template-columns: 1fr; max-width: 1180px; margin: 0 auto; }
footer { padding: 0 clamp(18px, 4vw, 48px) 28px; color: var(--muted); font-size: .9rem; }
@media (max-width: 980px) {
  .hero-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  main { grid-template-columns: 1fr; }
  aside { position: static; }
  .lesson-list { max-height: none; }
  .detail-top, .section-grid, .slide-grid { grid-template-columns: 1fr; }
  .deck-controls { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .deck-progress { grid-column: 1 / -1; order: -1; }
  .pptx-frame-wrap { min-height: 380px; }
  .time-row { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  header { padding-top: 20px; }
  .hero-grid { grid-template-columns: 1fr; }
  .actions a, .actions button { width: 100%; justify-content: center; text-align: center; }
  .tabs { padding-inline: 14px; }
  .content, .detail-head { padding-inline: 16px; }
  .deck-stage { min-height: 280px; }
  .deck-slide { padding: 22px; }
  .pptx-frame-wrap { min-height: 260px; }
}
@media print {
  body { background: #fff; }
  header, aside, .tabs, .actions, footer, .toast { display: none !important; }
  main { display: block; padding: 0; }
  .detail { border: 0; box-shadow: none; }
  section, .info-card, .slide-card { break-inside: avoid; }
}
"""


def js() -> str:
    payload = json.dumps(LESSONS, ensure_ascii=False, indent=2)
    return f"""
const LESSONS = {payload};

const list = document.querySelector('#lessonList');
const detail = document.querySelector('#detail');
const search = document.querySelector('#search');
const group = document.querySelector('#groupFilter');
const count = document.querySelector('#resultCount');
const chips = document.querySelectorAll('[data-chip]');
const focusToggle = document.querySelector('#focusToggle');
const toast = document.querySelector('#toast');

let currentId = localStorage.getItem('zsz5-current-lesson') || LESSONS[0].id;
let currentTab = 'scenario';
let quickFilter = 'all';
const slideState = {{}};

function typeLabel(lesson) {{
  if (lesson.id === '00') return 'adaptacja';
  if (lesson.id === '01') return 'VULCAN';
  if (lesson.id === '02') return 'statut';
  if (lesson.id === '03') return 'frekwencja';
  return 'MEN';
}}

function isAttendance(lesson) {{
  return [lesson.title, lesson.men, lesson.purpose, lesson.key_points.join(' ')].join(' ').toLowerCase().includes('frekwenc');
}}

function renderList() {{
  const q = search.value.trim().toLowerCase();
  const gf = group.value;
  const filtered = LESSONS.filter((lesson) => {{
    const hay = [lesson.title, lesson.group, lesson.men, lesson.purpose].join(' ').toLowerCase();
    const okText = !q || hay.includes(q);
    const okGroup = gf === 'all' || (gf === 'first' ? lesson.id === '00' : lesson.id !== '00');
    const okQuick = quickFilter === 'all'
      || (quickFilter === 'attendance' && isAttendance(lesson))
      || (quickFilter === 'men' && Number(lesson.id) >= 4)
      || (quickFilter === 'org' && Number(lesson.id) <= 3);
    return okText && okGroup && okQuick;
  }});
  list.innerHTML = '';
  count.textContent = `${{filtered.length}} z ${{LESSONS.length}}`;
  filtered.forEach((lesson) => {{
    const btn = document.createElement('button');
    btn.className = 'lesson-button';
    btn.type = 'button';
    btn.dataset.id = lesson.id;
    const attendanceTag = isAttendance(lesson) ? '<span class="tag attendance">frekwencja</span>' : '';
    const firstTag = lesson.id === '00' ? '<span class="tag first">klasy pierwsze</span>' : '';
    btn.innerHTML = `
      <span class="lesson-number">${{lesson.id}}</span>
      <strong>${{lesson.title}}</strong>
      <span>${{lesson.group}}</span>
      <div class="lesson-tags"><span class="tag">${{typeLabel(lesson)}}</span>${{attendanceTag}}${{firstTag}}</div>
    `;
    btn.addEventListener('click', () => renderDetail(lesson.id));
    list.appendChild(btn);
  }});
  if (!filtered.some((l) => l.id === currentId)) {{
    renderDetail(filtered[0]?.id || LESSONS[0].id);
  }} else {{
    markActive();
  }}
}}

function listItems(items) {{
  return '<ul>' + items.map((item) => `<li>${{item}}</li>`).join('') + '</ul>';
}}

function renderSchedule(rows) {{
  return `<div class="timeline">${{rows.map((r) => `<div class="time-row"><div class="time">${{r[0]}}</div><div class="segment">${{r[1]}}</div><div>${{r[2]}}</div></div>`).join('')}}</div>`;
}}

function getSlideIndex(lesson) {{
  const max = lesson.slides.length - 1;
  const saved = slideState[lesson.id] ?? 0;
  return Math.max(0, Math.min(max, saved));
}}

function setSlideIndex(lesson, index) {{
  const max = lesson.slides.length - 1;
  slideState[lesson.id] = Math.max(0, Math.min(max, index));
  if (currentTab === 'slides' && currentId === lesson.id) {{
    updateDeckView(lesson);
  }} else {{
    renderDetail(lesson.id);
  }}
}}

function moveSlide(lesson, delta) {{
  setSlideIndex(lesson, getSlideIndex(lesson) + delta);
}}

function renderSlideStage(lesson, index) {{
  const slide = lesson.slides[index];
  return `<article class="deck-slide">
    <small>Slajd ${{index + 1}} z ${{lesson.slides.length}} · lekcja ${{lesson.id}}</small>
    <h3>${{slide[0]}}</h3>
    ${{listItems(slide[1])}}
  </article>`;
}}

function renderDeck(lesson) {{
  const index = getSlideIndex(lesson);
  const progress = Math.round(((index + 1) / lesson.slides.length) * 100);
  return `<div class="deck-shell" data-deck>
    <div class="deck-stage" role="region" aria-live="polite" aria-label="Prezentacja: ${{lesson.title}}">
      ${{renderSlideStage(lesson, index)}}
    </div>
    <div class="deck-controls" aria-label="Sterowanie prezentacją">
      <button class="deck-btn" type="button" data-slide-action="first">Początek</button>
      <button class="deck-btn" type="button" data-slide-action="prev">Poprzedni</button>
      <div class="deck-progress" aria-label="Postęp prezentacji" style="--progress: ${{progress}}%"><span></span></div>
      <button class="deck-btn" type="button" data-slide-action="next">Następny</button>
      <button class="deck-btn" type="button" data-slide-action="last">Koniec</button>
      <button class="deck-btn primary" type="button" data-slide-action="fullscreen">Pełny ekran</button>
    </div>
    <p class="deck-help">Skróty: strzałki lewo/prawo zmieniają slajd, Home/End przechodzą na początek/koniec, F włącza pełny ekran.</p>
  </div>`;
}}

function updateDeckView(lesson) {{
  const index = getSlideIndex(lesson);
  const progress = Math.round(((index + 1) / lesson.slides.length) * 100);
  const stage = detail.querySelector('.deck-stage');
  const progressBar = detail.querySelector('.deck-progress');
  if (!stage || !progressBar) {{
    renderDetail(lesson.id);
    return;
  }}
  stage.innerHTML = renderSlideStage(lesson, index);
  progressBar.style.setProperty('--progress', `${{progress}}%`);
}}

function pptxUrl(lesson) {{
  return new URL(`../prezentacje_pptx/${{lesson.slug}}.pptx`, window.location.href).href;
}}

function pptxViewerUrl(lesson) {{
  return `https://view.officeapps.live.com/op/embed.aspx?src=${{encodeURIComponent(pptxUrl(lesson))}}`;
}}

function renderPptxEmbed(lesson) {{
  const pptx = pptxUrl(lesson);
  const viewer = pptxViewerUrl(lesson);
  const isLocal = ['localhost', '127.0.0.1'].includes(window.location.hostname);
  const localNote = isLocal
    ? 'Podgląd osadzony działa po publikacji na GitHub Pages. Lokalnie użyj przycisku Pobierz PPTX.'
    : 'To jest osadzony plik PPTX z folderu prezentacje_pptx, nie slajdy generowane przez stronę.';
  return `<div class="pptx-shell" data-pptx-embed>
    <div class="pptx-frame-wrap">
      <iframe class="pptx-frame" title="Prezentacja PPTX: ${{lesson.title}}" src="${{viewer}}" allowfullscreen loading="lazy"></iframe>
    </div>
    <div class="pptx-actions">
      <a class="deck-btn primary" href="${{pptx}}" download>Pobierz PPTX</a>
      <a class="deck-btn" href="${{viewer}}" target="_blank" rel="noopener">Otwórz w nowej karcie</a>
      <button class="deck-btn" type="button" data-pptx-action="fullscreen">Pełny ekran</button>
    </div>
    <p class="pptx-note">${{localNote}} Skrót: F włącza pełny ekran osadzenia.</p>
  </div>`;
}}

function renderChecklist(lesson) {{
  const checks = [
    'Sprawdzam grupę docelową lekcji.',
    'Mam otwarty scenariusz albo plik prezentacji MD.',
    'Nie pokazuję danych osobowych ani realnych spraw uczniów.',
    'Pilnuję czasu 30 minut.',
    'Kończę lekcję konkretnym zadaniem albo kartą wyjścia.',
  ];
  if (lesson.id === '00') checks.push('Uzupełniam lokalne miejsca i numery sal przed lekcją.');
  if (lesson.id === '01') checks.push('Potwierdzam procedurę VULCAN z sekretariatem.');
  if (lesson.id === '03') checks.push('Nie pokazuję rankingu frekwencji z nazwiskami.');
  return listItems(checks);
}}

function tabButton(id, label) {{
  return `<button class="tab ${{currentTab === id ? 'active' : ''}}" type="button" data-tab="${{id}}">${{label}}</button>`;
}}

function renderTabContent(lesson) {{
  if (currentTab === 'slides') {{
    return `<div class="content">${{renderPptxEmbed(lesson)}}</div>`;
  }}
  if (currentTab === 'checklist') {{
    return `<div class="content">
      <div class="section-grid">
        <section class="full"><h3>Checklista przed lekcją</h3>${{renderChecklist(lesson)}}</section>
        <section><h3>Materiały</h3>${{listItems(lesson.materials)}}</section>
        <section><h3>Przygotowanie</h3>${{listItems(lesson.prep)}}</section>
        <section class="full"><h3>Bezpieczeństwo i RODO</h3><p class="warning">${{lesson.privacy}}</p></section>
      </div>
    </div>`;
  }}
  return `<div class="content">
    <div class="section-grid">
      <section><h3>Cel</h3><p>${{lesson.purpose}}</p></section>
      <section><h3>Uczeń po lekcji</h3>${{listItems(lesson.outcomes)}}</section>
      <section class="full"><h3>Przebieg 30 minut</h3>${{renderSchedule(lesson.schedule)}}</section>
      <section><h3>Treści do powiedzenia wprost</h3>${{listItems(lesson.key_points)}}</section>
      <section><h3>Ćwiczenie główne</h3><p>${{lesson.activity}}</p></section>
      <section class="full"><h3>Bezpieczeństwo i RODO</h3><p class="warning">${{lesson.privacy}}</p></section>
      <section class="full"><h3>Sprawdzenie efektu</h3><p>${{lesson.assessment}}</p></section>
    </div>
  </div>`;
}}

function copyPlan(lesson) {{
  const text = `${{lesson.title}}\\nGrupa: ${{lesson.group}}\\nCel: ${{lesson.purpose}}\\n\\nPrzebieg:\\n${{lesson.schedule.map((r) => `${{r[0]}} - ${{r[1]}}: ${{r[2]}}`).join('\\n')}}`;
  navigator.clipboard?.writeText(text).then(() => showToast('Plan lekcji skopiowany')).catch(() => showToast('Nie udało się skopiować'));
}}

function showToast(message) {{
  toast.textContent = message;
  toast.classList.add('show');
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => toast.classList.remove('show'), 1800);
}}

function openFullscreen() {{
  const deck = detail.querySelector('[data-pptx-embed]') || detail.querySelector('[data-deck]');
  if (!deck) return;
  const request = deck.requestFullscreen || deck.webkitRequestFullscreen || deck.msRequestFullscreen;
  if (!request) {{
    showToast('Ta przeglądarka nie obsługuje pełnego ekranu');
    return;
  }}
  const result = request.call(deck);
  result?.catch?.(() => showToast('Nie udało się włączyć pełnego ekranu'));
}}

function bindPptxControls() {{
  detail.querySelectorAll('[data-pptx-action]').forEach((btn) => {{
    btn.addEventListener('click', () => {{
      if (btn.dataset.pptxAction === 'fullscreen') openFullscreen();
    }});
  }});
}}

function bindDeckControls(lesson) {{
  detail.querySelectorAll('[data-slide-action]').forEach((btn) => {{
    btn.addEventListener('click', () => {{
      const action = btn.dataset.slideAction;
      if (action === 'first') setSlideIndex(lesson, 0);
      if (action === 'prev') moveSlide(lesson, -1);
      if (action === 'next') moveSlide(lesson, 1);
      if (action === 'last') setSlideIndex(lesson, lesson.slides.length - 1);
      if (action === 'fullscreen') openFullscreen();
    }});
  }});
}}

function renderDetail(id) {{
  const lesson = LESSONS.find((item) => item.id === id) || LESSONS[0];
  currentId = lesson.id;
  localStorage.setItem('zsz5-current-lesson', currentId);
  detail.innerHTML = `
    <div class="detail-head">
      <div class="detail-top">
        <div>
          <span class="lesson-mark">Lekcja ${{lesson.id}}</span>
          <h2>${{lesson.title}}</h2>
          <p class="meta">${{lesson.group}} · 30 minut · ${{lesson.men}}</p>
        </div>
        <div class="focus-card">
          <strong>30 min</strong>
          <span>gotowy scenariusz, realny plik PPTX i checklista prowadzącego</span>
        </div>
      </div>
      <div class="actions">
        <a href="../scenariusze/${{lesson.slug}}.md">Scenariusz MD</a>
        <a class="secondary" href="../prezentacje_pptx/${{lesson.slug}}.pptx">PPTX</a>
        <a class="secondary" href="../prezentacje_md/${{lesson.slug}}.md">Prezentacja MD</a>
        <button class="secondary" type="button" data-action="copy">Kopiuj plan</button>
        <button class="secondary" type="button" data-action="print">Drukuj widok</button>
      </div>
    </div>
    <div class="tabs">
      ${{tabButton('scenario', 'Scenariusz')}}
      ${{tabButton('slides', 'Prezentacja')}}
      ${{tabButton('checklist', 'Checklista')}}
    </div>
    ${{renderTabContent(lesson)}}
  `;
  detail.querySelectorAll('[data-tab]').forEach((btn) => {{
    btn.addEventListener('click', () => {{
      currentTab = btn.dataset.tab;
      renderDetail(currentId);
    }});
  }});
  detail.querySelector('[data-action="copy"]').addEventListener('click', () => copyPlan(lesson));
  detail.querySelector('[data-action="print"]').addEventListener('click', () => window.print());
  if (currentTab === 'slides') bindPptxControls();
  markActive();
}}

function markActive() {{
  document.querySelectorAll('.lesson-button').forEach((btn) => {{
    btn.classList.toggle('active', btn.dataset.id === currentId);
  }});
}}

search.addEventListener('input', renderList);
group.addEventListener('change', renderList);
chips.forEach((chip) => {{
  chip.addEventListener('click', () => {{
    quickFilter = chip.dataset.chip;
    chips.forEach((item) => item.classList.toggle('active', item === chip));
    renderList();
  }});
}});
focusToggle.addEventListener('click', () => {{
  document.body.classList.toggle('focus-mode');
  focusToggle.textContent = document.body.classList.contains('focus-mode') ? 'Pokaż listę' : 'Tryb skupienia';
}});
document.addEventListener('keydown', (event) => {{
  if (currentTab !== 'slides') return;
  if (['INPUT', 'SELECT', 'TEXTAREA'].includes(event.target?.tagName)) return;
  if (event.key.toLowerCase() === 'f') {{
    event.preventDefault();
    openFullscreen();
  }}
}});
renderList();
renderDetail(currentId);
"""


def html() -> str:
    return """<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lekcje wychowawcze ZSZ5 2026/2027</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <div class="topline">
      <div>
        <p class="kicker">ZSZ5 · narzędzie dla wychowawcy</p>
        <h1>Lekcje wychowawcze ZSZ5 2026/2027</h1>
        <p class="subtitle">Scenariusze 30-minutowych lekcji i pliki Markdown pod prezentacje. Lekcja 0 jest tylko dla klas pierwszych; pozostałe lekcje są dla wszystkich klas Technikum nr 5 i BS I stopnia nr 5.</p>
      </div>
      <span class="badge">wersja robocza do użycia</span>
    </div>
    <div class="hero-grid" aria-label="Podsumowanie materiałów">
      <div class="metric"><strong>12</strong><span>lekcji wychowawczych</span></div>
      <div class="metric"><strong>30</strong><span>minut na scenariusz</span></div>
      <div class="metric"><strong>24</strong><span>pliki MD: scenariusze i prezentacje</span></div>
      <div class="metric"><strong>1</strong><span>lekcja startowa dla klas pierwszych</span></div>
    </div>
  </header>
  <main>
    <aside aria-label="Lista lekcji">
      <div class="panel-title">
        <strong>Wybór lekcji</strong>
        <span id="resultCount" class="count-pill">12 z 12</span>
      </div>
      <div class="filters">
        <label for="search">Szukaj</label>
        <input id="search" type="search" placeholder="frekwencja, statut, VULCAN">
        <label for="groupFilter">Zakres</label>
        <select id="groupFilter">
          <option value="all">Wszystkie lekcje</option>
          <option value="first">Tylko lekcja 0</option>
          <option value="allClasses">Lekcje dla wszystkich</option>
        </select>
      </div>
      <div class="quick-filters" aria-label="Szybkie filtry">
        <button class="chip active" type="button" data-chip="all">wszystkie</button>
        <button class="chip" type="button" data-chip="org">organizacyjne</button>
        <button class="chip" type="button" data-chip="attendance">frekwencja</button>
        <button class="chip" type="button" data-chip="men">MEN</button>
      </div>
      <div id="lessonList" class="lesson-list"></div>
    </aside>
    <article id="detail" class="detail"></article>
  </main>
  <footer>
    <button id="focusToggle" class="chip" type="button">Tryb skupienia</button>
    Źródła i zastrzeżenia są w pliku <a href="../zrodla.md">zrodla.md</a>. Przed użyciem uzupełnij lokalne numery sal i potwierdź procedurę przekazywania danych do VULCAN.
  </footer>
  <div id="toast" class="toast" role="status" aria-live="polite"></div>
  <script src="script.js"></script>
</body>
</html>
"""


def main() -> None:
    for path in [SCENARIOS, SLIDES, SITE]:
        path.mkdir(parents=True, exist_ok=True)

    for lesson in LESSONS:
        (SCENARIOS / f"{lesson['slug']}.md").write_text(scenario_md(lesson), encoding="utf-8")
        (SLIDES / f"{lesson['slug']}.md").write_text(slides_md(lesson), encoding="utf-8")

    (OUT / "README.md").write_text(readme_md(), encoding="utf-8")
    (OUT / "zrodla.md").write_text(sources_md(), encoding="utf-8")
    (OUT / "lessons.json").write_text(json.dumps(LESSONS, ensure_ascii=False, indent=2), encoding="utf-8")
    (SITE / "index.html").write_text(html(), encoding="utf-8")
    (SITE / "styles.css").write_text(css().strip() + "\n", encoding="utf-8")
    (SITE / "script.js").write_text(js().strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
