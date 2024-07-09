dic = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

dic["age"] = 30
print(dic)

# {'prenom': 'Paul', 'profession': 'Ingénieur', 'ville': 'Paris', 'age': 30}


# Pour éviter d'avoir une erreur si la clé n'existe pas, on doit d'abord vérifier avec une condition if.

if "age" in dic:
    del dic["age"]
print(dic)

# {'prenom': 'Paul', 'profession': 'Ingénieur', 'ville': 'Paris'}
