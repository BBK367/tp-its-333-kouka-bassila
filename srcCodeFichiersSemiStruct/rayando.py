import json

def lire_donnees(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_donnees(fichier, donnees):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    fichier = "BDD101/data.json"

    # 1) Lire le fichier JSON
    data = lire_donnees(fichier)
    print("Données originales :")
    print(data)

    # 2) Accéder au premier feature
    feature = data["features"][0]

    # 3) Mise à jour des coordonnées
    feature["geometry"]["coordinates"] = [48.8566, 2.3522]  # Exemple : Paris

    # 4) Ajout d’un couple clé / valeur dans properties
    feature["properties"]["ville"] = "Paris"

    # 5) Ajout d’une nouvelle propriété booléenne
    feature["properties"]["proprietes"] = True

    # 6) Sauvegarde
    sauvegarder_donnees(fichier, data)

    print("\nDonnées modifiées :")
    print(data)
