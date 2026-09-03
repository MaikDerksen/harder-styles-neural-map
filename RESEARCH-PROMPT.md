# Deep-Research-Auftrag: Harder-Styles-Szene NL / BE / DE

Dieses Dokument enthält fertige Prompts für eine Deep-Research-Web-KI
(ChatGPT Deep Research, Gemini Deep Research, Perplexity Deep Research,
Claude mit Websuche o. ä.). Die Ausgabe ist so spezifiziert, dass sie sich
ohne Nacharbeit in die **Harder Styles Neural Map** einspielen lässt.

---

## 0. So gehst du vor

1. **Nicht alles auf einmal.** Deep-Research-Tools brechen bei zu großen
   Aufträgen ab oder werden oberflächlich. Nimm die Arbeitspakete A–H aus
   Abschnitt 3 einzeln — ein Paket pro Recherchelauf.
2. **Immer zuerst Abschnitt 1 (Systemauftrag) + Abschnitt 2 (Schema)
   einfügen, dann das gewünschte Arbeitspaket.** Die drei Teile ergeben
   zusammen einen vollständigen Prompt.
3. **Ausgabe als reines JSON** in einem Codeblock. Kein Fließtext drumherum.
4. Ergebnis als `.json`-Datei speichern und mir in den Chat legen —
   Dateiname z. B. `paket-A-festivals.json`.
5. Wenn das Tool die Ausgabe abschneidet: sag ihm „mach bei
   `<letztes Objekt>` weiter, gleiches Format, nur die restlichen Einträge".

---

## 1. Systemauftrag (immer voranstellen)

```
Du bist Recherche-Assistent für eine Datenbank über die Harder-Styles-Szene
(Hardstyle, Raw Hardstyle, Hardcore, Uptempo, Frenchcore, Terror, Industrial
Hardcore, Zaag, Early/Millennium Hardcore) mit Schwerpunkt Niederlande,
Belgien und Deutschland. Italienische, französische, britische und
US-amerikanische Acts gehören dazu, sofern sie regelmäßig auf niederländischen
oder deutschen Line-ups stehen.

DEINE AUFGABE
Recherchiere im Web und gib strukturierte, belegte Daten aus. Du schreibst
keine Reportage, sondern füllst eine Datenbank.

HARTE REGELN — diese sind wichtiger als Vollständigkeit:
1. Jede einzelne Tatsachenbehauptung braucht eine Quelle mit URL. Ein Feld
   ohne Beleg lässt du leer oder setzt es auf null. Rate niemals.
2. Erfinde keine Tracks, keine Line-up-Namen, keine Labelzugehörigkeiten,
   keine Jahreszahlen, keine bürgerlichen Namen. Wenn du etwas nicht findest,
   schreib es in das Feld "gaps" am Ende der Ausgabe.
3. Unterscheide sauber zwischen BELEGT und EINGESCHÄTZT. Einschätzungen
   (z. B. "ähnliches Publikum") gehören ausschließlich in Kanten vom Typ
   "audience" und bekommen "confidence": "estimate".
4. Bei widersprüchlichen Quellen: nimm die primäre (Festivalseite, Label,
   Beatport, Discogs) und notiere den Widerspruch in "notes".
5. Line-ups gibst du EXAKT so wieder, wie sie angekündigt wurden — inklusive
   "A vs B", "A & B", "A pres. Show", "A LIVE". Vereinheitliche sie NICHT.
   Diese Schreibweise ist die Information: daraus werden B2B-Verbindungen.
6. Ein Act, der unter mehreren Schreibweisen läuft, bekommt einen kanonischen
   Namen und alle Varianten in "aliases".
7. Keine Zusammenfassung, keine Einleitung, keine Nachbemerkung. Nur JSON.

BEVORZUGTE QUELLEN (in dieser Reihenfolge)
- Offizielle Festival- und Veranstalterseiten: q-dance.com, artofdance.nl,
  b2s.nl, intentsfestival.nl, rebirthfestival.nl, bkjn.nl, i-motion.de,
  decibeloutdoor.nl, dominator-festival.nl, mastersofhardcore.com
- Release-Datenbanken: beatport.com, discogs.com, musicbrainz.org,
  hardtunes.com, bandcamp
- Szene-Presse: hardnews.nl, hardstyle.com, hardstylemag.com, hardcultr.com,
  partyflock.nl, residentadvisor.net
- Set-Datenbanken: 1001tracklists.com, edm.fandom.com, clashfinder
- Artist-Kanäle: SoundCloud, Spotify (Credits!), YouTube, Instagram, Linktree
Wikipedia nur als Einstieg, nie als alleinige Quelle.

SPRACHE
Feldnamen englisch (wie im Schema). Fließtextfelder mit dem Suffix "_de"
schreibst du auf Deutsch, sachlich, ohne Werbesprache, 2–4 Sätze.
```

---

## 2. Ausgabeschema (immer voranstellen)

```
AUSGABEFORMAT — genau dieses JSON, ein einziger Codeblock:

{
  "package": "A",                        // Buchstabe des Arbeitspakets
  "generated": "2026-09-02",
  "artists": [
    {
      "name": "Lekkerfaces",             // kanonische Schreibweise
      "aliases": ["lekkerfaces", "LEKKERFACES"],
      "real_name": null,                 // nur wenn öffentlich belegt
      "country": "IT",                   // ISO-2: NL BE DE IT FR UK US UA ...
      "city": null,
      "active_since": 2022,
      "genres": ["uptempo"],             // NUR Werte aus der Genre-Liste unten
      "labels": ["Black Reaper Records", "Partyraiser Recordings"],
      "projects": [                      // Duos, Live-Formationen, Alias-Acts
        {"name": "Pizzeria", "members": ["Lekkerfaces", "Mind Compressor"],
         "kind": "live", "source": "https://..."}
      ],
      "bio_de": "2–4 Sätze, sachlich, nur Belegtes.",
      "tracks": [
        {
          "title": "FA TI CO",
          "credits": ["Lekkerfaces", "Mind Compressor"],  // ALLE Beteiligten
          "role": "original",            // original | remix | edit | bootleg
          "label": "Black Reaper Records",
          "date": "2025-07-30",          // YYYY-MM-DD, sonst YYYY-MM oder YYYY
          "note": "#1 Masters of Hardcore Top 100 2025",
          "source": "https://..."
        }
      ],
      "anthems": [
        {"event": "REBiRTH Festival", "year": 2026, "title": "Take Control",
         "source": "https://..."}
      ],
      "links": {"beatport": "", "discogs": "", "soundcloud": "",
                "spotify": "", "instagram": ""},
      "sources": ["https://...", "https://..."]
    }
  ],
  "labels": [
    {
      "name": "Black Reaper Records",
      "founded": 2022,
      "country": "NL",
      "founders": ["Deadly Guns"],
      "parent": null,                    // Mutterlabel, falls vorhanden
      "sublabels": [],
      "genres": ["hardcore", "uptempo", "terror"],
      "roster": ["Deadly Guns", "Lekkerfaces", "Satirized", "Bloodlust"],
      "note_de": "1–3 Sätze.",
      "sources": ["https://..."]
    }
  ],
  "festivals": [
    {
      "name": "Defqon.1",
      "city": "Biddinghuizen",
      "country": "NL",
      "organizer": "Q-dance",
      "month": "Juni",
      "indoor": false,
      "capacity": "65000",
      "first_edition": 2003,
      "edition": "2025 — Where Legends Rise",   // die hier erfasste Ausgabe
      "date": "2025-06-26/29",
      "note_de": "2–4 Sätze: wofür das Festival steht, Bühnenlogik, Rolle in der Szene.",
      "anthem": {"title": "...", "artists": ["..."], "source": "https://..."},
      "stages": [
        {
          "stage": "BLACK",
          "day": "Freitag",
          "genre": "hardcore",           // Wert aus der Genre-Liste
          "acts": [
            "Deadly Guns",
            "Nosferatu & Tha Playah",     // gemeinsame Sets EXAKT so lassen
            "Dimitri K & MC Robs"
          ]
        }
      ],
      "sources": ["https://..."]
    }
  ],
  "links": [
    {
      "a": "Lekkerfaces",
      "b": "Mind Compressor",
      "type": "collab",                  // siehe Kantentypen unten
      "count": 3,                        // Anzahl belegter gemeinsamer Releases
      "weight": 5,                       // 1–5, siehe Gewichtungsregel
      "confidence": "documented",        // documented | estimate
      "evidence_de": "FA TI CO (Black Reaper, 30.07.2025), plus zwei weitere gemeinsame Tracks",
      "date": "2025-07-30",
      "source": "https://..."
    }
  ],
  "charts": [
    {
      "name": "Masters of Hardcore Top 100",
      "year": 2025,
      "entries": [
        {"rank": 1, "title": "FA TI CO", "artists": ["Lekkerfaces", "Mind Compressor"]}
      ],
      "source": "https://..."
    }
  ],
  "gaps": [
    "Für X war kein Line-up nach Bühnen auffindbar, nur eine Gesamtliste.",
    "Bürgerlicher Name von Y nirgends öffentlich belegt."
  ]
}

Leere Abschnitte lässt du als leeres Array stehen. Nichts weglassen.

GENRE-LISTE — ausschließlich diese Werte:
  hardstyle    Euphoric/Main Hardstyle, 150–155 BPM
  raw          Raw Hardstyle / Rawphoric, 150–160
  hardcore     Mainstream Hardcore / Gabber, 170–190
  uptempo      Uptempo Hardcore inkl. Bounce-Uptempo, 180–220
  frenchcore   Frenchcore, 190–210
  terror       Terror, Speedcore, Industrial/Crossbreed, 200+
  early        Early Hardcore, Millennium, Classics, Nu Style
  zaag         Zaag, Zaagstep, Hard Dance Crossover, 145–175
  techno       Hardtechno, Hard Trance, Schranz
  host         MC / Host (kein eigenes Produzentenprofil)
  other        alles andere (DnB, Hardtek, Tekno, Feestmuziek)

KANTENTYPEN
  crew       festes Duo, Live-Formation, gemeinsames Alias (Gunz for Hire,
             Slaughterhouse, Combined Forces, Pizzeria …)   → weight 4–5
  collab     gemeinsamer Release. weight = min(5, Anzahl gemeinsamer Tracks + 1)
  remix      A hat B remixt                                  → weight 2–3
  label      beide auf demselben Label; weight 5 wenn einer der beiden das
             Label führt, sonst 2–3
  b2b        angekündigtes gemeinsames Set („A vs B", „A & B" auf einem
             Line-up). count = Anzahl solcher Sets, weight = min(5, count+1)
  mc         MC/Host arbeitet regelmäßig für diesen Act        → weight 2–4
  audience   Hörer-Überschneidung. NUR mit "confidence": "estimate" und einer
             Begründung, die auf Belegbarem fußt (gleiches Label-Umfeld,
             gleiche Bühne, gemeinsame Presse-Nennung). weight 1–4

GEWICHTUNGSREGEL
weight bildet die Stärke der Verbindung ab, nicht deine Meinung über die
Musik. Im Zweifel niedriger ansetzen.

NAMENSREGELN
- Kanonisch ist die Schreibweise, die der Act selbst auf seinen eigenen
  Kanälen verwendet (SoundCloud/Instagram/Beatport-Artistseite).
- Punkte, Ausrufezeichen und Groß-/Kleinschreibung genau übernehmen
  ("F. Noize", "Vandal!sm", "N-Vitral", "Dr. Peacock").
- Alle abweichenden Schreibweisen, die dir in Line-ups begegnet sind,
  gehören in "aliases" — auch offensichtliche Tippfehler.
- Acts, deren Name ein "&" enthält, aber EIN Act sind (D-Block & S-te-Fan,
  Degos & Re-Done, DJ Rob & MC Joe, Taco & Tities), markierst du zusätzlich
  mit "single_act_with_ampersand": true.
```

---

## 3. Arbeitspakete

Jeweils an Abschnitt 1 + 2 anhängen.

### Paket A — Festivals und Line-ups

```
ARBEITSPAKET A: FESTIVALS UND LINE-UPS

Erfasse für jedes der folgenden Festivals die Editionen 2024, 2025 und 2026
(soweit veröffentlicht) mit VOLLSTÄNDIGEM Line-up, aufgeschlüsselt nach
Bühne und Tag. Wenn du keine Bühnenaufteilung findest, gib die Gesamtliste
als eine Bühne mit "stage": "Line-up" aus und vermerk das in "gaps".

Niederlande / Belgien:
  Defqon.1, Qlimax, Q-BASE, X-Qlusive, Ground Zero, Freaqshow (Q-dance)
  Dominator, Masters of Hardcore, Supremacy, Syndicate (Art of Dance)
  Decibel Outdoor, Shockerz, Harmony of Hardcore (b2s)
  Intents Festival, REBiRTH Festival, Emporium, Thunderdome, Hardshock,
  Pandemonium, Wish Outdoor, HARDFEST, BKJN Festival, Rotterdam Rave Hard,
  The Qontinent, Reverze, Hardstyle Sessions, Mystic Garden Hard

Deutschland (bitte besonders gründlich, hier ist die Datenlage dünn):
  Toxicator, Syndicate Dortmund, Q-BASE Weeze, Ruhr-in-Love, Mayday,
  Nature One, Airbeat One, Turbo Halle, Hardstyle Arena, Uptempo Poison,
  Hard Impact, Dark Sun, Nightmare Festival, Hardcore Nation,
  Ravekultur-Events, Zaag-/Uptempo-Clubreihen in NRW und Berlin
  → Suche zusätzlich aktiv nach deutschen Uptempo- und Zaag-Veranstaltungen,
    die ich nicht genannt habe. Liste sie mit auf.

Zu jeder Edition zusätzlich:
- offizieller Anthem inkl. Produzent
- Bühnennamen und welches Genre auf welcher Bühne läuft
- Besucherzahl, falls belegt
- alle als „vs", „&", „pres.", „B2B", „LIVE" angekündigten Sets EXAKT
  in der angekündigten Schreibweise

Fülle nur die Abschnitte "festivals", "links" (nur type "b2b") und "gaps".
```

### Paket B — Uptempo vollständig

```
ARBEITSPAKET B: UPTEMPO — VOLLSTÄNDIGE ERFASSUNG

Erfasse ALLE aktiven Uptempo-Hardcore-Acts aus NL, BE, DE und Italien.
Ausgangsliste (unvollständig, bitte ergänzen):
Lekkerfaces, The Dark Horror, Yoshiko, Mind Compressor, Noxiouz, Satirized,
Dimitri K, Partyraiser, Spitnoise, Deadly Guns, Abaddon, Angernoizer, Barber,
Major Conspiracy, Gezellige Uptempo, Kili, Kemal, Roosterz, Revealer,
Bössels, Pinotello, TukkerTempo, Dynamic Noise, The Dope Doctor, Kroefoe,
Unlocked, S-Kill, Spiady, Guizcore, Trespassed, Jur Terreur, Eraized,
Screecher, UDOW, Aalst, MT, TMO, Repix, Sjammienators, Vandal!sm, Ditzkickz,
Het Pompstation, Tomsku, Tharken, Unproven, Akimbo, Samynator, Bulletproof,
Juliëx, Namara, Elite Enemy, Manifest Destiny, DRS, Cryogenic, Irradiate,
Soulblast, F. Noize, Antenora, Toza, Sakyra, Hyperverb, Odium, Estasia,
System Overload, Xterminate, Røza, Lil Texas

Für jeden Act:
- vollständige Diskografie der letzten fünf Jahre, mindestens aber alle
  Releases mit mehr als einem Credit (das ist das Wichtigste — daraus
  entstehen die Verbindungen)
- Label-Historie mit Zeiträumen
- Live-Formationen und Alias-Projekte
- Auftritte auf den großen Festivals 2024–2026

Erzeuge daraus "links" vom Typ "collab" mit korrektem "count": zähle, wie oft
zwei Acts gemeinsam auf einem Release stehen. Das ist die zentrale Kennzahl.

Fülle "artists", "links", "labels" (nur Uptempo-Labels) und "gaps".
```

### Paket C — Hardstyle und Raw

```
ARBEITSPAKET C: HARDSTYLE UND RAW HARDSTYLE

Erfasse die aktiven Acts der Hardstyle- und Raw-Szene NL/BE/DE, die
2024–2026 auf mindestens einem der großen Festivals gespielt haben.

Schwerpunkt liegt auf VERBINDUNGEN, nicht auf Biografien:
- Duos und deren Mitglieder (Gunz for Hire = Ran-D + Adaro,
  D-Block & S-te-Fan, Sub Zero Project, Degos & Re-Done, Alpha Twins,
  Bass Modulators, Wasted Penguinz, Da Tweekaz, Primeshock, Audiotricz …)
  → alle mit "kind": "duo" in "projects"
- Solo-Aliasse von Duo-Mitgliedern und umgekehrt
- alle gemeinsamen Releases inkl. Remixe
- Label-Zugehörigkeit: Scantraxx (inkl. aller Sublabels), Dirty Workz,
  Gearbox Digital, Roughstate, Minus Is More, End of Line, Art of Creation,
  Spoontech, Theracords, Q-dance Records, Defqon.1 Records
- welcher MC für welchen Act hostet (type "mc")

Fülle "artists", "labels", "links" und "gaps".
```

### Paket D — Hardcore, Frenchcore, Terror

```
ARBEITSPAKET D: HARDCORE, FRENCHCORE, TERROR, INDUSTRIAL

Erfasse die aktiven Acts dieser Genres mit Auftritten 2024–2026 in NL/BE/DE,
inklusive der italienischen (Traxtorm-Umfeld), französischen (Frenchcore)
und britischen (Industrial/Crossbreed) Acts, die dort regelmäßig spielen.

Besonders wichtig:
- Live-Projekte und Doppelnamen (Slaughterhouse = Deadly Guns + N-Vitral,
  Combined Forces = Nosferatu + Tha Playah, weitere bitte suchen)
- Label-Landschaft: Masters of Hardcore, Neophyte Records, Traxtorm,
  Enzyme, PRSPCT, Genosha, Peacock Records, Barbaric Records,
  Black Reaper Records, Uptempo Hardcore Records, Partyraiser Recordings,
  Darkside Unleashed, Triple Six Records, Offensive Records, Footworxx
- die Gründergeneration und ihre Verbindungen zur Gegenwart
  (Marc Acardipane/PCP, Paul Elstak, Neophyte, Ruffneck, Partyraiser)

Fülle "artists", "labels", "links" und "gaps".
```

### Paket E — Labels vollständig

```
ARBEITSPAKET E: LABEL-LANDSCHAFT

Erfasse alle relevanten Labels der Harder Styles aus NL, BE und DE.
Für jedes Label: Gründungsjahr, Gründer, Mutterlabel und Sublabels,
Genre-Schwerpunkt, aktueller Roster mit Namen, und ob das Label zu einem
Veranstalter gehört (z. B. Q-dance Records → Q-dance).

Erzeuge daraus "links" vom Typ "label" zwischen allen Acts, die auf demselben
Label sind. Wenn einer der beiden das Label gegründet hat oder führt:
weight 5, sonst 2–3.

Fülle "labels", "links" und "gaps".
```

### Paket F — Deutschland im Detail

```
ARBEITSPAKET F: DIE DEUTSCHE SZENE

Die deutsche Harder-Styles-Szene ist in meiner Datenbank stark
unterrepräsentiert. Recherchiere gezielt:

1. Deutsche Produzenten und DJs in Hardstyle, Hardcore, Uptempo, Zaag und
   Hardtechno — aktiv 2020 bis heute. Ausgangspunkte: Dr Donk (Köln),
   NoiseFlow, Schlot, Beats by Luca, GPF, Marc Acardipane (Frankfurt),
   Miro, Scot Project, Neon Graveyard, Per Pleks, Polytoxic, Ally,
   Russian Village Boys, Hans Glock, Immer Hansi.
   → Suche aktiv nach weiteren. Wer spielt auf deutschen Hard-Dance-Floors?
2. Deutsche Labels: Clinic Recordings, Greazy Recordz, Crash Your Sound,
   Global Airbeatz, Planet Core Productions und Nachfolger, Kotzaak,
   Blut Records, weitere.
3. Deutsche Veranstalter und Reihen: I-Motion, Ravekultur, Uptempo Poison,
   Hard Impact — plus alles, was du sonst findest.
4. Die „Zaag"-Welle: Ursprung, wichtigste Tracks, wer sie trägt, wie sie
   mit dem niederländischen Uptempo verbunden ist.
5. Historische Achse: Frankfurter Hardcore-Schule (PCP, Marc Acardipane,
   The Mover) und ihr Verhältnis zur Rotterdamer Gabber-Schule. Wer hat
   mit wem gearbeitet?

Fülle "artists", "labels", "festivals", "links" und "gaps".
```

### Paket G — Gemeinsame Sets und Projekte

```
ARBEITSPAKET G: B2B, VS UND LIVE-PROJEKTE

Sonderauftrag, nur Verbindungen. Suche systematisch nach angekündigten
gemeinsamen Auftritten in der Harder-Styles-Szene 2022–2026:

- alle „A vs B", „A B2B B", „A & B", „A meets B"-Sets auf Festival- und
  Clubline-ups in NL, BE und DE
- alle Live-Formationen mit eigenem Namen und ihren Mitgliedern
- alle „presents"-Shows, bei denen mehrere Acts beteiligt sind
- Label-Showcases mit Namensnennung der beteiligten Acts
- Anthem-Kollaborationen für Events

Quellen: Festival-Timetables und Clashfinder, Partyflock-Eventseiten,
1001tracklists, Instagram-Ankündigungen der Veranstalter, Aftermovies.

Gib pro Paarung EINEN "links"-Eintrag vom Typ "b2b" aus, mit "count" =
Anzahl der belegten gemeinsamen Sets und einer Auflistung in "evidence_de"
im Format "Festival · Bühne · Jahr; Festival · Bühne · Jahr".

Fülle nur "links" und "gaps".
```

### Paket H — Charts und Rankings

```
ARBEITSPAKET H: CHARTS, ANTHEMS, AUSZEICHNUNGEN

Erfasse:
- Masters of Hardcore Top 100, Jahrgänge 2020–2025, jeweils die Top 50
- Hardstyle.com / Q-dance Top 100 der jeweiligen Jahre, Top 50
- Hardtunes-Jahrescharts, soweit verfügbar
- alle offiziellen Festival-Anthems 2015–2026 mit Produzent:
  Defqon.1, Qlimax, Decibel, Dominator, Intents, REBiRTH, Masters of
  Hardcore, Supremacy, Thunderdome, Syndicate, Reverze, The Qontinent
- DJ-Mag-Platzierungen von Harder-Styles-Acts

Fülle "charts", "artists" (nur "anthems" ergänzen) und "gaps".
```

---

## 4. Was schon in der Datenbank ist

Damit die Recherche keine Arbeit doppelt macht — das liegt bereits vor:

**Festivals mit Line-up (13):** Defqon.1 2025 (alle 13 Bühnen), Dominator 2025
(beide Tage), Decibel Outdoor 2025, Intents 2025, Syndicate 2025,
Masters of Hardcore 2025 (teilweise), REBiRTH 2025 (teilweise), BKJN 2026
(teilweise), HARDFEST (teilweise), Toxicator 2025, LET'S GET HYPER 2026,
Battle of Uptempo, Uptempo Poison.

**Acts:** 592 Namen aus diesen Line-ups, davon rund 50 mit recherchiertem
Profil (Biografie, Labels, Schlüsseltracks). Der Rest hat nur Name, Genre,
Land und Festivalauftritte.

**Kanten:** rund 1.380 — überwiegend „spielt dort" und automatisch aus
gemeinsamen Sets erzeugte B2B-Kanten, dazu rund 90 handrecherchierte
Verbindungen im Uptempo-Bereich.

**Größte Lücken, in dieser Reihenfolge:**
1. Diskografien — es fehlen fast alle gemeinsamen Releases außerhalb des
   Uptempo-Kerns. Das ist die wichtigste Lücke, weil „wer mit wem wie oft"
   genau daraus entsteht.
2. Deutschland — Acts, Labels und Events sind kaum abgedeckt.
3. Editionen vor 2025 — die Datenbank kennt praktisch nur ein Jahr.
4. Labels als eigene Ebene fehlen komplett.
5. Anthems und Chartplatzierungen fehlen bis auf Einzelfälle.

---

## 5. Wenn du das Ergebnis zurückbringst

Leg mir die JSON-Datei(en) einfach in den Chat. Ich prüfe dann:

- Namen gegen den Bestand abgleichen und Aliasse zusammenführen
- Kanten mit `confidence: "estimate"` bleiben gestrichelt und getrennt
  gekennzeichnet
- Kollaborations-Counts werden zu Kantengewichten
- neue Festivals werden zu Knoten, neue Bühnen zu Untergruppen

Wenn ein Paket nur teilweise geklappt hat, ist das kein Problem — die Karte
verträgt Teilmengen. Lieber 40 sauber belegte Acts als 300 geratene.
