from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    esmeDB = client['mydb']

    Produit = esmeDB['Produit']

    Produit1 = {
        "Nom": "Shampoing",
        "Description": "Shampoing adapté à tout types de cheveux",
        "Id": 1,
    }

    Produit2 = {
        "Nom": "Lait",
        "Description": "Lait de coco",
        "Id": 2,
    }

    Produit3 = {
        "Nom": "Livre",
        "Description": "MongoDB pour les nuls",
        "Id": 3,
    }

    Commande = esmeDB['Commande']

    Commande1 = {
        "Nom": "Lebon",
        "Prenom": "Arthur",
        "Description": "Commande 1 ",
        "Id": 1,
    }
    Commande2 = {
        "Nom": "Ledoux",
        "Prenom": "Pierre",
        "Description": "Commande 2 ",
        "Id": 2,
    }
    Commande3 = {
        "Nom": "Neny",
        "Prenom": "Paul",
        "Description": "Commande 3 ",
        "Id": 3,
    }

    InventaireProduits = esmeDB['InventaireProduits']

    InventaireProduits1 = {
        "Description": " Inventaire du produit 1 ",
        "Quantité": 100,
        "Id": 1,
    }
    InventaireProduits2 = {
        "Description": " Inventaire du produit 2 ",
        "Quantité": 100,
        "Id": 2,
    }
    InventaireProduits3 = {
        "Description": " Inventaire du produit 3 ",
        "Quantité": 100,
        "Id": 3,
    }

    Caisse = esmeDB['Caisse']

    Caisse1 = {
        "Description": " Caisse numéro 1 ",
        "Nb_Vente_Produit1":10,
        "Nb_Vente_Produit2": 10,
        "Nb_Vente_Produit3": 10,
        "Ventes" : [10,10,10]
    }

    Caisse2 = {
        "Description": " Caisse numéro 2 ",
        "Nb_Vente_Produit1": 10,
        "Nb_Vente_Produit2": 20,
        "Nb_Vente_Produit3": 30,
        "Ventes": [10, 20, 30]

    }

#Commandes=[Commande1,Commande2,Commande3]
#Commande.insert_one(Commandes)
#Caisses=[Caisse1,Caisse2]
Caisse.insert_one(Caisse1)
Caisse.insert_one(Caisse2)

#Combien de produits ont été vendus pour chaque caisses
collection_somme_ventes = Caisse.aggregate(
    [
        {
            "$addFields":
                {
                "_id": None,
                "Total_ventes": {"$sum": "$Ventes"}
                }
        }
    ]
)
for agg in collection_somme_ventes:
    print(agg)



#Voir combien de produits toutes caisses confondues ont été vendus hier
collection_combien_produits = Caisse.aggregate(
    [
        {
            "$addFields":
                {
                "_id": None,
                "Total_combien_produits": {"$sum": "$Nb_Vente_Produit1" + "$Nb_Vente_Produit2"}
                }
        }
    ]
)
for agg in collection_combien_produits:
    print(agg)



collection_max = Caisse.aggregate(
    [
        {
            "$addFields":
                {
                "_id": None,
                "max": {"$max": ["$Nb_Vente_Produit1","$Nb_Vente_Produit2","$Nb_Vente_Produit3"]}
                }
        }
    ]
)
for agg in collection_max:
    print(agg)

