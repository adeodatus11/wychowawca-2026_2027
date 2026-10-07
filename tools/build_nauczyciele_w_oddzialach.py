"""Buduje dane do strony `nauczyciele-w-oddzialach.html`.

Źródła:
- wykaz podziałów na grupy (`wykaz-podzialow-grup.html`, stała REPORT) -
  przedmioty prowadzone w grupach wraz z nauczycielami,
- opcjonalnie `dane/nauczyciele-w-oddzialach-uzupelnienie.csv` -
  przedmioty prowadzone dla całego oddziału (kolumny: klasa;przedmiot;nauczyciel).

Wynik: `nauczyciele-w-oddzialach-dane.js` z obiektem `window.NAUCZYCIELE_W_ODDZIALACH`.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS_PAGE = ROOT / "wykaz-podzialow-grup.html"
SUPPLEMENT_CSV = ROOT / "dane" / "nauczyciele-w-oddzialach-uzupelnienie.csv"
OUTPUT = ROOT / "nauczyciele-w-oddzialach-dane.js"


def load_groups_report() -> dict:
    text = GROUPS_PAGE.read_text(encoding="utf-8")
    match = re.search(r"const REPORT = (\{.*?\});\n", text, re.S)
    if not match:
        raise SystemExit(f"Nie znaleziono danych REPORT w {GROUPS_PAGE.name}")
    return json.loads(match.group(1))


def load_supplement() -> list[dict]:
    if not SUPPLEMENT_CSV.exists():
        return []
    rows = []
    with SUPPLEMENT_CSV.open(encoding="utf-8-sig", newline="") as handle:
        sample = handle.read(2048)
        handle.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=";,\t")
        for row in csv.DictReader(handle, dialect=dialect):
            klasa = (row.get("klasa") or "").strip()
            przedmiot = (row.get("przedmiot") or "").strip()
            nauczyciel = (row.get("nauczyciel") or "").strip()
            if klasa and przedmiot:
                rows.append({"klasa": klasa, "przedmiot": przedmiot, "nauczyciel": nauczyciel})
    return rows


def build() -> dict:
    report = load_groups_report()
    supplement = load_supplement()
    classes: dict[str, dict[str, dict]] = {item["id"]: {} for item in report["classes"]}

    def add(class_id: str, subject: str, teacher: str, group: str | None, scope: str) -> None:
        subjects = classes.setdefault(class_id, {})
        entry = subjects.setdefault(subject.lower(), {"subject": subject, "scope": scope, "teachers": []})
        if scope == "grupy":
            entry["scope"] = "grupy"
        for existing in entry["teachers"]:
            if existing["name"] == teacher:
                if group and group not in existing["groups"]:
                    existing["groups"].append(group)
                return
        entry["teachers"].append({"name": teacher, "groups": [group] if group else []})

    for row in supplement:
        add(row["klasa"], row["przedmiot"], row["nauczyciel"], None, "klasa")

    for item in report["classes"]:
        for division in item["divisions"]:
            for group in division["groups"]:
                for subject in group["subjects"]:
                    for teacher in subject["teachers"] or [""]:
                        add(item["id"], subject["subject"], teacher, group["name"], "grupy")

    teachers = set()
    result = []
    for class_id in sorted(classes, key=lambda value: (value[:1], value)):
        subjects = sorted(classes[class_id].values(), key=lambda entry: (entry["scope"] != "klasa", entry["subject"].lower()))
        for entry in subjects:
            teachers.update(teacher["name"] for teacher in entry["teachers"] if teacher["name"])
        result.append({"id": class_id, "subjects": subjects})

    return {
        "sourceTitle": report.get("sourceTitle", ""),
        "hasWholeClassSubjects": bool(supplement),
        "classes": result,
        "stats": {
            "classes": len(result),
            "teachers": len(teachers),
        },
    }


def main() -> None:
    data = build()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    OUTPUT.write_text(
        "// Plik generowany przez tools/build_nauczyciele_w_oddzialach.py - nie edytuj ręcznie.\n"
        f"window.NAUCZYCIELE_W_ODDZIALACH = {payload};\n",
        encoding="utf-8",
    )
    print(f"Zapisano {OUTPUT.name}: {data['stats']['classes']} oddziałów, {data['stats']['teachers']} nauczycieli")


if __name__ == "__main__":
    main()
