#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exécuteur de Syntaxis - Français
Exécute des programmes Python écrits en syntaxe française
"""

import os
import sys
import subprocess
from pathlib import Path

def afficher_menu():
    """Affiche le menu principal de l'exécuteur"""
    print("=" * 50)
    print("    EXÉCUTEUR DE SYNTAXIS - FRANÇAIS")
    print("=" * 50)
    print("1. Exécuter un programme spécifique")
    print("2. Lister les programmes disponibles")
    print("3. Traduire un programme en Python")
    print("4. Quitter")
    print("=" * 50)

def lister_programmes():
    """Liste tous les programmes disponibles"""
    programmes_dir = Path("programmes")
    if not programmes_dir.exists():
        print("❌ Dossier des programmes non trouvé")
        return
    
    programmes = list(programmes_dir.glob("*.synt"))
    if not programmes:
        print("❌ Aucun programme disponible")
        return
    
    print(f"\n📁 Programmes disponibles ({len(programmes)}):")
    for i, programme in enumerate(programmes, 1):
        print(f"   {i}. {programme.name}")
    
    return programmes

def executer_programme(programme_path):
    """Exécute un programme .synt"""
    try:
        # D'abord traduire en Python
        from traducteur import traduire_fichier
        
        nom_base = programme_path.stem
        fichier_python = f"{nom_base}.py"
        
        print(f"🔄 Traduction de {programme_path.name}...")
        traduire_fichier(programme_path, fichier_python)
        
        # Exécuter le code Python traduit
        print(f"🚀 Exécution de {fichier_python}...")
        print("-" * 30)
        
        resultat = subprocess.run([sys.executable, fichier_python], 
                                capture_output=True, text=True, encoding='utf-8')
        
        if resultat.stdout:
            print("📤 Sortie:")
            print(resultat.stdout)
        
        if resultat.stderr:
            print("⚠️  Erreurs:")
            print(resultat.stderr)
        
        if resultat.returncode == 0:
            print("✅ Programme exécuté avec succès")
        else:
            print(f"❌ Programme terminé avec le code de sortie: {resultat.returncode}")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution du programme: {e}")

def main():
    """Fonction principale de l'exécuteur"""
    while True:
        afficher_menu()
        
        try:
            option = input("\nSélectionnez une option (1-4): ").strip()
            
            if option == "1":
                programmes = lister_programmes()
                if programmes:
                    try:
                        num = int(input("Entrez le numéro du programme à exécuter: ")) - 1
                        if 0 <= num < len(programmes):
                            executer_programme(programmes[num])
                        else:
                            print("❌ Numéro de programme invalide")
                    except ValueError:
                        print("❌ Veuillez entrer un numéro valide")
                        
            elif option == "2":
                lister_programmes()
                
            elif option == "3":
                programmes = lister_programmes()
                if programmes:
                    try:
                        num = int(input("Entrez le numéro du programme à traduire: ")) - 1
                        if 0 <= num < len(programmes):
                            from traducteur import traduire_fichier
                            programme = programmes[num]
                            fichier_python = f"{programme.stem}.py"
                            traduire_fichier(programme, fichier_python)
                            print(f"✅ Programme traduit en {fichier_python}")
                        else:
                            print("❌ Numéro de programme invalide")
                    except ValueError:
                        print("❌ Veuillez entrer un numéro valide")
                        
            elif option == "4":
                print("👋 Au revoir!")
                break
                
            else:
                print("❌ Option invalide. Veuillez sélectionner 1-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir!")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
