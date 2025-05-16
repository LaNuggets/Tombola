import pandas as pd

def chipData(file):
    try:
        df = pd.read_excel(file)
    except Exception as e:
        print(f"Erreur lors de l'ouverture de '{file}' : {e}")
        return None, None, None
    c = df.columns.tolist()
    #columns def
    firstName = df[c[1]]
    lastName = df[c[2]]
    ticket = df[c[3]]
    #
    return firstName, lastName, ticket