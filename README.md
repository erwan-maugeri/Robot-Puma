# Robot-Puma

*Par Erwan Maugeri, Charles-Antoine Maisonneuve*

Ce projet a été réalisé dans le cadre d’un stage de Licence 2 Physique au Laboratoire d’Ingénierie des Systèmes de Versailles (LISV). Il porte sur la modélisation et la simulation en Python d’un robot manipulateur de type PUMA. Les travaux abordent la géométrie directe et inverse, la modélisation par les paramètres de Denavit-Hartenberg, l’étude du workspace ainsi que le suivi de trajectoires, avec des visualisations interactives en 3D.

## Contenu du dépôt

Le dépôt est organisé autour de trois fichiers principaux :

| Fichier | Description |
|---------|-------------|
| `rapport_stage.pdf` | Rapport final présentant la démarche, les résultats et les conclusions du projet. |
| `notebook_recherche.ipynb` | Notebook ayant servi aux recherches, aux calculs et aux expérimentations. Il contient les développements intermédiaires ayant conduit au rapport final. |
| `test_visualisation.py` | Script permettant de réaliser des essais indépendants et de visualiser les résultats 3D de manière interactive. |

## Notebook de recherche

Il s'agit d'un notebook structuré regroupant :

- les recherches effectuées pendant le stage
- les calculs et développements intermédiaires
- les expérimentations réalisées au cours du projet

Il constitue le support de travail ayant servi à la rédaction du rapport final.

## Visualisation 3D

Le script **[`test_visualisation.py`](./test_visualisation.py)** permet de travailler plus confortablement avec les visualisations 3D.

Il est notamment utile pour :

- tester rapidement une portion de code issue du notebook
- manipuler librement les représentations 3D (rotation, zoom, déplacement de la caméra) directement dans VS Code ou un environnement Python

(sous reserve de copier les bonnes cellules python depuis le Notebook de recherche)

## Rapport final

Le rapport complet est disponible dans :

[`rapport_stage.pdf`](./rapport_stage.pdf)

Il présente la méthodologie, les résultats obtenus ainsi que les conclusions du projet.