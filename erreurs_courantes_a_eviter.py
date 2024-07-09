"""
 La méthode get() en Python est très utile pour accéder aux valeurs
dans un dictionnaire tout en évitant les erreurs lorsque la clé n'existe pas.
Cependant, il y a quelques erreurs courantes ou pièges potentiels à garder à l'esprit lors de son utilisation.

Utilisation de get()
La méthode get() prend deux arguments :

La clé que vous voulez chercher.

Une valeur par défaut à retourner si la clé n'existe pas (ce paramètre est optionnel, par défaut il vaut None).

"""

etudiants = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Utilisation de get() avec une clé existante
print(etudiants.get('nom'))  # Alice

# Utilisation de get() avec une clé inexistante sans valeur par défaut
print(etudiants.get("profession"))  # Affiche None

# Utilisation de get() avec une clé inexistante et une valeur par défaut
print(etudiants.get("profession", "Non spécifié"))  # Affiche "Non spécifié"

"""
Erreurs et Pièges Courants

1. Ne pas Fournir une Valeur par Défaut
L'erreur la plus courante est de ne pas fournir une valeur par défaut lors de l'utilisation de get().
Si la clé n'existe pas, get() retournera None, ce qui peut parfois conduire à des comportements inattendus,
surtout si le code suivant ne s'attend pas à une valeur None.


2. Supposer que la Clé Existe
Une autre erreur courante est de supposer que la clé existe toujours. 
Cela peut conduire à des erreurs logiques si vous n'avez pas prévu le cas où la clé est absente.

3. Valeur par Défaut Incorrecte
Il est aussi possible de spécifier une valeur par défaut qui ne correspond pas au type attendu,
ce qui peut causer des erreurs plus tard dans le code.

4. Essayer de Modifier une Valeur avec get()

La méthode get() retourne une copie de la valeur associée à la clé, 
et non une référence directe à cette valeur dans le dictionnaire. 
Par conséquent, toute tentative de modifier cette valeur ne changera pas l'état du dictionnaire lui-même.
"""


