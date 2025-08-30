#!/usr/bin/env python3
"""
Syntaxis Spanish to Python Translator
Traduce código Syntaxis en español a Python estándar
"""

import sys
import re
from pathlib import Path

# Diccionario de traducción español -> python
TRANSLATIONS = {
    # Control de flujo
    'si': 'if',
    'sino': 'else',
    'sino_si': 'elif',
    'para': 'for',
    'mientras': 'while',
    'en': 'in',
    'romper': 'break',
    'continuar': 'continue',
    'pasar': 'pass',
    
    # Funciones
    'definir': 'def',
    'retornar': 'return',
    'imprimir': 'print',
    'entrada': 'input',
    
    # Tipos de datos
    'verdadero': 'True',
    'falso': 'False',
    'nada': 'None',
    
    # Funciones integradas
    'longitud': 'len',
    'tipo': 'type',
    'entero': 'int',
    'flotante': 'float',
    'cadena': 'str',
    'lista': 'list',
    'diccionario': 'dict',
    'conjunto': 'set',
    
    # Operadores lógicos
    'y': 'and',
    'o': 'or',
    'no': 'not',
    
    # Otros
    'clase': 'class',
    'importar': 'import',
    'desde': 'from',
    'como': 'as',
    'con': 'with',
    'intentar': 'try',
    'excepto': 'except',
    'finalmente': 'finally',
    'levantar': 'raise',
    'afirmar': 'assert',
    'global': 'global',
    'no_local': 'nonlocal',
    'rendimiento': 'yield',
    'lamba': 'lambda'
}

def translate_line(line):
    """Traduce una línea de código Syntaxis a Python"""
    # Preservar comentarios
    if line.strip().startswith('#'') or line.strip().startswith('"""'):
        return line
    
    # Traducir palabras clave
    translated_line = line
    for spanish, python in TRANSLATIONS.items():
        # Usar regex para evitar reemplazar palabras dentro de strings
        pattern = r'\b' + re.escape(spanish) + r'\b'
        translated_line = re.sub(pattern, python, translated_line)
    
    return translated_line

def translate_file(input_file, output_file=None):
    """Traduce un archivo .synt a Python"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        translated_lines = [translate_line(line) for line in lines]
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(translated_lines)
            print(f"Archivo traducido guardado como: {output_file}")
        else:
            # Mostrar en consola
            print("Código Python traducido:")
            print("-" * 40)
            for line in translated_lines:
                print(line.rstrip())
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
    except Exception as e:
        print(f"Error durante la traducción: {e}")

def main():
    """Función principal"""
    if len(sys.argv) < 2:
        print("Uso: python translator.py archivo.synt [archivo.py]")
        print("Si no se especifica archivo de salida, se muestra en consola")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not input_file.endswith('.synt'):
        print("Error: El archivo de entrada debe tener extensión .synt")
        sys.exit(1)
    
    if not Path(input_file).exists():
        print(f"Error: El archivo {input_file} no existe")
        sys.exit(1)
    
    translate_file(input_file, output_file)

if __name__ == "__main__":
    main()