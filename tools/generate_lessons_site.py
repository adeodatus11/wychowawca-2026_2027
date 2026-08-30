from __future__ import annotations

import html
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from generate_wytyczne_document_page import main as generate_wytyczne_document_page


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "materialy_lekcje_wychowawcze_2026_2027"
SITE = OUT / "strona_html"
LESSON_PAGES = SITE / "lekcje"
ROOT_LESSON_PAGES = ROOT / "lekcje"
ROOT_ASSETS = ROOT / "assets"
SITE_ASSETS = SITE / "assets"
LOGO_FILE = "logo-orzel-zsz5.png"
LOGO_FULL_FILE = "logo-school-master-full.png"
LOGO_FILES = (LOGO_FILE, LOGO_FULL_FILE)
EXTRA_SITE_FILES = (
    "spotkanie-z-uczniami-1-wrzesnia-2026.html",
    "prezentacja-1-wrzesnia.css",
    "prezentacja-1-wrzesnia.js",
    "wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html",
    "wytyczne-document.css",
    "wytyczne_wych_uczn_1_wrzes_2026_ost.docx",
)
ANALYSIS = ROOT / "analiza_i_opracowanie_tematow_lekcji_wychowawczych_2026_2027.md"
DOCX_SOURCE = ROOT / "Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx"


@dataclass(frozen=True)
class Source:
    key: str
    name: str
    url: str
    note: str


SOURCES = {
    "men_2026": Source(
        "men_2026",
        "MEN: podstawowe kierunki polityki oświatowej 2026/2027",
        "https://www.gov.pl/web/edukacja/podstawowe-kierunki-realizacji-polityki-oswiatowej-panstwa-w-roku-szkolnym-20262027",
        "Punkt odniesienia dla całego planu wychowawczo-profilaktycznego.",
    ),
    "zpe": Source(
        "zpe",
        "Zintegrowana Platforma Edukacyjna",
        "https://zpe.gov.pl/",
        "Materiały edukacyjne, kursy i zasoby do wykorzystania przez nauczyciela.",
    ),
    "zpe_ai": Source(
        "zpe_ai",
        "ZPE: Nauka z AI - cyberbezpieczne środowisko w szkole",
        "https://zpe.gov.pl/b/nauka-z-ai---cyberbezpieczne-srodowisko-w-szkole/P99FNDS7U",
        "Praktyczny kontekst dla tematów o AI, danych i bezpieczeństwie cyfrowym.",
    ),
    "nask_dezinformacja": Source(
        "nask_dezinformacja",
        "NASK: zjawisko dezinformacji - materiały edukacyjne",
        "https://www.gov.pl/web/nauka/zjawisko-dezinformacji--materialy-edukacyjne-nask",
        "Ćwiczenia i pomoce dydaktyczne do pracy z uczniami nad fake newsami.",
    ),
    "uodo": Source(
        "uodo",
        "UODO: ochrona danych osobowych",
        "https://uodo.gov.pl/",
        "Instytucjonalne źródło zasad ochrony danych osobowych.",
    ),
    "fdds": Source(
        "fdds",
        "Fundacja Dajemy Dzieciom Siłę: przemoc rówieśnicza i cyberprzemoc",
        "https://fdds.pl/cyberprzemoc-nie-chodzi-na-wagary-program-rowiesnicy-fundacji-dajemy-dzieciom-sile-pomaga-jej-przeciwdzialac/",
        "Materiał do kontekstu profilaktyki przemocy i cyberprzemocy.",
    ),
    "men_przemoc": Source(
        "men_przemoc",
        "MEN: ścieżka pomocy dla szkoły - przemoc rówieśnicza",
        "https://dokumenty.men.gov.pl/SCIEZKA-POMOCY-DLA-SZKOLY-przemoc-rowiesnicza-68c43ef1af0a9.docx",
        "Dokument pomocniczy do reagowania na przemoc rówieśniczą w szkole.",
    ),
    "zpe_zdrowie": Source(
        "zpe_zdrowie",
        "ZPE: edukacja zdrowotna",
        "https://zpe.gov.pl/edukacja-zdrowotna",
        "Programy, scenariusze i materiały dla nauczycieli oraz uczniów.",
    ),
    "zpe_pierwsza_pomoc": Source(
        "zpe_pierwsza_pomoc",
        "ZPE: ABC pierwszej pomocy",
        "https://zpe.gov.pl/a/abc-pierwszej-pomocy/DtLX9npeZ",
        "Film i materiał edukacyjny o podstawach pierwszej pomocy.",
    ),
    "wosp": Source(
        "wosp",
        "WOŚP: Ratujemy i Uczymy Ratować",
        "https://www.wosp.org.pl/uczymy-ratowac",
        "Materiały edukacyjne i program pierwszej pomocy.",
    ),
    "ore_doradztwo": Source(
        "ore_doradztwo",
        "ORE: materiały z doradztwa zawodowego",
        "https://doradztwo.ore.edu.pl/materialy/",
        "Materiały do pracy z uczniami i rodzicami w obszarze doradztwa zawodowego.",
    ),
    "ore_filmy": Source(
        "ore_filmy",
        "ORE: cykl filmów Drogi Zawodowe",
        "https://doradztwo.ore.edu.pl/cykl-filmow-drogi-zawodowe/",
        "Filmy o zainteresowaniach, mocnych stronach, doświadczeniach i decyzjach.",
    ),
    "ceo_feedback": Source(
        "ceo_feedback",
        "CEO: informacja zwrotna, czyli ocena kształtująca",
        "https://biblioteka.ceo.org.pl/informacja-zwrotna-czyli-ocena-ksztaltujaca/",
        "Praktyczne wyjaśnienie roli informacji zwrotnej w uczeniu się.",
    ),
    "projekt": Source(
        "projekt",
        "Jak pracować metodą projektu krok po kroku",
        "https://photon.education/pl/praca-metoda-projektu/",
        "Przystępny opis planowania i prowadzenia pracy projektowej.",
    ),
    "zpe_odpady": Source(
        "zpe_odpady",
        "ZPE: film - w jaki sposób radzić sobie z odpadami?",
        "https://zpe.gov.pl/a/film/Df0T0zIDT",
        "Film i ćwiczenia o rodzajach odpadów i gospodarowaniu odpadami.",
    ),
    "pah_woda": Source(
        "pah_woda",
        "PAH: Woda nie tylko w kranie",
        "https://www.youtube.com/watch?v=AB0RFjndmWU",
        "Animacja edukacyjna pomocna przy rozmowie o wodzie i odpowiedzialności.",
    ),
    "zsz5": Source(
        "zsz5",
        "ZSZ nr 5 we Wrocławiu",
        "https://zsz5.edupage.org/",
        "Lokalne dokumenty szkoły, statut, komunikaty i informacje organizacyjne.",
    ),
    "szkola_mistrzow": Source(
        "szkola_mistrzow",
        "Szkoła Mistrzów",
        "https://www.szkolamistrzow.info/",
        "Informacje o ofercie kształcenia zawodowego szkoły.",
    ),
    "saferinternet": Source(
        "saferinternet",
        "Polskie Centrum Programu Safer Internet: materiały edukacyjne",
        "https://www.saferinternet.pl/menu/materialy-edukacyjne.html",
        "Poradniki, scenariusze, raporty i materiały multimedialne o bezpieczeństwie online.",
    ),
    "saferinternet_dobrostan": Source(
        "saferinternet_dobrostan",
        "Safer Internet: poradniki i broszury o cyfrowym dobrostanie",
        "https://www.saferinternet.pl/menu/materialy-edukacyjne/poradniki-i-broszury.html",
        "Praktyczne publikacje o higienie cyfrowej, śladzie cyfrowym, hejcie i dobrostanie online.",
    ),
    "nask_cyberprofilaktyka": Source(
        "nask_cyberprofilaktyka",
        "Cyberprofilaktyka NASK",
        "https://akademia.nask.pl/",
        "Biblioteka poradników, scenariuszy i szkoleń o bezpieczeństwie dzieci i młodzieży w internecie.",
    ),
    "nask_kurs_dezinformacja": Source(
        "nask_kurs_dezinformacja",
        "NASK: kurs dla nauczycieli o dezinformacji",
        "https://www.nask.pl/aktualnosci/w-co-wierzyc-w-internecie-nowy-kurs-dla-nauczycieli-na-ose-it-szkole",
        "Opis kursu pokazującego metody dezinformacji i sposoby rozmowy z uczniami o wiarygodności treści.",
    ),
    "fdds_przemoc_scenariusz": Source(
        "fdds_przemoc_scenariusz",
        "FDDS: przemoc rówieśnicza - scenariusz dla młodzieży 13-18 lat",
        "https://edukacja.fdds.pl/course/view.php?id=902",
        "Scenariusz zajęć o przemocy offline i online oraz reagowaniu z perspektywy świadka i osoby pokrzywdzonej.",
    ),
    "fdds_ramie": Source(
        "fdds_ramie",
        "FDDS: #ramięwramię - scenariusze o przemocy rówieśniczej",
        "https://edukacja.fdds.pl/course/view.php?id=683",
        "Materiały do rozmowy o roli świadka, granicach, zachowaniach raniących i szukaniu pomocy.",
    ),
    "szkola_z_klasa_materialy": Source(
        "szkola_z_klasa_materialy",
        "Fundacja Szkoła z Klasą: biblioteka materiałów",
        "https://www.szkolazklasa.org.pl/materialy/",
        "Biblioteka poradników, scenariuszy, kart pracy i pomysłów wzmacniających relacje oraz aktywność uczniów.",
    ),
    "szkola_z_klasa_razem": Source(
        "szkola_z_klasa_razem",
        "Szkoła z Klasą: Razem w Klasie - przewodnik dla szkół",
        "https://www.szkolazklasa.org.pl/materialy/razem-w-klasie-przewodnik-dla-szkol/",
        "Przewodnik o integracji, pracy z różnorodną klasą i budowaniu relacji.",
    ),
    "szkola_z_klasa_odpornosc": Source(
        "szkola_z_klasa_odpornosc",
        "Szkoła z Klasą: materiały o odporności psychicznej",
        "https://www.szkolazklasa.org.pl/obszary/szkola-z-klasa/materialy-edukacyjne/",
        "Materiały dla nauczycieli o dialogu, odporności psychicznej i relacjach w klasie.",
    ),
    "ceo_feedback_blog": Source(
        "ceo_feedback_blog",
        "CEO: jak udzielać informacji zwrotnej",
        "https://ceo.org.pl/co-warto-wiedziec-o-informacji-zwrotnej/",
        "Krótki artykuł o informacji zwrotnej jako komunikacie odnoszącym się do pracy, aktywności lub zachowania.",
    ),
    "ceo_project_pdf": Source(
        "ceo_project_pdf",
        "CEO: metoda projektu edukacyjnego",
        "https://alosus.ceo.org.pl/sites/alosus.ceo.org.pl/files/metoda_projektu_edukacyjnego_katarzyna_soltan-mlodozeniec.pdf",
        "Praktyczny poradnik o planowaniu projektu, rolach, kryteriach sukcesu i ewaluacji.",
    ),
    "ore_doradcy_2023": Source(
        "ore_doradcy_2023",
        "ORE: materiały edukacyjne dla doradców zawodowych",
        "https://ore.edu.pl/2023/12/materialy-edukacyjne-dla-doradcow-zawodowych/",
        "Publikacje, scenariusze i karty pracy dla osób prowadzących doradztwo zawodowe.",
    ),
    "ore_zasoby": Source(
        "ore_zasoby",
        "ORE: zasoby do pracy z uczniami",
        "https://doradztwo.ore.edu.pl/zasoby-pracy-uczniami-klas-7-8-szkoly-podstawowej-oraz-gimnazjum/",
        "Materiały metodyczne o potencjale uczniów, zdolnościach, twórczości i wyborach edukacyjnych.",
    ),
    "uzaleznienia": Source(
        "uzaleznienia",
        "Uzależnienia behawioralne: portal wiedzy i artykułów",
        "https://uzaleznieniabehawioralne.pl/",
        "Artykuły i materiały o zachowaniach ryzykownych, grach, hazardzie, sieci i profilaktyce.",
    ),
    "who_mental": Source(
        "who_mental",
        "WHO: adolescent mental health",
        "https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health",
        "Zwięzłe omówienie zdrowia psychicznego nastolatków, czynników ryzyka i znaczenia wsparcia.",
    ),
    "unicef_teen": Source(
        "unicef_teen",
        "UNICEF: supporting your teen's mental health",
        "https://www.unicef.org/parenting/health/four-things-you-can-do-support-your-teens-mental-health",
        "Praktyczne wskazówki dotyczące słuchania nastolatka, spokojnego konfliktu i wspierania sprawczości.",
    ),
    "unicef_stress": Source(
        "unicef_stress",
        "UNICEF: what is stress?",
        "https://www.unicef.org/parenting/mental-health/what-is-stress",
        "Materiał pomagający zrozumieć stres nastolatków i rolę dorosłych w regulacji napięcia.",
    ),
    "pah_edukacja": Source(
        "pah_edukacja",
        "PAH: edukacja globalna",
        "https://www.pah.org.pl/zaangazuj-sie/edukacjaglobalna/",
        "Materiały i szkolenia o edukacji globalnej, odpowiedzialności, wodzie i kryzysach humanitarnych.",
    ),
    "pah_dla_szkol": Source(
        "pah_dla_szkol",
        "PAH: programy dla szkół",
        "https://www.pah.org.pl/zaangazuj-sie/dla-szkol/",
        "Programy edukacyjne dla szkół, m.in. Lekcje Pomagania i Godziny Wychowawcze ze Światem.",
    ),
    "pah_woda_materialy": Source(
        "pah_woda_materialy",
        "PAH: Światowy Dzień Wody - materiały",
        "https://www.pah.org.pl/akcja-swiatowy-dzien-wody/",
        "Scenariusze, quizy, karty dyskusji i materiały merytoryczne o wodzie.",
    ),
}


LESSON_META = [
    {
        "goal": 1,
        "month": "Wrzesień",
        "title": "Poznajmy się – budujemy zespół klasowy/ Reintegracja klasy – jak odbudować współpracę?",
        "area": "Integracja klasy",
        "must": [
            "Klasa nie staje się zespołem automatycznie; zespół buduje się przez codzienne zachowania.",
            "Każdy uczeń ma prawo do bezpiecznego wejścia w grupę bez ujawniania spraw prywatnych.",
            "Zasady współpracy mają sens tylko wtedy, gdy klasa potrafi do nich wrócić po konflikcie.",
        ],
        "sources": ["men_2026", "zsz5"],
        "video": ("Wspólnie łatwiej. Jak budować dobre relacje w klasie", "https://www.youtube.com/watch?v=Cs3UpXMJ0Ko"),
    },
    {
        "goal": 1,
        "month": "Luty",
        "title": "Komunikacja, która pomaga – jak rozmawiać ze sobą?",
        "area": "Integracja klasy",
        "must": [
            "Mówimy o zachowaniu i skutkach, nie o wartości osoby.",
            "Komunikat pomocny zawiera fakt, skutek, potrzebę i prośbę.",
            "Ostry komentarz często zamyka rozmowę; konkretna prośba daje szansę na zmianę.",
        ],
        "sources": ["men_2026"],
        "video": ("Komunikacja bez przemocy (NVC) - Magdalena Malinowska-Berggren, Joanna Flis", "https://www.youtube.com/watch?v=lYfuhIjcyKs"),
    },
    {
        "goal": 1,
        "month": "Kwiecień",
        "title": "Nasza klasa – jak wspólnie rozwiązywać trudności?",
        "area": "Integracja klasy",
        "must": [
            "Rozwiązanie problemu zaczyna się od oddzielenia faktów od opinii.",
            "Nie każda trudność wymaga szukania winnego; często potrzebny jest mały krok naprawczy.",
            "Jeżeli trudność dotyczy przemocy lub zagrożenia, uruchamiamy pomoc dorosłych.",
        ],
        "sources": ["men_2026", "men_przemoc"],
        "video": ("Konflikt w grupie - fakty i mity", "https://www.youtube.com/watch?v=_cXiIE4Pnr4"),
    },
    {
        "goal": 2,
        "month": "Wrzesień",
        "title": "Moja szkoła, moja społeczność – za co jestem odpowiedzialny?",
        "area": "Odpowiedzialność społeczna",
        "must": [
            "Odpowiedzialność ucznia dotyczy też atmosfery, bezpieczeństwa i przestrzeni szkoły.",
            "Wspólnota szkolna działa wtedy, gdy każdy wykonuje małe obowiązki bez przypominania.",
            "Reagowanie na zagrożenie jest elementem odpowiedzialności, nie donoszeniem.",
        ],
        "sources": ["men_2026", "zsz5"],
        "video": ("Być wychowawcą lub wychowawczynią klasy. Co to tak naprawdę znaczy?", "https://www.youtube.com/watch?v=nF3OOHrpmZo"),
    },
    {
        "goal": 2,
        "month": "Listopad",
        "title": "Odpowiedzialność za bezpieczeństwo swoje i innych",
        "area": "Odpowiedzialność społeczna",
        "must": [
            "Najpierw dbamy o bezpieczeństwo, dopiero później wyjaśniamy szczegóły.",
            "Nie nagrywamy i nie udostępniamy sytuacji zagrożenia.",
            "Uczeń ma prawo i obowiązek wezwać dorosłego, gdy ktoś może ucierpieć.",
        ],
        "sources": ["men_2026", "zsz5", "zpe_pierwsza_pomoc"],
        "video": ("ABC pierwszej pomocy", "https://zpe.gov.pl/a/abc-pierwszej-pomocy/DtLX9npeZ"),
    },
    {
        "goal": 2,
        "month": "Maj",
        "title": "Patriotyzm współczesny – co oznacza dla młodego człowieka?",
        "area": "Odpowiedzialność społeczna",
        "must": [
            "Patriotyzm to nie tylko symbole i święta, ale też odpowiedzialność za wspólnotę.",
            "Szacunek do innych ludzi i języka debaty jest częścią postawy obywatelskiej.",
            "Współczesny patriotyzm można pokazać przez uczciwość, pracę, pomoc i troskę o otoczenie.",
        ],
        "sources": ["men_2026"],
        "video": ("Co to jest patriotyzm?", "https://www.youtube.com/watch?v=rP7IBvMJICc"),
    },
    {
        "goal": 2,
        "month": "Marzec",
        "title": "Wolontariat i działanie dla innych – dlaczego warto pomagać?",
        "area": "Odpowiedzialność społeczna",
        "must": [
            "Pomaganie powinno być konkretne, potrzebne i szanujące godność odbiorcy.",
            "Wolontariat rozwija odpowiedzialność, współpracę i sprawczość.",
            "Dobre działanie społeczne ma cel, opiekuna, granice i bezpieczny sposób wykonania.",
        ],
        "sources": ["men_2026"],
        "video": ("Wolontariusz: kto to taki? | Edukujemy o Wolontariacie", "https://www.youtube.com/watch?v=vzs6bBqVCoE"),
    },
    {
        "goal": 3,
        "month": "Październik",
        "title": "Sen, ruch i odżywianie – fundamenty zdrowia",
        "area": "Edukacja zdrowotna",
        "must": [
            "Sen, ruch i jedzenie wpływają na koncentrację, nastrój, frekwencję i gotowość do nauki.",
            "Nie chodzi o idealny styl życia, tylko o jeden realny nawyk do poprawy.",
            "Nie komentujemy wyglądu ani masy ciała; rozmawiamy o funkcjonowaniu i zdrowiu.",
        ],
        "sources": ["men_2026", "zpe_zdrowie"],
        "video": ("Dlaczego śpimy? Sen jako fundament zdrowia i nauki", "https://www.youtube.com/watch?v=GqZSUajM1Ws"),
    },
    {
        "goal": 3,
        "month": "Listopad",
        "title": "Pierwsza pomoc – wiem, jak reagować",
        "area": "Edukacja zdrowotna",
        "must": [
            "Nie trzeba być ratownikiem, żeby rozpocząć właściwe działanie: zabezpiecz, sprawdź, wezwij pomoc.",
            "W sytuacji zagrożenia nie nagrywamy i nie tłoczymy się wokół poszkodowanego.",
            "Dyspozytor i osoby dorosłe prowadzą działanie; uczeń ma szybko zgłosić problem.",
        ],
        "sources": ["zpe_pierwsza_pomoc", "wosp"],
        "video": ("Film, dzięki któremu możesz uratować komuś życie", "https://www.youtube.com/watch?v=k1KswfV4qwU"),
    },
    {
        "goal": 3,
        "month": "Luty",
        "title": "Stres i regeneracja – jak dbać o swój organizm?",
        "area": "Edukacja zdrowotna",
        "must": [
            "Stres bywa normalną reakcją, ale przeciążenie wymaga reakcji i odpoczynku.",
            "Regeneracja to nie lenistwo; to warunek uczenia się i zdrowia.",
            "Jeżeli stres odbiera sen, jedzenie, bezpieczeństwo lub chęć życia, trzeba powiedzieć dorosłemu.",
        ],
        "sources": ["zpe_zdrowie"],
        "video": ("Jak radzić sobie ze stresem? Warsztaty dla uczniów", "https://www.youtube.com/watch?v=2H3rW60hlbM"),
    },
    {
        "goal": 3,
        "month": "Kwiecień",
        "title": "Odpowiedzialne decyzje prozdrowotne",
        "area": "Edukacja zdrowotna",
        "must": [
            "Decyzje zdrowotne mają skutki krótko- i długoterminowe.",
            "Rozsądna alternatywa jest skuteczniejsza niż samo straszenie konsekwencjami.",
            "W razie problemów zdrowotnych uczeń nie zostaje sam: rodzic, wychowawca, pielęgniarka, lekarz, pedagog lub psycholog.",
        ],
        "sources": ["zpe_zdrowie"],
        "video": ("Zdrowy styl życia #8 [Moje bezpieczeństwo]", "https://www.youtube.com/watch?v=u84AzBAcI10"),
    },
    {
        "goal": 4,
        "month": "Październik",
        "title": "Moje dane w sieci – jak je chronić?",
        "area": "Bezpieczeństwo cyfrowe",
        "must": [
            "Dane osobowe, zdjęcia, lokalizacja i hasła mogą mieć konsekwencje poza Internetem.",
            "Nie publikujemy dokumentów, planu dnia, danych rodziny ani informacji umożliwiających identyfikację.",
            "Ochrona danych to codzienny nawyk, nie tylko formalny przepis.",
        ],
        "sources": ["uodo", "zpe_ai", "nask_dezinformacja"],
        "video": ("CyberBezpieczni - bezpieczeństwo w sieci", "https://www.youtube.com/watch?v=wH92EtBAJzU"),
    },
    {
        "goal": 4,
        "month": "Listopad",
        "title": "Sztuczna inteligencja – korzystam odpowiedzialnie",
        "area": "Bezpieczeństwo cyfrowe",
        "must": [
            "AI może pomagać w uczeniu się, ale nie zastępuje myślenia i odpowiedzialności ucznia.",
            "Do publicznych narzędzi AI nie wpisujemy danych osobowych ani spraw szkolnych innych osób.",
            "Odpowiedzi AI trzeba sprawdzać w źródłach, bo mogą być błędne lub nieaktualne.",
        ],
        "sources": ["zpe_ai", "zpe", "uodo"],
        "video": ("Sztuczna inteligencja a edukacja", "https://www.youtube.com/watch?v=nO2qXnUDfus"),
    },
    {
        "goal": 4,
        "month": "Marzec",
        "title": "Fake news i manipulacja – jak rozpoznać, że ktoś chce mnie wprowadzić w błąd?",
        "area": "Bezpieczeństwo cyfrowe",
        "must": [
            "Silne emocje, presja udostępnienia i brak źródła to sygnały ostrzegawcze.",
            "Przed podaniem dalej sprawdzamy autora, datę, źródło i potwierdzenie w innym miejscu.",
            "Udostępnianie fałszywych treści może szkodzić innym, nawet jeśli robimy to bez złej intencji.",
        ],
        "sources": ["nask_dezinformacja", "zpe"],
        "video": ("PEWNI W SIECI - Dezinformacja i fake newsy", "https://www.youtube.com/watch?v=u3k1Nj2QSIw"),
    },
    {
        "goal": 4,
        "month": "Maj",
        "title": "Aktywność off-line – jak zachować równowagę cyfrową?",
        "area": "Bezpieczeństwo cyfrowe",
        "must": [
            "Telefon jest narzędziem, ale może zabierać sen, uwagę i relacje.",
            "Równowaga cyfrowa nie oznacza zakazu, tylko świadomy wybór czasu i sytuacji.",
            "Aktywność off-line musi być realna dla ucznia, krótka i możliwa do powtórzenia.",
        ],
        "sources": ["zpe_ai", "men_2026"],
        "video": ("10 zasad higieny cyfrowej", "https://www.youtube.com/watch?v=QvylySSkZ8M"),
    },
    {
        "goal": 5,
        "month": "Wrzesień",
        "title": "Jak mówić o swoich potrzebach i trudnościach?",
        "area": "Wsparcie ucznia",
        "must": [
            "Proszenie o pomoc jest umiejętnością, nie słabością.",
            "Trudność można nazwać prosto: mam problem z..., potrzebuję..., proszę o...",
            "Uczeń nie musi opowiadać prywatnych spraw na forum klasy.",
        ],
        "sources": ["men_2026", "zsz5"],
        "video": ("Nonviolent Communication - Marshall Rosenberg (napisy PL)", "https://www.youtube.com/watch?v=Q-Si2l8-jxo"),
    },
    {
        "goal": 5,
        "month": "Listopad",
        "title": "Kto może mi pomóc w szkole?",
        "area": "Wsparcie ucznia",
        "must": [
            "W szkole jest kilka ścieżek pomocy: wychowawca, nauczyciel, pedagog, psycholog, doradca, pielęgniarka, dyrekcja.",
            "Nie każdy problem trzeba rozwiązywać samodzielnie.",
            "W sytuacji zagrożenia zdrowia lub życia pomoc dorosłego jest natychmiastowa.",
        ],
        "sources": ["zsz5", "men_2026"],
        "video": ("Jak budować relacje i wzmacniać uczniów w klasie", "https://www.youtube.com/watch?v=QcmBRziAyRk"),
    },
    {
        "goal": 5,
        "month": "Marzec",
        "title": "Współpraca ucznia, rodzica i szkoły – dlaczego jest ważna?",
        "area": "Wsparcie ucznia",
        "must": [
            "Wsparcie działa lepiej, gdy uczeń, rodzic i szkoła mają wspólne informacje.",
            "Ukrywanie problemu zwykle zwiększa jego koszt.",
            "Rozmowa wspierająca opiera się na faktach, planie i terminie sprawdzenia.",
        ],
        "sources": ["men_2026", "zsz5"],
        "video": ("Jak rodzic może budować relację z nauczycielami?", "https://www.youtube.com/watch?v=MR-uhRVFxG4"),
    },
    {
        "goal": 5,
        "month": "Maj",
        "title": "Moje mocne strony i obszary, w których potrzebuję wsparcia",
        "area": "Wsparcie ucznia",
        "must": [
            "Każdy uczeń ma zasoby, które można nazwać i wykorzystać.",
            "Obszar do rozwoju nie jest etykietą; to informacja, gdzie potrzebny jest plan lub wsparcie.",
            "Nie porównujemy uczniów publicznie.",
        ],
        "sources": ["ore_doradztwo", "ore_filmy"],
        "video": ("Jaki jestem? Oto jest pytanie?", "https://www.youtube.com/watch?v=4gp_EQ7F_bo"),
    },
    {
        "goal": 6,
        "month": "Październik",
        "title": "Przemoc rówieśnicza – jak reagować, gdy ktoś przekracza granice?",
        "area": "Profilaktyka kryzysów",
        "must": [
            "Konflikt i przemoc to nie to samo.",
            "Świadek ma wpływ: nie nagrywa, nie wzmacnia, nie udostępnia, szuka dorosłego.",
            "Przemocy nie rozwiązujemy publicznym zawstydzaniem ani odwetem.",
        ],
        "sources": ["fdds", "men_przemoc"],
        "video": ("Przemoc rówieśnicza online i offline", "https://www.youtube.com/watch?v=UbEoIa1E1-k"),
    },
    {
        "goal": 6,
        "month": "Listopad",
        "title": "Uzależnienia behawioralne – kiedy korzystanie staje się problemem?",
        "area": "Profilaktyka kryzysów",
        "must": [
            "Problem zaczyna się wtedy, gdy tracimy kontrolę i mimo szkód kontynuujemy zachowanie.",
            "Sygnały ryzyka to zaniedbywanie snu, szkoły, relacji, obowiązków i ukrywanie zachowania.",
            "Rozmowa z dorosłym jest sposobem przerwania spirali, nie karą.",
        ],
        "sources": ["zpe_zdrowie", "zpe_ai"],
        "video": ("Higiena cyfrowa, czyli profilaktyka e-uzależnień", "https://www.youtube.com/watch?v=JEGFYp4OVcQ"),
    },
    {
        "goal": 6,
        "month": "Luty",
        "title": "Zdrowie psychiczne – gdzie i jak szukać pomocy?",
        "area": "Profilaktyka kryzysów",
        "must": [
            "Kryzys psychiczny wymaga pomocy tak samo jak uraz fizyczny.",
            "Nie obiecujemy tajemnicy, jeżeli zagrożone jest zdrowie lub życie.",
            "Uczeń może zacząć od jednej osoby dorosłej, której ufa.",
        ],
        "sources": ["zpe_zdrowie", "zsz5"],
        "video": ("Jak rozmawiać z nastolatkiem, żeby chciał słuchać?", "https://www.youtube.com/watch?v=Dh3EGv9Vimc"),
    },
    {
        "goal": 6,
        "month": "Kwiecień",
        "title": "Konflikt bez agresji – jak rozwiązywać trudne sytuacje?",
        "area": "Profilaktyka kryzysów",
        "must": [
            "Celem rozmowy konfliktowej nie jest wygrana, tylko zatrzymanie szkody i ustalenie kolejnego kroku.",
            "Agresja, ironia i publiczne upokarzanie zwykle eskalują problem.",
            "Dobra rozmowa opiera się na faktach, potrzebach i propozycji rozwiązania.",
        ],
        "sources": ["fdds", "men_przemoc"],
        "video": ("Konflikt w grupie - fakty i mity", "https://www.youtube.com/watch?v=_cXiIE4Pnr4"),
    },
    {
        "goal": 7,
        "month": "Październik",
        "title": "Moje mocne strony i przyszły zawód",
        "area": "Doradztwo zawodowe",
        "must": [
            "Mocne strony są punktem wyjścia do wyborów edukacyjno-zawodowych.",
            "W zawodzie liczą się zarówno umiejętności techniczne, jak i postawa.",
            "Uczeń powinien umieć podać dowód swojej mocnej strony.",
        ],
        "sources": ["ore_doradztwo", "ore_filmy", "szkola_mistrzow"],
        "video": ("Drogi Zawodowe - Mocne strony", "https://www.youtube.com/watch?v=DCMlt_8GXLM"),
    },
    {
        "goal": 7,
        "month": "Listopad",
        "title": "Kompetencje, których oczekuje pracodawca",
        "area": "Doradztwo zawodowe",
        "must": [
            "Pracodawca patrzy na umiejętności zawodowe i na zachowania: punktualność, odpowiedzialność, komunikację.",
            "Kompetencje miękkie widać w konkretnych sytuacjach, nie w deklaracjach.",
            "Praktyki są miejscem budowania opinii o sobie.",
        ],
        "sources": ["ore_doradztwo", "ore_filmy", "szkola_mistrzow"],
        "video": ("Czego pracodawcy oczekują od kandydatów do pracy?", "https://www.youtube.com/watch?v=63QVdxPKV-I"),
    },
    {
        "goal": 7,
        "month": "Marzec",
        "title": "Praktyki zawodowe – jak wykorzystać je do budowania swojej przyszłości?",
        "area": "Doradztwo zawodowe",
        "must": [
            "Praktyki są doświadczeniem zawodowym, a nie tylko obowiązkiem do zaliczenia.",
            "Punktualność, pytania i dokumentowanie zadań pomagają budować przyszłe referencje.",
            "Uczeń ma wpływ na to, co wyniesie z praktyk.",
        ],
        "sources": ["ore_doradztwo", "ore_filmy", "szkola_mistrzow"],
        "video": ("Drogi Zawodowe - Pierwsze doświadczenia", "https://www.youtube.com/watch?v=STSlRxKnIyE"),
    },
    {
        "goal": 7,
        "month": "Maj",
        "title": "Jak podejmować świadome decyzje dotyczące swojej kariery?",
        "area": "Doradztwo zawodowe",
        "must": [
            "Decyzja zawodowa wymaga informacji, porównania opcji i rozmowy z osobami kompetentnymi.",
            "Nie ma jednej dobrej ścieżki dla wszystkich.",
            "Pierwszy krok jest ważniejszy niż idealny plan na całe życie.",
        ],
        "sources": ["ore_doradztwo", "ore_filmy", "szkola_mistrzow"],
        "video": ("Drogi Zawodowe - Decyzje", "https://www.youtube.com/watch?v=qefETYPjBs0"),
    },
    {
        "goal": 8,
        "month": "Październik",
        "title": "Ciekawość prowadzi do wiedzy – jak samodzielnie szukać odpowiedzi?",
        "area": "Uczenie się i projekt",
        "must": [
            "Dobre pytanie pomaga znaleźć dobrą odpowiedź.",
            "Nie wystarczy pierwszy wynik z Internetu; trzeba sprawdzić źródło i sens informacji.",
            "Ciekawość można zamienić w mały plan poszukiwania.",
        ],
        "sources": ["zpe", "nask_dezinformacja"],
        "video": ("Wierzyć czy nie? Jak oceniać wiarygodność źródeł informacji w sieci", "https://www.youtube.com/watch?v=K3p-VsXJIFs"),
    },
    {
        "goal": 8,
        "month": "Listopad",
        "title": "Od pomysłu do działania – jak stworzyć dobry projekt?",
        "area": "Uczenie się i projekt",
        "must": [
            "Pomysł staje się projektem dopiero wtedy, gdy ma cel, role, termin i kryterium sukcesu.",
            "Projekt wymaga współpracy, konsultacji i sprawdzania postępu.",
            "Nauczyciel wspiera proces, ale nie wykonuje pracy za uczniów.",
        ],
        "sources": ["projekt"],
        "video": ("Czym jest metoda projektu?", "https://www.youtube.com/watch?v=n78QV3OqnzA"),
    },
    {
        "goal": 8,
        "month": "Marzec",
        "title": "Informacja zwrotna – jak wykorzystać ją do rozwoju?",
        "area": "Uczenie się i projekt",
        "must": [
            "Informacja zwrotna mówi, co działa, co poprawić i jaki jest następny krok.",
            "Feedback dotyczy pracy lub zachowania, nie wartości osoby.",
            "Uczeń korzysta z informacji zwrotnej dopiero wtedy, gdy robi po niej konkretne działanie.",
        ],
        "sources": ["ceo_feedback"],
        "video": ("Informacja zwrotna - trudne narzędzie czy dobra komunikacja", "https://www.youtube.com/watch?v=aTpnPo3EMXI"),
    },
    {
        "goal": 8,
        "month": "Maj",
        "title": "Wiedza nie ma granic – jak łączyć informacje z różnych dziedzin?",
        "area": "Uczenie się i projekt",
        "must": [
            "Realne zadania rzadko należą do jednego przedmiotu.",
            "Wiedza zawodowa, ogólna, cyfrowa i społeczna wzajemnie się uzupełnia.",
            "Łączenie dziedzin pomaga rozwiązywać praktyczne problemy.",
        ],
        "sources": ["zpe", "projekt"],
        "video": ("Edukacja dla przyszłości - dyskusja", "https://www.youtube.com/watch?v=f93q36pGyeA"),
    },
    {
        "goal": 9,
        "month": "Październik",
        "title": "Oszczędzanie energii i wody – co możemy zrobić w szkole i w domu?",
        "area": "Edukacja ekologiczna",
        "must": [
            "Oszczędzanie energii i wody zaczyna się od małych, powtarzalnych zachowań.",
            "Działanie ekologiczne musi być konkretne: kto, co, gdzie i od kiedy.",
            "W szkole szukamy rozwiązań realnych, nie tylko deklaracji.",
        ],
        "sources": ["pah_woda", "zpe_odpady"],
        "video": ("Webinar wprowadzający do akcji Światowy Dzień Wody z PAH", "https://www.youtube.com/watch?v=wPrO9__b00k"),
    },
    {
        "goal": 9,
        "month": "Listopad",
        "title": "Jak codzienne decyzje wpływają na środowisko?",
        "area": "Edukacja ekologiczna",
        "must": [
            "Codzienne decyzje dotyczą odpadów, wody, energii, transportu i zakupów.",
            "Uczeń nie odpowiada za cały problem globalny, ale ma wpływ na swoje nawyki.",
            "Lepsza alternatywa musi być możliwa do wykonania w realnym życiu ucznia.",
        ],
        "sources": ["zpe_odpady", "pah_woda"],
        "video": ("Czy technologia i AI szkodzą środowisku?", "https://www.youtube.com/watch?v=C9FZtXpnanY"),
    },
    {
        "goal": 9,
        "month": "Marzec",
        "title": "Segregacja odpadów w praktyce",
        "area": "Edukacja ekologiczna",
        "must": [
            "Segregacja działa tylko wtedy, gdy odpady trafiają do właściwych pojemników.",
            "Zabrudzone lub źle posegregowane odpady mogą utrudniać recykling.",
            "Najpierw ograniczamy ilość odpadów, a dopiero potem je segregujemy.",
        ],
        "sources": ["zpe_odpady"],
        "video": ("Jak są segregowane odpady? - Fabryki w Polsce", "https://www.youtube.com/watch?v=CwAP97KJTIg"),
    },
    {
        "goal": 9,
        "month": "Maj",
        "title": "Szkoła odpowiedzialna za środowisko",
        "area": "Edukacja ekologiczna",
        "must": [
            "Odpowiedzialność ekologiczna szkoły wymaga małych projektów, które da się wdrożyć i sprawdzić.",
            "Dobry projekt ma opiekuna, zgodę, termin i miernik efektu.",
            "Lepiej zrobić jedno małe działanie niż zapisać dużą deklarację bez wykonania.",
        ],
        "sources": ["zpe_odpady", "projekt"],
        "video": ("O angażowaniu młodych ludzi w akcje na rzecz klimatu i środowiska", "https://www.youtube.com/watch?v=exmwH6-x8g8"),
    },
]


def slugify(value: str) -> str:
    value = value.translate(str.maketrans({
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ż": "z",
        "ź": "z",
        "Ą": "A",
        "Ć": "C",
        "Ę": "E",
        "Ł": "L",
        "Ń": "N",
        "Ó": "O",
        "Ś": "S",
        "Ż": "Z",
        "Ź": "Z",
    }))
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return re.sub(r"-+", "-", ascii_text)


def normalize_title(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"\s*/\s*", "/", value)
    value = re.sub(r"\s+", " ", value)
    return value


SHORT_TITLES = [
    "Integracja i reintegracja klasy",
    "Komunikacja, która pomaga",
    "Wspólne rozwiązywanie trudności",
    "Odpowiedzialność za społeczność szkolną",
    "Bezpieczeństwo swoje i innych",
    "Współczesny patriotyzm",
    "Wolontariat i pomaganie",
    "Sen, ruch i odżywianie",
    "Pierwsza pomoc",
    "Stres i regeneracja",
    "Decyzje prozdrowotne",
    "Dane w sieci",
    "Odpowiedzialne korzystanie z AI",
    "Fake news i manipulacja",
    "Równowaga cyfrowa",
    "Mówienie o potrzebach",
    "Mapa pomocy w szkole",
    "Współpraca uczeń - rodzic - szkoła",
    "Mocne strony i wsparcie",
    "Reagowanie na przemoc rówieśniczą",
    "Uzależnienia behawioralne",
    "Zdrowie psychiczne i pomoc",
    "Konflikt bez agresji",
    "Mocne strony i przyszły zawód",
    "Kompetencje oczekiwane przez pracodawcę",
    "Praktyki zawodowe",
    "Decyzje dotyczące kariery",
    "Samodzielne szukanie odpowiedzi",
    "Dobry projekt",
    "Informacja zwrotna",
    "Łączenie wiedzy z różnych dziedzin",
    "Oszczędzanie energii i wody",
    "Codzienne decyzje a środowisko",
    "Segregacja odpadów",
    "Szkoła odpowiedzialna za środowisko",
]


GOAL_CONTEXT = {
    1: "Ten obszar dotyczy klasy jako środowiska codziennego funkcjonowania, a nie tylko formalnej grupy uczniów. Dla wychowawcy ważne jest uchwycenie, czy uczniowie czują się w klasie widziani, czy potrafią prosić o pomoc i czy mają wspólne, zrozumiałe zasady współpracy.",
    2: "Odpowiedzialność społeczna warto pokazywać przez konkretne zachowania: reagowanie, troskę o wspólną przestrzeń, szacunek do ludzi i gotowość do małego działania. Uczniowie szybciej rozumieją ten cel, gdy widzą związek między postawą obywatelską a zwykłym dniem w szkole.",
    3: "Edukacja zdrowotna nie powinna brzmieć jak lista zakazów. Jej sens polega na tym, żeby uczeń rozumiał wpływ codziennych decyzji na sen, koncentrację, emocje, relacje i bezpieczeństwo oraz umiał wybrać jeden realny krok, który może wykonać bez poczucia zawstydzenia.",
    4: "Bezpieczeństwo cyfrowe wymaga języka bliskiego doświadczeniu uczniów. Wychowawca nie musi znać każdej aplikacji, ale powinien pomóc klasie zobaczyć mechanizmy: ślad cyfrowy, presję reakcji, manipulację, prywatność, odpowiedzialność za publikowanie i granice korzystania z narzędzi AI.",
    5: "Wsparcie ucznia zaczyna się od obniżenia progu proszenia o pomoc. Lekcje z tego obszaru mają pokazać, że trudność można nazwać prosto, bez publicznego zwierzania się, oraz że szkoła ma konkretne osoby i procedury, które pomagają działać bez chaosu.",
    6: "Profilaktyka kryzysów wymaga spokoju i precyzji. Wychowawca powinien oddzielać konflikt od przemocy, trudny nastrój od kryzysu, korzystanie od utraty kontroli oraz reakcję pomocową od karania. Najważniejsze jest uczenie uczniów, kiedy nie wolno zostać samemu z problemem.",
    7: "Doradztwo zawodowe ma sens wtedy, gdy łączy samoocenę ucznia z realnym światem pracy. Nie chodzi o szybkie wskazanie jednego zawodu, ale o uczenie zbierania informacji, nazywania swoich zasobów, rozumienia oczekiwań pracodawcy i wykorzystywania praktyk jako doświadczenia.",
    8: "Uczenie się i projekt warto prowadzić przez pytania, próbowanie i poprawianie. Ten obszar pomaga uczniom widzieć wiedzę jako narzędzie działania: szukają informacji, sprawdzają źródła, planują zadania, korzystają z informacji zwrotnej i łączą różne dziedziny.",
    9: "Edukacja ekologiczna powinna zejść z poziomu ogólnych haseł do poziomu decyzji, procedur i małych wdrożeń. Uczniowie potrzebują zobaczyć, że odpowiedzialność środowiskowa w szkole oznacza konkret: mniej strat, lepszą segregację, oszczędzanie zasobów i sprawdzanie efektu.",
}


GOAL_SHORT_LABELS = {
    1: "Relacje",
    2: "Odpowiedzialność",
    3: "Zdrowie",
    4: "Cyfrowe",
    5: "Wsparcie",
    6: "Kryzysy",
    7: "Kariera",
    8: "Uczenie",
    9: "Ekologia",
}


GOAL_META = {
    1: "Integracja klasy, komunikacja, zasady współpracy i rozwiązywanie codziennych napięć zanim urosną do poważnego problemu.",
    2: "Odpowiedzialność za szkołę i innych ludzi: reagowanie, wolontariat, patriotyzm codzienny i troska o wspólną przestrzeń.",
    3: "Zdrowie rozumiane praktycznie: sen, ruch, stres, pierwsza pomoc, decyzje prozdrowotne i wpływ na koncentrację oraz emocje.",
    4: "Bezpieczne funkcjonowanie w sieci: prywatność, AI, manipulacja informacyjna, higiena cyfrowa i odpowiedzialność za publikowanie.",
    5: "Obniżenie progu proszenia o pomoc: potrzeby ucznia, mapa wsparcia w szkole, współpraca z rodzicami i nazywanie mocnych stron.",
    6: "Spokojne rozpoznawanie sytuacji ryzykownych: przemoc, kryzys psychiczny, uzależnienia behawioralne i konflikt bez agresji.",
    7: "Doradztwo zawodowe połączone z praktyką: zasoby ucznia, kompetencje pracownicze, praktyki i decyzje o dalszej ścieżce.",
    8: "Uczenie się przez działanie: pytania, planowanie projektu, źródła, informacja zwrotna i łączenie wiedzy z różnych dziedzin.",
    9: "Ekologia jako konkretne decyzje szkolne: oszczędzanie zasobów, segregacja, ograniczanie strat i sprawdzanie efektów działań.",
}


LESSON_FOCUS = [
    "W tej lekcji kluczowe jest stworzenie klasy, w której uczniowie mogą wejść w rozmowę bez presji odsłaniania prywatnych spraw. Wychowawca powinien obserwować, kto łatwo zabiera głos, kto zostaje na marginesie i jakie zachowania klasa sama uznaje za wspierające lub utrudniające współpracę.",
    "Komunikację warto pokazać jako umiejętność, której można się nauczyć, a nie jako cechę charakteru. Najważniejsze jest przesunięcie rozmowy z etykietowania osoby na opis faktu, skutku, potrzeby i prośby.",
    "Rozwiązywanie trudności w klasie nie powinno zaczynać się od szukania winnego. Wychowawca pomaga klasie nazwać fakty, ustalić realny wpływ problemu na codzienność i wybrać jeden mały krok, który można sprawdzić po określonym czasie.",
    "Odpowiedzialność za społeczność szkolną warto odczarować jako coś większego niż dyżury i regulaminy. Chodzi o zauważanie skutków własnych zachowań dla innych: hałasu, spóźnień, obojętności, komentarzy, dbania o przestrzeń i reagowania, gdy komuś dzieje się krzywda.",
    "Bezpieczeństwo swoje i innych wymaga szybkiego rozpoznawania sytuacji, których uczeń nie powinien rozwiązywać sam. Lekcja ma wzmocnić prosty odruch: zatrzymaj ryzykowne zachowanie, nie nagrywaj, wezwij dorosłego, pomóż bez dokładania chaosu.",
    "Patriotyzm współczesny dobrze wybrzmiewa wtedy, gdy nie zostaje zamknięty w akademiach i symbolach. Warto pokazać go jako odpowiedzialność za język, pracę, uczciwość, lokalną wspólnotę i sposób traktowania ludzi, z którymi się nie zgadzamy.",
    "Wolontariat nie jest tylko spontanicznym pomaganiem. Nauczyciel powinien pokazać, że dobre działanie społeczne ma odbiorcę, cel, granice, opiekuna i sprawdzalny efekt, a pomaganie bez słuchania potrzeb może być nieskuteczne.",
    "Rozmowa o śnie, ruchu i odżywianiu łatwo może wejść w ocenianie wyglądu lub stylu życia. Trzeba trzymać ją przy funkcjonowaniu: energii, koncentracji, nastroju, regeneracji i jednym nawyku, który uczeń może realnie zmienić.",
    "Pierwsza pomoc na lekcji wychowawczej ma zbudować gotowość do reakcji, nie zastępować szkolenia ratowniczego. Uczeń powinien wiedzieć, że najważniejsze są bezpieczeństwo miejsca, wezwanie pomocy i nierobienie rzeczy, które pogarszają sytuację.",
    "Stres warto omawiać bez straszenia i bez banalizowania. Uczniowie potrzebują zrozumieć różnicę między mobilizacją a przeciążeniem oraz rozpoznać sygnały, przy których odpoczynek, rozmowa i pomoc dorosłego są konieczne.",
    "Decyzje prozdrowotne są dobrym tematem do uczenia przewidywania skutków. Wychowawca prowadzi uczniów od pytania „co chcę teraz?” do pytania „co mi to zrobi za tydzień, miesiąc, rok i kto może mi pomóc wybrać rozsądniej?”.",
    "Dane w sieci trzeba pokazać konkretnie: zdjęcie, lokalizacja, plan dnia, dokument, hasło, informacja o rodzinie. Uczeń powinien zobaczyć, że prywatność nie jest abstrakcyjnym przepisem, tylko ochroną realnych osób i relacji.",
    "AI najlepiej omawiać jako narzędzie, które może pomagać, ale wymaga kontroli użytkownika. Najważniejsze jest rozróżnienie: można użyć do pomysłu, treningu i porządkowania myśli, ale nie wolno oddawać odpowiedzialności ani danych innych osób.",
    "Fake news i manipulacja działają często przez emocje, pośpiech i pozór autorytetu. Wychowawca powinien pomóc uczniom zatrzymać automatyczne udostępnianie i przećwiczyć proste pytania: kto mówi, skąd to wie, kiedy to powstało, kto jeszcze to potwierdza.",
    "Równowaga cyfrowa nie oznacza moralizowania o telefonach. Chodzi o zauważenie, kiedy ekran zaczyna wypierać sen, ruch, rozmowę, koncentrację i odpoczynek, oraz o zaplanowanie małego, wykonalnego eksperymentu offline.",
    "Mówienie o potrzebach warto ćwiczyć w bezpiecznych, fikcyjnych sytuacjach. Uczeń nie ma obowiązku ujawniać prywatnej historii, ale powinien poznać prosty schemat komunikatu, który można wykorzystać w rozmowie z dorosłym.",
    "Mapa pomocy w szkole powinna być maksymalnie konkretna. Uczniowie mają wiedzieć, do kogo iść z problemem edukacyjnym, emocjonalnym, zdrowotnym, przemocowym lub organizacyjnym oraz kiedy sprawa wymaga natychmiastowej reakcji.",
    "Współpraca ucznia, rodzica i szkoły często zaczyna się dopiero w kryzysie. Ta lekcja ma pokazać, że wcześniejsza rozmowa oparta na faktach i planie zmniejsza napięcie, porządkuje odpowiedzialność i daje uczniowi większe poczucie wpływu.",
    "Mocne strony trzeba odróżnić od pochwał ogólnych. Uczeń powinien nauczyć się podawać dowód: sytuację, zachowanie, efekt. Równie ważne jest nazwanie obszaru wsparcia bez robienia z niego etykiety.",
    "Przemoc rówieśnicza wymaga jasnych granic językowych. Wychowawca powinien pokazać różnicę między konfliktem a przemocą oraz szczególnie mocno omówić rolę świadka, bo to świadkowie często wzmacniają albo zatrzymują krzywdzenie.",
    "Uzależnienia behawioralne warto omawiać przez utratę kontroli i koszty, a nie przez demonizowanie gier czy telefonu. Uczniowie powinni rozpoznawać sygnały: zaniedbywanie snu, szkoły, relacji, ukrywanie zachowania i kontynuowanie mimo szkód.",
    "Zdrowie psychiczne trzeba przedstawić jako część zdrowia, a nie temat wstydliwy. Najważniejsze jest pokazanie, że kryzys nie musi być rozwiązywany na forum klasy, ale nie wolno zostawać z nim samemu, gdy pojawia się zagrożenie.",
    "Konflikt bez agresji wymaga zatrzymania eskalacji i powrotu do faktów. Nauczyciel pomaga uczniom zobaczyć, że celem rozmowy nie jest publiczne zwycięstwo, tylko ograniczenie szkody i ustalenie następnego kroku.",
    "Mocne strony w kontekście zawodu powinny być połączone z przykładami działania. Uczeń ma zobaczyć, że punktualność, dokładność, komunikacja, ciekawość techniczna czy odporność na stres mają znaczenie dopiero wtedy, gdy widać je w praktyce.",
    "Kompetencje pracownicze warto omawiać przez konkretne sytuacje z praktyk i pracy, nie przez listę cech. Pracodawca ocenia nie tylko wiedzę zawodową, lecz także komunikację, odpowiedzialność, uczenie się na błędach i stosunek do zespołu.",
    "Praktyki zawodowe są pierwszym miejscem budowania reputacji zawodowej. Uczeń powinien rozumieć, że pytania, punktualność, dokumentowanie zadań i kultura komunikacji mogą później zamienić się w referencje lub realną ofertę pracy.",
    "Decyzje dotyczące kariery rzadko są jednorazowe. Warto uczyć uczniów porównywania opcji, zbierania informacji, rozmowy z praktykami i przyjmowania, że pierwsza decyzja może być krokiem, a nie wyrokiem na całe życie.",
    "Samodzielne szukanie odpowiedzi to nie tylko użycie wyszukiwarki. Uczeń powinien nauczyć się formułować pytanie, rozpoznawać dobre źródło, notować wnioski i sprawdzać, czy odpowiedź rzeczywiście pasuje do problemu.",
    "Dobry projekt zaczyna się od celu i odbiorcy. Wychowawca powinien pilnować, żeby uczniowie nie zostali na poziomie hasła, lecz określili role, termin, zasoby, kryterium sukcesu i sposób sprawdzenia efektu.",
    "Informacja zwrotna ma rozwijać, a nie tylko oceniać. Uczniowie powinni zobaczyć różnicę między komentarzem, który rani albo zamyka, a informacją, która wskazuje mocną stronę, konkretną poprawkę i następny krok.",
    "Łączenie wiedzy z różnych dziedzin warto pokazać przez realny problem, np. zadanie zawodowe, projekt ekologiczny albo analizę informacji. Uczniowie mają zobaczyć, że matematyka, język, technologia i kompetencje społeczne pracują razem.",
    "Oszczędzanie energii i wody powinno zejść do poziomu zachowań w klasie, warsztacie, domu i internacie. Najlepiej działa pytanie: gdzie tracimy zasób, kto ma wpływ i jak sprawdzimy, czy coś się zmieniło.",
    "Codzienne decyzje środowiskowe warto omawiać bez przerzucania na uczniów odpowiedzialności za cały kryzys klimatyczny. Chodzi o rozumienie wpływu i wybór alternatywy możliwej do wykonania w ich realnym życiu.",
    "Segregacja odpadów jest praktyką, która wymaga znajomości lokalnych zasad i konsekwencji błędów. Uczniowie powinni zrozumieć, że recykling zaczyna się od ograniczenia odpadów, a dopiero potem od właściwego pojemnika.",
    "Szkoła odpowiedzialna za środowisko to nie deklaracja w gablocie, tylko mały projekt z opiekunem, terminem i miernikiem efektu. Wychowawca pomaga klasie wybrać działanie, które da się wdrożyć, sprawdzić i utrzymać.",
]


VIDEO_NOTES = [
    "Materiał pomaga wejść w temat relacji i pokazuje, że klasa potrzebuje świadomie budowanych zasad, nie tylko formalnego bycia razem. Warto obejrzeć go pod kątem jednego przykładu do rozmowy o atmosferze w grupie.",
    "Rozmowa o NVC porządkuje różnicę między oceną, faktem, potrzebą i prośbą. Nauczyciel może potraktować ją jako dorosłe tło do przygotowania prostych komunikatów, które uczniowie przećwiczą w klasie.",
    "Materiał porządkuje myślenie o konflikcie i pomaga nie mylić trudności grupowej z szukaniem winnego. Przyda się do przygotowania pytań o fakty, emocje i możliwe kroki naprawcze.",
    "Rozmowa o roli wychowawcy pomaga spojrzeć na klasę jak na społeczność, którą trzeba prowadzić przez relacje, zasady i odpowiedzialność. Warto wybrać z niej jeden przykład codziennego zachowania dorosłego, które wzmacnia kulturę klasy.",
    "Materiał o pierwszej pomocy pokazuje prosty schemat reakcji w sytuacji zagrożenia. Dobrze obejrzeć go przed lekcją, żeby mówić uczniom krótko: zabezpiecz, sprawdź, wezwij pomoc.",
    "Film pomaga odsunąć temat patriotyzmu od samej symboliki i rozpocząć rozmowę o postawie obywatelskiej. Warto wykorzystać go jako pretekst do pytania, jak wygląda odpowiedzialność za wspólnotę dziś.",
    "Materiał pokazuje wolontariat jako odpowiedzialne działanie, a nie tylko dobry gest. Nauczyciel może wyciągnąć z niego pytania o motywację, granice pomocy, rolę organizatora i realny skutek dla odbiorcy.",
    "Film daje dorosły kontekst do rozmowy o śnie jako warunku koncentracji, uczenia się i nastroju. Warto użyć go do przełożenia tematu zdrowia na jeden konkretny nawyk, który uczeń może sprawdzić w tygodniu.",
    "Materiał wzmacnia najważniejszy komunikat: uczeń nie musi być ratownikiem, żeby rozpocząć właściwe działanie. Warto obejrzeć go pod kątem spokojnego języka instrukcji.",
    "Warsztatowy materiał pomaga pokazać stres jako reakcję organizmu, którą można zauważać i regulować. Nauczyciel może wykorzystać go do rozmowy o sygnałach przeciążenia i prostych sposobach regeneracji.",
    "Wideolekcja porządkuje podstawowe elementy zdrowego stylu życia bez wchodzenia w ocenianie wyglądu. Warto obejrzeć ją pod kątem decyzji zdrowotnych, które mają skutek dla energii, frekwencji i nauki.",
    "Film może posłużyć jako wprowadzenie do rozmowy o podstawowych zasadach cyberbezpieczeństwa. Najważniejsze jest wyłapanie prostych zachowań chroniących dane i prywatność.",
    "Materiał pomaga zrozumieć, że AI jest narzędziem wymagającym kontroli, źródeł i odpowiedzialności. Warto obejrzeć go pod kątem przykładów, kiedy AI pomaga, a kiedy może zaszkodzić.",
    "Odcinek o dezinformacji pokazuje, jak łatwo treść w sieci może wpływać na emocje i decyzje. Nauczyciel może przygotować na jego podstawie prosty filtr: źródło, data, autor, dowód, emocja.",
    "Film o higienie cyfrowej pomaga przenieść rozmowę z zakazów na równowagę i samoregulację. Dobry do przygotowania krótkiego eksperymentu offline dla uczniów.",
    "Wystąpienie Rosenberga pokazuje porozumienie bez przemocy w wersji źródłowej i dorosłej. Nauczyciel może przełożyć je na szkolny schemat: co się stało, co czuję, czego potrzebuję, o co proszę.",
    "Film można potraktować jako inspirację do myślenia o relacji uczeń-dorosły. Warto wyłapać przykłady zachowań nauczyciela, które obniżają próg proszenia o pomoc.",
    "Materiał pomaga przygotować rozmowę o tym, że rodzic i szkoła nie są przeciwnymi stronami. Warto wykorzystać go do nazwania roli faktów, planu i spokojnego kontaktu.",
    "Film z cyklu doradczego pomaga uczniom myśleć o sobie przez pytania i obserwację, a nie przez etykiety. Nauczyciel może wykorzystać go do rozmowy o mocnych stronach i wsparciu.",
    "Materiał o przemocy online i offline pomaga rozdzielić konflikt, żart i krzywdzenie. Warto obejrzeć go szczególnie pod kątem roli świadka i reakcji dorosłych.",
    "Film o higienie cyfrowej i e-uzależnieniach porządkuje temat utraty kontroli. Nauczyciel może wyłapać sygnały ryzyka, które uczniowie łatwo rozpoznają w codzienności.",
    "Materiał pomaga przygotować spokojny język rozmowy z nastolatkiem w trudnościach. Warto obejrzeć go pod kątem tego, jak słuchać bez natychmiastowego oceniania.",
    "Film o konflikcie w grupie pozwala zobaczyć, że nie każda trudność wymaga eskalacji. Nauczyciel może z niego wziąć przykłady pytań, które zatrzymują agresję.",
    "Film z cyklu ORE pomaga mówić o mocnych stronach jako o zasobach zawodowych. Warto obejrzeć go przed lekcją, żeby przygotować pytania o dowody i przykłady działań.",
    "Webinar pokazuje oczekiwania pracodawców wobec kandydatów i pozwala zejść z ogólników o kompetencjach miękkich do konkretnych zachowań: punktualności, komunikacji, odpowiedzialności i uczenia się.",
    "Film z cyklu ORE o pierwszych doświadczeniach zawodowych pomaga pokazać praktyki jako element budowania reputacji. Warto wykorzystać go do rozmowy o postawie w miejscu pracy.",
    "Film ORE pomaga nauczycielowi rozmawiać o decyzjach bez presji idealnego wyboru. Przygotowuje do pytań o opcje, informacje, konsekwencje i pierwszy możliwy krok.",
    "Materiał o wiarygodności źródeł pomaga pokazać uczniom, że dobre szukanie odpowiedzi wymaga sprawdzenia autora, kontekstu i potwierdzenia. Warto przed lekcją przygotować jeden przykład do wspólnej oceny.",
    "Krótka rozmowa o metodzie projektu pomaga uporządkować różnicę między pomysłem a projektem. Nauczyciel może wykorzystać ją do nazwania celu, ról, terminu, produktu i kryterium sukcesu.",
    "Wystąpienie CEO pokazuje informację zwrotną jako narzędzie komunikacji i rozwoju, a nie oceniania osoby. Nauczyciel może przygotować jeden model zdania: mocna strona, wskazówka, następny krok.",
    "Dyskusja o edukacji przyszłości pomaga zobaczyć, że realne problemy łączą wiedzę, technologię, komunikację i odpowiedzialność. Warto użyć jej do przygotowania przykładu zadania wymagającego kilku typów wiedzy.",
    "Webinar PAH daje nauczycielowi dojrzalszy kontekst do rozmowy o wodzie: zasoby, odpowiedzialność i globalne zależności. Z materiału warto wybrać jeden przykład, który da się przełożyć na szkołę lub dom.",
    "Rozmowa o środowiskowym koszcie technologii pozwala połączyć codzienne decyzje cyfrowe z odpowiedzialnością ekologiczną. Warto potraktować ją jako punkt wyjścia do pytania, gdzie technologia pomaga, a gdzie generuje koszt.",
    "Reportaż z sortowni pokazuje praktyczny sens segregacji i to, co dzieje się z odpadami po wyrzuceniu. Przyda się do ćwiczenia z typowymi błędami oraz rozmowy o ograniczaniu odpadów u źródła.",
    "Materiał CEO pokazuje, jak angażować młodych ludzi w realne działania klimatyczne i środowiskowe. Warto poszukać w nim inspiracji do małego projektu klasowego z terminem, opiekunem i miernikiem efektu.",
]


OPENING_QUESTIONS = [
    "Co sprawia, że w klasie łatwiej jest się uczyć i być sobą?",
    "Jaki komunikat od drugiej osoby pomaga wam współpracować, a jaki od razu zamyka rozmowę?",
    "Z jaką trudnością klasową da się coś zrobić bez szukania winnego?",
    "Po czym poznajemy, że uczeń naprawdę dba o społeczność szkoły?",
    "W jakiej sytuacji w szkole nie wolno udawać, że nic się nie dzieje?",
    "Jak można pokazać odpowiedzialność za Polskę i lokalną wspólnotę bez wielkich słów?",
    "Kiedy pomaganie jest naprawdę pomocą, a kiedy tylko dobrym gestem bez efektu?",
    "Który nawyk najbardziej wpływa na waszą energię w szkole: sen, ruch czy jedzenie?",
    "Co jest pierwszą rzeczą, którą powinien zrobić świadek sytuacji zagrożenia?",
    "Po czym poznajecie, że stres jeszcze mobilizuje, a kiedy zaczyna przeciążać?",
    "Jaką decyzję zdrowotną łatwo podjąć dziś, ale jej skutki widać dopiero później?",
    "Jakiej jednej informacji o sobie nie chcielibyście zobaczyć publicznie w internecie?",
    "Kiedy AI pomaga się uczyć, a kiedy zaczyna wykonywać pracę za ucznia?",
    "Co powinno zapalić lampkę ostrzegawczą, zanim udostępnimy informację dalej?",
    "Co tracimy jako pierwsze, kiedy telefon zabiera nam za dużo czasu?",
    "Jak można powiedzieć dorosłemu o trudności, nie opowiadając wszystkiego na forum klasy?",
    "Do kogo w szkole poszlibyście z problemem, którego nie da się rozwiązać samemu?",
    "Co pomaga uczniowi, rodzicowi i szkole rozmawiać o problemie bez wzajemnego oskarżania?",
    "Po czym poznajemy mocną stronę: po deklaracji czy po konkretnym zachowaniu?",
    "Czym różni się konflikt od przemocy?",
    "Kiedy korzystanie z telefonu, gry albo internetu przestaje być zwykłą rozrywką?",
    "Jaki sygnał mówi, że z trudnością psychiczną nie powinno się zostawać samemu?",
    "Co w konflikcie najczęściej dolewa oliwy do ognia, a co pomaga go zatrzymać?",
    "Która wasza mocna strona może mieć znaczenie w przyszłej pracy?",
    "Jakie zachowanie na praktykach może zrobić lepsze wrażenie niż sama deklaracja umiejętności?",
    "Co można zrobić na praktykach, żeby po ich zakończeniu mieć realny dowód doświadczenia?",
    "Jaką informację trzeba zdobyć, zanim podejmie się decyzję o dalszej nauce albo pracy?",
    "Od jakiego pytania zaczyna się dobre szukanie odpowiedzi?",
    "Po czym poznać, że pomysł stał się już projektem?",
    "Jaka informacja zwrotna naprawdę pomaga coś poprawić?",
    "Jaki szkolny albo zawodowy problem wymaga wiedzy z więcej niż jednego przedmiotu?",
    "Gdzie w szkole albo w domu najłatwiej marnujemy wodę lub energię?",
    "Która codzienna decyzja ma mały koszt dla nas, ale dobry skutek dla środowiska?",
    "Jaki błąd w segregacji odpadów widzicie najczęściej?",
    "Jakie jedno działanie ekologiczne szkoła mogłaby realnie wdrożyć i sprawdzić po miesiącu?",
]


AREA_SOURCE_KEYS = {
    "Integracja klasy": ["szkola_z_klasa_razem", "szkola_z_klasa_materialy", "szkola_z_klasa_odpornosc"],
    "Odpowiedzialność społeczna": ["szkola_z_klasa_materialy", "szkola_z_klasa_razem"],
    "Edukacja zdrowotna": ["zpe_zdrowie", "szkola_z_klasa_odpornosc", "unicef_stress"],
    "Bezpieczeństwo cyfrowe": ["saferinternet", "saferinternet_dobrostan", "nask_cyberprofilaktyka"],
    "Wsparcie ucznia": ["szkola_z_klasa_odpornosc", "unicef_teen", "zsz5"],
    "Profilaktyka kryzysów": ["fdds_przemoc_scenariusz", "fdds_ramie", "who_mental"],
    "Doradztwo zawodowe": ["ore_doradztwo", "ore_doradcy_2023", "ore_zasoby", "szkola_mistrzow"],
    "Uczenie się i projekt": ["ceo_project_pdf", "ceo_feedback_blog", "zpe"],
    "Edukacja ekologiczna": ["pah_edukacja", "pah_dla_szkol", "pah_woda_materialy", "zpe_odpady"],
}


MONTH_ORDER = ["Wrzesień", "Październik", "Listopad", "Luty", "Marzec", "Kwiecień", "Maj"]


LESSON_EXTRA_SOURCE_KEYS = {
    3: ["fdds_przemoc_scenariusz"],
    5: ["zpe_pierwsza_pomoc", "wosp"],
    7: ["pah_dla_szkol", "pah_edukacja"],
    9: ["zpe_pierwsza_pomoc", "wosp"],
    12: ["uodo", "nask_cyberprofilaktyka"],
    13: ["zpe_ai", "uodo"],
    14: ["nask_kurs_dezinformacja", "nask_dezinformacja"],
    15: ["saferinternet_dobrostan", "uzaleznienia"],
    20: ["men_przemoc", "fdds_przemoc_scenariusz", "fdds_ramie"],
    21: ["uzaleznienia", "saferinternet_dobrostan"],
    22: ["who_mental", "unicef_teen", "szkola_z_klasa_odpornosc"],
    23: ["fdds_przemoc_scenariusz", "szkola_z_klasa_odpornosc"],
    29: ["ceo_project_pdf"],
    30: ["ceo_feedback", "ceo_feedback_blog"],
    32: ["pah_woda", "pah_woda_materialy"],
}


def clean_inline_markdown(value: str) -> str:
    return re.sub(r"`([^`]+)`", r"„\1”", value)


def esc(value: str) -> str:
    return html.escape(clean_inline_markdown(value), quote=True)


def paragraph(text: str) -> str:
    return f"<p>{esc(text)}</p>"


def list_html(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul>"


def tidy_html(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


def prep_items(lesson: dict) -> list[str]:
    return [
        "Przeczytaj „Szczegółowy opis dla nauczyciela” i zaznacz jeden przykład, którym otworzysz rozmowę z klasą.",
        f"Przygotuj pytanie startowe: „{lesson['opening_question']}”. Nie zamieniaj go na ogólne pytanie o temat.",
        "Przy tematach wrażliwych pracuj na przykładach fikcyjnych; nie proś uczniów o prywatne zwierzenia na forum.",
        f"Ustal, jak zapiszesz efekt lekcji: {lesson['evidence']}",
    ]


def unique_keys(keys: list[str]) -> list[str]:
    seen = set()
    result = []
    for key in keys:
        if key in seen:
            continue
        seen.add(key)
        result.append(key)
    return result


def source_keys_for_lesson(idx: int, item: dict) -> list[str]:
    base = [key for key in item["sources"] if key != "men_2026"]
    area = AREA_SOURCE_KEYS.get(item["area"], [])
    extra = LESSON_EXTRA_SOURCE_KEYS.get(idx, [])
    return unique_keys([*base, *area, *extra])[:6]


def teacher_context_html(lesson: dict) -> str:
    lesson_idx = int(lesson["id"]) - 1
    paragraphs = [
        GOAL_CONTEXT[lesson["goal"]],
        LESSON_FOCUS[lesson_idx],
        lesson["flow"],
    ]
    return "".join(paragraph(text) for text in paragraphs)


def source_links_html(sources: list[dict]) -> str:
    return "".join(
        f'<li><a href="{esc(source["url"])}">{esc(source["name"])}</a><span>{esc(source["note"])}</span></li>'
        for source in sources
    )


def lesson_count_label(count: int) -> str:
    if count == 1:
        return "1 lekcja"
    if 2 <= count % 10 <= 4 and not 12 <= count % 100 <= 14:
        return f"{count} lekcje"
    return f"{count} lekcji"


def schedule_html(lesson: dict) -> str:
    rows = [
        ("0-3 min", "Start", f"Zadaj pytanie otwierające: „{lesson['opening_question']}”. Zbierz 2-3 szybkie odpowiedzi bez oceniania."),
        ("3-8 min", "Kontekst", lesson["must_be_said"][0]),
        ("8-20 min", "Ćwiczenie główne", lesson["activity"]),
        ("20-26 min", "Omówienie", "Nazwij wnioski klasy i połącz je z codziennym funkcjonowaniem w szkole."),
        ("26-30 min", "Domknięcie", f"Uczniowie zapisują wniosek lub produkt pracy. Dowód realizacji: {lesson['evidence']}"),
    ]
    body = "".join(
        f"<tr><td>{esc(time)}</td><td>{esc(segment)}</td><td>{esc(action)}</td></tr>"
        for time, segment, action in rows
    )
    return f"<table class=\"schedule\"><thead><tr><th>Czas</th><th>Segment</th><th>Działanie nauczyciela i klasy</th></tr></thead><tbody>{body}</tbody></table>"


def parse_analysis() -> dict[str, dict[str, str]]:
    raw = ANALYSIS.read_text(encoding="utf-8")
    pattern = re.compile(r"^###\s+\d+\.\s+(?P<title>.+?)\n(?P<body>.*?)(?=^###\s+\d+\.|\Z)", re.S | re.M)
    lessons: dict[str, dict[str, str]] = {}
    for match in pattern.finditer(raw):
        title = match.group("title").strip()
        body = match.group("body")
        fields: dict[str, str] = {}
        for label in ["Sens tematu", "Rezultaty", "Przebieg", "Ćwiczenie", "Dowód realizacji", "Uwaga"]:
            field_re = re.compile(rf"\*\*{re.escape(label)}:\*\*\s*(.*?)(?=\n\n\*\*|\Z)", re.S)
            field_match = field_re.search(body)
            fields[label] = " ".join(field_match.group(1).strip().split()) if field_match else ""
        lessons[title] = fields
    return lessons


def validate_against_docx(expected_titles: list[str]) -> None:
    try:
        from docx import Document
    except Exception:
        return
    if not DOCX_SOURCE.exists():
        return
    doc = Document(DOCX_SOURCE)
    found = []
    for table in doc.tables:
        for row in table.rows[1:]:
            title = row.cells[0].text.strip().replace("\n", " ")
            if title:
                found.append(title)
    if found != expected_titles:
        missing = [item for item in found if item not in expected_titles]
        extra = [item for item in expected_titles if item not in found]
        raise RuntimeError(f"Topic mismatch with DOCX. Missing={missing!r}; extra={extra!r}")


def build_lessons() -> list[dict]:
    analysis = parse_analysis()
    analysis_by_normalized = {normalize_title(title): fields for title, fields in analysis.items()}
    expected_titles = [item["title"] for item in LESSON_META]
    if len(OPENING_QUESTIONS) != len(LESSON_META):
        raise RuntimeError("OPENING_QUESTIONS must contain one question per lesson")
    if len(VIDEO_NOTES) != len(LESSON_META):
        raise RuntimeError("VIDEO_NOTES must contain one note per lesson")
    validate_against_docx(expected_titles)
    lessons = []
    for idx, item in enumerate(LESSON_META, 1):
        title = item["title"]
        fields = analysis.get(title) or analysis_by_normalized.get(normalize_title(title))
        if not fields:
            raise RuntimeError(f"Missing analysis section for: {title}")
        slug = f"{idx:02d}"
        source_keys = source_keys_for_lesson(idx, item)
        lessons.append(
            {
                "id": f"{idx:02d}",
                "slug": slug,
                "url": f"lekcje/{slug}.html",
                "title": title,
                "display_title": SHORT_TITLES[idx - 1],
                "goal": item["goal"],
                "month": item["month"],
                "area": item["area"],
                "duration": "30 minut",
                "opening_question": OPENING_QUESTIONS[idx - 1],
                "purpose": fields["Sens tematu"],
                "outcomes": [part.strip() for part in re.split(r"\s+oraz\s+|\s+i\s+", fields["Rezultaty"], maxsplit=1) if part.strip()],
                "results_text": fields["Rezultaty"],
                "flow": fields["Przebieg"],
                "activity": fields["Ćwiczenie"],
                "evidence": fields["Dowód realizacji"],
                "safety": fields["Uwaga"],
                "must_be_said": item["must"],
                "source_keys": source_keys,
                "sources": [SOURCES[key].__dict__ for key in source_keys],
                "teacher_video": {"title": item["video"][0], "url": item["video"][1], "note": VIDEO_NOTES[idx - 1]},
            }
        )
    return lessons


def page_shell(title: str, body: str, rel_prefix: str = "") -> str:
    return tidy_html(f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="{rel_prefix}styles.css">
</head>
<body>
{body}
</body>
</html>
""")


def brand_html(rel_prefix: str = "", variant: str = "compact") -> str:
    variant_class = "brand-strip-full" if variant == "full" else "brand-strip-compact"
    return f"""
    <div class="brand-strip {variant_class}">
      <img class="brand-logo-full" src="{rel_prefix}assets/{LOGO_FULL_FILE}" alt="Zespół Szkół Zawodowych nr 5 we Wrocławiu - Szkoła Mistrzów" width="1931" height="301">
      <img class="brand-logo-mark" src="{rel_prefix}assets/{LOGO_FILE}" alt="Logo ZSZ5 we Wrocławiu" width="437" height="298">
      <div class="brand-text">
        <strong>Szkoła Mistrzów</strong>
        <span>Zespół Szkół Zawodowych nr 5 we Wrocławiu</span>
      </div>
    </div>
"""


def render_lesson(lesson: dict, prev_lesson: dict | None, next_lesson: dict | None) -> str:
    source_links = source_links_html(lesson["sources"])
    nav_prev = f'<a class="nav-link" href="{esc(prev_lesson["slug"])}.html">Poprzednia lekcja</a>' if prev_lesson else ""
    nav_next = f'<a class="nav-link" href="{esc(next_lesson["slug"])}.html">Następna lekcja</a>' if next_lesson else ""
    body = f"""
  <header class="site-header compact lesson-header">
    <div class="lesson-header-inner">
      <div class="lesson-topbar">
        {brand_html("../")}
        <a class="back-link" href="../index.html">← Wróć do planu</a>
      </div>
      <p class="kicker">Cel {lesson["goal"]} · {esc(lesson["area"])} · {esc(lesson["month"])}</p>
      <h1>{esc(lesson["display_title"])}</h1>
      <p class="subtitle"><strong>Temat z planu:</strong> {esc(lesson["title"])}</p>
      <p class="subtitle">Materiał dla wychowawcy: kontekst tematu, konkretne pytanie startowe, przebieg rozmowy, ćwiczenie i komunikaty, które trzeba powiedzieć uczniom wprost.</p>
    </div>
  </header>
  <main class="lesson-layout">
    <aside class="lesson-aside">
      <div class="aside-card">
        <strong>Czas</strong>
        <span>{esc(lesson["duration"])}</span>
      </div>
      <div class="aside-card">
        <strong>Dowód realizacji</strong>
        <span>{esc(lesson["evidence"])}</span>
      </div>
      <div class="aside-card video-card">
        <strong>Film dla nauczyciela</strong>
        <span>{esc(lesson["teacher_video"]["note"])}</span>
        <a class="resource-link" href="{esc(lesson["teacher_video"]["url"])}" target="_blank" rel="noopener noreferrer">Otwórz w nowej karcie: {esc(lesson["teacher_video"]["title"])}</a>
      </div>
      <div class="aside-card resource-card">
        <strong>Do pogłębienia tematu</strong>
        <ul class="compact-source-list">{source_links}</ul>
      </div>
    </aside>
    <article class="lesson-content">
      <section>
        <h2>Po co ta lekcja</h2>
        {paragraph(lesson["purpose"])}
      </section>
      <section>
        <h2>Przewidywane rezultaty</h2>
        {paragraph(lesson["results_text"])}
      </section>
      <section>
        <h2>Przygotowanie nauczyciela</h2>
        {list_html(prep_items(lesson))}
      </section>
      <section class="must">
        <h2>Co musi wybrzmieć</h2>
        {list_html(lesson["must_be_said"])}
      </section>
      <section>
        <h2>Przebieg 30 minut</h2>
        {schedule_html(lesson)}
      </section>
      <section>
        <h2>Szczegółowy opis dla nauczyciela</h2>
        {teacher_context_html(lesson)}
      </section>
      <section>
        <h2>Ćwiczenie główne</h2>
        {paragraph(lesson["activity"])}
      </section>
      <section>
        <h2>Uwaga dla wychowawcy</h2>
        {paragraph(lesson["safety"])}
      </section>
      <nav class="lesson-nav">
        {nav_prev}
        <a class="nav-link primary" href="../index.html">Wróć do listy</a>
        {nav_next}
      </nav>
    </article>
  </main>
"""
    return page_shell(f'{lesson["id"]}. {lesson["display_title"]}', body, rel_prefix="../")


def render_index(lessons: list[dict]) -> str:
    goal_options = "".join(
        f'<option value="{goal_id}">{goal_id}. {esc(label)}</option>'
        for goal_id, label in GOAL_SHORT_LABELS.items()
    )
    goal_map_items = "".join(
        f"""
          <article class="goal-item">
            <span class="goal-token">{goal_id}</span>
            <div>
              <h3>{esc(GOAL_SHORT_LABELS[goal_id])}</h3>
              <p>{esc(GOAL_META[goal_id])}</p>
            </div>
          </article>"""
        for goal_id in GOAL_SHORT_LABELS
    )
    month_sections = []
    for month in MONTH_ORDER:
        group = [lesson for lesson in lessons if lesson["month"] == month]
        if not group:
            continue
        cards = []
        for lesson in group:
            goal_label = GOAL_SHORT_LABELS[lesson["goal"]]
            cards.append(
                f"""
          <a class="lesson-card" href="{esc(lesson["url"])}" data-goal="{lesson["goal"]}" data-goal-label="{esc(goal_label)}" data-month="{esc(lesson["month"])}" data-area="{esc(lesson["area"])}">
            <span class="card-top">
              <span class="lesson-id">{lesson["id"]}</span>
              <span class="lesson-meta">{esc(goal_label)} · {esc(lesson["area"])}</span>
            </span>
            <strong>{esc(lesson["display_title"])}</strong>
            <span class="full-topic">Temat z planu: {esc(lesson["title"])}</span>
            <span class="lesson-result"><b>Efekt:</b> {esc(lesson["evidence"])}</span>
            <span class="open-label">Otwórz lekcję</span>
          </a>"""
            )
        month_sections.append(
            f"""
      <section class="month-section" data-month-section="{esc(month)}">
        <div class="month-heading">
          <div>
            <h2>{esc(month)}</h2>
          </div>
          <span>{esc(lesson_count_label(len(group)))}</span>
        </div>
        <div class="lesson-grid">
          {''.join(cards)}
        </div>
      </section>"""
        )
    body = f"""
  <header class="site-header home-header">
    <div class="hero-copy">
      {brand_html(variant="full")}
      <p class="kicker">Materiały dla wychowawcy</p>
      <h1>Plan pracy wychowawczo-profilaktycznej 2026/2027</h1>
      <p class="subtitle">35 lekcji ułożonych miesiącami. Każda strona prowadzi wychowawcę przez sens tematu, pytanie otwierające, ćwiczenie, najważniejsze komunikaty dla uczniów, film i źródła do pogłębienia.</p>
    </div>
    <div class="metrics" aria-label="Podsumowanie">
      <div><strong>35</strong><span>lekcji</span></div>
      <div><strong>9</strong><span>obszarów</span></div>
      <div><strong>30</strong><span>minut</span></div>
      <div><strong>7</strong><span>miesięcy</span></div>
    </div>
  </header>
  <main class="index-layout">
    <section class="presentation-entry" aria-labelledby="presentation-title">
      <div>
        <p class="kicker">Start roku szkolnego</p>
        <h2 id="presentation-title">Prezentacja na spotkanie z uczniami 1 września 2026</h2>
        <p>Wstęp dla wychowawcy oraz osobny tryb slajdów z przyciskiem pełnego ekranu i prostymi komunikatami dla uczniów.</p>
      </div>
      <div class="entry-actions">
        <a class="presentation-button" href="spotkanie-z-uczniami-1-wrzesnia-2026.html">Otwórz prezentację</a>
      </div>
    </section>
    <section class="presentation-entry document-entry" aria-labelledby="guidelines-title">
      <div>
        <p class="kicker">Teczka wychowawcy</p>
        <h2 id="guidelines-title">Wytyczne na spotkanie z uczniami 1 września</h2>
        <p>Pełna treść dokumentu Word odtworzona jeden do jednego oraz oryginalny plik do pobrania.</p>
      </div>
      <div class="entry-actions">
        <a class="presentation-button" href="wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html">Otwórz wytyczne</a>
        <a class="presentation-button secondary" href="wytyczne_wych_uczn_1_wrzes_2026_ost.docx" download>Pobierz Word</a>
      </div>
    </section>
    <section class="toolbar" aria-label="Filtrowanie lekcji">
      <label for="search">Szukaj tematu</label>
      <input id="search" type="search" placeholder="np. AI, przemoc, praktyki, zdrowie">
      <label for="goalFilter">Obszar</label>
      <select id="goalFilter">
        <option value="all">Wszystkie obszary</option>
        {goal_options}
      </select>
      <p id="count" class="count">35 lekcji</p>
      <p class="filter-help">Obszar pokazuje główny cel wychowawczy lekcji. Jedna lekcja może wspierać kilka spraw, ale filtr prowadzi po jej najważniejszym zadaniu.</p>
    </section>
    <section class="overview" aria-labelledby="overview-title">
      <div class="overview-block">
        <h2 id="overview-title">Jak pracować z tą stroną</h2>
        <p>Strona jest praktycznym przewodnikiem dla wychowawcy. Najpierw wybierz miesiąc albo obszar po lewej, potem otwórz temat i przeczytaj krótki opis celu lekcji. Ten opis pomaga zrozumieć, po co dana rozmowa jest prowadzona i czego warto pilnować w klasie.</p>
        <p>Na stronie lekcji zacznij od pytania otwierającego, skorzystaj z proponowanego ćwiczenia i koniecznie wypowiedz komunikaty z sekcji „Co musi wybrzmieć”. Film traktuj przede wszystkim jako przygotowanie dla nauczyciela; można go wykorzystać także z klasą, jeśli pasuje do potrzeb lub sytuacji w klasie.</p>
      </div>
      <div class="overview-block">
        <h2>Cele programu w skrócie</h2>
        <p>Dziewięć obszarów porządkuje cały plan. Krótkie nazwy w filtrze są skrótami roboczymi, a poniższe opisy pokazują, co realnie ma zostać wzmocnione u uczniów.</p>
        <div class="goal-map">
          {goal_map_items}
        </div>
      </div>
    </section>
    <section class="lesson-list-section">
      <h2>Lista lekcji według miesięcy</h2>
      <div id="lessonGrid" class="month-list">
        {''.join(month_sections)}
      </div>
    </section>
  </main>
  <script src="script.js"></script>
"""
    return page_shell("Plan pracy wychowawczo-profilaktycznej 2026/2027", body)


CSS = """
:root {
  --bg: #f3f6f8;
  --panel: #ffffff;
  --ink: #14212b;
  --muted: #5d6d7c;
  --line: #dbe3ea;
  --accent: #0b6b5f;
  --accent-soft: #e5f4f1;
  --blue: #255d9a;
  --blue-soft: #e8f1fb;
  --amber-soft: #fff4df;
  --shadow: 0 18px 45px rgba(20, 33, 43, .09);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.55;
}
a { color: var(--accent); }
a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible {
  outline: 3px solid rgba(37, 93, 154, .28);
  outline-offset: 2px;
}
.site-header {
  padding: 24px clamp(18px, 5vw, 64px);
  background: linear-gradient(135deg, #fff, #f7fbfc 58%, #e8f5f2);
  border-bottom: 1px solid var(--line);
}
.site-header.compact { padding-bottom: 22px; }
.lesson-header {
  padding: 20px clamp(18px, 4vw, 56px) 24px;
}
.lesson-header-inner {
  width: min(100%, 1840px);
  margin: 0 auto;
}
.lesson-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 18px;
}
.lesson-topbar .brand-strip {
  margin-bottom: 0;
}
.home-header {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 430px);
  gap: 28px;
  align-items: end;
}
.hero-copy {
  min-width: 0;
}
.brand-strip {
  display: inline-flex;
  align-items: center;
  gap: 15px;
  max-width: 100%;
  margin-bottom: 14px;
  color: var(--ink);
}
.brand-logo-full,
.brand-logo-mark {
  display: block;
  height: auto;
  object-fit: contain;
  object-position: left center;
}
.brand-logo-full {
  width: min(430px, 72vw);
  max-height: 72px;
}
.brand-logo-mark {
  width: 78px;
  max-height: 58px;
}
.brand-strip-full {
  display: flex;
  width: min(460px, 100%);
}
.brand-strip-full .brand-logo-mark,
.brand-strip-full .brand-text {
  display: none;
}
.brand-strip-compact .brand-logo-full {
  display: none;
}
.brand-text {
  min-width: 0;
}
.brand-strip strong {
  display: block;
  font-size: 1.05rem;
  line-height: 1.15;
}
.brand-strip span {
  display: block;
  margin-top: 2px;
  color: var(--muted);
  font-size: .9rem;
}
.kicker {
  margin: 0 0 8px;
  color: var(--accent);
  font-size: .82rem;
  font-weight: 850;
  text-transform: uppercase;
  letter-spacing: .04em;
}
h1 {
  margin: 0;
  max-width: 1060px;
  font-size: clamp(1.85rem, 3.5vw, 2.8rem);
  line-height: 1.08;
  letter-spacing: 0;
  overflow-wrap: anywhere;
}
h2 {
  margin: 0 0 12px;
  font-size: clamp(1.18rem, 2vw, 1.55rem);
  line-height: 1.2;
}
.subtitle {
  max-width: 980px;
  margin: 13px 0 0;
  color: var(--muted);
  font-size: 1rem;
}
.metrics {
  display: grid;
  grid-template-columns: repeat(4, minmax(150px, 1fr));
  gap: 12px;
  margin-top: 22px;
  max-width: 980px;
}
.home-header .metrics {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  align-self: center;
  margin-top: 0;
  max-width: none;
}
.metrics div, .toolbar, .lesson-card, .lesson-content, .lesson-aside .aside-card, .note, .overview-block {
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--panel);
  box-shadow: var(--shadow);
}
.metrics div { padding: 14px; }
.home-header .metrics div { padding: 12px; }
.metrics strong { display: block; font-size: 1.55rem; }
.metrics span, .lesson-card span, .aside-card span, .source-list span { color: var(--muted); }
.index-layout {
  display: grid;
  grid-template-columns: minmax(260px, 340px) minmax(0, 1fr);
  gap: 20px;
  padding: 22px clamp(18px, 5vw, 64px) 40px;
}
.presentation-entry {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 18px;
  align-items: center;
  border: 1px solid #b9ddd6;
  border-radius: 10px;
  padding: 18px;
  background: linear-gradient(135deg, #ffffff, #e5f4f1);
  box-shadow: var(--shadow);
}
.presentation-entry h2 {
  margin-bottom: 8px;
}
.presentation-entry p:not(.kicker) {
  max-width: 900px;
  margin: 0;
  color: var(--muted);
}
.presentation-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 10px 14px;
  background: var(--accent);
  color: #fff;
  font-weight: 850;
  text-decoration: none;
  white-space: nowrap;
}
.presentation-button.secondary {
  background: #fff;
  color: var(--accent);
}
.presentation-button:hover {
  background: #08564d;
}
.presentation-button.secondary:hover {
  background: var(--accent-soft);
  color: var(--accent);
}
.entry-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: flex-end;
}
.toolbar {
  align-self: start;
  position: sticky;
  top: 16px;
  display: grid;
  gap: 10px;
  padding: 16px;
}
label { font-weight: 800; font-size: .9rem; }
input, select {
  width: 100%;
  min-height: 42px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 10px;
  background: #fff;
  font: inherit;
}
.count {
  margin: 0;
  display: inline-flex;
  color: var(--blue);
  background: var(--blue-soft);
  border-radius: 999px;
  padding: 6px 10px;
  font-weight: 800;
}
.filter-help {
  margin: 4px 0 0;
  color: var(--muted);
  font-size: .9rem;
  line-height: 1.4;
}
.overview, .lesson-list-section {
  grid-column: 2;
}
.overview {
  display: grid;
  gap: 14px;
}
.overview-block {
  padding: 18px;
}
.overview-block p {
  margin: 0;
  color: var(--muted);
}
.overview-block p + p {
  margin-top: 10px;
}
.goal-map {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 10px;
  margin-top: 14px;
}
.goal-item {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 10px;
  padding: 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fbfdff;
}
.goal-token {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--ink);
  color: #fff;
  font-weight: 900;
}
.goal-item h3 {
  margin: 0 0 4px;
  font-size: .98rem;
  line-height: 1.2;
}
.goal-item p {
  font-size: .9rem;
  line-height: 1.4;
}
.month-list {
  display: grid;
  gap: 20px;
}
.month-section {
  display: grid;
  gap: 12px;
}
.month-section.is-hidden,
.lesson-card.is-hidden {
  display: none !important;
}
.month-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--line);
}
.month-heading h2 { margin: 0; }
.month-heading > span {
  flex: 0 0 auto;
  color: var(--muted);
  font-size: .9rem;
  font-weight: 800;
}
.lesson-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 13px;
}
.lesson-card {
  display: grid;
  grid-template-rows: auto auto auto 1fr auto;
  gap: 9px;
  padding: 15px;
  color: var(--ink);
  text-decoration: none;
}
.lesson-card:hover { border-color: var(--accent); background: var(--accent-soft); }
.card-top {
  display: flex;
  align-items: center;
  gap: 9px;
  min-width: 0;
}
.lesson-id {
  flex: 0 0 auto;
  min-width: 38px;
  padding: 3px 8px;
  border-radius: 8px;
  background: var(--ink);
  color: #fff !important;
  font-weight: 900;
  text-align: center;
}
.lesson-meta {
  min-width: 0;
  font-size: .82rem;
  font-weight: 800;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.lesson-card strong {
  font-size: 1.08rem;
  line-height: 1.25;
}
.full-topic {
  display: -webkit-box;
  font-size: .9rem;
  line-height: 1.38;
  overflow: hidden;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.lesson-result {
  font-size: .92rem;
  line-height: 1.4;
}
.lesson-result b { color: var(--ink); }
.open-label {
  width: fit-content;
  margin-top: 4px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 6px 10px;
  color: var(--accent) !important;
  font-weight: 850;
}
.lesson-card:hover .open-label {
  background: var(--accent);
  color: #fff !important;
}
.note {
  grid-column: 2;
  margin-top: 20px;
  padding: 18px;
}
.back-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 12px;
  background: #fff;
  margin-bottom: 16px;
  font-weight: 800;
  text-decoration: none;
  white-space: nowrap;
}
.lesson-topbar .back-link {
  flex: 0 0 auto;
  margin-bottom: 0;
}
.lesson-layout {
  display: grid;
  grid-template-columns: minmax(260px, 340px) minmax(0, 1fr);
  gap: 22px;
  width: min(100%, 1840px);
  margin: 0 auto;
  padding: 22px clamp(18px, 4vw, 40px) 42px;
  align-items: start;
}
.lesson-aside {
  display: grid;
  gap: 12px;
  position: sticky;
  top: 16px;
}
.aside-card { padding: 14px; }
.aside-card strong { display: block; margin-bottom: 8px; }
.video-card { background: var(--amber-soft); }
.video-card span, .resource-card span {
  display: block;
  margin-bottom: 10px;
  font-size: .92rem;
}
.resource-card {
  background: #fbfdff;
}
.resource-link {
  display: inline-flex;
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 10px;
  font-weight: 850;
  text-decoration: none;
}
.compact-source-list {
  display: grid;
  gap: 11px;
  margin: 0;
  padding-left: 18px;
}
.compact-source-list a {
  display: inline-block;
  font-weight: 850;
  line-height: 1.25;
}
.lesson-content {
  padding: 22px;
  min-width: 0;
}
.lesson-content section + section {
  margin-top: 24px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
}
.must {
  background: var(--accent-soft);
  border: 1px solid #b9ddd6;
  border-radius: 10px;
  padding: 18px !important;
}
li + li { margin-top: 6px; }
.source-list {
  display: grid;
  gap: 10px;
  padding-left: 20px;
}
.schedule {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
}
.schedule th, .schedule td {
  border-bottom: 1px solid var(--line);
  padding: 10px;
  text-align: left;
  vertical-align: top;
  overflow-wrap: anywhere;
}
.schedule th {
  background: var(--blue-soft);
  color: var(--blue);
  font-size: .88rem;
}
.schedule td:first-child {
  width: 92px;
  font-weight: 850;
  white-space: nowrap;
}
.source-list a { font-weight: 800; }
.lesson-content a { overflow-wrap: anywhere; }
.source-list span { display: block; font-size: .92rem; }
.lesson-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 28px;
  padding-top: 20px;
  border-top: 1px solid var(--line);
}
.nav-link {
  display: inline-flex;
  align-items: center;
  min-height: 40px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 12px;
  text-decoration: none;
  font-weight: 800;
}
.nav-link.primary { background: var(--accent); color: #fff; }
@media (max-width: 1080px) {
  .home-header {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .home-header .metrics {
    grid-template-columns: repeat(4, minmax(130px, 1fr));
    margin-top: 0;
  }
}
@media (max-width: 840px) {
  .metrics, .index-layout, .lesson-layout { grid-template-columns: 1fr; }
  .home-header .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .presentation-entry { grid-template-columns: 1fr; }
  .presentation-button { width: fit-content; }
  .entry-actions { justify-content: flex-start; }
  .toolbar, .lesson-aside { position: static; }
  .lesson-content { order: 1; }
  .lesson-aside { order: 2; }
  .note, .overview, .lesson-list-section { grid-column: auto; }
  .month-heading { align-items: start; flex-direction: column; }
  .schedule { display: block; overflow-x: auto; }
}
@media (max-width: 640px) {
  .lesson-topbar {
    align-items: flex-start;
    flex-direction: column;
    gap: 12px;
  }
}
@media (max-width: 520px) {
  .brand-strip {
    gap: 12px;
    margin-bottom: 16px;
  }
  .brand-strip-full {
    width: 100%;
  }
  .brand-strip-full .brand-logo-full {
    display: none;
  }
  .brand-strip-full .brand-logo-mark,
  .brand-strip-full .brand-text {
    display: block;
  }
  .brand-logo-mark {
    width: 60px;
    max-height: 46px;
  }
  .brand-strip strong { font-size: .98rem; }
  .brand-strip span { font-size: .82rem; }
}
"""


JS = """
const search = document.querySelector('#search');
const goalFilter = document.querySelector('#goalFilter');
const cards = Array.from(document.querySelectorAll('.lesson-card'));
const monthSections = Array.from(document.querySelectorAll('.month-section'));
const count = document.querySelector('#count');

function normalize(value) {
  return value.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
}

function applyFilters() {
  const query = normalize(search.value || '');
  const goal = goalFilter.value;
  let visible = 0;
  cards.forEach((card) => {
    const text = normalize(card.textContent);
    const matchesText = !query || text.includes(query);
    const matchesGoal = goal === 'all' || card.dataset.goal === goal;
    const show = matchesText && matchesGoal;
    card.hidden = !show;
    card.classList.toggle('is-hidden', !show);
    if (show) visible += 1;
  });
  monthSections.forEach((section) => {
    const hasVisibleCard = Array.from(section.querySelectorAll('.lesson-card')).some((card) => !card.hidden);
    const hideSection = !hasVisibleCard;
    section.hidden = hideSection;
    section.classList.toggle('is-hidden', hideSection);
  });
  count.textContent = `${visible} z ${cards.length} lekcji`;
}

search.addEventListener('input', applyFilters);
goalFilter.addEventListener('change', applyFilters);
applyFilters();
"""


def write_sources(lessons: list[dict]) -> None:
    used = []
    for key in SOURCES:
        if any(key in lesson["source_keys"] for lesson in lessons):
            used.append(SOURCES[key])
    lines = [
        "# Źródła do planu pracy wychowawczo-profilaktycznej 2026/2027",
        "",
        "Źródła zweryfikowano przy opracowywaniu materiałów w sierpniu 2026 r. Linki do filmów są materiałami inspiracyjnymi dla nauczyciela, a nie obowiązkową treścią do odtworzenia uczniom.",
        "",
        "## Źródła merytoryczne",
        "",
    ]
    for source in used:
        lines.append(f"- [{source.name}]({source.url}) - {source.note}")
    lines.extend(["", "## Filmy i inspiracje wideo dla nauczyciela", ""])
    for lesson in lessons:
        lines.append(f"- {lesson['id']}. [{lesson['teacher_video']['title']}]({lesson['teacher_video']['url']}) - {lesson['title']}")
    (OUT / "zrodla.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(lessons: list[dict]) -> None:
    text = f"""# Plan pracy wychowawczo-profilaktycznej 2026/2027

Publikacja zawiera {len(lessons)} opracowanych tematów lekcji wychowawczych wynikających z pliku `Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx`.

## Zawartość

- osobna strona HTML dla każdej lekcji,
- indeks główny z wyszukiwaniem i filtrowaniem po celu,
- dodatkowa prezentacja startowa `spotkanie-z-uczniami-1-wrzesnia-2026.html`,
- wersja dokumentu do teczki wychowawcy `wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html` z pobieraniem pliku Word,
- plik `lessons.json` z danymi lekcji,
- zbiorcze źródła i filmy inspiracyjne w `zrodla.md`.

Foldery `scenariusze`, `prezentacje_md` i `prezentacje_pptx` mogą zawierać wcześniejsze robocze materiały. Aktualna wersja planu 2026/2027 jest generowana do folderu `strona_html`.

## Jak korzystać

Otwórz `strona_html/index.html`, wybierz temat i prowadź lekcję według przewodnika. Każda lekcja jest zaplanowana na 30 minut i zawiera: cel, przewidywane rezultaty, przebieg, ćwiczenie, komunikaty, które muszą wybrzmieć, dowód realizacji, źródła i film albo inspirację wideo dla nauczyciela.

Prezentacja startowa dla spotkania z uczniami 1 września 2026 r. działa w przeglądarce, obsługuje kliknięcie w slajd, strzałki, spację i tryb pełnoekranowy. Przed właściwą prezentacją znajduje się osobny wstęp z notatkami dla wychowawcy.

Wersja do teczki wychowawcy zawiera pełną treść dokumentu `wytyczne_wych_uczn_1_wrzes_2026_ost.docx` oraz link do pobrania oryginalnego pliku Word.

## Uwaga

Przy tematach dotyczących zdrowia psychicznego, przemocy, danych osobowych i sytuacji rodzinnych nie zbieramy prywatnych historii uczniów na forum klasy. W razie ujawnienia zagrożenia zdrowia lub życia wychowawca uruchamia procedury szkoły.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def write_root_readme(lessons: list[dict]) -> None:
    text = f"""# Plan pracy wychowawczo-profilaktycznej 2026/2027

Publiczna strona z materiałami dla wychowawców ZSZ5 na rok szkolny 2026/2027.

## Aktualna wersja

- źródło tematów: `Plan pracy wychowawczo profilaktycznej szkoly 2026.2027.docx`,
- liczba tematów: {len(lessons)},
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
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def main() -> None:
    lessons = build_lessons()
    generate_wytyczne_document_page()
    SITE.mkdir(parents=True, exist_ok=True)
    if LESSON_PAGES.exists():
        shutil.rmtree(LESSON_PAGES)
    if ROOT_LESSON_PAGES.exists():
        shutil.rmtree(ROOT_LESSON_PAGES)
    LESSON_PAGES.mkdir(parents=True, exist_ok=True)
    ROOT_LESSON_PAGES.mkdir(parents=True, exist_ok=True)
    SITE_ASSETS.mkdir(parents=True, exist_ok=True)
    for logo_file in LOGO_FILES:
        if (ROOT_ASSETS / logo_file).exists():
            shutil.copy2(ROOT_ASSETS / logo_file, SITE_ASSETS / logo_file)
    (SITE / "styles.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (SITE / "script.js").write_text(JS.strip() + "\n", encoding="utf-8")
    (SITE / "index.html").write_text(render_index(lessons), encoding="utf-8")
    (ROOT / "styles.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (ROOT / "script.js").write_text(JS.strip() + "\n", encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(lessons), encoding="utf-8")
    for file_name in EXTRA_SITE_FILES:
        source = ROOT / file_name
        if source.exists():
            shutil.copy2(source, SITE / file_name)
    for idx, lesson in enumerate(lessons):
        prev_lesson = lessons[idx - 1] if idx > 0 else None
        next_lesson = lessons[idx + 1] if idx < len(lessons) - 1 else None
        lesson_html = render_lesson(lesson, prev_lesson, next_lesson)
        (LESSON_PAGES / f"{lesson['slug']}.html").write_text(lesson_html, encoding="utf-8")
        (ROOT_LESSON_PAGES / f"{lesson['slug']}.html").write_text(lesson_html, encoding="utf-8")
    (OUT / "lessons.json").write_text(json.dumps(lessons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_sources(lessons)
    write_readme(lessons)
    write_root_readme(lessons)
    print(f"Generated {len(lessons)} lesson pages in {LESSON_PAGES} and {ROOT_LESSON_PAGES}")


if __name__ == "__main__":
    main()
