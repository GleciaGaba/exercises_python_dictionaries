"""
Les dictionnaires
Dans cet exercice, nous avons un dictionnaire qui représente plusieurs employés d'une entreprise avec différents id.

Patrick a quitté l'entreprise cette année, nous devons donc l'enlever du dictionnaire.

Julie a fêté son anniversaire hier, il faut donc changer son âge (elle a maintenant 26 ans).

Paul quant à lui fêtera son anniversaire la semaine prochaine. Nous voulons donc récupérer
son âge pour savoir quel âge il aura.

Notre dictionnaire sera donc égal à la fin du script à :

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 26}
            }
Il faudra également récupérer l'âge de Paul dans une variable 'age_paul', qui devra donc être égale à 32.


"""

employes = {
    "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
    "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
    "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
}

cle_a_suprimer = ""

for cle, value in employes.items():
    if value["prenom"] == "Patrick":
        cle_a_suprimer = cle

if cle_a_suprimer:
    del employes[cle_a_suprimer]
print(employes)

age_julie = 0
for cle, value in employes.items():
    if value["prenom"] == "Julie":
        value["age"] = 26
        age_julie = value
print(age_julie)

for cle, value in employes.items():
    if value["prenom"] == "Paul":
        age_paul = value.get("age", "Vide")
print(age_paul)


# ---------------------------------------------------------------------------------------------------------------------

del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]