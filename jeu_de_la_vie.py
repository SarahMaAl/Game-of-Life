#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jeu de la Vie - Automate cellulaire de John Conway

Ce programme simule le célèbre jeu de la vie. Il sauvegarde les résultats toutes
les 50 itérations dans des sous-dossiers nommés "output/i_pattern/j_generation".

Le programme continue à tourner jusqu'à interruption manuelle.

Auteur: Sarah MARTIN-ALONSO
Date: 2024-10-04
Licence: MIT
"""

import os
import numpy as np
import matplotlib.pyplot as plt

GRID_SIZE = 50
ALIVE = 1
DEAD = 0
SAVE_INTERVAL = 50  # Sauvegarde toutes les 50 itérations
OUTPUT_DIR = 'output'


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


def find_next_output_directory(base_dir: str) -> str:
    """
    Trouve le prochain dossier 'i_pattern' disponible pour la sauvegarde.
    Les dossiers sont nommés "01_pattern", "02_pattern", etc.
    
    :param base_dir: Dossier de base pour la sauvegarde
    :return: Chemin du prochain dossier disponible
    """
    pattern_number = 1
    while True:
        output_path = os.path.join(base_dir, f"{pattern_number:02d}_pattern")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            return output_path
        pattern_number += 1


def save_grid(grid: np.ndarray, iteration: int, output_dir: str):
    """
    Sauvegarde la grille actuelle sous forme d'image PNG dans le sous-dossier 'j_generation'.
    
    :param grid: Grille actuelle
    :param iteration: Numéro de l'itération
    :param output_dir: Dossier de sauvegarde
    """
    generation_number = (iteration // SAVE_INTERVAL)
    generation_dir = os.path.join(output_dir, f"{generation_number:02d}_generation")
    
    if not os.path.exists(generation_dir):
        os.makedirs(generation_dir)

    plt.imshow(grid, cmap='binary')
    plt.title(f"Iteration {iteration}")
    plt.axis('off')
    output_file = os.path.join(generation_dir, f"iteration_{iteration:04d}.png")
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    # Initialisation de la grille
    grid = random_grid(GRID_SIZE)

    # Trouver le prochain dossier 'i_pattern' disponible
    pattern_dir = find_next_output_directory(OUTPUT_DIR)

    # Compteur d'itérations
    iteration = 0

    # Simulation infinie jusqu'à arrêt manuel
    try:
        while True:
            grid = update(grid)
            iteration += 1

            # Sauvegarde toutes les 50 itérations
            if iteration % SAVE_INTERVAL == 0:
                save_grid(grid, iteration, pattern_dir)
                print(f"Pattern sauvegardé à l'itération {iteration} dans {pattern_dir}")

    except KeyboardInterrupt:
        print("Simulation interrompue par l'utilisateur.")
