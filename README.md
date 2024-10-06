# Jeu de la Vie - Automate cellulaire de John Conway

Ce projet implémente une simulation du célèbre **Jeu de la Vie** de **John Conway**, un automate cellulaire basé sur des règles simples permettant de modéliser l'évolution de populations de cellules.

## Fonctionnalités

- **Initialisation aléatoire** : La grille initiale est générée aléatoirement avec des cellules vivantes ou mortes.
- **Mise à jour des générations** : La simulation applique les règles du jeu à chaque cellule en fonction de ses voisins pour déterminer son état dans la génération suivante.
- **Sauvegarde automatique** : Les résultats sont automatiquement sauvegardés toutes les 50 itérations dans des sous-dossiers organisés en fonction des itérations.
  - Chaque sauvegarde est effectuée dans un sous-dossier `output/i_pattern/j_generation`, où `i` correspond au numéro de modèle et `j` au nombre d'itérations divisé par 50.
- **Arrêt manuel** : La simulation tourne indéfiniment jusqu'à ce qu'elle soit interrompue manuellement (Ctrl+C).

## Règles du Jeu de la Vie

1. **Survie** : Une cellule vivante reste en vie si elle a 2 ou 3 voisins vivants, sinon elle meurt (surpopulation ou sous-population).
2. **Naissance** : Une cellule morte devient vivante si elle a exactement 3 voisins vivants.

## Structure du projet

- **game_of_life.py** : Le fichier principal contenant la logique de la simulation.
- **output/** : Le dossier de sortie où sont sauvegardés les résultats.
  - Chaque sous-dossier `i_pattern/` correspond à une exécution de la simulation.
  - Chaque sous-dossier `j_generation/` contient les grilles sauvegardées toutes les 50 itérations sous forme d'image PNG.

## Comment exécuter le programme

### Prérequis

- Python 3.x
- Bibliothèques nécessaires :
  - numpy
  - matplotlib

Installez les dépendances avec la commande suivante :

pip install numpy matplotlib

### Exécution

Lancez la simulation avec la commande suivante :

python game_of_life.py

### Arrêt

Pour arrêter la simulation, appuyez sur `Ctrl+C` dans la console.

## Structure des fichiers de sortie

Les fichiers de sortie sont organisés comme suit :

output/
├── 01_pattern/
│   ├── 00_generation/
│   │   └── iteration_0050.png
│   ├── 01_generation/
│   │   └── iteration_0100.png
│   └── ...
└── 02_pattern/
    └── ...

## Auteur

- **Sarah MARTIN-ALONSO**  
  Étudiante en physique médicale.

## Licence

Ce projet est sous licence MIT.
