# Backlog

Die Tickets zu diesem Projekt. Maschinenlesbar liegen sie in
[`scripts/issues.json`](scripts/issues.json); mit
[`scripts/create-issues.sh`](scripts/create-issues.sh) landen sie als
GitHub-Issues im Repository:

```bash
export GITHUB_TOKEN=ghp_...
./scripts/create-issues.sh MaikDerksen/harder-styles-neural-map
```

Wer einen anderen Tracker nutzt, importiert `issues.json` — Titel, Text und
Labels stehen dort in einer Form, die jedes System frisst.

---

## Als Nächstes

### Zoom und Pan im Graphen

`feature`

Der Graph hat aktuell keine Kameraführung: Man kann weder zoomen noch verschieben. Bei 592 Knoten ist die Übersicht dadurch nur begrenzt lesbar, und auf dem Handy fehlt die Bedienbarkeit fast völlig — Pinch-to-Zoom greift nicht, weil `touch-action: none` auf dem Canvas liegt.

**Zu tun**
- Transform-Matrix (Skalierung + Offset) vor das Rendering ziehen und in `pick()` invers anwenden, damit Klickziele weiter stimmen.
- Mausrad zoomt auf den Cursor, Drag verschiebt, Doppelklick auf leere Fläche setzt zurück.
- Touch: ein Finger verschiebt, zwei Finger zoomen.
- Beim Fokussieren eines Knotens die Kamera weich auf ihn fahren, statt nur das Layout umzubauen.

**Fertig, wenn** die Karte auf einem 400-px-Display mit den Fingern bedienbar ist und die Trefferflächen bei jedem Zoomlevel sitzen.

### Dubletten und Alias-Kollisionen bereinigen

`daten` · `bug`

Die Line-up-Listen sind uneinheitlich geschrieben, die Normalisierung in `key()` fängt nur Punkte, Apostrophe, Bindestriche und Leerzeichen ab. Dadurch stehen mutmaßlich mehrere Acts doppelt im Graphen.

**Bekannte Verdachtsfälle**
- `Noxious` (Intents) gegen `Noxiouz` — vermutlich derselbe Act, aktuell per ALIAS zusammengeführt, aber ungeprüft.
- `Dr Z` gegen `Dr. Z-Vago` — vermutlich zwei verschiedene Acts, aktuell getrennt, ebenfalls ungeprüft.
- `Brunze` / `Bruhze`, `FLO` / `MC Flo`, `Vandalism` / `Vandal!sm`, `Darkraver` / `The Darkraver`, `UDOW` / `Udow`.

**Zu tun**
- Skript, das alle Knoten mit Levenshtein-Abstand ≤ 2 oder gleichem Soundex paarweise ausgibt.
- Jeden Treffer gegen Beatport oder die eigenen Kanäle des Acts prüfen.
- Ergebnis in `ALIAS` eintragen — oder bewusst als getrennt markieren, damit der nächste Durchlauf nicht wieder darüber stolpert.

**Fertig, wenn** die Liste abgearbeitet ist und für jeden Verdachtsfall eine belegte Entscheidung dokumentiert ist.

### Recherche-Paket A einspielen: Festival-Line-ups 2024–2026

`daten` · `recherche`

Die Datenbank kennt praktisch nur das Jahr 2025 und 13 Festivals. `RESEARCH-PROMPT.md`, Paket A, deckt die fehlenden Häuser und Jahrgänge ab.

**Zu tun**
- Paket A an ein Deep-Research-Tool geben, Ergebnis als JSON zurückholen.
- Namen gegen den Bestand abgleichen (siehe Ticket zu Alias-Kollisionen), dann in den `FEST`-Block übernehmen.
- Line-up-Schreibweisen unverändert lassen — die B2B-Kanten entstehen daraus automatisch.

**Fertig, wenn** Qlimax, Q-BASE, Thunderdome, Emporium, Supremacy, Shockerz, Ground Zero, The Qontinent und Reverze als Knoten mit Line-up drin sind.

### Recherche-Paket B einspielen: Uptempo-Diskografien

`daten` · `recherche`

Die größte inhaltliche Lücke. „Wer mit wem wie oft" entsteht ausschließlich aus gemeinsamen Releases, und außerhalb des Uptempo-Kerns fehlen die fast vollständig — es gibt rund 90 handrecherchierte Verbindungen für über 590 Acts.

**Zu tun**
- Paket B aus `RESEARCH-PROMPT.md` laufen lassen.
- Aus den Credits pro Paar zählen, wie viele gemeinsame Releases belegt sind, und daraus `weight = min(5, count + 1)` setzen.
- `LINKS` erweitern, `META` für die neu profilierten Acts ergänzen.

**Fertig, wenn** jeder Act mit mindestens drei Festivalauftritten entweder belegte Collab-Kanten hat oder in `gaps` dokumentiert ist.

### Multi-Arch-Image bauen und auf dem NAS ausrollen

`betrieb`

Deploy-Dateien liegen bereit (`Dockerfile`, `nginx.conf`, `docker-compose.yml`, `deploy/harder-styles.yml`), sind aber noch nie gebaut oder ausgerollt worden.

**Zu tun**
```bash
docker buildx build --platform linux/amd64,linux/arm64 \
  -t maik05/harder-styles-neural-map:latest --push .
```
- Auf dem NAS `deploy/harder-styles.yml` als Compose-Stack anlegen (Port 8084, 8083 ist belegt).
- Reverse Proxy: Host auf `<SERVER-IP>:8084`.
- Healthcheck und Neustartverhalten einmal prüfen.

**Fertig, wenn** die Karte im Heimnetz unter ihrem eigenen Hostnamen läuft.

## Danach

### Recherche-Paket G einspielen: B2B-Sets und Live-Projekte

`daten` · `recherche`

B2B-Kanten entstehen bisher nur aus den 13 erfassten Line-ups. Paket G sucht systematisch nach gemeinsamen Sets 2022–2026 und nach benannten Live-Formationen.

**Zu tun**
- Paket G laufen lassen.
- Live-Projekte als `projects`-Einträge übernehmen und als `crew`-Kanten abbilden (Slaughterhouse, Combined Forces, Pizzeria, Gunz for Hire und was sonst gefunden wird).
- Mehrfach gespielte Paarungen hochzählen statt doppelt anzulegen.

**Fertig, wenn** die Rangliste „häufigste B2B-Paarungen" auf mehr als einer Festivalsaison beruht.

### Recherche-Paket F einspielen: die deutsche Szene

`daten` · `recherche`

Deutschland ist deutlich unterrepräsentiert: 17 Acts, zwei Festivals, eine Clubreihe. Für eine Karte, die NL **und** DE abbilden soll, ist das zu dünn.

**Zu tun**
- Paket F laufen lassen: deutsche Produzenten, Labels, Veranstalter, die Zaag-Welle und die historische Achse Frankfurt–Rotterdam.
- Prüfen, ob die Genre-Zuordnung `zaag` für die deutschen Acts trägt oder ob eine eigene Kategorie sinnvoller ist.

**Fertig, wenn** die deutsche Seite des Graphen ohne den Umweg über Dr Donk mit dem niederländischen Kern verbunden ist.

### Labels als eigene Knotenebene

`feature` · `daten`

Labels sind aktuell nur Textfelder in `META` und ein Kantentyp. Als eigene Knoten würden sie dasselbe leisten wie die Festivals: Struktur ins Layout bringen und einen zweiten Navigationsweg öffnen (Black Reaper → Roster → Acts).

**Zu tun**
- Recherche-Paket E einspielen.
- Dritten Knotentyp `label` einführen, eigene Form (Quadrat), eigener Filter.
- `label`-Kanten paarweise durch Act→Label ersetzen, sonst explodiert die Kantenzahl.
- Panel für Labels: Gründung, Gründer, Roster, Sublabels, Genre-Mix.

**Fertig, wenn** man von einem Act über sein Label zu Roster-Kollegen navigieren kann.

### Daten aus index.html in eine data.json auslagern

`architektur`

`index.html` ist auf 110 KB gewachsen, davon ist der größte Teil Datenblock. Mit den Recherchepaketen wird das schnell mehr. Daten und Code in einer Datei zu mischen macht Diffs unlesbar und Merges riskant.

**Zu tun**
- `FEST`, `META`, `LINKS`, `GENRE`, `COUNTRY`, `ALIAS`, `DIRECTORY` nach `data.json` ziehen.
- Beim Laden per `fetch` holen; da die Seite auch als Artifact und als `file://` läuft, einen Fallback vorsehen (eingebettetes `<script type="application/json">` beim Build).
- Kleines Build-Skript, das `data.json` für die Single-File-Auslieferung wieder einbettet.

**Fertig, wenn** ein Datenupdate ein Diff in `data.json` ist und der Code unberührt bleibt.

### Eigene Rotation über URL teilbar machen

`feature`

Die Auswahl liegt im `localStorage` und bleibt damit auf einem Gerät. Wer seine Rotation jemandem zeigen will, kann es nicht — genau das ist aber der naheliegende Anwendungsfall („schau mal, was ich höre und was mir empfohlen wird").

**Zu tun**
- Auswahl als `?acts=a,b,c` in die URL schreiben (Kurz-IDs, nicht die vollen Namen).
- Beim Laden: URL-Parameter hat Vorrang vor `localStorage`, wird aber nicht automatisch gespeichert — sondern per Knopf „übernehmen".
- Teilen-Knopf, der die URL in die Zwischenablage legt.

**Fertig, wenn** ein geteilter Link beim Empfänger dieselbe Hervorhebung und dieselben Empfehlungen zeigt.

### Vercel-Deployment einrichten

`betrieb`

`vercel.json` und `.vercelignore` liegen bereit, analog zum Speisekarte-Trainer.

**Zu tun**
- `vercel deploy --prod --yes` aus dem Projektverzeichnis.
- Prüfen, ob die Google-Fonts unter der Vercel-Domain laden; falls nicht, Fallback-Stack kontrollieren.
- Link in die README eintragen.

**Hinweis:** Der `localStorage` hängt an der Domain. Die Rotation auf Vercel und auf dem eigenen Server sind getrennte Stände — dasselbe Verhalten wie beim Speisekarte-Trainer.

## Irgendwann

### Abstoßung auf Barnes-Hut umstellen

`performance`

Die Kräfteberechnung ist O(n²) über alle sichtbaren Knoten. Mit dem Kern-Filter sind das rund 320 Knoten und damit etwa 51.000 Paare pro Frame — noch tragbar. Ohne Filter sind es 592 Knoten und 175.000 Paare, und auf schwächeren Geräten ruckelt es.

**Zu tun**
- Quadtree aufbauen und Barnes-Hut mit θ ≈ 0,9 verwenden.
- Alternativ: Kräfte nur alle zwei Frames neu berechnen und dazwischen interpolieren.
- Vorher messen, damit hinterher belegbar ist, dass es etwas gebracht hat.

**Fertig, wenn** die Vollansicht auf einem Mittelklasse-Handy flüssig läuft.

### Zeitfilter über Festival-Editionen

`feature`

Sobald mehrere Jahrgänge in der Datenbank sind (Paket A), braucht es einen Weg, sie zu trennen — sonst verschmelzen fünf Jahre Szenegeschichte zu einem Bild.

**Zu tun**
- Jahr an `plays`- und `b2b`-Kanten hängen.
- Jahresschieber oder Jahres-Chips in der Filterleiste.
- Interessant wird die Bewegung: welche Acts kommen dazu, welche verschwinden.

**Fertig, wenn** man 2023 und 2026 nebeneinander vergleichen kann.

### Tastaturbedienung und Screenreader-Zugang

`a11y`

Der Graph ist reines Canvas und damit für Tastatur und Screenreader nicht existent. Panel, Filter und Suche sind bedienbar, der Kern der Anwendung nicht.

**Zu tun**
- Verstecktes, aber fokussierbares Listen-Pendant zum Graphen (`aria-hidden` nur auf dem Canvas).
- Pfeiltasten springen zwischen Nachbarn des fokussierten Knotens, Enter fokussiert.
- `aria-live` meldet den Fokuswechsel.

**Fertig, wenn** man die Karte ohne Maus vollständig erkunden kann.

### Recherche-Paket H einspielen: Anthems und Charts

`daten` · `recherche`

Chartplatzierungen und Festival-Anthems sind bisher Einzelfälle in den Profiltexten. Als eigene Datenebene machen sie sichtbar, wer die Szene in welchem Jahr geprägt hat.

**Zu tun**
- Paket H laufen lassen (MOH Top 100 2020–2025, Anthem-Historie 2015–2026).
- Anthems am Act und am Festival anzeigen.
- Überlegen, ob Chartplatzierungen in die Knotengröße einfließen sollen — oder ob das die Karte verzerrt.

