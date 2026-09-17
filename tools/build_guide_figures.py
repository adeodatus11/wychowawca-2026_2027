#!/usr/bin/env python3
"""Buduje infografiki SVG dla poradników bazy wiedzy i wstawia je do artykułów.

Każdy artykuł ma jedną infografikę podsumowującą jego najważniejsze treści.
Grafiki są składane w pionie (format portretowy), aby pozostawały czytelne
na telefonie bez powiększania; pełny ekran i powiększenie zapewnia
guide-figures.js.

Skrypt jest idempotentny: podmienia zawartość między znacznikami
<!-- infografika:start --> i <!-- infografika:end -->.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

W = 340                 # szerokość viewBox (wąski format = większy tekst na telefonie)
MARGIN = 12
INK = "#14212b"
MUTED = "#5d6d7c"
LINE = "#dbe3ea"
TEAL, TEAL_SOFT = "#0b6b5f", "#e5f4f1"
BLUE, BLUE_SOFT = "#255d9a", "#e8f1fb"
ALERT, ALERT_SOFT = "#a8322a", "#fdeceb"
AMBER, AMBER_SOFT = "#7a5200", "#fff4df"

TONES = {
    "teal": (TEAL_SOFT, TEAL),
    "blue": (BLUE_SOFT, BLUE),
    "alert": (ALERT_SOFT, ALERT),
    "amber": (AMBER_SOFT, AMBER),
    "plain": ("#ffffff", TEAL),
}

FONT = "system-ui, -apple-system, 'Segoe UI', sans-serif"

# Rzeczywiste szerokości znaków zmierzone w przeglądarce dla tego samego stosu
# fontów (tools/glyph-widths.json, generowane skryptem kalibrującym). Szacowanie
# "na oko" dawało za wąskie wiersze i tekst wychodził poza kartę.
_GLYPHS = json.loads((Path(__file__).resolve().parent / "glyph-widths.json").read_text(
    encoding="utf-8"))["widths"]
SAFETY = 1.03   # zapas na inne systemowe kroje (Segoe UI, SF Pro) i kerning


def text_w(s: str, size: float, variant: str = "n400") -> float:
    table = _GLYPHS[variant]
    fallback = table["a"]
    return sum(table.get(c, fallback) for c in s) * size * SAFETY


def wrap(s: str, size: float, maxw: float, variant: str = "n400") -> list[str]:
    """Zawija tekst na podstawie zmierzonych szerokości znaków."""
    lines: list[str] = []
    for hard in s.split("\n"):
        cur = ""
        for word in hard.split():
            trial = f"{cur} {word}".strip()
            if cur and text_w(trial, size, variant) > maxw:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
    return [ln for ln in lines if ln != ""] or [""]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tspans(lines: list[str], x: float, lh: float) -> str:
    out = []
    for i, ln in enumerate(lines):
        dy = "0" if i == 0 else f"{lh}"
        out.append(f'<tspan x="{x:g}" dy="{dy}">{esc(ln)}</tspan>')
    return "".join(out)


class Fig:
    """Prosty układ pionowy: karty dodawane jedna pod drugą."""

    def __init__(self, title: str, subtitle: str = ""):
        self.parts: list[str] = []
        self.y = MARGIN
        self._title(title, subtitle)

    def _title(self, title: str, subtitle: str):
        x = MARGIN + 2
        maxw = W - 2 * MARGIN - 4
        lines = wrap(title, 20, maxw, "n800")
        self.parts.append(
            f'<text x="{x}" y="{self.y + 18:g}" font-size="20" font-weight="800" '
            f'fill="{INK}">{tspans(lines, x, 24)}</text>'
        )
        self.y += 18 + 24 * (len(lines) - 1)
        if subtitle:
            sub = wrap(subtitle, 13.5, maxw)
            self.y += 17
            self.parts.append(
                f'<text x="{x}" y="{self.y:g}" font-size="13.5" fill="{MUTED}">'
                f'{tspans(sub, x, 17)}</text>'
            )
            self.y += 17 * (len(sub) - 1)
        self.y += 16

    def card(self, *, tone="plain", badge=None, heading=None, bullets=(),
             body=None, foot=None):
        fill, accent = TONES[tone]
        top = self.y
        inner_l = MARGIN + (52 if badge else 16)
        inner_r = W - MARGIN - 16
        maxw = inner_r - inner_l
        y = top + 16
        body_parts: list[str] = []

        if heading:
            hl = wrap(heading, 16.5, maxw, "n750")
            body_parts.append(
                f'<text x="{inner_l}" y="{y + 13:g}" font-size="16.5" font-weight="750" '
                f'fill="{accent}">{tspans(hl, inner_l, 20)}</text>'
            )
            y += 13 + 20 * (len(hl) - 1) + 9

        if body:
            bl = wrap(body, 14.5, maxw)
            body_parts.append(
                f'<text x="{inner_l}" y="{y + 11:g}" font-size="14.5" fill="{INK}">'
                f'{tspans(bl, inner_l, 18.5)}</text>'
            )
            y += 11 + 18.5 * (len(bl) - 1) + 8

        for item in bullets:
            bl = wrap(item, 14.5, maxw - 14)
            dot_y = y + 7
            body_parts.append(
                f'<circle cx="{inner_l + 3:g}" cy="{dot_y:g}" r="2.6" fill="{accent}"/>'
            )
            body_parts.append(
                f'<text x="{inner_l + 14:g}" y="{y + 11:g}" font-size="14.5" fill="{INK}">'
                f'{tspans(bl, inner_l + 14, 18.5)}</text>'
            )
            y += 11 + 18.5 * (len(bl) - 1) + 9

        if foot:
            fl = wrap(foot, 13, maxw, "i400")
            y += 2
            body_parts.append(
                f'<text x="{inner_l}" y="{y + 10:g}" font-size="13" font-style="italic" '
                f'fill="{MUTED}">{tspans(fl, inner_l, 16.5)}</text>'
            )
            y += 10 + 16.5 * (len(fl) - 1) + 6

        h = max(y + 10 - top, 54)
        stroke = accent if tone != "plain" else LINE
        self.parts.append(
            f'<rect x="{MARGIN}" y="{top}" width="{W - 2 * MARGIN}" height="{h:g}" rx="11" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        )
        if badge:
            cy = top + 30
            self.parts.append(
                f'<circle cx="{MARGIN + 27}" cy="{cy:g}" r="15" fill="{accent}"/>'
                f'<text x="{MARGIN + 27}" y="{cy + 5.5:g}" font-size="15.5" font-weight="800" '
                f'fill="#ffffff" text-anchor="middle">{esc(badge)}</text>'
            )
        self.parts.extend(body_parts)
        self.y = top + h

    def arrow(self, tone="plain"):
        _, accent = TONES[tone]
        cx = W / 2
        y = self.y + 5
        self.parts.append(
            f'<path d="M{cx} {y} l0 12 m-6 -6 l6 6 l6 -6" fill="none" stroke="{accent}" '
            f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" '
            f'opacity=".75"/>'
        )
        self.y = y + 17

    def gap(self, n=10):
        self.y += n

    def strip(self, text: str, tone="teal"):
        fill, accent = TONES[tone]
        top = self.y
        inner_l = MARGIN + 16
        maxw = W - 2 * MARGIN - 32
        lines = wrap(text, 14.5, maxw, "n700")
        h = 22 + 18.5 * len(lines)
        self.parts.append(
            f'<rect x="{MARGIN}" y="{top}" width="{W - 2 * MARGIN}" height="{h:g}" rx="11" '
            f'fill="{accent}"/>'
        )
        self.parts.append(
            f'<text x="{inner_l}" y="{top + 26:g}" font-size="14.5" font-weight="700" '
            f'fill="#ffffff">{tspans(lines, inner_l, 18.5)}</text>'
        )
        self.y = top + h

    def render(self, fid: str, title: str, desc: str) -> str:
        h = self.y + MARGIN
        return (
            f'<svg class="guide-figure-svg" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {W} {h:g}" role="img" '
            f'aria-labelledby="{fid}-t {fid}-d" font-family="{FONT}">'
            f'<title id="{fid}-t">{esc(title)}</title>'
            f'<desc id="{fid}-d">{esc(desc)}</desc>'
            f'<rect width="{W}" height="{h:g}" fill="#ffffff"/>'
            + "".join(self.parts)
            + "</svg>"
        )


# --------------------------------------------------------------------------
# Definicje infografik
# --------------------------------------------------------------------------

def fig_trudne() -> tuple[str, str, str]:
    title = "Trudne zachowania: trzy poziomy reakcji"
    desc = (
        "Poziom 1, codzienna reakcja na lekcji: krótka wskazówka, powiedz czego oczekujesz, "
        "pomóż wrócić do pracy, nie ustalaj przyczyn przy całej klasie. "
        "Poziom 2, konsultacja z zespołem pomocy psychologiczno-pedagogicznej: przy powtarzających "
        "się trudnościach, nagłej zmianie funkcjonowania, zgłoszeniu krzywdzenia lub gdy sam "
        "potrzebujesz wsparcia; nie trzeba czekać na kryzys ani zbierać uwag. "
        "Poziom 3, pilna pomoc pod numerem 112 lub 999: przemoc i groźby, wypowiedź o samobójstwie "
        "lub samouszkodzeniu, podejrzenie zatrucia, nagłe zagrożenie zdrowia; nie czekaj na zgodę "
        "dyrekcji ani na kontakt z rodzicem, zapewnij ciągłość opieki nad uczniem i nad klasą. "
        "Po każdym zdarzeniu zapisz fakty: datę, miejsce, zachowanie, swoją reakcję, skutek i osobę, "
        "której przekazano sprawę."
    )
    f = Fig(title, "Od krótkiej wskazówki na lekcji po wezwanie służb ratunkowych.")
    f.card(
        tone="teal", badge="1", heading="Codzienna reakcja na lekcji",
        bullets=[
            "Podejdź, powiedz spokojnie, czego oczekujesz, i daj chwilę na reakcję.",
            "Pomóż wrócić do pracy: wskaż pierwszy krok, udostępnij materiał.",
            "Nie ustalaj przyczyn zachowania przy całej klasie.",
        ],
        foot="Najpierw sprawdź, czy wystarczy krótka wskazówka.",
    )
    f.arrow("blue")
    f.card(
        tone="blue", badge="2", heading="Konsultacja z zespołem",
        bullets=[
            "Trudności wracają mimo zastosowanych zmian.",
            "Nagła zmiana funkcjonowania, silny lęk, zgłoszenie krzywdzenia.",
            "Prośba ucznia o pomoc albo twoja własna potrzeba wsparcia.",
        ],
        foot="Nie trzeba czekać na kryzys ani zbierać określonej liczby uwag.",
    )
    f.arrow("alert")
    f.card(
        tone="alert", badge="3", heading="Pilna pomoc — 112 lub 999",
        bullets=[
            "Przemoc, bójka, groźby — wezwij dorosłego, chroń osoby zagrożone.",
            "Wypowiedź o samobójstwie lub samouszkodzeniu — zostań z uczniem, zapytaj wprost.",
            "Podejrzenie zatrucia — nie czekaj na ciężkie objawy.",
        ],
        foot="Nie czekaj na zgodę dyrekcji ani na kontakt z rodzicem.",
    )
    f.gap(12)
    f.strip("Zawsze zapisz fakty: data, miejsce, zachowanie, reakcja, skutek, komu przekazano.")
    return f.render("fig-trudne", title, desc), title, desc


def fig_spektrum() -> tuple[str, str, str]:
    title = "Uczeń w spektrum autyzmu na lekcji"
    desc = (
        "Zacznij od potrzeb konkretnego ucznia: ta sama diagnoza oznacza różne potrzeby, "
        "sprawdź czy uczeń rozumie zadanie, wie jak zacząć i może pracować w danych warunkach. "
        "Jak mówić: podaj jeden krok naraz, sprawdź zrozumienie prosząc o wskazanie pierwszej "
        "czynności zamiast pytania czy wszystko jasne, zostaw czas i nie powtarzaj polecenia coraz "
        "głośniej, zapowiadaj zmiany, nie wymagaj kontaktu wzrokowego jako dowodu słuchania. "
        "Warunki pracy: sprawdź hałas, światło, ruch za plecami i zapachy, miejsce wybierz wspólnie "
        "z uczniem, ostatnia ławka nie jest uniwersalnym rozwiązaniem, nie przerywaj nieszkodliwej "
        "samoregulacji. Gdy narasta przeciążenie, możliwe sygnały to zasłanianie uszu, coraz szybsze "
        "powtarzanie słów, gwałtowne pobudzenie lub nagłe wycofanie; ogranicz liczbę słów i bodźców, "
        "daj przestrzeń, nie nalegaj na wyjaśnienia ani przeprosiny, nie dotykaj bez uprzedzenia. "
        "Przerwę zaplanuj wcześniej: sygnał, miejsce, osoba sprawująca opiekę i sposób powrotu."
    )
    f = Fig(title, "Ta sama diagnoza, różne potrzeby. Sprawdzaj, co pomaga temu uczniowi.")
    f.card(
        tone="teal", heading="Jak mówić",
        bullets=[
            "Jeden krok naraz; dłuższą instrukcję zapisz w punktach.",
            "Zamiast „wszystko jasne?” poproś o wskazanie pierwszej czynności.",
            "Zostaw czas. Nie powtarzaj polecenia coraz głośniej.",
            "Zapowiadaj zmiany: co się zmienia, co zostaje, co dalej.",
        ],
        foot="Nie wymagaj patrzenia w oczy jako dowodu słuchania.",
    )
    f.gap(10)
    f.card(
        tone="blue", heading="Warunki pracy",
        bullets=[
            "Sprawdź hałas, światło, ruch za plecami, zapachy, bliskość innych.",
            "Miejsce wybierz wspólnie z uczniem i sprawdź efekt.",
            "Nie przerywaj nieszkodliwej samoregulacji.",
        ],
        foot="Ostatnia ławka nie jest uniwersalnym rozwiązaniem. Celem jest udział w lekcji.",
    )
    f.gap(10)
    f.card(
        tone="amber", heading="Gdy narasta przeciążenie",
        body="Możliwe sygnały: zasłanianie uszu, coraz szybsze powtarzanie słów, "
             "gwałtowne pobudzenie albo nagłe wycofanie.",
        bullets=[
            "Ogranicz liczbę słów, pytań i mówiących osób.",
            "Zmniejsz bodźce i daj przestrzeń. Nie otaczaj ucznia grupą dorosłych.",
            "Nie nalegaj na wyjaśnienia, przeprosiny ani dokończenie zadania.",
            "Nie dotykaj ucznia bez uprzedzenia.",
        ],
        foot="Uwzględnij też ból, chorobę, lęk i krzywdzenie przez innych.",
    )
    f.gap(12)
    f.strip("Przerwę zaplanuj wcześniej: sygnał · miejsce · osoba sprawująca opiekę · powrót.",
            tone="teal")
    return f.render("fig-spektrum", title, desc), title, desc


def fig_integracja() -> tuple[str, str, str]:
    title = "Pierwsze spotkanie integracyjne"
    desc = (
        "Przed wyjściem: rodzina zna miejsce, godziny, koszt, potrzebny ubiór, zasady udziału i "
        "sposób kontaktu; składy zespołów ustala prowadzący; sprawdź regulamin terenu i miejsce na "
        "ognisko. W trakcie spotkania prowadź od łatwego do trudniejszego: powitanie obniżające "
        "presję, imiona, krótkie rozmowy w parach, zadanie zespołowe bez rywalizacji, wspólne "
        "odkrywanie miejsca, ognisko i swobodna rozmowa, zakończenie bez rankingu sympatii. "
        "Po powrocie do szkoły wybierz z klasą jeden pomysł możliwy do realizacji, planuj krótkie "
        "zadania ze zmiennymi rolami i po dwóch do czterech tygodni zapytaj, czy każdy ma z kim "
        "pracować i do kogo zwrócić się po pomoc. Czego nie robić na pierwszym spotkaniu: ćwiczeń "
        "wymagających bliskiego kontaktu i dużego zaufania, chodzenia z zasłoniętymi oczami, "
        "obowiązkowych występów solo, wybierania drużyn przez kapitanów, rywalizacji według "
        "pochodzenia."
    )
    f = Fig(title, "Plan, który pozwala uczestniczyć bez presji i zawstydzania.")
    f.card(
        tone="blue", badge="1", heading="Przed wyjściem",
        bullets=[
            "Rodzina zna miejsce, godziny, koszt, ubiór, zasady i kontakt.",
            "Składy zespołów ustala prowadzący — nikt nie czeka na wybranie.",
            "Sprawdź regulamin terenu i miejsce na ognisko.",
        ],
    )
    f.arrow("teal")
    f.card(
        tone="teal", badge="2", heading="W trakcie: od łatwego do trudniejszego",
        bullets=[
            "Powitanie obniżające presję, potem imiona.",
            "Krótkie rozmowy w parach, ze zmianą rozmówcy.",
            "Zadanie zespołowe bez rywalizacji, potem wspólne odkrywanie miejsca.",
            "Ognisko i swobodna rozmowa; zakończenie bez rankingu sympatii.",
        ],
    )
    f.arrow("blue")
    f.card(
        tone="blue", badge="3", heading="Po powrocie do szkoły",
        bullets=[
            "Wybierzcie jeden pomysł z lasu możliwy do realizacji.",
            "Krótkie zadania ze zmiennymi rolami przez kolejne tygodnie.",
            "Po 2–4 tygodniach zapytaj: „Czy masz z kim pracować?”, "
            "„Czy wiesz, do kogo zwrócić się po pomoc?”.",
        ],
        foot="Sygnał krzywdzenia — reaguj od razu, nie czekaj na podsumowanie.",
    )
    f.gap(12)
    f.card(
        tone="alert", heading="Nie na pierwszym spotkaniu",
        bullets=[
            "Ćwiczenia wymagające bliskiego kontaktu i dużego zaufania.",
            "Chodzenie po lesie z zasłoniętymi oczami.",
            "Obowiązkowe występy solo przed nieznaną jeszcze grupą.",
            "Wybieranie drużyn przez kapitanów.",
            "Rywalizacja według pochodzenia — żadnych drużyn „Polska kontra Ukraina”.",
        ],
    )
    return f.render("fig-integracja", title, desc), title, desc


def fig_toaleta() -> tuple[str, str, str]:
    title = "Wyjście do toalety: trzy sytuacje"
    desc = (
        "Zwykła potrzeba fizjologiczna: uczeń szkoły ponadpodstawowej może krótko wyjść sam, "
        "bez publicznego dopytywania o szczegóły; przy kilku chętnych naraz można poprosić, "
        "by wychodzili pojedynczo; zostawienie telefonu w sali to rozwiązanie porządkowe, "
        "nie kara ani wymóg ustawowy. Złe samopoczucie: uczeń z zawrotami głowy, nudnościami "
        "lub ryzykiem zasłabnięcia nie powinien iść sam — statut przewiduje skierowanie do "
        "pielęgniarki w towarzystwie drugiej osoby. Nagłe zagrożenie zdrowia: zostań przy uczniu, "
        "udziel pierwszej pomocy w granicach swoich umiejętności, wezwij 112, poproś o wsparcie "
        "innego pracownika i możliwie szybko zapewnij opiekę reszcie klasy. Nadzór ma być "
        "adekwatny do okoliczności, nie absolutny; nauczyciel nie diagnozuje ucznia, ale powinien "
        "zauważyć, że zwykła sytuacja przestaje być zwykła."
    )
    f = Fig(title, "Ta sama prośba może znaczyć co innego. Oceniaj sytuację, nie regułę.")
    f.card(
        tone="teal", heading="Zwykła potrzeba fizjologiczna",
        body="Uczeń może krótko wyjść sam.",
        bullets=[
            "Przyjmij zgłoszenie normalnie, bez publicznego dopytywania o szczegóły.",
            "Kilka osób naraz — poproś, by wychodziły pojedynczo.",
            "Telefon zostawiony w sali to rozwiązanie porządkowe, nie kara.",
        ],
    )
    f.gap(10)
    f.card(
        tone="amber", heading="Złe samopoczucie",
        body="Uczeń nie powinien zostać bez wsparcia.",
        bullets=[
            "Zawroty głowy, nudności, bladość, ryzyko zasłabnięcia — nie wysyłaj samego.",
            "Skierowanie do pielęgniarki w towarzystwie drugiej osoby.",
            "Przy niewielkich dolegliwościach: usiąść, napić się wody, obserwuj efekt.",
        ],
    )
    f.gap(10)
    f.card(
        tone="alert", heading="Nagłe zagrożenie zdrowia",
        body="Priorytetem jest pomoc uczniowi.",
        bullets=[
            "Zostań przy uczniu i zabezpiecz sytuację.",
            "Udziel pierwszej pomocy w granicach swoich umiejętności.",
            "Wezwij 112, poproś o wsparcie innego pracownika.",
            "Możliwie szybko zapewnij opiekę reszcie klasy.",
        ],
    )
    f.gap(12)
    f.strip("Nadzór adekwatny do okoliczności, nie absolutny. "
            "Zauważ, kiedy zwykła sytuacja przestaje być zwykła.")
    return f.render("fig-toaleta", title, desc), title, desc


def fig_woda() -> tuple[str, str, str]:
    title = "Picie i jedzenie na lekcji"
    desc = (
        "Kilka łyków wody z zamykanej butelki w zwykłej sali można traktować jako normalny element "
        "lekcji, o ile nie zakłóca pracy klasy. Posiłek przy ławce — kanapka, sałatka, napój w "
        "otwartym kubku — może poczekać do przerwy. Przy stanowisku komputerowym i w pracowni "
        "zawodowej nie stawiamy otwartych napojów; można odejść od stanowiska, napić się w "
        "bezpiecznym miejscu i wrócić do pracy. Wyjście z lekcji po jedzenie co do zasady nie jest "
        "potrzebne, a samowolne wyjście poza teren szkoły to osobna sprawa. Gdy uczeń jest blady, "
        "osłabiony lub ma zawroty głowy, zajmujemy się jego stanem zdrowia, a nie egzekwowaniem "
        "zasady, że na lekcji się nie je."
    )
    f = Fig(title, "Rozróżnij kilka łyków wody od posiłku — i jedno i drugie od złego samopoczucia.")
    f.card(
        tone="teal", heading="Tak, w zwykłej sali",
        bullets=[
            "Kilka łyków wody z zamykanej butelki i powrót do pracy.",
            "Warunek: nie zakłóca pracy klasy i nie stwarza zagrożenia.",
        ],
        foot="Statut nie zawiera ogólnego zakazu picia podczas lekcji.",
    )
    f.gap(10)
    f.card(
        tone="amber", heading="To poczeka do przerwy",
        bullets=[
            "Kanapka, sałatka, napój w otwartym kubku, posiłek przy ławce.",
            "Wyjście z lekcji po jedzenie — co do zasady nie ma takiej potrzeby.",
            "Samowolne wyjście poza teren szkoły to osobna sprawa.",
        ],
        foot="„Kanapkę zjesz na przerwie” nie kłóci się ze zgodą na wodę.",
    )
    f.gap(10)
    f.card(
        tone="blue", heading="Pracownia i stanowisko komputerowe",
        bullets=[
            "Nie stawiamy otwartych napojów przy sprzęcie.",
            "Można odejść od stanowiska, napić się i wrócić do pracy.",
        ],
        foot="To co innego niż zakaz picia przez całą lekcję.",
    )
    f.gap(10)
    f.card(
        tone="alert", heading="Uczeń blady, osłabiony, z zawrotami głowy",
        bullets=[
            "Zajmij się stanem zdrowia, nie egzekwowaniem zasady.",
            "Skierowanie do pielęgniarki w towarzystwie drugiej osoby.",
        ],
    )
    f.gap(12)
    f.strip("Czasem właściwą reakcją jest „nie”, czasem „tak”, a czasem trzeba odłożyć "
            "lekcję i zająć się uczniem.")
    return f.render("fig-woda", title, desc), title, desc


# --------------------------------------------------------------------------
# Wstawianie do artykułów
# --------------------------------------------------------------------------

ARTICLES = [
    # plik, builder, nagłówek przed którym wstawiamy figurę, podpis
    ("trudne-zachowania-na-lekcji.html", fig_trudne, "codzienne-sytuacje",
     "Od krótkiej wskazówki na lekcji, przez konsultację z zespołem, po wezwanie "
     "służb ratunkowych."),
    ("uczen-w-spektrum-autyzmu.html", fig_spektrum, "komunikacja",
     "Jak mówić, jakie warunki sprawdzić i co robić, gdy narasta przeciążenie."),
    ("integracja-klasy-na-poczatku-roku.html", fig_integracja, "codzienna-praca",
     "Przygotowanie wyjścia, przebieg spotkania, praca po powrocie oraz ćwiczenia, "
     "których nie proponujemy na pierwszym spotkaniu."),
    ("toaleta-podczas-lekcji-a-odpowiedzialnosc-nauczyciela.html", fig_toaleta,
     "wyjscie-na-lekcji",
     "Zwykła potrzeba fizjologiczna, złe samopoczucie i nagłe zagrożenie zdrowia "
     "wymagają różnych reakcji."),
    ("woda-na-lekcji-i-picie.html", fig_woda, "woda",
     "Co można zrobić w zwykłej sali, co poczeka do przerwy, co zmienia pracownia "
     "i kiedy liczy się tylko stan ucznia."),
]

START = "<!-- infografika:start -->"
END = "<!-- infografika:end -->"


def figure_html(svg: str, fid: str, title: str, caption: str) -> str:
    return (
        f'{START}\n'
        f'<figure class="guide-figure" id="{fid}">\n'
        f'<div class="guide-figure-frame">{svg}</div>\n'
        f'<figcaption class="guide-figure-caption">'
        f'<span class="guide-figure-label">Infografika</span> {esc(caption)}</figcaption>\n'
        f'<button class="guide-figure-open presentation-button secondary" type="button" '
        f'data-figure-open="{fid}">Powiększ infografikę</button>\n'
        f'</figure>\n'
        f'{END}'
    )


def inject(path: Path, block: str, before_id: str) -> str:
    t = path.read_text(encoding="utf-8")
    notes = []

    # arkusz stylów
    if 'href="guide-figures.css"' not in t:
        t = t.replace(
            '<link rel="stylesheet" href="integracja-klasy-polsko-ukrainskiej.css">',
            '<link rel="stylesheet" href="integracja-klasy-polsko-ukrainskiej.css">'
            '<link rel="stylesheet" href="guide-figures.css">', 1)
        notes.append("css")

    # skrypt podglądu
    if 'src="guide-figures.js"' not in t:
        t = t.replace('</body>', '<script src="guide-figures.js" defer></script>\n</body>', 1)
        notes.append("js")

    # sama figura
    if START in t:
        t = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, t, flags=re.S)
        notes.append("figura zaktualizowana")
    else:
        m = re.search(r'\n?[ \t]*<h2 id="' + re.escape(before_id) + r'"', t)
        if not m:
            raise SystemExit(f"{path.name}: nie znaleziono <h2 id=\"{before_id}\">")
        indent = re.match(r'\n?([ \t]*)', m.group(0)).group(1)
        t = t[:m.start()] + "\n" + indent + block.replace("\n", "\n" + indent) + t[m.start():]
        notes.append("figura wstawiona")

    path.write_text(t, encoding="utf-8")
    return ", ".join(notes)


def main() -> None:
    for name, builder, before_id, caption in ARTICLES:
        svg, title, _desc = builder()
        fid = re.search(r'aria-labelledby="([\w-]+)-t', svg).group(1)
        block = figure_html(svg, fid, title, caption)
        height = re.search(r'viewBox="0 0 \d+ ([\d.]+)"', svg).group(1)
        for base in (ROOT, ROOT / "materialy_lekcje_wychowawcze_2026_2027" / "strona_html"):
            path = base / name
            if path.exists():
                note = inject(path, block, before_id)
                where = "root" if base == ROOT else "strona_html"
                print(f"{name:52s} {where:12s} h={height:>6s}  {note}")


if __name__ == "__main__":
    main()
