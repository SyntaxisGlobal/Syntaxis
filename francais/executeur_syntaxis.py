#!/usr/bin/env python3
"""
Syntaxis French Program Executor
Exécute les programmes Syntaxis écrits en français
"""

import os
import sys
import subprocess
from pathlib import Path
from traducteur import traduire_fichier

def lister_programmes():
    """Liste tous les programmes .synt disponibles"""
    programmes_dir = Path("programmes")
    if not programmes_dir.exists():
        print("Erreur: Le répertoire 'programmes' n'a pas été trouvé")
        return []
    
    programmes = list(programmes_dir.glob("*.synt"))
    if not programmes:
        print("Aucun programme .synt trouvé")
        return []
    
    print("Programmes disponibles:")
    for i, programme in enumerate(programmes, 1):
        print(f"  {i}. {programme.name}")
    
    return programmes

def selectionner_programme(programmes):
    """Permet à l'utilisateur de sélectionner un programme"""
    while True:
        try:
            choix = input("\nSélectionne un programme (numéro) ou 'q' pour quitter: ").strip()
            if choix.lower() == 'q':
                return None
            
            choix_num = int(choix)
            if 1 <= choix_num <= len(programmes):
                return programmes[choix_num - 1]
            else:
                print(f"Veuillez sélectionner un numéro entre 1 et {len(programmes)}")
        except ValueError:
            print("Veuillez entrer un numéro valide")

def executer_programme(chemin_programme):
    """Exécute un programme Syntaxis"""
    print(f"\nExécution de: {chemin_programme.name}")
    print("-" * 50)
    
    # Traduire vers Python
    temp_py = chemin_programme.with_suffix('.py')
    traduire_fichier(chemin_programme, temp_py)
    
    try:
        # Exécuter le code Python traduit
        resultat = subprocess.run([sys.executable, str(temp_py)], 
                                capture_output=True, text=True, encoding='utf-8')
        
        if resultat.stdout:
            print("Sortie:")
            print(resultat.stdout)
        
        if resultat.stderr:
            print("Erreurs:")
            print(resultat.stderr)
        
        if resultat.returncode == 0:
            print("\n✅ Programme exécuté avec succès")
        else:
            print(f"\n❌ Programme terminé avec le code de sortie: {resultat.returncode}")
            
    except Exception as e:
        print(f"Erreur lors de l'exécution du programme: {e}")
    
    finally:
        # Nettoyer le fichier temporaire
        if temp_py.exists():
            temp_py.unlink()

def main():
    """Fonction principale"""
    print("🚀 Exécuteur de Programmes Syntaxis - Français")
    print("=" * 50)
    
    # Changer au répertoire des programmes
    os.chdir(Path(__file__).parent)
    
    programmes = lister_programmes()
    if not programmes:
        return
    
    while True:
        selectionne = selectionner_programme(programmes)
        if selectionne is None:
            break
        
        executer_programme(selectionne)
        
        # Demander s'il veut exécuter un autre
        encore = input("\nExécuter un autre programme? (o/n): ").strip().lower()
        if encore not in ['o', 'oui', 'y', 'yes']:
            break
    
    print("\n👋 Au revoir!")

if __name__ == "__main__":
    main()











