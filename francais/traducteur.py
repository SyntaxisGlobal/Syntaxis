#!/usr/bin/env python3
"""
Syntaxis French to Python Translator
Traduit le code Syntaxis en français vers Python standard
"""

import sys
import re
from pathlib import Path

# Dictionnaire de traduction français -> python
TRADUCTIONS = {
    # Contrôle de flux
    'si': 'if',
    'sinon': 'else',
    'sinon_si': 'elif',
    'pour': 'for',
    'tant_que': 'while',
    'dans': 'in',
    'rompre': 'break',
    'continuer': 'continue',
    'passer': 'pass',
    
    # Fonctions
    'definir': 'def',
    'retourner': 'return',
    'afficher': 'print',
    'entree': 'input',
    
    # Types de données
    'vrai': 'True',
    'faux': 'False',
    'rien': 'None',
    
    # Fonctions intégrées
    'longueur': 'len',
    'type': 'type',
    'entier': 'int',
    'flottant': 'float',
    'chaine': 'str',
    'liste': 'list',
    'dictionnaire': 'dict',
    'ensemble': 'set',
    
    # Opérateurs logiques
    'et': 'and',
    'ou': 'or',
    'non': 'not',
    
    # Autres
    'classe': 'class',
    'importer': 'import',
    'depuis': 'from',
    'comme': 'as',
    'avec': 'with',
    'essayer': 'try',
    'sauf': 'except',
    'finalement': 'finally',
    'lever': 'raise',
    'affirmer': 'assert',
    'global': 'global',
    'non_local': 'nonlocal',
    'rendement': 'yield',
    'lambda': 'lambda'
}

def traduire_ligne(ligne):
    """Traduit une ligne de code Syntaxis vers Python"""
    # Préserver les commentaires
    if ligne.strip().startswith('#') or ligne.strip().startswith('"""'):
        return ligne
    
    # Traduire les mots-clés
    ligne_traduite = ligne
    for francais, python in TRADUCTIONS.items():
        # Utiliser regex pour éviter de remplacer les mots dans les chaînes
        pattern = r'\b' + re.escape(francais) + r'\b'
        ligne_traduite = re.sub(pattern, python, ligne_traduite)
    
    return ligne_traduite

def traduire_fichier(fichier_entree, fichier_sortie=None):
    """Traduit un fichier .synt vers Python"""
    try:
        with open(fichier_entree, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
        
        lignes_traduites = [traduire_ligne(ligne) for ligne in lignes]
        
        if fichier_sortie:
            with open(fichier_sortie, 'w', encoding='utf-8') as f:
                f.writelines(lignes_traduites)
            print(f"Fichier traduit sauvegardé comme: {fichier_sortie}")
        else:
            # Afficher dans la console
            print("Code Python traduit:")
            print("-" * 40)
            for ligne in lignes_traduites:
                print(ligne.rstrip())
            
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier_entree} n'a pas été trouvé")
    except Exception as e:
        print(f"Erreur pendant la traduction: {e}")

def main():
    """Fonction principale"""
    if len(sys.argv) < 2:
        print("Usage: python traducteur.py fichier.synt [fichier.py]")
        print("Si aucun fichier de sortie n'est spécifié, affiché dans la console")
        sys.exit(1)
    
    fichier_entree = sys.argv[1]
    fichier_sortie = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not fichier_entree.endswith('.synt'):
        print("Erreur: Le fichier d'entrée doit avoir l'extension .synt")
        sys.exit(1)
    
    if not Path(fichier_entree).exists():
        print(f"Erreur: Le fichier {fichier_entree} n'existe pas")
        sys.exit(1)
    
    traduire_fichier(fichier_entree, fichier_sortie)

if __name__ == "__main__":
    main()