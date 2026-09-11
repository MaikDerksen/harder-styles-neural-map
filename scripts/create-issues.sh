#!/usr/bin/env bash
# Legt die Tickets aus scripts/issues.json als GitHub-Issues an.
#
#   export GITHUB_TOKEN=ghp_...        # Scope: repo
#   ./scripts/create-issues.sh MaikDerksen/harder-styles-neural-map
#
# Ohne Argument wird das Remote "origin" des aktuellen Repos verwendet.
# Das Skript legt zuerst die Labels an (bereits vorhandene werden übersprungen)
# und danach die Issues. Mehrfaches Ausführen erzeugt doppelte Issues —
# GitHub kennt keine Idempotenz für Issue-Titel.

set -euo pipefail

cd "$(dirname "$0")/.."

REPO="${1:-}"
if [ -z "$REPO" ]; then
  REPO="$(git remote get-url origin 2>/dev/null \
    | sed -E 's#(git@github\.com:|https://github\.com/)##; s#\.git$##')"
fi
if [ -z "$REPO" ]; then
  echo "Kein Repository angegeben und kein origin-Remote gefunden." >&2
  echo "Aufruf: $0 <owner>/<repo>" >&2
  exit 1
fi

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "GITHUB_TOKEN ist nicht gesetzt. Token mit repo-Scope anlegen unter" >&2
  echo "https://github.com/settings/tokens und exportieren." >&2
  exit 1
fi

command -v jq >/dev/null || { echo "jq wird benötigt (brew/apt install jq)." >&2; exit 1; }

API="https://api.github.com"
AUTH=(-H "Authorization: Bearer $GITHUB_TOKEN"
      -H "Accept: application/vnd.github+json"
      -H "Content-Type: application/json"
      -H "X-GitHub-Api-Version: 2022-11-28")

echo "Repository: $REPO"

# --- Labels ---------------------------------------------------------------
# name:farbe:beschreibung
LABELS=(
  "daten:1D76DB:Datenbestand erweitern oder korrigieren"
  "recherche:5319E7:Hängt an einem Deep-Research-Lauf"
  "feature:0E8A16:Neue Funktion"
  "bug:D73A4A:Etwas stimmt nicht"
  "architektur:FBCA04:Struktur des Projekts"
  "performance:C2E0C6:Laufzeit und Ressourcen"
  "betrieb:006B75:Deployment und Hosting"
  "a11y:BFD4F2:Barrierefreiheit"
  "prio:hoch:B60205:Als Nächstes"
  "prio:mittel:E99695:Danach"
  "prio:niedrig:F9D0C4:Irgendwann"
)

echo "Labels anlegen …"
for entry in "${LABELS[@]}"; do
  name="${entry%%:*}"; rest="${entry#*:}"
  # "prio:hoch" enthält selbst einen Doppelpunkt — Sonderfall abfangen
  case "$entry" in
    prio:*) name="prio:${rest%%:*}"; rest="${rest#*:}" ;;
  esac
  color="${rest%%:*}"; desc="${rest#*:}"
  code=$(curl -sS -o /dev/null -w '%{http_code}' -X POST "$API/repos/$REPO/labels" \
    "${AUTH[@]}" \
    -d "$(jq -nc --arg n "$name" --arg c "$color" --arg d "$desc" \
          '{name:$n, color:$c, description:$d}')")
  case "$code" in
    201) echo "  + $name" ;;
    422) echo "  = $name (existiert)" ;;
    *)   echo "  ! $name (HTTP $code)" ;;
  esac
done

# --- Issues ---------------------------------------------------------------
count=$(jq 'length' scripts/issues.json)
echo "$count Issues anlegen …"

for i in $(seq 0 $((count - 1))); do
  payload=$(jq -c ".[$i] | {title, body, labels}" scripts/issues.json)
  title=$(jq -r ".[$i].title" scripts/issues.json)
  response=$(curl -sS -X POST "$API/repos/$REPO/issues" "${AUTH[@]}" -d "$payload")
  number=$(echo "$response" | jq -r '.number // empty')
  if [ -n "$number" ]; then
    echo "  #$number  $title"
  else
    echo "  FEHLER bei: $title" >&2
    echo "$response" | jq -r '.message // .' >&2
    exit 1
  fi
  sleep 1   # GitHub drosselt schnelle Schreibzugriffe
done

echo "Fertig: https://github.com/$REPO/issues"
