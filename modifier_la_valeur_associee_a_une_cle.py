dic = {
        "prenom": "Paul",
        "profession": "Ingénieur",
        "ville": "Paris"
}

update_dic = dic["prenom"] = "Julie"

print(update_dic)

# {'prenom': 'Julie', 'profession': 'Ingénieur', 'ville': 'Paris'}
