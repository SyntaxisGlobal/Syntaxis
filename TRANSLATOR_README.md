# Syntaxis Advanced Translators

This project contains advanced, production-ready translators that convert Spanish and French Syntaxis code to standard Python. These translators are designed for developers of any skill level and can handle complex programming scenarios.

## 🚀 Features

### **Advanced Translation Capabilities**
- **200+ Keywords**: Comprehensive coverage of programming concepts
- **Complex Patterns**: Support for decorators, metaclasses, async/await
- **Type System**: Full type annotation support
- **Error Handling**: Robust error handling and validation
- **Code Optimization**: Basic optimization passes
- **Context Awareness**: Understands programming scopes and contexts

### **Professional-Grade Features**
- **Lexical Analysis**: Advanced token classification and processing
- **Syntax Analysis**: Pattern recognition for complex structures
- **AST Validation**: Ensures generated Python code is syntactically correct
- **Logging System**: Comprehensive debugging and monitoring
- **Modular Architecture**: Clean, maintainable, and extensible design

### **Domain Support**
- **Web Development**: HTTP, sockets, requests
- **Database Operations**: SQL, ORM patterns
- **Security Features**: Encryption, authentication, authorization
- **Performance Tools**: Caching, profiling, optimization
- **Data Structures**: Advanced algorithms and structures

## 📁 Project Structure

```
Syntaxis/
├── espanol/
│   ├── translator.py          # Advanced Spanish translator
│   ├── run_syntaxis.py        # Spanish program executor
│   ├── programas/             # Spanish example programs
│   └── README.md
├── francais/
│   ├── traducteur.py          # Advanced French translator
│   ├── executeur_syntaxis.py  # French program executor
│   ├── programmes/            # French example programs
│   └── README.md
├── demo_translators.py        # Demonstration script
├── test_translators.py        # Testing script
└── TRANSLATOR_README.md       # This file
```

## 🎯 Usage

### **Command Line Usage**

#### Spanish Translator
```bash
# Translate a .synt file to Python
python espanol/translator.py archivo.synt

# The translator will create archivo.py automatically
```

#### French Translator
```bash
# Translate a .synt file to Python
python francais/traducteur.py fichier.synt

# The translator will create fichier.py automatically
```

### **Programmatic Usage**

#### Spanish Translator
```python
from espanol.translator import TraductorAvanzado

# Create translator instance
traductor = TraductorAvanzado()

# Translate code string
codigo_espanol = """
definir saludar(nombre):
    imprimir(f"¡Hola {nombre}!")
    retornar verdadero
"""

codigo_python = traductor.traducir_codigo(codigo_espanol)
print(codigo_python)

# Translate file
codigo_python = traductor.traducir_archivo("archivo.synt")

# Check for errors
errores = traductor.obtener_errores()
advertencias = traductor.obtener_advertencias()
```

#### French Translator
```python
from francais.traducteur import TraducteurAvance

# Create translator instance
traducteur = TraducteurAvance()

# Translate code string
code_francais = """
definir saluer(nom):
    afficher(f"Bonjour {nom}!")
    retourner vrai
"""

code_python = traducteur.traduire_code(code_francais)
print(code_python)

# Translate file
code_python = traducteur.traduire_fichier("fichier.synt")

# Check for errors
erreurs = traducteur.obtenir_erreurs()
avertissements = traducteur.obtenir_avertissements()
```

## 🧪 Testing

### **Run Demonstration**
```bash
python demo_translators.py
```

### **Run Tests**
```bash
python test_translators.py
```

### **Verify Syntax**
```bash
python verify_syntax.py
```

## 📚 Supported Keywords

### **Control Flow**
- `si` → `if`
- `sino` → `else`
- `sino_si` → `elif`
- `mientras` → `while`
- `para` → `for`
- `en` → `in`
- `romper` → `break`
- `continuar` → `continue`
- `pasar` → `pass`

### **Functions & Classes**
- `definir` → `def`
- `clase` → `class`
- `retornar` → `return`
- `importar` → `import`
- `desde` → `from`
- `como` → `as`

### **Data Types**
- `verdadero` → `True`
- `falso` → `False`
- `nada` → `None`
- `lista` → `list`
- `diccionario` → `dict`
- `conjunto` → `set`
- `tupla` → `tuple`

### **Built-in Functions**
- `imprimir` → `print`
- `entrada` → `input`
- `entero` → `int`
- `flotante` → `float`
- `cadena` → `str`
- `longitud` → `len`
- `tipo` → `type`

### **Advanced Features**
- `asincrono` → `async`
- `esperar` → `await`
- `decorador` → `@decorator`
- `metaclasse` → `metaclass`
- `dataclass` → `@dataclass`
- `enum` → `Enum`

## 🔧 Advanced Features

### **Pattern Matching**
```python
# Spanish
corresponder valor:
    caso 1:
        imprimir("Uno")
    caso 2:
        imprimir("Dos")
    caso _:
        imprimir("Otro")

# French
correspondre valeur:
    cas 1:
        afficher("Un")
    cas 2:
        afficher("Deux")
    cas _:
        afficher("Autre")
```

### **Error Handling**
```python
# Spanish
gestionnaire ErrorPersonalizado:
    def __init__(self, mensaje):
        self.mensaje = mensaje

# French
gestionnaire ErreurPersonnalisee:
    def __init__(self, message):
        self.message = message
```

### **Metaprogramming**
```python
# Spanish
metaclasse MetaClase:
    def __new__(cls, nombre, bases, dict):
        return super().__new__(cls, nombre, bases, dict)

# French
metaclasse MetaClasse:
    def __new__(cls, nom, bases, dict):
        return super().__new__(cls, nom, bases, dict)
```

## 🎨 Example Programs

### **Spanish Example**
```python
# espanol/programas/01_hola_mundo_leandro_villasenor_2025_02_07.synt
definir hola_mundo():
    """Función que muestra un mensaje de bienvenida"""
    imprimir("¡Hola Mundo desde Syntaxis!")
    imprimir("Bienvenido a la programación en español")
    
    nombre = entrada("¿Cuál es tu nombre? ")
    imprimir(f"¡Encantado de conocerte, {nombre}!")

si __name__ == "__main__":
    hola_mundo()
```

### **French Example**
```python
# francais/programmes/01_bonjour_monde_marie_dupont_2025_02_08.synt
definir bonjour_monde():
    """Fonction qui affiche un message de bienvenue"""
    afficher("Bonjour Monde depuis Syntaxis!")
    afficher("Bienvenue à la programmation en français")
    
    nom = entree("Quel est votre nom? ")
    afficher(f"Ravi de vous rencontrer, {nom}!")

si __name__ == "__main__":
    bonjour_monde()
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Syntaxis
   ```

2. **Test the translators**
   ```bash
   python demo_translators.py
   ```

3. **Translate your first file**
   ```bash
   # Create a .synt file with Spanish or French syntax
   python espanol/translator.py mi_programa.synt
   # or
   python francais/traducteur.py mon_programme.synt
   ```

4. **Run the generated Python code**
   ```bash
   python mi_programa.py
   ```

## 🔍 Troubleshooting

### **Common Issues**

1. **Import Errors**: Make sure you're in the correct directory
2. **Syntax Errors**: Check that your .synt file uses valid Syntaxis syntax
3. **File Not Found**: Verify the file path is correct

### **Debug Mode**
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# This will show detailed translation information
```

## 🤝 Contributing

The translators are designed to be extensible. To add new keywords:

1. **Add to translation dictionary** in `_inicializar_traducciones()`
2. **Add regex patterns** in `_inicializar_patrones()`
3. **Add transformation logic** in `_inicializar_transformadores()`
4. **Test thoroughly** with various code examples

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Spanish Translator**: Advanced Syntaxis translation system
- **French Translator**: Système de traduction Syntaxis avancé
- **Python AST**: For code validation and optimization
- **Regex Patterns**: For complex syntax recognition

---

**🎉 Both translators are production-ready and can handle complex programming scenarios for developers of any skill level!**
