#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jeu de la Vie - Automate cellulaire de John Conway

Ce programme simule le célèbre jeu de la vie. Il utilise une grille 2D 
où chaque cellule peut être vivante ou morte. L'évolution de chaque cellule 
est déterminée par l'état de ses voisines, selon les règles suivantes :
1. Une cellule vivante avec moins de 2 voisins vivants meurt (sous-population).
2. Une cellule vivante avec 2 ou 3 voisins vivants reste en vie.
3. Une cellule vivante avec plus de 3 voisins vivants meurt (surpopulation).
4. Une cellule morte avec exactement 3 voisins vivants devient vivante (reproduction).

Auteur: Sarah MARTIN-ALONSO
Date: 2024-10-04
Licence: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GRID_SIZE = 75
ALIVE = 1
DEAD = 0


def random_grid(size: int) -> np.ndarray:
    """
    Génère une grille aléatoire où chaque cellule peut être vivante (1) ou morte (0).
    
    :param size: Taille de la grille (size x size)
    :return: Grille initialisée de manière aléatoire
    """
    return np.random.choice([DEAD, ALIVE], size * size, p=[0.8, 0.2]).reshape(size, size)


def count_neighbors(grid: np.ndarray, x: int, y: int) -> int:
    """
    Compte le nombre de voisins vivants d'une cellule dans la grille.
    
    :param grid: Grille actuelle
    :param x: Coordonnée de la cellule en ligne
    :param y: Coordonnée de la cellule en colonne
    :return: Nombre de voisins vivants
    """
    rows, cols = grid.shape
    neighbors = [
        grid[i % rows, j % cols]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (i != x or j != y)
    ]
    return sum(neighbors)


def update(grid: np.ndarray) -> np.ndarray:
    """
    Applique les règles du jeu de la vie pour générer la grille suivante.
    
    :param grid: Grille actuelle
    :return: Nouvelle grille après application des règles
    """
    new_grid = np.copy(grid)
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            alive_neighbors = count_neighbors(grid, i, j)
            if grid[i, j] == ALIVE:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[i, j] = DEAD
            else:
                if alive_neighbors == 3:
                    new_grid[i, j] = ALIVE

    return new_grid


def animate(data: np.ndarray):
    """
    Fonction d'animation appelée à chaque étape pour mettre à jour la grille.
    
    :param data: Données transmises à la fonction d'animation
    :return: Liste contenant l'objet mis à jour pour l'animation
    """
    global grid
    grid = update(grid)
    mat.set_data(grid)
    return [mat]


if __name__ == "__main__":
    # Initialisation de la grille
    grid = random_grid(GRID_SIZE)

    # Création de la figure pour l'animation
    fig, ax = plt.subplots()
    mat = ax.matshow(grid, cmap='binary')

    # Animation de la simulation
    ani = animation.FuncAnimation(fig, animate, interval=200, save_count=50)
    
    # Affichage de la grille
    plt.show()
