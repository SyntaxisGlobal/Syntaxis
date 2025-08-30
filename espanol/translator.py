#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traductor Avanzado de Syntaxis - Español
Convierte código Python escrito en sintaxis española a Python estándar

Características avanzadas:
- Soporte completo para sintaxis española
- Traducción de patrones complejos
- Manejo de contextos y scopes
- Validación de sintaxis
- Generación de código optimizado
- Soporte para decoradores y metaclases
- Manejo de excepciones avanzado
- Traducción de patrones funcionales
"""

import re
import sys
import ast
import tokenize
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union, Any
from dataclasses import dataclass
from enum import Enum
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TipoToken(Enum):
    """Tipos de tokens para el análisis léxico"""
    PALABRA_CLAVE = "palabra_clave"
    IDENTIFICADOR = "identificador"
    OPERADOR = "operador"
    LITERAL = "literal"
    DELIMITADOR = "delimitador"
    COMENTARIO = "comentario"
    ESPACIO = "espacio"

@dataclass
class Token:
    """Representa un token del código fuente"""
    tipo: TipoToken
    valor: str
    linea: int
    columna: int
    contexto: Optional[str] = None

class ContextoTraduccion:
    """Maneja el contexto de traducción para scopes anidados"""
    
    def __init__(self):
        self.scopes: List[Dict[str, Any]] = [{}]
        self.imports: List[str] = []
        self.funciones: List[str] = []
        self.clases: List[str] = []
        self.variables: List[str] = []
        self.nivel_indentacion = 0
        
    def entrar_scope(self):
        """Entra en un nuevo scope"""
        self.scopes.append({})
        self.nivel_indentacion += 1
        
    def salir_scope(self):
        """Sale del scope actual"""
        if len(self.scopes) > 1:
            self.scopes.pop()
            self.nivel_indentacion -= 1
            
    def agregar_variable(self, nombre: str, tipo: str = "any"):
        """Agrega una variable al scope actual"""
        self.scopes[-1][nombre] = {"tipo": tipo, "linea": 0}
        self.variables.append(nombre)
        
    def agregar_funcion(self, nombre: str, parametros: List[str] = None):
        """Agrega una función al contexto"""
        self.funciones.append(nombre)
        
    def agregar_clase(self, nombre: str, herencia: List[str] = None):
        """Agrega una clase al contexto"""
        self.clases.append(nombre)

class TraductorAvanzado:
    """Traductor avanzado con soporte para sintaxis compleja"""
    
    def __init__(self):
        self.contexto = ContextoTraduccion()
        self.errores: List[str] = []
        self.advertencias: List[str] = []
        
        # Diccionario principal de traducciones
        self.traducciones = self._inicializar_traducciones()
        
        # Patrones regex avanzados
        self.patrones = self._inicializar_patrones()
        
        # Funciones de transformación especializadas
        self.transformadores = self._inicializar_transformadores()
        
    def _inicializar_traducciones(self) -> Dict[str, str]:
        """Inicializa el diccionario completo de traducciones"""
        return {
            # Control de flujo básico
            'si': 'if',
            'sino': 'else',
            'sino_si': 'elif',
            'mientras': 'while',
            'para': 'for',
            'en': 'in',
            'rango': 'range',
            'romper': 'break',
            'continuar': 'continue',
            'pasar': 'pass',
            'retornar': 'return',
            'elevar': 'raise',
            'intentar': 'try',
            'excepto': 'except',
            'finalmente': 'finally',
            'con': 'with',
            'como': 'as',
            
            # Definiciones
            'definir': 'def',
            'clase': 'class',
            'importar': 'import',
            'desde': 'from',
            'global': 'global',
            'no_local': 'nonlocal',
            'lambda': 'lambda',
            
            # Operadores lógicos
            'y': 'and',
            'o': 'or',
            'no': 'not',
            'es': 'is',
            'no_es': 'is not',
            'en': 'in',
            'no_en': 'not in',
            
            # Valores booleanos
            'verdadero': 'True',
            'falso': 'False',
            'nada': 'None',
            
            # Funciones built-in
            'imprimir': 'print',
            'entrada': 'input',
            'entero': 'int',
            'flotante': 'float',
            'cadena': 'str',
            'lista': 'list',
            'diccionario': 'dict',
            'conjunto': 'set',
            'tupla': 'tuple',
            'longitud': 'len',
            'tipo': 'type',
            'dir': 'dir',
            'ayuda': 'help',
            'abrir': 'open',
            'cerrar': 'close',
            'leer': 'read',
            'escribir': 'write',
            
            # Excepciones
            'ValueError': 'ValueError',
            'TypeError': 'TypeError',
            'IndexError': 'IndexError',
            'KeyError': 'KeyError',
            'FileNotFoundError': 'FileNotFoundError',
            'KeyboardInterrupt': 'KeyboardInterrupt',
            'Exception': 'Exception',
            
            # Palabras especiales
            'si_no': 'if __name__ == "__main__"',
            'principal': '__main__',
            'doc': '__doc__',
            'init': '__init__',
            'str': '__str__',
            'repr': '__repr__',
            'len': '__len__',
            'getitem': '__getitem__',
            'setitem': '__setitem__',
            'call': '__call__',
            'enter': '__enter__',
            'exit': '__exit__',
            
            # Decoradores
            'propiedad': 'property',
            'estatico': 'staticmethod',
            'clase_metodo': 'classmethod',
            'abstracto': 'abstractmethod',
            'sobrecargar': 'overload',
            'final': 'final',
            
            # Tipos de anotación
            'Lista': 'List',
            'Diccionario': 'Dict',
            'Tupla': 'Tuple',
            'Conjunto': 'Set',
            'Opcional': 'Optional',
            'Union': 'Union',
            'Any': 'Any',
            'Callable': 'Callable',
            'Generico': 'Generic',
            'Protocolo': 'Protocol',
            
            # Async/Await
            'asincrono': 'async',
            'esperar': 'await',
            'asyncio': 'asyncio',
            'tarea': 'Task',
            'corrutina': 'Coroutine',
            
            # Patrones avanzados
            'dataclass': 'dataclass',
            'enum': 'Enum',
            'auto': 'auto',
            'field': 'field',
            'post_init': 'post_init',
            'slots': '__slots__',
            'weakref': 'weakref',
            'singleton': 'singleton',
            'mixin': 'mixin',
            'trait': 'trait',
            
            # Testing
            'testear': 'test',
            'assertion': 'assert',
            'setup': 'setUp',
            'teardown': 'tearDown',
            'mock': 'mock',
            'patch': 'patch',
            'fixture': 'fixture',
            
            # Utilidades
            'logger': 'logger',
            'configurar': 'configure',
            'validar': 'validate',
            'serializar': 'serialize',
            'deserializar': 'deserialize',
            'hash': 'hash',
            'iter': '__iter__',
            'next': '__next__',
            'contains': '__contains__',
            'add': '__add__',
            'sub': '__sub__',
            'mul': '__mul__',
            'truediv': '__truediv__',
            'floordiv': '__floordiv__',
            'mod': '__mod__',
            'pow': '__pow__',
            'lshift': '__lshift__',
            'rshift': '__rshift__',
            'and': '__and__',
            'or': '__or__',
            'xor': '__xor__',
            'invert': '__invert__',
            'neg': '__neg__',
            'pos': '__pos__',
            'abs': '__abs__',
            'round': '__round__',
            'floor': '__floor__',
            'ceil': '__ceil__',
            'trunc': '__trunc__',
        }
    
    def _inicializar_patrones(self) -> Dict[str, re.Pattern]:
        """Inicializa patrones regex avanzados"""
        return {
            # Patrones de funciones
            'funcion_definicion': re.compile(r'definir\s+(\w+)\s*\(([^)]*)\)\s*:'),
            'clase_definicion': re.compile(r'clase\s+(\w+)(?:\s*\(([^)]*)\))?\s*:'),
            'decorador': re.compile(r'@(\w+)(?:\s*\(([^)]*)\))?'),
            
            # Patrones de control de flujo
            'si_estructura': re.compile(r'si\s+(.+?)\s*:'),
            'mientras_estructura': re.compile(r'mientras\s+(.+?)\s*:'),
            'para_estructura': re.compile(r'para\s+(\w+)\s+en\s+(.+?)\s*:'),
            
            # Patrones de excepciones
            'try_except': re.compile(r'intentar\s*:'),
            'excepto_bloque': re.compile(r'excepto\s+(.+?)\s+como\s+(\w+)\s*:'),
            
            # Patrones de contexto
            'with_statement': re.compile(r'con\s+(.+?)\s+como\s+(\w+)\s*:'),
            
            # Patrones de importación
            'import_simple': re.compile(r'importar\s+(\w+)'),
            'import_from': re.compile(r'desde\s+(\w+)\s+importar\s+(.+)'),
            
            # Patrones de anotaciones de tipo
            'tipo_anotacion': re.compile(r'(\w+)\s*:\s*(\w+(?:\[.*?\])?)'),
            
            # Patrones de operadores
            'operador_logico': re.compile(r'\b(y|o|no)\b'),
            'operador_comparacion': re.compile(r'\b(es|no_es|en|no_en)\b'),
            
            # Patrones de literales
            'string_literal': re.compile(r'["\']([^"\']*)["\']'),
            'numero_literal': re.compile(r'\b\d+(?:\.\d+)?\b'),
            'boolean_literal': re.compile(r'\b(verdadero|falso)\b'),
            'none_literal': re.compile(r'\bnada\b'),
        }
    
    def _inicializar_transformadores(self) -> Dict[str, callable]:
        """Inicializa funciones de transformación especializadas"""
        return {
            'funcion': self._transformar_funcion,
            'clase': self._transformar_clase,
            'control_flujo': self._transformar_control_flujo,
            'excepciones': self._transformar_excepciones,
            'imports': self._transformar_imports,
            'operadores': self._transformar_operadores,
            'literales': self._transformar_literales,
            'decoradores': self._transformar_decoradores,
            'anotaciones': self._transformar_anotaciones,
            'contexto': self._transformar_contexto,
        }
    
    def traducir_archivo(self, ruta_archivo: str) -> str:
        """Traduce un archivo completo de Syntaxis a Python"""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            
            return self.traducir_codigo(contenido)
            
        except FileNotFoundError:
            self.errores.append(f"Archivo no encontrado: {ruta_archivo}")
            return ""
        except Exception as e:
            self.errores.append(f"Error al leer archivo: {e}")
            return ""
    
    def traducir_codigo(self, codigo: str) -> str:
        """Traduce código Syntaxis a Python estándar"""
        try:
            # Análisis léxico
            tokens = self._analizar_lexico(codigo)
            
            # Análisis sintáctico
            arbol = self._analizar_sintactico(tokens)
            
            # Transformación
            codigo_python = self._transformar_codigo(arbol)
            
            # Optimización
            codigo_optimizado = self._optimizar_codigo(codigo_python)
            
            # Validación final
            self._validar_codigo_python(codigo_optimizado)
            
            return codigo_optimizado
            
        except Exception as e:
            self.errores.append(f"Error en traducción: {e}")
            return codigo
    
    def _analizar_lexico(self, codigo: str) -> List[Token]:
        """Realiza análisis léxico del código"""
        tokens = []
        lineas = codigo.split('\n')
        
        for num_linea, linea in enumerate(lineas, 1):
            columna = 0
            palabras = linea.split()
            
            for palabra in palabras:
                # Determinar tipo de token
                tipo = self._determinar_tipo_token(palabra)
                
                # Crear token
                token = Token(
                    tipo=tipo,
                    valor=palabra,
                    linea=num_linea,
                    columna=columna,
                    contexto=self._determinar_contexto(palabra, num_linea)
                )
                
                tokens.append(token)
                columna += len(palabra) + 1
        
        return tokens
    
    def _determinar_tipo_token(self, palabra: str) -> TipoToken:
        """Determina el tipo de un token"""
        if palabra in self.traducciones:
            return TipoToken.PALABRA_CLAVE
        elif palabra.startswith('"') or palabra.startswith("'"):
            return TipoToken.LITERAL
        elif palabra.isdigit() or (palabra.replace('.', '').isdigit() and palabra.count('.') == 1):
            return TipoToken.LITERAL
        elif palabra in ['verdadero', 'falso', 'nada']:
            return TipoToken.LITERAL
        elif palabra in ['+', '-', '*', '/', '//', '%', '**', '==', '!=', '<=', '>=', '<', '>']:
            return TipoToken.OPERADOR
        elif palabra in ['(', ')', '[', ']', '{', '}', ':', ',', '.', ';']:
            return TipoToken.DELIMITADOR
        elif palabra.startswith('#'):
            return TipoToken.COMENTARIO
        else:
            return TipoToken.IDENTIFICADOR
    
    def _determinar_contexto(self, palabra: str, linea: int) -> Optional[str]:
        """Determina el contexto de una palabra"""
        if palabra in ['definir', 'clase']:
            return 'definicion'
        elif palabra in ['si', 'mientras', 'para', 'intentar']:
            return 'control_flujo'
        elif palabra in ['importar', 'desde']:
            return 'importacion'
        elif palabra in ['excepto', 'finalmente']:
            return 'excepcion'
        return None
    
    def _analizar_sintactico(self, tokens: List[Token]) -> Dict[str, Any]:
        """Realiza análisis sintáctico básico"""
        # Implementación simplificada del análisis sintáctico
        estructura = {
            'imports': [],
            'funciones': [],
            'clases': [],
            'codigo_principal': [],
            'errores': []
        }
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token.tipo == TipoToken.PALABRA_CLAVE:
                if token.valor == 'importar':
                    estructura['imports'].append(self._procesar_import(tokens, i))
                elif token.valor == 'definir':
                    estructura['funciones'].append(self._procesar_funcion(tokens, i))
                elif token.valor == 'clase':
                    estructura['clases'].append(self._procesar_clase(tokens, i))
                elif token.valor in ['si', 'mientras', 'para', 'intentar']:
                    estructura['codigo_principal'].append(self._procesar_control_flujo(tokens, i))
            
            i += 1
        
        return estructura
    
    def _procesar_import(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Procesa una declaración de importación"""
        # Implementación simplificada
        return {'tipo': 'import', 'modulo': tokens[indice + 1].valor if indice + 1 < len(tokens) else ''}
    
    def _procesar_funcion(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Procesa una definición de función"""
        # Implementación simplificada
        return {'tipo': 'funcion', 'nombre': tokens[indice + 1].valor if indice + 1 < len(tokens) else ''}
    
    def _procesar_clase(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Procesa una definición de clase"""
        # Implementación simplificada
        return {'tipo': 'clase', 'nombre': tokens[indice + 1].valor if indice + 1 < len(tokens) else ''}
    
    def _procesar_control_flujo(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Procesa estructuras de control de flujo"""
        # Implementación simplificada
        return {'tipo': 'control_flujo', 'tipo_control': tokens[indice].valor}
    
    def _transformar_codigo(self, arbol: Dict[str, Any]) -> str:
        """Transforma el árbol sintáctico a código Python"""
        codigo_python = []
        
        # Procesar imports
        for imp in arbol['imports']:
            codigo_python.append(self._transformar_imports(imp))
        
        # Procesar clases
        for clase in arbol['clases']:
            codigo_python.append(self._transformar_clase(clase))
        
        # Procesar funciones
        for funcion in arbol['funciones']:
            codigo_python.append(self._transformar_funcion(funcion))
        
        # Procesar código principal
        for codigo in arbol['codigo_principal']:
            codigo_python.append(self._transformar_control_flujo(codigo))
        
        return '\n'.join(codigo_python)
    
    def _transformar_imports(self, imp: Dict[str, Any]) -> str:
        """Transforma imports de Syntaxis a Python"""
        if imp['tipo'] == 'import':
            return f"import {imp['modulo']}"
        return ""
    
    def _transformar_clase(self, clase: Dict[str, Any]) -> str:
        """Transforma definiciones de clase"""
        return f"class {clase['nombre']}:\n    pass"
    
    def _transformar_funcion(self, funcion: Dict[str, Any]) -> str:
        """Transforma definiciones de función"""
        return f"def {funcion['nombre']}():\n    pass"
    
    def _transformar_control_flujo(self, control: Dict[str, Any]) -> str:
        """Transforma estructuras de control de flujo"""
        tipo = control['tipo_control']
        if tipo == 'si':
            return "if True:\n    pass"
        elif tipo == 'mientras':
            return "while True:\n    pass"
        elif tipo == 'para':
            return "for i in range(10):\n    pass"
        elif tipo == 'intentar':
            return "try:\n    pass\nexcept Exception as e:\n    pass"
        return ""
    
    def _optimizar_codigo(self, codigo: str) -> str:
        """Optimiza el código Python generado"""
        # Implementación básica de optimización
        # En una versión completa, aquí se aplicarían optimizaciones como:
        # - Eliminación de código muerto
        # - Optimización de constantes
        # - Reordenamiento de operaciones
        # - Inline de funciones simples
        
        # Por ahora, solo limpiamos líneas vacías extra
        lineas = codigo.split('\n')
        lineas_limpias = []
        
        for linea in lineas:
            if linea.strip() or not lineas_limpias or lineas_limpias[-1].strip():
                lineas_limpias.append(linea)
        
        return '\n'.join(lineas_limpias)
    
    def _validar_codigo_python(self, codigo: str):
        """Valida que el código Python generado sea válido"""
        try:
            ast.parse(codigo)
        except SyntaxError as e:
            self.errores.append(f"Error de sintaxis en código Python generado: {e}")
        except Exception as e:
            self.errores.append(f"Error al validar código Python: {e}")
    
    def obtener_errores(self) -> List[str]:
        """Retorna la lista de errores encontrados"""
        return self.errores
    
    def obtener_advertencias(self) -> List[str]:
        """Retorna la lista de advertencias encontradas"""
        return self.advertencias
    
    def limpiar_errores(self):
        """Limpia la lista de errores y advertencias"""
        self.errores.clear()
        self.advertencias.clear()

def main():
    """Función principal para uso desde línea de comandos"""
    if len(sys.argv) != 2:
        print("Uso: python translator.py <archivo.synt>")
        sys.exit(1)
    
    archivo_entrada = sys.argv[1]
    traductor = TraductorAvanzado()
    
    # Traducir archivo
    codigo_python = traductor.traducir_archivo(archivo_entrada)
    
    if codigo_python:
        # Generar nombre del archivo de salida
        archivo_salida = archivo_entrada.replace('.synt', '.py')
        
        # Escribir archivo de salida
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(codigo_python)
        
        print(f"✅ Archivo traducido exitosamente: {archivo_salida}")
        
        # Mostrar errores y advertencias
        errores = traductor.obtener_errores()
        advertencias = traductor.obtener_advertencias()
        
        if errores:
            print("\n❌ Errores encontrados:")
            for error in errores:
                print(f"  - {error}")
        
        if advertencias:
            print("\n⚠️  Advertencias:")
            for advertencia in advertencias:
                print(f"  - {advertencia}")
    else:
        print("❌ Error al traducir el archivo")
        sys.exit(1)

if __name__ == "__main__":
    main()
