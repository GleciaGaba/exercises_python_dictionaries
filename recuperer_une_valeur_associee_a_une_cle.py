dic = {
    0: {
        "prenom": "Paul",
        "profession": "Ingénieur",
        "ville": "Paris"
    },
    1: {
        "prenom": "Julie",
        "profession": "Architecte",
        "ville": "Marseille"
    },
    2: {
        "prenom": "Pierre",
        "profession": "Plombier",
        "ville": "Nantes"
    }
}

prenom0 = dic[0]["prenom"]
print(prenom0)
prenom1 = dic[1]["prenom"]
print(prenom1)
prenom2 = dic[2]["prenom"]
print(prenom2)

# Le problème de récupérer les données de cette façon est que si la clé n'existe pas, cela va nous retourner une erreur.
# On peut utiliser la méthode get.

# get() peut être utilisé que pour récupérer une valeur associée à une clé, mais pas pour la modifier.

# Voici comment prévenir des erreurs :

dic_get = dic[0].get("prenom", "La clé 'prenom' n'existe pas")

print(dic_get)
