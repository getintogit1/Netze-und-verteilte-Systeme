# Netzwerk-Lernquiz für "Netze und Verteilte Systeme" 🧠🌐

Dieses Python-Tool bietet ein interaktives Lernquiz zur Vorbereitung auf die Klausur im Modul **Netze und Verteilte Systeme**. Es hilft Studierenden, Fragen aus verschiedenen Themenbereichen des OSI-Modells zu beantworten, den Schwierigkeitsgrad einzuschätzen und gezielt zu wiederholen.

---

## 📚 Projektübersicht

Das Skript lädt eine CSV-Datei mit Fragen, Kategorien und Antworten und bietet zwei Modi:

- **Trainingsmodus** (noch nicht kategorisierte Fragen)
- **Gezielter Wiederholungsmodus** (Fragen mit Schwierigkeitsbewertung)

---

## 🧩 Funktionen

- Zufällige Auswahl von Fragen
- Bewertung des Schwierigkeitsgrads durch den Nutzer (1–3)
- Speicherung der Bewertung in der Datei
- Kategorisierte Wiederholung mit ausgewogener Verteilung:
  - 50 % einfache Fragen (`Rank 3`)
  - 30 % mittlere Fragen (`Rank 2`)
  - 20 % schwere Fragen (`Rank 1`)

---

## 🗃️ Anforderungen

- Python 3.x
- `pandas`-Bibliothek (`pip install pandas`)
- CSV-Datei `Questions.csv` mit folgenden Spalten:

| Fragenummer | Frage | Antwort | Rank | Themenbereich |
|-------------|-------|---------|------|----------------|

> Falls `Rank` noch nicht vorhanden ist, wird die Spalte automatisch ergänzt.

---

## ▶️ Nutzung

```bash
python quiz.py
