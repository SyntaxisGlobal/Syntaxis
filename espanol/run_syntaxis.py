#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejecutor de Syntaxis - Español
Ejecuta programas Python escritos en sintaxis española
"""

import os
import sys
import subprocess
from pathlib import Path

def mostrar_menu():
    """Muestra el menú principal del ejecutor"""
    print("=" * 50)
    print("    EJECUTOR DE SYNTAXIS - ESPAÑOL")
    print("=" * 50)
    print("1. Ejecutar programa específico")
    print("2. Listar programas disponibles")
    print("3. Traducir programa a Python")
    print("4. Salir")
    print("=" * 50)

def listar_programas():
    """Lista todos los programas disponibles"""
    programas_dir = Path("programas")
    if not programas_dir.exists():
        print("❌ No se encontró la carpeta de programas")
        return
    
    programas = list(programas_dir.glob("*.synt"))
    if not programas:
        print("❌ No hay programas disponibles")
        return
    
    print(f"\n📁 Programas disponibles ({len(programas)}):")
    for i, programa in enumerate(programas, 1):
        print(f"   {i}. {programa.name}")
    
    return programas

def ejecutar_programa(programa_path):
    """Ejecuta un programa .synt"""
    try:
        # Primero traducir a Python
        from translator import traducir_archivo
        
        nombre_base = programa_path.stem
        archivo_python = f"{nombre_base}.py"
        
        print(f"🔄 Traduciendo {programa_path.name}...")
        traducir_archivo(programa_path, archivo_python)
        
        # Ejecutar el código Python traducido
        print(f"🚀 Ejecutando {archivo_python}...")
        print("-" * 30)
        
        resultado = subprocess.run([sys.executable, archivo_python], 
                                 capture_output=True, text=True, encoding='utf-8')
        
        if resultado.stdout:
            print("📤 Salida:")
            print(resultado.stdout)
        
        if resultado.stderr:
            print("⚠️  Errores:")
            print(resultado.stderr)
        
        if resultado.returncode == 0:
            print("✅ Programa ejecutado exitosamente")
        else:
            print(f"❌ Programa terminó con código de salida: {resultado.returncode}")
            
    except Exception as e:
        print(f"❌ Error al ejecutar el programa: {e}")

def main():
    """Función principal del ejecutor"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                programas = listar_programas()
                if programas:
                    try:
                        num = int(input("Ingresa el número del programa a ejecutar: ")) - 1
                        if 0 <= num < len(programas):
                            ejecutar_programa(programas[num])
                        else:
                            print("❌ Número de programa inválido")
                    except ValueError:
                        print("❌ Por favor ingresa un número válido")
                        
            elif opcion == "2":
                listar_programas()
                
            elif opcion == "3":
                programas = listar_programas()
                if programas:
                    try:
                        num = int(input("Ingresa el número del programa a traducir: ")) - 1
                        if 0 <= num < len(programas):
                            from translator import traducir_archivo
                            programa = programas[num]
                            archivo_python = f"{programa.stem}.py"
                            traducir_archivo(programa, archivo_python)
                            print(f"✅ Programa traducido a {archivo_python}")
                        else:
                            print("❌ Número de programa inválido")
                    except ValueError:
                        print("❌ Por favor ingresa un número válido")
                        
            elif opcion == "4":
                print("👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción inválida. Por favor selecciona 1-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
