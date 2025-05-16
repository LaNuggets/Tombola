from getData import *
import re

file = "tombola.xlsx"

firstName, lastName, ticket = chipData(file)

rows = []
seen_names = set()  # Keep names already seen

for fname, lname, tickets in zip(firstName, lastName, ticket):
    s = str(tickets)
    match = re.search(r"\d+", s)
    try:
        if match:
            nb_tickets = int(match.group())

            full_name = f"{fname.strip().lower()}_{lname.strip().lower()}"
            for i in range(nb_tickets):
                # Show number of tickets only for the first occurrence
                tarif_value = tickets if i == 0 else ""
                rows.append({
                    "Prénom": fname,
                    "Nom": lname,
                    "Tarif": tarif_value
                })
    except ValueError:
        print(f"Valeur invalide pour le nombre de tickets : {tickets}")

# Create DataFrame
df = pd.DataFrame(rows)

# Add ticket number
df["Numéro du ticket"] = range(1, len(df) + 1)

# Organize all column
df = df[["Numéro du ticket", "Prénom", "Nom", "Tarif"]]

# Save as exel
df.to_excel("participants.xlsx", index=False)
