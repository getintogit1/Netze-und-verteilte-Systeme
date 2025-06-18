#!/usr/bin/env python3

import pandas as pd
import random


df = pd.read_csv("Questions.csv")  # Passe den Dateinamen an
if 'Rank' not in df.columns:
    df['Rank'] = None

inputUser = int(input(print("Sind die Fragen noch nicht Kategorisiert: drücke 0, sind sie bereits Kategorisiert drücke 1")))
if inputUser == 0:
    df = df.sample(frac=1).reset_index(drop=True)

if inputUser == 1:
# Reihen mit definierter Bewertung auswählen
    df = df[df['Rank'].isin([1, 2, 3])]

# Anteile berechnen
    num_questions = 30  # Beispiel: 30 Fragen insgesamt
    n3 = int(num_questions * 0.5)
    n2 = int(num_questions * 0.3)
    n1 = num_questions - n3 - n2

    sampled = pd.concat([
        df[df['Rank'] == 3].sample(n=min(n3, len(df[df['Rank'] == 3]))),
        df[df['Rank'] == 2].sample(n=min(n2, len(df[df['Rank'] == 2]))),
        df[df['Rank'] == 1].sample(n=min(n1, len(df[df['Rank'] == 1])))
    ]).sample(frac=1).reset_index(drop=True)

print("Netzwerk-Lernquiz gestartet! (Drücke Enter für nächste Frage, 'q' zum Beenden)\n")

for index, row in df.iterrows():
    if pd.isna(row['Fragenummer']):
        continue
    print(f"Frage {int(row['Fragenummer'])}: {row['Frage']}")
    print(f"Schwierigeit: {row['Rank']}")
    print(f"Kategorie: {row['Themenbereich']}")
    user_input = input("Antwort (drücke Enter, um Lösung zu sehen, 'q' zum Beenden): ")

    if user_input.lower() == 'q':
        print("Beendet. Viel Erfolg bei der Klausur!")
        break
    
    print(f"📘 Richtige Antwort:\n{row['Antwort']}\n{'-'*75}")    # Benutzerbewertung abfragen
    while True:
        try:
            difficulty = input("Wie gut konntest du die Frage? (1 = schwer, 2 = ok, 3 = einfach): ")
            if difficulty.lower() == 'q':
                break
            if difficulty in ['1', '2', '3']:
                df.at[index, 'Rank'] = int(difficulty) 
                df.to_csv("Questions.csv", index=False)
                break
            else:
                print("Bitte gib 1, 2 oder 3 ein.")
               
        except:
            raise
    print('-' * 75)


