# Deep-Research-Auftrag: nur Uptempo

Ausschnitt aus [`RESEARCH-PROMPT.md`](RESEARCH-PROMPT.md), zugeschnitten auf
**einen einzigen Recherchelauf**. Der große Auftrag deckt acht Arbeitspakete
über die gesamte Harder-Styles-Szene ab — dafür bricht jedes Deep-Research-Tool
vorher ab. Dieser hier bleibt bei Uptempo und nimmt von den Festivals nur die
Uptempo-Bühnen mit.

**So benutzen:** Den Block unten komplett kopieren und als einzigen Prompt
abschicken. Er ist in sich geschlossen, es muss nichts vorangestellt werden.
Ergebnis als `.json` speichern und mir in den Chat legen.

Wenn die Ausgabe abgeschnitten wird: „mach bei `<letztes Objekt>` weiter,
gleiches Format, nur die restlichen Einträge."

---

````
Du recherchierst für eine Datenbank über UPTEMPO HARDCORE (180–220 BPM),
Schwerpunkt Niederlande, Belgien, Deutschland und Italien. Du schreibst keine
Reportage, sondern füllst eine Datenbank. Ausgabe ist ausschließlich JSON.

WICHTIG ZUR ABGRENZUNG
Nur Uptempo. Hardstyle, Raw, Mainstream-Hardcore, Frenchcore und Terror
interessieren nur dort, wo sie einen Uptempo-Act berühren — also als
Kollaborationspartner, Labelkollege oder B2B-Partner. Nimm keine reinen
Hardstyle-Line-ups auf.

Bei Festivals interessiert AUSSCHLIESSLICH die Uptempo-Bühne. Defqon.1 hat
370 Acts; davon brauche ich die rund 30 der YELLOW-Stage und sonst keinen.

HARTE REGELN — wichtiger als Vollständigkeit
1. Jede Tatsachenbehauptung braucht eine Quelle mit URL. Ohne Beleg bleibt das
   Feld leer oder null. Rate nie.
2. Erfinde keine Tracks, Line-up-Namen, Labels, Jahreszahlen oder bürgerlichen
   Namen. Was du nicht findest, kommt ans Ende in "gaps".
3. Einschätzungen ausschließlich als Kante vom Typ "audience" mit
   "confidence": "estimate". Alles andere ist belegt oder existiert nicht.
4. Line-up-Einträge gibst du EXAKT wieder, wie sie angekündigt wurden —
   "A vs B", "A & B", "A pres. Show", "A LIVE". Nicht vereinheitlichen: aus
   dieser Schreibweise werden später die B2B-Verbindungen erzeugt.
5. Ein Act mit mehreren Schreibweisen bekommt einen kanonischen Namen (den,
   den er selbst auf SoundCloud/Instagram/Beatport benutzt) und alle Varianten
   in "aliases".
6. Widersprüchliche Quellen: primäre gewinnt (Festivalseite, Label, Beatport,
   Discogs), Widerspruch in "notes" vermerken.
7. Keine Einleitung, keine Zusammenfassung. Nur der JSON-Block.

REIHENFOLGE — arbeite strikt von oben nach unten
Falls dein Budget ausgeht, ist ein vollständig belegter oberer Teil mehr wert
als eine angefangene Gesamtabdeckung.

1. KOLLABORATIONEN. Für die 25 wichtigsten Uptempo-Acts jede belegte
   gemeinsame Veröffentlichung der letzten fünf Jahre: Titel, alle Credits,
   Label, Datum. Das ist der Kern des Auftrags — die Datenbank misst daran,
   wer mit wem wie oft arbeitet.
2. LABELS. Uptempo-Labels mit Gründungsjahr, Gründer und aktuellem Roster:
   Black Reaper Records, Partyraiser Recordings, Uptempo Hardcore Records,
   Barbaric Records, Triple Six Records, Darkside Unleashed, Uptempo Is The
   Tempo Records, Gabberecords, Footworxx, Afterlife — plus was du sonst
   findest.
3. UPTEMPO-BÜHNEN der großen Festivals, Jahrgänge 2024, 2025, 2026:
   Defqon.1 (YELLOW), Dominator (The Zoo by Snakepit), Decibel Outdoor
   (Uptempo-Bühne inkl. der SAVAGE-Marathon-Sets), Intents (Uptempo-Areas),
   Masters of Hardcore (Masters of Extreme Hardcore), REBiRTH (RESiST),
   HARDFEST (Lucify), Syndicate Dortmund (Uptempo-Floor), Ground Zero,
   Hardshock, Pandemonium, Emporium, Q-BASE, Thunderdome, The Qontinent.
   Hat ein Festival keine Uptempo-Bühne, lass es weg statt es zu erwähnen.
4. REINE UPTEMPO-EVENTS, komplettes Line-up:
   BKJN Festival, Uptempo Is The Tempo, Snakepit, Battle of Uptempo,
   LET'S GET HYPER, Uptempo Poison, Hard Impact — und suche aktiv nach
   weiteren, gerade in Deutschland. Dort ist die Datenlage am dünnsten.
5. PROFILE für Acts, die unten in der Startliste stehen: Land, Stadt, aktiv
   seit, Labels, Live-Formationen und Alias-Projekte, zwei bis vier Sätze
   Beschreibung.
6. B2B-PAARUNGEN 2022–2026 aus Timetables, Clashfindern und Ankündigungen.
   Eine Kante pro Paarung, "count" = Anzahl belegter gemeinsamer Sets.
7. Falls noch Luft ist: Masters of Hardcore Top 100 der Jahre 2024 und 2025,
   jeweils die Top 30, aber nur die Uptempo-Einträge.

STARTLISTE — 64 Acts, die schon in der Datenbank stehen
Für diese fehlen vor allem Diskografien und Profile. Die Liste ist
unvollständig: Ergänze aktive Uptempo-Acts, die fehlen.

Lekkerfaces, The Dark Horror, Yoshiko, Mind Compressor, Noxiouz, Satirized,
Dimitri K, Partyraiser, Spitnoise, Abaddon, Angernoizer, Major Conspiracy,
Gezellige Uptempo, Kili, Kemal, Roosterz, Revealer, Bössels, Pinotello,
TukkerTempo, Dynamic Noise, Repix, Sjammienators, Vandal!sm, Ditzkickz,
Het Pompstation, Tomsku, The Dope Doctor, Kroefoe, Unlocked, S-Kill, Spiady,
Guizcore, Trespassed, Jur Terreur, Lil Texas, F. Noize, MT, TMO, Revellers,
STV, Aradia, Estasia, Neko, Opgekonkerd, Terrorclown, NSD, Illuszion,
Invaderz, Triple Six, Mad Sin, Catnip, Dr Evil, Papero, Vandal, Wakan,
Broodje, Elitepauper, XEPTOR, Sakyra, Antenora, Toza, Xterminate, Røza

Grenznah, aber relevant, weil eng verbunden: Deadly Guns, Unproven, Akimbo,
Samynator, Bulletproof, Juliëx, Namara, Elite Enemy, Manifest Destiny, DRS,
Cryogenic, Irradiate, Soulblast, Barber, Tharken, Eraized, Screecher, UDOW,
Aalst, Rosbeek, Complex, Amigo, Tharoza.

UMFANG
Höchstens 120 Acts. Lieber 40 sauber belegte als 120 geratene.

QUELLEN, in dieser Reihenfolge
- Festival- und Veranstalterseiten: q-dance.com, artofdance.nl, b2s.nl,
  intentsfestival.nl, rebirthfestival.nl, bkjn.nl, hardfest.nl, i-motion.de
- Release-Datenbanken: beatport.com, discogs.com, musicbrainz.org,
  hardtunes.com, bandcamp
- Szene-Presse: hardnews.nl, hardstyle.com, hardstylemag.com, hardcultr.com,
  partyflock.nl
- Sets und Timetables: 1001tracklists.com, clashfinder, edm.fandom.com
- Kanäle der Acts: SoundCloud, Spotify (Credits!), YouTube, Instagram
Wikipedia nur als Einstieg, nie als alleinige Quelle.

AUSGABEFORMAT — genau dieses JSON, ein einziger Codeblock

{
  "scope": "uptempo",
  "generated": "JJJJ-MM-TT",
  "artists": [
    {
      "name": "Lekkerfaces",
      "aliases": ["lekkerfaces"],
      "real_name": null,
      "country": "IT",
      "city": null,
      "active_since": 2022,
      "genres": ["uptempo"],
      "labels": ["Black Reaper Records", "Partyraiser Recordings"],
      "projects": [
        {"name": "Pizzeria", "members": ["Lekkerfaces", "Mind Compressor"],
         "kind": "live", "source": "https://..."}
      ],
      "bio_de": "2 bis 4 Sätze, sachlich, nur Belegtes, keine Werbesprache.",
      "tracks": [
        {"title": "FA TI CO",
         "credits": ["Lekkerfaces", "Mind Compressor"],
         "role": "original",
         "label": "Black Reaper Records",
         "date": "2025-07-30",
         "note": "Platz 1 der Masters of Hardcore Top 100 2025",
         "source": "https://..."}
      ],
      "anthems": [
        {"event": "REBiRTH Festival", "year": 2026, "title": "Take Control",
         "source": "https://..."}
      ],
      "links": {"beatport": "", "discogs": "", "soundcloud": "", "spotify": ""},
      "sources": ["https://..."]
    }
  ],
  "labels": [
    {"name": "Black Reaper Records", "founded": 2022, "country": "NL",
     "founders": ["Deadly Guns"], "parent": null, "sublabels": [],
     "roster": ["Deadly Guns", "Lekkerfaces", "Satirized"],
     "note_de": "1 bis 3 Sätze.", "sources": ["https://..."]}
  ],
  "festivals": [
    {"name": "Defqon.1", "city": "Biddinghuizen", "country": "NL",
     "organizer": "Q-dance", "edition": "2024", "date": "2024-06-27/30",
     "note_de": "Nur die Uptempo-Bühne erfasst.",
     "anthem": null,
     "stages": [
       {"stage": "YELLOW", "day": "Freitag", "genre": "uptempo",
        "acts": ["Lekkerfaces & Rosbeek", "Unproven", "Irradiate"]}
     ],
     "sources": ["https://..."]}
  ],
  "links": [
    {"a": "Lekkerfaces", "b": "Mind Compressor", "type": "collab",
     "count": 3, "weight": 4, "confidence": "documented",
     "evidence_de": "FA TI CO (Black Reaper, 30.07.2025) plus zwei weitere",
     "date": "2025-07-30", "source": "https://..."}
  ],
  "charts": [
    {"name": "Masters of Hardcore Top 100", "year": 2025,
     "entries": [{"rank": 1, "title": "FA TI CO",
                  "artists": ["Lekkerfaces", "Mind Compressor"]}],
     "source": "https://..."}
  ],
  "gaps": ["Für X war kein Line-up nach Bühnen auffindbar."]
}

Leere Abschnitte bleiben als leeres Array stehen. Nichts weglassen.

GENRE-WERTE — nur diese
  uptempo     Uptempo Hardcore inklusive Bounce-Uptempo, 180–220 BPM
  hardcore    Mainstream-Hardcore, 170–190
  frenchcore  Frenchcore, 190–210
  terror      Terror, Speedcore, Industrial, 200+
  raw         Raw Hardstyle, 150–160
  zaag        Zaag, Zaagstep, Hard-Dance-Crossover, 145–175
  host        MC oder Host ohne eigenes Produzentenprofil

KANTENTYPEN
  crew       festes Duo, Live-Formation, gemeinsames Alias        weight 4–5
  collab     gemeinsamer Release; weight = min(5, count + 1)
  remix      A hat B remixt                                       weight 2–3
  label      gleiches Label; 5 wenn einer der beiden es führt, sonst 2–3
  b2b        angekündigtes gemeinsames Set; weight = min(5, count + 1)
  mc         MC oder Host arbeitet regelmäßig für diesen Act      weight 2–4
  audience   Hörer-Überschneidung, nur mit "confidence": "estimate",
             begründet über Label-Umfeld, gemeinsame Bühne oder
             gemeinsame Presse-Nennung                            weight 1–4

NAMENSREGELN
Punkte, Ausrufezeichen und Groß-/Kleinschreibung exakt übernehmen:
"F. Noize", "Vandal!sm", "Dr. Peacock", "N-Vitral". Abweichende Schreibweisen
aus Line-ups gehören in "aliases", auch offensichtliche Tippfehler. Ein Name
mit kaufmännischem Und, der EINEN Act bezeichnet (etwa "DJ Rob & MC Joe"),
bekommt zusätzlich "single_act_with_ampersand": true.
````

---

## Danach

JSON hier in den Chat legen. Abgeglichen wird gegen den Bestand: Aliasse
zusammenführen, Kollaborations-Counts zu Kantengewichten, neue Uptempo-Bühnen
als Festival-Knoten. Teilmengen sind kein Problem — die Karte verträgt sie.

Die übrigen Genres, die deutsche Szene im Detail, die Label-Ebene als eigene
Knotenart und die Chart-Historie stehen weiterhin als Pakete C bis H in
[`RESEARCH-PROMPT.md`](RESEARCH-PROMPT.md) bereit.
