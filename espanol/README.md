# Syntaxis - Español 🇪🇸

**Syntaxis** es un sistema innovador que permite escribir código Python usando sintaxis en español, haciendo la programación más accesible para hispanohablantes.

## Características Principales

- **Sintaxis en Español**: Escribe código usando palabras clave en español
- **Traducción Automática**: Convierte automáticamente a Python estándar
- **Ejecución Directa**: Ejecuta programas .synt sin necesidad de compilación manual
- **Soporte Completo**: Maneja estructuras complejas, decoradores, metaclases y más
- **Validación de Sintaxis**: Detecta errores antes de la ejecución

## Estructura del Proyecto

```
espanol/
├── README.md                 # Este archivo
├── translator.py            # Traductor principal de Syntaxis a Python
├── run_syntaxis.py         # Ejecutor interactivo de programas
└── programas/              # Directorio de programas de ejemplo
    ├── hola_mundo_leandro_villasenor_2025_02_07.synt
    ├── calculadora_dario_cifuentes_2025_02_15.synt
    ├── conversor_monedas_luis_hernandez_2025_03_15.synt
    ├── juego_adivinanza_inaki_cordero_2025_04_15.synt
    ├── gestor_contactos_octavio_esquivel_2025_05_20.synt
    └── gestor_notas_soraya_morales_2025_07_25.synt
```

## Instalación y Uso

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas

### Ejecutar un Programa

1. **Usando el ejecutor interactivo:**
   ```bash
   python run_syntaxis.py
   ```

2. **Ejecutar programa específico:**
   ```bash
   python run_syntaxis.py
   # Selecciona opción 1 y elige el programa
   ```

3. **Traducir manualmente:**
   ```python
   from translator import traducir_archivo
   traducir_archivo("programa.synt", "programa.py")
   ```

## Sintaxis de Syntaxis

### Palabras Clave Principales

| Syntaxis (Español) | Python (Inglés) | Descripción |
|-------------------|-----------------|-------------|
| `definir` | `def` | Definir función |
| `clase` | `class` | Definir clase |
| `si` | `if` | Condición if |
| `sino` | `else` | Condición else |
| `para` | `for` | Bucle for |
| `mientras` | `while` | Bucle while |
| `imprimir` | `print` | Imprimir texto |
| `entrada` | `input` | Obtener entrada del usuario |
| `retornar` | `return` | Retornar valor |
| `importar` | `import` | Importar módulo |

### Ejemplo de Código

```python
# Syntaxis (Español)
definir saludar(nombre):
    si nombre:
        imprimir(f"¡Hola {nombre}!")
    sino:
        imprimir("¡Hola desconocido!")

# Se traduce automáticamente a:
# def saludar(nombre):
#     if nombre:
#         print(f"¡Hola {nombre}!")
#     else:
#         print("¡Hola desconocido!")
```

## Características Avanzadas

### Contexto de Traducción
- Manejo de scopes anidados
- Seguimiento de variables, funciones y clases
- Validación de tipos y contextos

### Patrones Regex Avanzados
- Detección de patrones complejos
- Traducción de expresiones regulares
- Manejo de literales y operadores

### Manejo de Errores
- Detección temprana de errores de sintaxis
- Mensajes de error en español
- Sugerencias de corrección

## Cómo Funciona

1. **Análisis Léxico**: El código .synt se convierte en tokens
2. **Análisis Sintáctico**: Se valida la estructura del código
3. **Traducción**: Se aplican las reglas de traducción
4. **Generación**: Se produce código Python válido
5. **Ejecución**: Se ejecuta el código Python resultante
---

**¡Disfruta programando en español con Syntaxis!**
