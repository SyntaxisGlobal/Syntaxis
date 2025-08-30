# Syntaxis - Français 🇫🇷

**Syntaxis** est un système innovant qui permet d'écrire du code Python en utilisant une syntaxe française, rendant la programmation plus accessible aux francophones.

## Caractéristiques Principales

- **Syntaxe en Français** : Écrivez du code en utilisant des mots-clés français
- **Traduction Automatique** : Convertit automatiquement en Python standard
- **Exécution Directe** : Exécute les programmes .synt sans compilation manuelle
- **Support Complet** : Gère les structures complexes, décorateurs, métaclasses et plus
- **Validation de Syntaxe** : Détecte les erreurs avant l'exécution

## Structure du Projet

```
francais/
├── README.md                 # Ce fichier
├── traducteur.py            # Traducteur principal de Syntaxis vers Python
├── executeur_syntaxis.py    # Exécuteur interactif de programmes
└── programmes/              # Répertoire des programmes d'exemple
    ├── bonjour_monde_marie_dupont_2025_02_08.synt
    ├── calculatrice_pierre_martin_2025_03_12.synt
    ├── liste_taches_sophie_bernard_2025_04_18.synt
    ├── convertisseur_devises_lucas_dubois_2025_06_15.synt
    └── jeu_devinettes_emma_leroy_2025_07_20.synt
```

## Installation et Utilisation

### Prérequis
- Python 3.7 ou supérieur
- Aucune dépendance externe requise

### Exécuter un Programme

1. **En utilisant l'exécuteur interactif :**
   ```bash
   python executeur_syntaxis.py
   ```

2. **Exécuter un programme spécifique :**
   ```bash
   python executeur_syntaxis.py
   # Sélectionnez l'option 1 et choisissez le programme
   ```

3. **Traduire manuellement :**
   ```python
   from traducteur import traducir_archivo
   traducir_archivo("programme.synt", "programme.py")
   ```

## Syntaxe de Syntaxis

### Mots-Clés Principaux

| Syntaxis (Français) | Python (Anglais) | Description |
|---------------------|------------------|-------------|
| `definir` | `def` | Définir une fonction |
| `classe` | `class` | Définir une classe |
| `si` | `if` | Condition if |
| `sinon` | `else` | Condition else |
| `pour` | `for` | Boucle for |
| `tant_que` | `while` | Boucle while |
| `imprimer` | `print` | Imprimer du texte |
| `entree` | `input` | Obtenir l'entrée de l'utilisateur |
| `retourner` | `return` | Retourner une valeur |
| `importer` | `import` | Importer un module |

### Exemple de Code

```python
# Syntaxis (Français)
definir saluer(nom):
    si nom:
        imprimer(f"Bonjour {nom}!")
    sinon:
        imprimer("Bonjour inconnu!")

# Se traduit automatiquement en :
# def saluer(nom):
#     if nom:
#         print(f"Bonjour {nom}!")
#     else:
#         print("Bonjour inconnu!")
```

## Programmes d'Exemple

### 1. Bonjour Monde
- **Fichier** : `bonjour_monde_marie_dupont_2025_02_08.synt`
- **Auteur** : Marie Dupont
- **Description** : Programme de base d'introduction

### 2. Calculatrice
- **Fichier** : `calculatrice_pierre_martin_2025_03_12.synt`
- **Auteur** : Pierre Martin
- **Description** : Calculatrice de base avec opérations arithmétiques

### 3. Liste de Tâches
- **Fichier** : `liste_taches_sophie_bernard_2025_04_18.synt`
- **Auteur** : Sophie Bernard
- **Description** : Gestionnaire de liste de tâches

### 4. Convertisseur de Devises
- **Fichier** : `convertisseur_devises_lucas_dubois_2025_06_15.synt`
- **Auteur** : Lucas Dubois
- **Description** : Convertit entre différentes devises

### 5. Jeu de Devinettes
- **Fichier** : `jeu_devinettes_emma_leroy_2025_07_20.synt`
- **Auteur** : Emma Leroy
- **Description** : Jeu interactif de devinettes

## Caractéristiques Avancées

### Contexte de Traduction
- Gestion des portées imbriquées
- Suivi des variables, fonctions et classes
- Validation des types et contextes

### Modèles Regex Avancés
- Détection de modèles complexes
- Traduction d'expressions régulières
- Gestion des littéraux et opérateurs

### Gestion des Erreurs
- Détection précoce des erreurs de syntaxe
- Messages d'erreur en français
- Suggestions de correction

## Comment Ça Marche

1. **Analyse Lexicale** : Le code .synt est converti en tokens
2. **Analyse Syntaxique** : La structure du code est validée
3. **Traduction** : Les règles de traduction sont appliquées
4. **Génération** : Du code Python valide est produit
5. **Exécution** : Le code Python résultant est exécuté

---

**Profitez de la programmation en français avec Syntaxis !**
