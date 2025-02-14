#Lexical.py
import re
from difflib import get_close_matches

class LexicalError(Exception):
    """Excepción personalizada para errores léxicos"""
    def __init__(self, message, line_number=None, suggestion=None):
        self.message = message
        self.line_number = line_number
        self.suggestion = suggestion
        super().__init__(self.message)

class LexicalAnalyzer:
    # Lista de palabras clave válidas
    VALID_KEYWORDS = {
        'START', 'END', 'PATTERN', 'SIZE', 'COLOR', 'REPEAT',
        'POINTS', 'PETALS', 'LEVELS', 'COUNT'
    }

    # Lista de tipos de patrones válidos
    VALID_PATTERNS = {
        'CIRCLE', 'DIAMOND', 'TRIANGLE', 'SQUARE', 'STAR',
        'LOTUS', 'MAZE', 'PETALS_RADIATE', 'DOTS', 'YINYANG'
    }

    @staticmethod
    def _find_similar_word(word, valid_words):
        """Encuentra palabras similares en caso de error tipográfico"""
        matches = get_close_matches(word.upper(), valid_words, n=1, cutoff=0.6)
        return matches[0] if matches else None

    @staticmethod
    def _get_line_number(code, position):
        """Obtiene el número de línea basado en la posición en el código"""
        return code[:position].count('\n') + 1

    @staticmethod
    def lex(code):
        tokens = []
        current_line = 1
        position = 0

        # Dividir el código en líneas para un mejor seguimiento
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            words = line.strip().split()
            
            i = 0
            while i < len(words):
                word = words[i]
                
                try:
                    # Verificar START y END
                    if word.upper() in {'START', 'END'}:
                        if word.upper() != word:
                            suggestion = word.upper()
                            raise LexicalError(
                                f"'{word}' debe estar en mayúsculas", 
                                line_num,
                                f"¿Quisiste decir '{suggestion}'?"
                            )
                        tokens.append(Token(word, word))
                        i += 1
                        continue

                    # Verificar PATTERN y su tipo
                    if word.upper() == 'PATTERN':
                        if word != 'PATTERN':
                            suggestion = 'PATTERN'
                            raise LexicalError(
                                f"'{word}' debe estar en mayúsculas",
                                line_num,
                                f"¿Quisiste decir '{suggestion}'?"
                            )
                        
                        # Verificar si hay un tipo de patrón después
                        if i + 1 >= len(words):
                            raise LexicalError(
                                "Falta el tipo de patrón después de PATTERN",
                                line_num
                            )
                        
                        pattern_type = words[i + 1].upper()
                        if pattern_type not in LexicalAnalyzer.VALID_PATTERNS:
                            suggestion = LexicalAnalyzer._find_similar_word(
                                pattern_type,
                                LexicalAnalyzer.VALID_PATTERNS
                            )
                            error_msg = f"Tipo de patrón no válido: '{words[i + 1]}'"
                            if suggestion:
                                error_msg += f"\n¿Quisiste decir '{suggestion}'?"
                            raise LexicalError(error_msg, line_num)
                        
                        tokens.append(Token('PATTERN', f'PATTERN {pattern_type}'))
                        i += 2
                        continue

                    # Verificar atributos (SIZE, COLOR, etc.)
                    if word.upper() in {'SIZE', 'COLOR', 'REPEAT', 'POINTS', 'PETALS', 'LEVELS', 'COUNT'}:
                        if word.upper() != word:
                            suggestion = word.upper()
                            raise LexicalError(
                                f"'{word}' debe estar en mayúsculas",
                                line_num,
                                f"¿Quisiste decir '{suggestion}'?"
                            )
                        
                        # Verificar si hay un valor después del atributo
                        if i + 1 >= len(words):
                            raise LexicalError(
                                f"Falta el valor después de {word}",
                                line_num
                            )
                        
                        value = words[i + 1]
                        
                        # Validaciones específicas por tipo de atributo
                        if word == 'SIZE':
                            try:
                                size = int(value)
                                if size <= 0:
                                    raise LexicalError(
                                        f"El valor de SIZE debe ser positivo, encontrado: {value}",
                                        line_num
                                    )
                            except ValueError:
                                raise LexicalError(
                                    f"El valor de SIZE debe ser un número, encontrado: {value}",
                                    line_num
                                )
                        
                        elif word == 'COLOR':
                            if not re.match(r'^#[0-9A-Fa-f]{6}$', value):
                                raise LexicalError(
                                    f"Color no válido: {value}. Debe ser en formato hexadecimal (ejemplo: #FF0000)",
                                    line_num
                                )
                        
                        tokens.append(Token(word, f'{word} {value}'))
                        i += 2
                        continue

                    # Si la palabra no coincide con ningún token válido
                    suggestion = LexicalAnalyzer._find_similar_word(
                        word,
                        LexicalAnalyzer.VALID_KEYWORDS
                    )
                    error_msg = f"Token no reconocido: '{word}'"
                    if suggestion:
                        error_msg += f"\n¿Quisiste decir '{suggestion}'?"
                    raise LexicalError(error_msg, line_num)

                except LexicalError as e:
                    # Re-lanzar el error con el número de línea si no lo tiene
                    if not e.line_number:
                        e.line_number = line_num
                    raise e

                i += 1

        return tokens

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"