import pandas as pd

def chipData(file):
    try:
        df = pd.read_excel(file)
    except Exception:
        print("Je n'ai pas trouvé le fichier excel. je cherche #{file} dans le répairtoire où je suis\n")
    c = df.columns.tolist()
    #columns def
    firstName = df[c[0]]
    lastName = df[c[1]]
    ticketNumber = df[c[2]]
    #
    return firstName, lastName, ticketNumber