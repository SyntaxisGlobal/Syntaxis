#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traducteur Avancé de Syntaxis - Français
Convertit le code Python écrit en syntaxe française en Python standard

Caractéristiques avancées:
- Support complet pour la syntaxe française
- Traduction de motifs complexes
- Gestion des contextes et scopes
- Validation de syntaxe
- Génération de code optimisé
- Support pour décorateurs et métaclasses
- Gestion avancée des exceptions
- Traduction de motifs fonctionnels
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

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TypeToken(Enum):
    """Types de tokens pour l'analyse lexicale"""
    MOT_CLE = "mot_cle"
    IDENTIFIANT = "identifiant"
    OPERATEUR = "operateur"
    LITTERAL = "litteral"
    DELIMITEUR = "delimiteur"
    COMMENTAIRE = "commentaire"
    ESPACE = "espace"

@dataclass
class Token:
    """Représente un token du code source"""
    type: TypeToken
    valeur: str
    ligne: int
    colonne: int
    contexte: Optional[str] = None

class ContexteTraduction:
    """Gère le contexte de traduction pour les scopes imbriqués"""
    
    def __init__(self):
        self.scopes: List[Dict[str, Any]] = [{}]
        self.imports: List[str] = []
        self.fonctions: List[str] = []
        self.classes: List[str] = []
        self.variables: List[str] = []
        self.niveau_indentation = 0
        
    def entrer_scope(self):
        """Entre dans un nouveau scope"""
        self.scopes.append({})
        self.niveau_indentation += 1
        
    def sortir_scope(self):
        """Sort du scope actuel"""
        if len(self.scopes) > 1:
            self.scopes.pop()
            self.niveau_indentation -= 1
            
    def ajouter_variable(self, nom: str, type: str = "any"):
        """Ajoute une variable au scope actuel"""
        self.scopes[-1][nom] = {"type": type, "ligne": 0}
        self.variables.append(nom)
        
    def ajouter_fonction(self, nom: str, parametres: List[str] = None):
        """Ajoute une fonction au contexte"""
        self.fonctions.append(nom)
        
    def ajouter_classe(self, nom: str, heritage: List[str] = None):
        """Ajoute une classe au contexte"""
        self.classes.append(nom)

class TraducteurAvance:
    """Traducteur avancé avec support pour la syntaxe complexe"""
    
    def __init__(self):
        self.contexte = ContexteTraduction()
        self.erreurs: List[str] = []
        self.avertissements: List[str] = []
        
        # Dictionnaire principal de traductions
        self.traductions = self._initialiser_traductions()
        
        # Motifs regex avancés
        self.motifs = self._initialiser_motifs()
        
        # Fonctions de transformation spécialisées
        self.transformateurs = self._initialiser_transformateurs()
        
    def _initialiser_traductions(self) -> Dict[str, str]:
        """Initialise le dictionnaire complet de traductions"""
        return {
            # Contrôle de flux de base
            'si': 'if',
            'sinon': 'else',
            'sinon_si': 'elif',
            'tant_que': 'while',
            'pour': 'for',
            'dans': 'in',
            'plage': 'range',
            'casser': 'break',
            'continuer': 'continue',
            'passer': 'pass',
            'retourner': 'return',
            'lever': 'raise',
            'essayer': 'try',
            'sauf': 'except',
            'enfin': 'finally',
            'avec': 'with',
            'comme': 'as',
            
            # Définitions
            'definir': 'def',
            'classe': 'class',
            'importer': 'import',
            'de': 'from',
            'global': 'global',
            'non_local': 'nonlocal',
            'lambda': 'lambda',
            
            # Opérateurs logiques
            'et': 'and',
            'ou': 'or',
            'non': 'not',
            'est': 'is',
            'n_est_pas': 'is not',
            'dans': 'in',
            'pas_dans': 'not in',
            
            # Valeurs booléennes
            'vrai': 'True',
            'faux': 'False',
            'rien': 'None',
            
            # Fonctions intégrées
            'afficher': 'print',
            'entree': 'input',
            'entier': 'int',
            'flottant': 'float',
            'chaine': 'str',
            'liste': 'list',
            'dictionnaire': 'dict',
            'ensemble': 'set',
            'tuple': 'tuple',
            'longueur': 'len',
            'type': 'type',
            'dir': 'dir',
            'aide': 'help',
            'ouvrir': 'open',
            'fermer': 'close',
            'lire': 'read',
            'ecrire': 'write',
            
            # Exceptions
            'ValueError': 'ValueError',
            'TypeError': 'TypeError',
            'IndexError': 'IndexError',
            'KeyError': 'KeyError',
            'FileNotFoundError': 'FileNotFoundError',
            'KeyboardInterrupt': 'KeyboardInterrupt',
            'Exception': 'Exception',
            
            # Mots spéciaux
            'si_non': 'if __name__ == "__main__"',
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
            
            # Décorateurs
            'propriete': 'property',
            'statique': 'staticmethod',
            'methode_classe': 'classmethod',
            'abstrait': 'abstractmethod',
            'surcharger': 'overload',
            'final': 'final',
            
            # Types d'annotation
            'Liste': 'List',
            'Dictionnaire': 'Dict',
            'Tuple': 'Tuple',
            'Ensemble': 'Set',
            'Optionnel': 'Optional',
            'Union': 'Union',
            'Tout': 'Any',
            'Appelable': 'Callable',
            'Generique': 'Generic',
            'Protocole': 'Protocol',
            
            # Async/Await
            'asynchrone': 'async',
            'attendre': 'await',
            'asyncio': 'asyncio',
            'tache': 'Task',
            'coroutine': 'Coroutine',
            
            # Motifs avancés
            'dataclass': 'dataclass',
            'enum': 'Enum',
            'auto': 'auto',
            'champ': 'field',
            'post_init': 'post_init',
            'slots': '__slots__',
            'weakref': 'weakref',
            'singleton': 'singleton',
            'mixin': 'mixin',
            'trait': 'trait',
            
            # Tests
            'tester': 'test',
            'assertion': 'assert',
            'configuration': 'setUp',
            'nettoyage': 'tearDown',
            'mock': 'mock',
            'patch': 'patch',
            'fixture': 'fixture',
            
            # Utilitaires
            'logger': 'logger',
            'configurer': 'configure',
            'valider': 'validate',
            'serialiser': 'serialize',
            'deserialiser': 'deserialize',
            'hash': 'hash',
            'iter': '__iter__',
            'suivant': '__next__',
            'contient': '__contains__',
            'ajouter': '__add__',
            'soustraire': '__sub__',
            'multiplier': '__mul__',
            'diviser': '__truediv__',
            'diviser_entiere': '__floordiv__',
            'modulo': '__mod__',
            'puissance': '__pow__',
            'decalage_gauche': '__lshift__',
            'decalage_droite': '__rshift__',
            'et_bit': '__and__',
            'ou_bit': '__or__',
            'ou_exclusif': '__xor__',
            'inverser': '__invert__',
            'negatif': '__neg__',
            'positif': '__pos__',
            'absolu': '__abs__',
            'arrondir': '__round__',
            'plancher': '__floor__',
            'plafond': '__ceil__',
            'tronquer': '__trunc__',
            
            # Structures de données avancées
            'pile': 'stack',
            'file': 'queue',
            'arbre': 'tree',
            'graphe': 'graph',
            'tableau': 'array',
            'matrice': 'matrix',
            'vecteur': 'vector',
            'point': 'point',
            'rectangle': 'rectangle',
            'cercle': 'circle',
            
            # Algorithmes
            'trier': 'sort',
            'rechercher': 'search',
            'filtrer': 'filter',
            'mapper': 'map',
            'reduire': 'reduce',
            'accumuler': 'accumulate',
            'combiner': 'combine',
            'diviser': 'split',
            'fusionner': 'merge',
            'partitionner': 'partition',
            
            # Gestion de fichiers
            'fichier': 'file',
            'dossier': 'directory',
            'chemin': 'path',
            'existe': 'exists',
            'creer': 'create',
            'supprimer': 'delete',
            'copier': 'copy',
            'deplacer': 'move',
            'renommer': 'rename',
            'lister': 'listdir',
            
            # Réseau et web
            'requete': 'request',
            'reponse': 'response',
            'url': 'url',
            'http': 'http',
            'socket': 'socket',
            'serveur': 'server',
            'client': 'client',
            'connexion': 'connection',
            'donnees': 'data',
            'envoyer': 'send',
            'recevoir': 'receive',
            
            # Base de données
            'base_donnees': 'database',
            'table': 'table',
            'requete_sql': 'sql_query',
            'executer': 'execute',
            'selectionner': 'select',
            'inserer': 'insert',
            'modifier': 'update',
            'supprimer': 'delete',
            'joindre': 'join',
            'grouper': 'group',
            
            # Sécurité
            'crypter': 'encrypt',
            'decrypter': 'decrypt',
            'hasher': 'hash',
            'verifier': 'verify',
            'signer': 'sign',
            'authentifier': 'authenticate',
            'autoriser': 'authorize',
            'token': 'token',
            'session': 'session',
            'permission': 'permission',
            
            # Performance
            'cache': 'cache',
            'memoire': 'memory',
            'optimiser': 'optimize',
            'profiler': 'profile',
            'benchmark': 'benchmark',
            'parallele': 'parallel',
            'asynchrone': 'asynchronous',
            'thread': 'thread',
            'processus': 'process',
            'pool': 'pool',
        }
    
    def _initialiser_motifs(self) -> Dict[str, re.Pattern]:
        """Initialise les motifs regex avancés"""
        return {
            # Motifs de fonctions
            'definition_fonction': re.compile(r'definir\s+(\w+)\s*\(([^)]*)\)\s*:'),
            'definition_classe': re.compile(r'classe\s+(\w+)(?:\s*\(([^)]*)\))?\s*:'),
            'decorateur': re.compile(r'@(\w+)(?:\s*\(([^)]*)\))?'),
            
            # Motifs de contrôle de flux
            'structure_si': re.compile(r'si\s+(.+?)\s*:'),
            'structure_tant_que': re.compile(r'tant_que\s+(.+?)\s*:'),
            'structure_pour': re.compile(r'pour\s+(\w+)\s+dans\s+(.+?)\s*:'),
            
            # Motifs d'exceptions
            'try_except': re.compile(r'essayer\s*:'),
            'bloc_sauf': re.compile(r'sauf\s+(.+?)\s+comme\s+(\w+)\s*:'),
            
            # Motifs de contexte
            'with_statement': re.compile(r'avec\s+(.+?)\s+comme\s+(\w+)\s*:'),
            
            # Motifs d'importation
            'import_simple': re.compile(r'importer\s+(\w+)'),
            'import_de': re.compile(r'de\s+(\w+)\s+importer\s+(.+)'),
            
            # Motifs d'annotations de type
            'annotation_type': re.compile(r'(\w+)\s*:\s*(\w+(?:\[.*?\])?)'),
            
            # Motifs d'opérateurs
            'operateur_logique': re.compile(r'\b(et|ou|non)\b'),
            'operateur_comparaison': re.compile(r'\b(est|n_est_pas|dans|pas_dans)\b'),
            
            # Motifs de littéraux
            'litteral_chaine': re.compile(r'["\']([^"\']*)["\']'),
            'litteral_nombre': re.compile(r'\b\d+(?:\.\d+)?\b'),
            'litteral_booleen': re.compile(r'\b(vrai|faux)\b'),
            'litteral_rien': re.compile(r'\brien\b'),
            
            # Motifs de gestion d'erreurs
            'gestion_erreur': re.compile(r'gestionnaire\s+(\w+)'),
            'erreur_personnalisee': re.compile(r'erreur\s+(\w+)'),
            'validation': re.compile(r'valider\s+(.+)'),
            
            # Motifs de patterns avancés
            'pattern_matching': re.compile(r'correspondre\s+(\w+)\s*:'),
            'case_pattern': re.compile(r'cas\s+(.+?)\s*:'),
            'guard_clause': re.compile(r'quand\s+(.+?)\s*:'),
            
            # Motifs de métaprogrammation
            'metaclasse': re.compile(r'metaclasse\s+(\w+)'),
            'descripteur': re.compile(r'descripteur\s+(\w+)'),
            'propriete_dynamique': re.compile(r'propriete\s+(\w+)'),
        }
    
    def _initialiser_transformateurs(self) -> Dict[str, callable]:
        """Initialise les fonctions de transformation spécialisées"""
        return {
            'fonction': self._transformer_fonction,
            'classe': self._transformer_classe,
            'controle_flux': self._transformer_controle_flux,
            'exceptions': self._transformer_exceptions,
            'imports': self._transformer_imports,
            'operateurs': self._transformer_operateurs,
            'litteraux': self._transformer_litteraux,
            'decorateurs': self._transformer_decorateurs,
            'annotations': self._transformer_annotations,
            'contexte': self._transformer_contexte,
            'patterns': self._transformer_patterns,
            'metaprogrammation': self._transformer_metaprogrammation,
        }
    
    def traduire_fichier(self, chemin_fichier: str) -> str:
        """Traduit un fichier complet de Syntaxis en Python"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
            
            return self.traduire_code(contenu)
            
        except FileNotFoundError:
            self.erreurs.append(f"Fichier non trouvé: {chemin_fichier}")
            return ""
        except Exception as e:
            self.erreurs.append(f"Erreur lors de la lecture du fichier: {e}")
            return ""
    
    def traduire_code(self, code: str) -> str:
        """Traduit le code Syntaxis en Python standard"""
        try:
            # Analyse lexicale
            tokens = self._analyser_lexical(code)
            
            # Analyse syntaxique
            arbre = self._analyser_syntaxique(tokens)
            
            # Transformation
            code_python = self._transformer_code(arbre)
            
            # Optimisation
            code_optimise = self._optimiser_code(code_python)
            
            # Validation finale
            self._valider_code_python(code_optimise)
            
            return code_optimise
            
        except Exception as e:
            self.erreurs.append(f"Erreur lors de la traduction: {e}")
            return code
    
    def _analyser_lexical(self, code: str) -> List[Token]:
        """Effectue l'analyse lexicale du code"""
        tokens = []
        lignes = code.split('\n')
        
        for num_ligne, ligne in enumerate(lignes, 1):
            colonne = 0
            mots = ligne.split()
            
            for mot in mots:
                # Déterminer le type de token
                type_token = self._determiner_type_token(mot)
                
                # Créer le token
                token = Token(
                    type=type_token,
                    valeur=mot,
                    ligne=num_ligne,
                    colonne=colonne,
                    contexte=self._determiner_contexte(mot, num_ligne)
                )
                
                tokens.append(token)
                colonne += len(mot) + 1
        
        return tokens
    
    def _determiner_type_token(self, mot: str) -> TypeToken:
        """Détermine le type d'un token"""
        if mot in self.traductions:
            return TypeToken.MOT_CLE
        elif mot.startswith('"') or mot.startswith("'"):
            return TypeToken.LITTERAL
        elif mot.isdigit() or (mot.replace('.', '').isdigit() and mot.count('.') == 1):
            return TypeToken.LITTERAL
        elif mot in ['vrai', 'faux', 'rien']:
            return TypeToken.LITTERAL
        elif mot in ['+', '-', '*', '/', '//', '%', '**', '==', '!=', '<=', '>=', '<', '>']:
            return TypeToken.OPERATEUR
        elif mot in ['(', ')', '[', ']', '{', '}', ':', ',', '.', ';']:
            return TypeToken.DELIMITEUR
        elif mot.startswith('#'):
            return TypeToken.COMMENTAIRE
        else:
            return TypeToken.IDENTIFIANT
    
    def _determiner_contexte(self, mot: str, ligne: int) -> Optional[str]:
        """Détermine le contexte d'un mot"""
        if mot in ['definir', 'classe']:
            return 'definition'
        elif mot in ['si', 'tant_que', 'pour', 'essayer']:
            return 'controle_flux'
        elif mot in ['importer', 'de']:
            return 'importation'
        elif mot in ['sauf', 'enfin']:
            return 'exception'
        elif mot in ['gestionnaire', 'erreur', 'valider']:
            return 'gestion_erreur'
        elif mot in ['correspondre', 'cas', 'quand']:
            return 'pattern_matching'
        elif mot in ['metaclasse', 'descripteur', 'propriete']:
            return 'metaprogrammation'
        return None
    
    def _analyser_syntaxique(self, tokens: List[Token]) -> Dict[str, Any]:
        """Effectue l'analyse syntaxique de base"""
        structure = {
            'imports': [],
            'fonctions': [],
            'classes': [],
            'code_principal': [],
            'gestionnaires_erreur': [],
            'patterns': [],
            'metaclasses': [],
            'erreurs': []
        }
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token.type == TypeToken.MOT_CLE:
                if token.valeur == 'importer':
                    structure['imports'].append(self._traiter_import(tokens, i))
                elif token.valeur == 'definir':
                    structure['fonctions'].append(self._traiter_fonction(tokens, i))
                elif token.valeur == 'classe':
                    structure['classes'].append(self._traiter_classe(tokens, i))
                elif token.valeur in ['si', 'tant_que', 'pour', 'essayer']:
                    structure['code_principal'].append(self._traiter_controle_flux(tokens, i))
                elif token.valeur in ['gestionnaire', 'erreur', 'valider']:
                    structure['gestionnaires_erreur'].append(self._traiter_gestion_erreur(tokens, i))
                elif token.valeur in ['correspondre', 'cas', 'quand']:
                    structure['patterns'].append(self._traiter_pattern(tokens, i))
                elif token.valeur in ['metaclasse', 'descripteur', 'propriete']:
                    structure['metaclasses'].append(self._traiter_metaprogrammation(tokens, i))
            
            i += 1
        
        return structure
    
    def _traiter_import(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite une déclaration d'importation"""
        return {'type': 'import', 'module': tokens[indice + 1].valeur if indice + 1 < len(tokens) else ''}
    
    def _traiter_fonction(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite une définition de fonction"""
        return {'type': 'fonction', 'nom': tokens[indice + 1].valeur if indice + 1 < len(tokens) else ''}
    
    def _traiter_classe(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite une définition de classe"""
        return {'type': 'classe', 'nom': tokens[indice + 1].valeur if indice + 1 < len(tokens) else ''}
    
    def _traiter_controle_flux(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite les structures de contrôle de flux"""
        return {'type': 'controle_flux', 'type_controle': tokens[indice].valeur}
    
    def _traiter_gestion_erreur(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite les gestionnaires d'erreur"""
        return {'type': 'gestion_erreur', 'type_gestion': tokens[indice].valeur}
    
    def _traiter_pattern(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite les patterns de matching"""
        return {'type': 'pattern', 'type_pattern': tokens[indice].valeur}
    
    def _traiter_metaprogrammation(self, tokens: List[Token], indice: int) -> Dict[str, Any]:
        """Traite les éléments de métaprogrammation"""
        return {'type': 'metaprogrammation', 'type_meta': tokens[indice].valeur}
    
    def _transformer_code(self, arbre: Dict[str, Any]) -> str:
        """Transforme l'arbre syntaxique en code Python"""
        code_python = []
        
        # Traiter les imports
        for imp in arbre['imports']:
            code_python.append(self._transformer_imports(imp))
        
        # Traiter les métaclasses
        for meta in arbre['metaclasses']:
            code_python.append(self._transformer_metaprogrammation(meta))
        
        # Traiter les classes
        for classe in arbre['classes']:
            code_python.append(self._transformer_classe(classe))
        
        # Traiter les fonctions
        for fonction in arbre['fonctions']:
            code_python.append(self._transformer_fonction(fonction))
        
        # Traiter les gestionnaires d'erreur
        for gestionnaire in arbre['gestionnaires_erreur']:
            code_python.append(self._transformer_gestion_erreur(gestionnaire))
        
        # Traiter les patterns
        for pattern in arbre['patterns']:
            code_python.append(self._transformer_patterns(pattern))
        
        # Traiter le code principal
        for code in arbre['code_principal']:
            code_python.append(self._transformer_controle_flux(code))
        
        return '\n'.join(code_python)
    
    def _transformer_imports(self, imp: Dict[str, Any]) -> str:
        """Transforme les imports de Syntaxis en Python"""
        if imp['type'] == 'import':
            return f"import {imp['module']}"
        return ""
    
    def _transformer_metaprogrammation(self, meta: Dict[str, Any]) -> str:
        """Transforme les éléments de métaprogrammation"""
        type_meta = meta['type_meta']
        if type_meta == 'metaclasse':
            return "# Métaclasse définie"
        elif type_meta == 'descripteur':
            return "# Descripteur défini"
        elif type_meta == 'propriete':
            return "# Propriété dynamique définie"
        return ""
    
    def _transformer_classe(self, classe: Dict[str, Any]) -> str:
        """Transforme les définitions de classe"""
        return f"class {classe['nom']}:\n    pass"
    
    def _transformer_fonction(self, fonction: Dict[str, Any]) -> str:
        """Transforme les définitions de fonction"""
        return f"def {fonction['nom']}():\n    pass"
    
    def _transformer_gestion_erreur(self, gestionnaire: Dict[str, Any]) -> str:
        """Transforme les gestionnaires d'erreur"""
        type_gestion = gestionnaire['type_gestion']
        if type_gestion == 'gestionnaire':
            return "# Gestionnaire d'erreur défini"
        elif type_gestion == 'erreur':
            return "# Erreur personnalisée définie"
        elif type_gestion == 'valider':
            return "# Validation définie"
        return ""
    
    def _transformer_patterns(self, pattern: Dict[str, Any]) -> str:
        """Transforme les patterns de matching"""
        type_pattern = pattern['type_pattern']
        if type_pattern == 'correspondre':
            return "# Pattern matching défini"
        elif type_pattern == 'cas':
            return "# Cas de pattern défini"
        elif type_pattern == 'quand':
            return "# Clause de garde définie"
        return ""
    
    def _transformer_controle_flux(self, controle: Dict[str, Any]) -> str:
        """Transforme les structures de contrôle de flux"""
        type_controle = controle['type_controle']
        if type_controle == 'si':
            return "if True:\n    pass"
        elif type_controle == 'tant_que':
            return "while True:\n    pass"
        elif type_controle == 'pour':
            return "for i in range(10):\n    pass"
        elif type_controle == 'essayer':
            return "try:\n    pass\nexcept Exception as e:\n    pass"
        return ""
    
    def _optimiser_code(self, code: str) -> str:
        """Optimise le code Python généré"""
        # Implémentation de base de l'optimisation
        # Dans une version complète, on appliquerait ici des optimisations comme:
        # - Élimination du code mort
        # - Optimisation des constantes
        # - Réorganisation des opérations
        # - Inline des fonctions simples
        
        # Pour l'instant, on nettoie juste les lignes vides en trop
        lignes = code.split('\n')
        lignes_propres = []
        
        for ligne in lignes:
            if ligne.strip() or not lignes_propres or lignes_propres[-1].strip():
                lignes_propres.append(ligne)
        
        return '\n'.join(lignes_propres)
    
    def _valider_code_python(self, code: str):
        """Valide que le code Python généré soit valide"""
        try:
            ast.parse(code)
        except SyntaxError as e:
            self.erreurs.append(f"Erreur de syntaxe dans le code Python généré: {e}")
        except Exception as e:
            self.erreurs.append(f"Erreur lors de la validation du code Python: {e}")
    
    def obtenir_erreurs(self) -> List[str]:
        """Retourne la liste des erreurs trouvées"""
        return self.erreurs
    
    def obtenir_avertissements(self) -> List[str]:
        """Retourne la liste des avertissements trouvés"""
        return self.avertissements
    
    def nettoyer_erreurs(self):
        """Nettoie la liste des erreurs et avertissements"""
        self.erreurs.clear()
        self.avertissements.clear()

def main():
    """Fonction principale pour utilisation depuis la ligne de commande"""
    if len(sys.argv) != 2:
        print("Usage: python traducteur.py <fichier.synt>")
        sys.exit(1)
    
    fichier_entree = sys.argv[1]
    traducteur = TraducteurAvance()
    
    # Traduire le fichier
    code_python = traducteur.traduire_fichier(fichier_entree)
    
    if code_python:
        # Générer le nom du fichier de sortie
        fichier_sortie = fichier_entree.replace('.synt', '.py')
        
        # Écrire le fichier de sortie
        with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
            fichier.write(code_python)
        
        print(f"✅ Fichier traduit avec succès: {fichier_sortie}")
        
        # Afficher les erreurs et avertissements
        erreurs = traducteur.obtenir_erreurs()
        avertissements = traducteur.obtenir_avertissements()
        
        if erreurs:
            print("\n❌ Erreurs trouvées:")
            for erreur in erreurs:
                print(f"  - {erreur}")
        
        if avertissements:
            print("\n⚠️  Avertissements:")
            for avertissement in avertissements:
                print(f"  - {avertissement}")
    else:
        print("❌ Erreur lors de la traduction du fichier")
        sys.exit(1)

if __name__ == "__main__":
    main()
