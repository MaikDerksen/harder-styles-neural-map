#!/usr/bin/env python3
"""Spielt die JSON-Ausgabe eines Deep-Research-Laufs in index.html ein.

    ./scripts/add-research.py data/research-uptempo-2026-09.json

Die Datei wird unverändert in den RESEARCH-Block von index.html gehängt.
Eingefaltet wird sie erst beim Laden der Seite durch applyResearch() —
so bleibt die Rohform mitsamt Quellenangaben nachvollziehbar und ein
späterer Lauf lässt sich neu einspielen, ohne die Stammdaten anzufassen.

Ein Lauf, der schon drin ist (gleicher scope + generated), wird ersetzt
statt doppelt angehängt.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

REQUIRED = ("artists", "labels", "festivals", "links")
KNOWN_TYPES = {"crew", "collab", "remix", "label", "b2b", "mc", "audience"}


def check(payload, name):
    """Meldet Auffälligkeiten, bricht aber nur bei echten Formatfehlern ab."""
    problems, notes = [], []

    if not isinstance(payload, dict):
        problems.append("Wurzelelement ist kein Objekt.")
        return problems, notes

    for field in REQUIRED:
        if field not in payload:
            notes.append(f"Feld '{field}' fehlt — wird als leer behandelt.")
        elif not isinstance(payload[field], list):
            problems.append(f"Feld '{field}' ist keine Liste.")

    for i, link in enumerate(payload.get("links") or []):
        if not isinstance(link, dict):
            problems.append(f"links[{i}] ist kein Objekt.")
            continue
        if not link.get("a") or not link.get("b"):
            problems.append(f"links[{i}] hat keine zwei Endpunkte.")
        t = link.get("type")
        if t not in KNOWN_TYPES:
            problems.append(f"links[{i}] hat unbekannten Typ {t!r}.")
        if link.get("confidence") == "estimate" and t != "audience":
            notes.append(
                f"links[{i}] ist eine Schätzung mit Typ {t!r} — "
                "wird beim Einfalten zu 'audience' umgehängt."
            )

    for i, art in enumerate(payload.get("artists") or []):
        if not art.get("name"):
            problems.append(f"artists[{i}] hat keinen Namen.")
        for t in art.get("tracks") or []:
            if not t.get("source"):
                notes.append(f"Track ohne Quelle: {art.get('name')} — {t.get('title')}")

    for i, fest in enumerate(payload.get("festivals") or []):
        if not fest.get("name"):
            problems.append(f"festivals[{i}] hat keinen Namen.")
        if not fest.get("stages"):
            notes.append(f"Festival ohne Bühnen: {fest.get('name')}")

    return problems, notes


def block_bounds(text):
    """Grenzen des RESEARCH-Arrays in index.html."""
    start = text.index("var RESEARCH = [")
    open_bracket = text.index("[", start)
    depth, i, in_str, quote, esc = 0, open_bracket, False, "", False
    while i < len(text):
        c = text[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                in_str = False
        elif c in "\"'":
            in_str, quote = True, c
        elif c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return open_bracket, i
        i += 1
    raise ValueError("RESEARCH-Block in index.html nicht gefunden.")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1

    text = INDEX.read_text(encoding="utf-8")
    start, end = block_bounds(text)
    inner = text[start + 1:end].strip()
    runs = json.loads("[" + inner + "]") if inner else []

    for path in argv[1:]:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        name = Path(path).name
        problems, notes = check(payload, name)

        for n in notes[:12]:
            print(f"  Hinweis: {n}")
        if len(notes) > 12:
            print(f"  … und {len(notes) - 12} weitere Hinweise")
        if problems:
            print(f"\n{name}: FEHLER, nichts eingespielt:", file=sys.stderr)
            for p in problems:
                print(f"  - {p}", file=sys.stderr)
            return 1

        stamp = (payload.get("scope"), payload.get("generated"))
        runs = [r for r in runs if (r.get("scope"), r.get("generated")) != stamp]
        runs.append(payload)

        counts = {f: len(payload.get(f) or []) for f in REQUIRED}
        print(f"  {name}: " + ", ".join(f"{v} {k}" for k, v in counts.items()))

    body = ",\n".join(json.dumps(r, ensure_ascii=False, indent=1) for r in runs)
    INDEX.write_text(text[:start + 1] + "\n" + body + "\n" + text[end:], encoding="utf-8")
    print(f"index.html aktualisiert — {len(runs)} Recherchelauf/-läufe eingebettet.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
