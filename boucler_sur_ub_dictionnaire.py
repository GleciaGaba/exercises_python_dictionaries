d = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

# Cette méthode récupère une liste de toutes les clés.
# d.keys() >>> ["prenom", "profession", "ville"]


# Cette méthode récupère une liste de toutes les valeurs.
# d.values() >>> ["Paul", "Ingénieur", "Paris"]

# d.items() >>> Retourne des tuples avec la clé et la valeur

"""
Bien sûr ! La méthode items() est très utile lorsqu'on travaille avec des dictionnaires en Python.
Elle permet de récupérer une vue de toutes les paires clé-valeur présentes dans le dictionnaire. 
Cette vue peut être utilisée pour itérer sur le dictionnaire de manière efficace.

"""
etudiants = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "cours": ["Math", "Physique", "Informatique"]
}

for cle, valeur in etudiants.items():
    print(f"{cle}: {valeur}")