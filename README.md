# Syntaxis

**Syntaxis** is a multilingual programming system that allows you to write Python code using Spanish or French keywords. It automatically translates your code to standard Python and executes it.

## What It Does

- Write code in Spanish or French instead of English
- Automatically converts to Python
- Run programs immediately
- Learn Python concepts in your native language

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyntaxisGlobal/Syntaxis.git
   cd Syntaxis
   ```

2. **Choose your language**
   - **Spanish**: `cd espanol`
   - **French**: `cd francais`

3. **Run a program**
   ```bash
   # Spanish
   python run_syntaxis.py
   
   # French
   python executeur_syntaxis.py
   ```

## Basic Syntax

### Spanish Keywords
- `definir` = `def` (define function)
- `si` = `if` (if condition)
- `sino` = `else` (else)
- `para` = `for` (for loop)
- `mientras` = `while` (while loop)
- `imprimir` = `print` (print)
- `entrada` = `input` (input)

### French Keywords
- `definir` = `def` (define function)
- `si` = `if` (if condition)
- `sinon` = `else` (else)
- `pour` = `for` (for loop)
- `tant_que` = `while` (while loop)
- `afficher` = `print` (print)
- `entree` = `input` (input)

## Example

```python
# Spanish
definir saludar(nombre):
    si nombre:
        imprimir(f"¡Hola {nombre}!")
    sino:
        imprimir("¡Hola desconocido!")

# French
definir saluer(nom):
    si nom:
        afficher(f"Bonjour {nom}!")
    sinon:
        afficher("Bonjour inconnu!")
```

## Project Structure

```
Syntaxis/
├── espanol/          # Spanish programs and translator
├── francais/         # French programs and translator
└── README.md         # This file
```

## Requirements

- Python 3.7 or higher
- No external dependencies

