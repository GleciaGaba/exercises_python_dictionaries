"""
Introduction aux Dictionnaires en Python
Les dictionnaires en Python sont des collections non ordonnées de paires clé-valeur.
Chaque élément dans un dictionnaire est une paire composée d'une clé unique et d'une valeur associée.
Les dictionnaires sont des structures de données mutables, ce qui signifie que vous pouvez modifier
leur contenu après leur création.

Création d'un Dictionnaire
Vous pouvez créer un dictionnaire en utilisant des accolades {} et en séparant les
clés et les valeurs par des deux-points :. Par exemple :

Dans cet exemple, 'nom', 'âge', et 'ville' sont des clés, et 'Alice', 25, et 'Paris' sont les valeurs correspondantes.

"""

# Dans cet exemple, 'nom', 'âge', et 'ville' sont des clés, et 'Alice', 25, et 'Paris' sont les valeurs correspondantes.

mon_dictionnaire = {
    "nom": "Alice",
    "âge": 25,
    "ville": "Paris"
}

"""
Ajouter ou Modifier des Éléments
Vous pouvez ajouter une nouvelle paire clé-valeur ou modifier une valeur existante en utilisant la syntaxe suivante :
"""

mon_dictionnaire["profession"] = "Ingénieur"
mon_dictionnaire["âge"] = 26

print(mon_dictionnaire)

"""
Supprimer des Éléments
Pour supprimer une paire clé-valeur, utilisez l'instruction del :
"""

del mon_dictionnaire["ville"]

print(mon_dictionnaire)

age = mon_dictionnaire.pop("âge")
print(age)
print(mon_dictionnaire)


"""
Itération sur un Dictionnaire
Il est possible d'itérer sur les clés, les valeurs ou les paires clé-valeur d'un dictionnaire :

"""

for cle in mon_dictionnaire:
    print(cle)
for cle, valeur in mon_dictionnaire.items():
    print(f'{cle}: {valeur}')


"""
Méthodes Utiles
Voici quelques méthodes couramment utilisées avec les dictionnaires :

keys(): retourne une vue des clés du dictionnaire.

values(): retourne une vue des valeurs du dictionnaire.

items(): retourne une vue des paires clé-valeur du dictionnaire.

get(key, default): retourne la valeur associée à key si elle existe, sinon retourne default.

update(dict2): met à jour le dictionnaire avec les paires clé-valeur de dict2.

"""

# creation d'un dictionnaire

etudiants = {
    "nom": "Bob",
    "age": 22,
    "cours": ["Math", "Physique", 'Informatique']

}

# Ajouter une nouvelle paire clé-valeur

etudiants["adresse"] = "123 Rue Principale"
print(etudiants)


# Modifier une valeur existante
etudiants["age"] = 23

print(etudiants)

# Itérer sur le dictionnaire

for cle, valeur in etudiants.items():
    print(f"{cle}: {valeur}")

# Accéder et itérer sur les cours

for cours in etudiants['cours']:
    print(cours)



# Utiliser un méthode
nom = etudiants.get("non", "Inconnu")
print(nom)

# Supprimer une paire clé-valeur

del etudiants["cours"]
print(etudiants)