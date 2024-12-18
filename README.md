# Simulation de Circuits R, L, C

## Description
Ce projet est une application de simulation numérique permettant de calculer les réponses temporelles de circuits électriques composés de résistances (R), d'inductances (L) et de capacités (C). Il utilise des méthodes numériques classiques pour résoudre les équations différentielles ordinaires (EDO) associées à différents types de circuits.

## Fonctionnalités
- Simulation de filtres de premier ordre (RC, RL).
- Simulation de filtres de second ordre (RLC série).
- Utilisation de méthodes numériques :
  - Méthode d'Euler.
  - Méthode de Runge-Kutta.
  - Différences finies.
- Prise en charge de signaux d'entrée tels que des créneaux et des sinusoïdes.
- Interpolation de signaux d'entrée pour des résolutions temporelles précises.
- Extension possible à des circuits plus complexes en cascade avec des AOP-suiveurs.

## Prérequis
- Python 3.x ou supérieur
- Bibliothèques Python :
  - NumPy
  - Matplotlib (pour visualisation)
  
## Installation
Clonez ce dépôt Git :
```bash
git clone https://github.com/votre-utilisateur/simulation-rlc.git
cd simulation-rlc
