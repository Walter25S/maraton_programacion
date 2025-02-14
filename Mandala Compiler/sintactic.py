#sintactic.py

class SyntaxError(Exception):
    """Clase base para errores sintácticos"""
    def __init__(self, message, token=None, line_number=None):
        self.message = message
        self.token = token
        self.line_number = line_number
        super().__init__(self.message)

class SintacticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = -1
        self.line_number = 1
        self.advance()

    def advance(self):
        """Avanza al siguiente token y mantiene un registro de la línea actual"""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            # Incrementar número de línea si encontramos un salto de línea
            if self.current_token and '\n' in str(self.current_token.value):
                self.line_number += 1
        else:
            self.current_token = None

    def error(self, message):
        """Genera un error sintáctico con información detallada"""
        raise SyntaxError(
            f"Error en línea {self.line_number}: {message}",
            token=self.current_token,
            line_number=self.line_number
        )

    def expect(self, token_type):
        """Verifica si el token actual es del tipo esperado"""
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            self.error(f"Se esperaba {token_type}, se encontró {self.current_token and self.current_token.type}")

    def parse(self):
        """Analiza la estructura completa del programa"""
        try:
            # Verificar START
            if not self.tokens:
                self.error("El programa está vacío")
            
            self.parse_start()
            
            # Verificar que haya al menos un patrón
            if not self.current_token or (
                self.current_token.type != 'PATTERN' and 
                self.current_token.type != 'END'
            ):
                self.error("Se esperaba al menos un patrón o END")

            # Analizar patrones
            while self.current_token and self.current_token.type != 'END':
                self.parse_pattern()

            # Verificar END
            self.parse_end()

            # Verificar que no haya tokens después de END
            if self.current_token:
                self.error("Se encontraron tokens después de END")

        except SyntaxError as e:
            raise e
        except Exception as e:
            self.error(f"Error inesperado: {str(e)}")

    def parse_start(self):
        """Verifica la declaración START"""
        if not self.current_token:
            self.error("El programa debe comenzar con START")
        if self.current_token.type != 'START':
            self.error("El programa debe comenzar con START")
        self.advance()

    def parse_end(self):
        """Verifica la declaración END"""
        if not self.current_token:
            self.error("Falta la declaración END al final del programa")
        if self.current_token.type != 'END':
            self.error("El programa debe terminar con END")
        self.advance()

    def parse_pattern(self):
        """Analiza la estructura de un patrón"""
        if self.current_token.type != 'PATTERN':
            self.error("Se esperaba un patrón (PATTERN)")

        # Guardar el token del patrón para mensajes de error más específicos
        pattern_token = self.current_token
        self.advance()

        # Verificar que el patrón tenga un tipo válido
        if not self.current_token:
            self.error(f"Falta el tipo de patrón después de PATTERN")

        # Lista de atributos requeridos y opcionales según el tipo de patrón
        pattern_type = pattern_token.value.split()[1]
        required_attributes = {'SIZE', 'COLOR', 'REPEAT'}
        optional_attributes = set()

        # Agregar atributos específicos según el tipo de patrón
        if pattern_type == 'STAR':
            required_attributes.add('POINTS')
        elif pattern_type == 'LOTUS':
            required_attributes.add('PETALS')
        elif pattern_type == 'MAZE':
            required_attributes.add('LEVELS')
        elif pattern_type == 'DOTS':
            required_attributes.add('COUNT')

        # Conjunto para rastrear atributos encontrados
        found_attributes = set()

        # Analizar atributos del patrón
        while self.current_token and self.current_token.type in {
            'SIZE', 'COLOR', 'REPEAT', 'POINTS', 'PETALS', 'LEVELS', 'COUNT'
        }:
            # Verificar duplicados
            if self.current_token.type in found_attributes:
                self.error(f"Atributo duplicado: {self.current_token.type}")
            
            found_attributes.add(self.current_token.type)
            self.advance()

        # Verificar atributos requeridos faltantes
        missing_attributes = required_attributes - found_attributes
        if missing_attributes:
            self.error(
                f"Faltan atributos requeridos para el patrón {pattern_type}: "
                f"{', '.join(missing_attributes)}"
            )

        # Verificar atributos no permitidos
        invalid_attributes = found_attributes - (required_attributes | optional_attributes)
        if invalid_attributes:
            self.error(
                f"Atributos no permitidos para el patrón {pattern_type}: "
                f"{', '.join(invalid_attributes)}"
            )

    def check_attribute_order(self, attributes):
        """Verifica que los atributos estén en un orden lógico"""
        expected_order = ['SIZE', 'COLOR', 'REPEAT']
        current_pos = -1
        
        for attr in attributes:
            if attr in expected_order:
                new_pos = expected_order.index(attr)
                if new_pos < current_pos:
                    self.error(f"Orden incorrecto de atributos. Se sugiere: {', '.join(expected_order)}")
                current_pos = new_pos