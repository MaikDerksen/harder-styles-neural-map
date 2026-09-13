# Harder Styles Neural Map

Eine interaktive Netzwerkkarte der Harder-Styles-Szene in den Niederlanden,
Belgien und Deutschland — Hardstyle, Raw, Hardcore, Uptempo, Frenchcore,
Terror, Zaag und Early/Millennium. Acts und Festivals sind Knoten, ihre
Beziehungen sind Kanten. Man klickt sich vom Bekannten ins Unbekannte.

**Aktueller Stand:** 666 Acts · 17 Festivals · rund 1.970 Verbindungen.

## Öffnen

`index.html` ist eine einzelne, in sich geschlossene Datei ohne Build-Schritt
und ohne Abhängigkeiten außer den Google Fonts. Im Browser öffnen genügt:

```
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

Für eine geteilte Version reicht GitHub Pages (Settings → Pages → Branch
`main`, Ordner `/`) — dann liegt die Karte unter
`https://<user>.github.io/harder-styles-neural-map/`.

## Was die Karte kann

**Fokussieren.** Ein Klick auf einen Act rückt ihn ins Zentrum, seine direkten
Verbindungen fächern sich auf einem Ring auf, Signalimpulse laufen über die
Kanten. Der nächste Klick geht eine Ebene tiefer; der Pfad oben links zeigt
die Route und springt auf Klick zurück.

**Eigene Rotation.** Wer die Seite öffnet, markiert seine eigenen Acts. Die
Auswahl liegt im `localStorage` des Browsers, verlässt das Gerät nicht und
steuert Hervorhebungen und Empfehlungen. Ein Knopf lädt ein Uptempo-Starterpack.

**Empfehlungen.** Für jeden nicht markierten Act wird eine Nähe zur eigenen
Auswahl berechnet: gewichtete Summe der direkten Kanten plus ein Bonus für
gemeinsam bespielte Festivals. Die Begründung steht in der Liste dabei.

**Filtern.** Zwölf Genres, sechs Kantentypen, Festival-Knoten und ein Schalter
„nur vernetzter Kern" (blendet Acts aus, die nur einmal auf einem Line-up
stehen — von 666 bleiben rund 400).

**Festivals lesen.** Jedes Festival hat ein eigenes Panel mit Line-up nach
Bühne, Genre-Mix und der Angabe, wie viele der eigenen Acts dort spielen.

## Kantentypen

| Typ | Bedeutung | Belegt? |
|---|---|---|
| Inner Circle | festes Duo oder Live-Projekt | ja |
| Track zusammen | gemeinsamer Release | ja |
| B2B / vs | gemeinsames Set auf einem Line-up | ja |
| Gleiches Label | gemeinsames Zuhause | ja |
| Spielt dort | Act steht auf dem Line-up | ja |
| Hörer-Nähe | Szene-Einschätzung | **nein — Schätzung** |

Hörer-Nähe-Kanten sind gestrichelt gezeichnet und im Panel als Einschätzung
gekennzeichnet. Es sind keine Streaming-Daten; solche Daten liegen hier nicht
vor und werden auch nicht simuliert.

## Wie die Daten entstehen

Die Line-ups stehen im Quelltext so, wie sie angekündigt wurden — inklusive
`"Nosferatu & Tha Playah"` oder `"Dimitri K & MC Robs"`. Beim Laden zerlegt
die Seite solche Einträge in einzelne Acts und legt zwischen ihnen eine
B2B-Kante an; mehrfach gespielte Paarungen werden hochgezählt. Namen mit
kaufmännischem Und, die einen einzigen Act bezeichnen (`D-Block & S-te-Fan`,
`DJ Rob & MC Joe`), stehen auf einer Ausnahmeliste.

Schreibweisen werden über eine Normalisierung und eine Alias-Tabelle
zusammengeführt, weil Line-up-Listen uneinheitlich sind (`lekkerfaces`,
`F.Noize`, `NoiseFlow`).

### Quellen

Vollständige Line-ups: Defqon.1 2025 (alle 13 Bühnen), Dominator 2025,
Decibel Outdoor 2025, Intents 2025 und 2026, Syndicate 2025. Teilweise:
Masters of Hardcore 2025 und 2026, REBiRTH 2025, BKJN 2026, HARDFEST,
Toxicator 2025, LET'S GET HYPER 2026, Battle of Uptempo, Uptempo Poison,
Snakepit 2025, BKJN vs. Partyraiser Snowfall 2026, DETOUR 2025,
The Prophecy Uptempo Edition 2025.

Tracks, Labels und Studio-Achsen aus Beatport, Discogs, SoundCloud und
Szene-Presse (hardnews.nl, hardstyle.com, hardstylemag.com).

Die Rohausgaben der Rechercheläufe liegen unverändert in [`data/`](data) und
stecken zusätzlich im `RESEARCH`-Block von `index.html`. Beim Laden faltet
`applyResearch()` sie in die Stammdaten ein — so bleibt jede Angabe auf ihre
Quelle zurückführbar, und ein neuer Lauf lässt sich mit
`scripts/add-research.py` nachschieben, ohne die Stammdaten anzufassen.
Schlüsseltracks aus der Recherche tragen im Panel einen Quellenlink.

Rund 65 Acts haben ein recherchiertes Profil mit Biografie, Labels und
Schlüsseltracks. Alle übrigen führen nur, was aus Line-ups und belegten
Releases hervorgeht — und sagen das im Panel auch. Lieber eine dünne Karte
als eine erfundene Biografie.

## Auf den eigenen Server bringen

Gleiche Einrichtung wie beim Speisekarte-Trainer, nur auf Port **8084**
(8083 ist dort belegt).

```bash
docker compose up -d --build            # lokal → http://localhost:8084
```

Multi-Arch-Image bauen und veröffentlichen — beide Architekturen zwingend,
sonst startet es auf dem Raspberry Pi nicht (`exec format error`):

```bash
docker buildx build --platform linux/amd64,linux/arm64 \
  -t maik05/harder-styles-neural-map:latest --push .
```

Auf dem NAS (OpenMediaVault → Dienste → Compose) den Stack aus
[`deploy/harder-styles.yml`](deploy/harder-styles.yml) anlegen, im Reverse
Proxy einen Host auf `<SERVER-IP>:8084` zeigen lassen. Ein Volume braucht es
nicht: Die eigene Rotation liegt im Browser, der Container ist zustandslos.

Für die öffentliche Variante:

```bash
vercel deploy --prod --yes
```

`vercel.json` schaltet den Build ab und setzt `no-cache`. Zu beachten: Der
`localStorage` hängt an der Domain — die Rotation auf Vercel und auf dem
eigenen Server sind getrennte Stände.

## Tickets

Der Backlog steht in [`BACKLOG.md`](BACKLOG.md), maschinenlesbar in
[`scripts/issues.json`](scripts/issues.json). Als GitHub-Issues anlegen:

```bash
export GITHUB_TOKEN=ghp_...
./scripts/create-issues.sh MaikDerksen/harder-styles-neural-map
```

## Daten erweitern

Zwei Aufträge liegen bereit. Für einen einzelnen Recherchelauf:
[`RESEARCH-PROMPT-UPTEMPO.md`](RESEARCH-PROMPT-UPTEMPO.md) — ein
in sich geschlossener Prompt, der nur Uptempo abdeckt und von den Festivals
nur die Uptempo-Bühnen mitnimmt. Klein genug, dass ein Deep-Research-Tool
ihn zu Ende bringt.

`RESEARCH-PROMPT.md` ist der vollständige Auftrag über die ganze Szene, deren
JSON-Ausgabe direkt in dieses Datenmodell passt: Systemauftrag mit Regeln
gegen erfundene Fakten, vollständiges Ausgabeschema, Genre- und
Kantentyp-Enums sowie acht thematische Arbeitspakete. Der Abschnitt am Ende
listet den aktuellen Bestand und die größten Lücken.

Die Datenblöcke im Quelltext von `index.html` sind kommentiert und in dieser
Reihenfolge aufgebaut:

| Block | Inhalt |
|---|---|
| Teil 1 | `FEST` — Festivals mit Line-ups nach Bühne |
| Teil 2 | `GENRE`, `COUNTRY` — Zuordnung der Acts |
| Teil 3 | `META`, `ALIAS`, `LINKS`, `DIRECTORY` — Profile und kuratierte Kanten |
| Teil 3b | `RESEARCH` — Rohausgaben der Deep-Research-Läufe |
| Teil 4 | `applyResearch()`, Graph-Aufbau, Normalisierung, Scoring |
| Teil 5 | Physik und Rendering (Canvas, eigene Force-Simulation) |
| Teil 6 | Interaktion und Panel |

Neue Acts brauchen keinen Eintrag: Wer in einem Line-up auftaucht, wird
automatisch zum Knoten. `META` ergänzt nur das, was darüber hinausgeht.
