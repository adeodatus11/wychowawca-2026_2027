from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from docx import Document


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "materialy_lekcje_wychowawcze_2026_2027" / "strona_html"


@dataclass(frozen=True)
class DocumentPageConfig:
    source_docx: Path
    output_html: Path
    title: str


DEFAULT_CONFIG = DocumentPageConfig(
    source_docx=ROOT / "wytyczne_wych_uczn_1_wrzes_2026_ost.docx",
    output_html=ROOT / "wytyczne-na-spotkanie-z-uczniami-1-wrzesnia-2026.html",
    title="Wytyczne na spotkanie z uczniami 1 września - wersja do teczki wychowawców",
)


def slug_class(value: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", value.lower()).strip("-") or "unknown"


def paragraph_num_info(paragraph):
    ppr = paragraph._p.pPr
    if ppr is None or ppr.numPr is None:
        return None
    num = ppr.numPr
    num_id = num.numId.val if num.numId is not None else None
    ilvl = num.ilvl.val if num.ilvl is not None else 0
    return str(num_id), int(ilvl)


def run_html(run) -> str:
    parts: list[str] = []
    for child in run._r:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "t":
            parts.append(html.escape(child.text or "").replace("\xa0", "&nbsp;"))
        elif tag == "tab":
            parts.append("\t")
        elif tag in {"br", "cr"}:
            parts.append("<br>")
    text = "".join(parts)
    if not text:
        return ""
    if run.bold:
        text = f"<strong>{text}</strong>"
    if run.italic:
        text = f"<em>{text}</em>"
    if run.underline:
        text = f"<u>{text}</u>"
    return text


def paragraph_html(paragraph, main_counter: int) -> tuple[str, int]:
    content = "".join(run_html(run) for run in paragraph.runs)
    if not content:
        content = "&nbsp;"

    classes = ["word-paragraph"]
    style_name = slug_class(paragraph.style.name)
    classes.append(f"style-{style_name}")

    alignment = paragraph.alignment
    if alignment is not None:
        classes.append(f"align-{slug_class(alignment.name)}")

    num_info = paragraph_num_info(paragraph)
    marker = ""
    if num_info:
        num_id, level = num_info
        classes.extend([f"num-{num_id}", f"level-{level}"])
        if num_id == "2" and level == 0:
            main_counter += 1
            marker = f"{main_counter}."
            classes.append("main-number")
        elif level >= 1:
            marker = "•"
            classes.append("sub-bullet")
        else:
            marker = "•"
            classes.append("word-bullet")
    else:
        left = paragraph.paragraph_format.left_indent
        if left is not None and left.pt and left.pt > 0:
            classes.append("manual-indent")

    if marker:
        body = f'<span class="word-marker">{html.escape(marker)}</span><span class="word-text">{content}</span>'
    else:
        body = f'<span class="word-text">{content}</span>'
    return f'<p class="{" ".join(classes)}">{body}</p>', main_counter


def build_document_body(source_docx: Path) -> str:
    doc = Document(source_docx)
    paragraphs: list[str] = []
    counter = 0
    for paragraph in doc.paragraphs:
        rendered, counter = paragraph_html(paragraph, counter)
        paragraphs.append(rendered)
    return "\n".join(paragraphs)


def build_page(config: DocumentPageConfig) -> str:
    document_body = build_document_body(config.source_docx)
    title = html.escape(config.title)
    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="wytyczne-document.css">
</head>
<body class="document-view-body">
  <header class="doc-site-header">
    <a class="doc-brand" href="index.html" aria-label="Wróć do strony głównej">
      <img src="assets/logo-school-master-full.png" alt="Szkoła Mistrzów - Zespół Szkół Zawodowych nr 5 we Wrocławiu" width="1931" height="301">
    </a>
    <nav class="doc-actions" aria-label="Akcje dokumentu">
      <a class="doc-action" href="index.html">Wróć do materiałów</a>
      <a class="doc-action primary" href="{config.source_docx.name}" download>Pobierz dokument Word</a>
    </nav>
  </header>
  <main class="doc-page-shell">
    <section class="doc-hero" aria-labelledby="doc-title">
      <p class="kicker">Dokument do pobrania i wglądu</p>
      <h1 id="doc-title">{title}</h1>
      <p>Treść poniżej została odtworzona bezpośrednio z pliku Word. Oryginał można pobrać przyciskiem „Pobierz dokument Word”.</p>
    </section>
    <article class="word-document" aria-label="{title}">
      {document_body}
    </article>
  </main>
</body>
</html>
"""


def generate_page(config: DocumentPageConfig) -> None:
    if not config.source_docx.exists():
        raise FileNotFoundError(config.source_docx)
    config.output_html.write_text(build_page(config), encoding="utf-8")
    SITE.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config.output_html, SITE / config.output_html.name)
    shutil.copy2(config.source_docx, SITE / config.source_docx.name)


def main(config: DocumentPageConfig | None = None) -> None:
    generate_page(config or DEFAULT_CONFIG)


if __name__ == "__main__":
    main()
