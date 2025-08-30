#!/usr/bin/env python3
"""
Syntaxis Spanish Program Executor
Ejecuta programas Syntaxis escritos en español
"""

import os
import sys
import subprocess
from pathlib import Path
from translator import translate_file

def list_programs():
    """Lista todos los programas .synt disponibles"""
    programas_dir = Path("programas")
    if not programas_dir.exists():
        print("Error: No se encontró el directorio 'programas'")
        return []
    
    programs = list(programas_dir.glob("*.synt"))
    if not programs:
        print("No se encontraron programas .synt")
        return []
    
    print("Programas disponibles:")
    for i, program in enumerate(programs, 1):
        print(f"  {i}. {program.name}")
    
    return programs

def select_program(programs):
    """Permite al usuario seleccionar un programa"""
    while True:
        try:
            choice = input("\nSelecciona un programa (número) o 'q' para salir: ").strip()
            if choice.lower() == 'q':
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(programs):
                return programs[choice_num - 1]
            else:
                print(f"Por favor selecciona un número entre 1 y {len(programs)}")
        except ValueError:
            print("Por favor ingresa un número válido")

def run_program(program_path):
    """Ejecuta un programa Syntaxis"""
    print(f"\nEjecutando: {program_path.name}")
    print("-" * 50)
    
    # Traducir a Python
    temp_py = program_path.with_suffix('.py')
    translate_file(program_path, temp_py)
    
    try:
        # Ejecutar el código Python traducido
        result = subprocess.run([sys.executable, str(temp_py)], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.stdout:
            print("Salida:")
            print(result.stdout)
        
        if result.stderr:
            print("Errores:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ Programa ejecutado exitosamente")
        else:
            print(f"\n❌ Programa terminó con código de salida: {result.returncode}")
            
    except Exception as e:
        print(f"Error ejecutando el programa: {e}")
    
    finally:
        # Limpiar archivo temporal
        if temp_py.exists():
            temp_py.unlink()

def main():
    """Función principal"""
    print("🚀 Ejecutor de Programas Syntaxis - Español")
    print("=" * 50)
    
    # Cambiar al directorio de programas
    os.chdir(Path(__file__).parent)
    
    programs = list_programs()
    if not programs:
        return
    
    while True:
        selected = select_program(programs)
        if selected is None:
            break
        
        run_program(selected)
        
        # Preguntar si quiere ejecutar otro
        again = input("\n¿Ejecutar otro programa? (s/n): ").strip().lower()
        if again not in ['s', 'si', 'y', 'yes']:
            break
    
    print("\n👋 ¡Hasta luego!")

if __name__ == "__main__":
    main()











