#semantic.py
import re

class SemanticError(Exception):
    """Excepción personalizada para errores semánticos."""
    pass

class SemanticAnalyzer:
    def __init__(self, tokens):
        """Inicializa el analizador semántico con una lista de tokens."""
        self.tokens = tokens
        self.shapes = []  # Lista para almacenar las formas analizadas

    def analyze(self):
        """Analiza la lista de tokens y construye estructuras de formas válidas."""
        shape = {}  # Diccionario para almacenar los atributos de la forma actual
        for token in self.tokens:
            try:
                if token.type == 'PATTERN':
                    # Si ya hay una forma en progreso, la validamos y la agregamos
                    if shape:
                        self._validate_shape(shape)
                        self.shapes.append(shape)
                        shape = {}  # Reiniciamos el diccionario para la nueva forma
                    
                    # Extraemos el tipo de patrón (ejemplo: CIRCLE, STAR, etc.)
                    pattern_type = token.value.split()[1]
                    if pattern_type not in ('CIRCLE', 'DIAMOND', 'TRIANGLE', 'SQUARE', 'STAR', 'LOTUS', 'MAZE', 'PETALS_RADIATE', 'DOTS', 'YINYANG'):
                        raise SemanticError(f"Patrón no reconocido: {pattern_type}")
                    
                    shape['type'] = 'PATTERN'
                    shape['pattern_type'] = pattern_type

                elif token.type == 'CIRCLE':
                    # Si ya hay una forma en progreso, la validamos y la agregamos
                    if shape:
                        self._validate_shape(shape)
                        self.shapes.append(shape)
                        shape = {}
                    
                    shape['type'] = 'CIRCLE'  # Se establece el tipo de forma

                elif token.type == 'SIZE':
                    size = int(token.value.split()[1])
                    if size <= 0:
                        raise SemanticError("El tamaño (SIZE) debe ser un número positivo.")
                    shape['size'] = size

                elif token.type == 'COLOR':
                    color = token.value.split()[1]
                    # Validar que el color esté en formato hexadecimal
                    if not re.match(r'^#[0-9A-Fa-f]{6}$', color):
                        raise SemanticError(f"Color no válido: {color}. Debe ser en formato hexadecimal (ejemplo: #FF0000).")
                    shape['color'] = color

                elif token.type == 'REPEAT':
                    repeat = int(token.value.split()[1])
                    if repeat <= 0:
                        raise SemanticError("El número de repeticiones (REPEAT) debe ser un número positivo.")
                    shape['repeat'] = repeat

                elif token.type == 'POINTS':
                    points = int(token.value.split()[1])
                    if points < 3:
                        raise SemanticError("El número de puntas (POINTS) debe ser al menos 3 y positivo.")
                    shape['points'] = points

                elif token.type == 'PETALS':
                    petals = int(token.value.split()[1])
                    if petals <= 0:
                        raise SemanticError("El número de pétalos (PETALS) debe ser un número positivo.")
                    shape['petals'] = petals

                elif token.type == 'LEVELS':
                    levels = int(token.value.split()[1])
                    if levels <= 0:
                        raise SemanticError("El número de niveles (LEVELS) debe ser un número positivo.")
                    shape['levels'] = levels

                elif token.type == 'COUNT':
                    count = int(token.value.split()[1])
                    if count <= 0:
                        raise SemanticError("El número de puntos (COUNT) debe ser un número positivo.")
                    shape['count'] = count

            except ValueError as e:
                raise SemanticError(f"Error en el valor del token {token.type}: {e}")

        # Agregar la última forma procesada
        if shape:
            self._validate_shape(shape)
            self.shapes.append(shape)

        return self.shapes

    def _validate_shape(self, shape):
        """Valida que la forma tenga los atributos requeridos."""
        if 'type' not in shape:
            raise SemanticError("La forma no tiene un tipo definido.")

        if shape['type'] == 'PATTERN':
            if 'pattern_type' not in shape:
                raise SemanticError("El patrón no tiene un tipo definido.")
            if shape['pattern_type'] == 'STAR' and 'points' not in shape:
                raise SemanticError("El patrón STAR requiere el atributo POINTS.")
            if shape['pattern_type'] == 'LOTUS' and 'petals' not in shape:
                raise SemanticError("El patrón LOTUS requiere el atributo PETALS.")
            if shape['pattern_type'] == 'MAZE' and 'levels' not in shape:
                raise SemanticError("El patrón MAZE requiere el atributo LEVELS.")
            if shape['pattern_type'] == 'DOTS' and 'count' not in shape:
                raise SemanticError("El patrón DOTS requiere el atributo COUNT.")

        if 'size' not in shape:
            raise SemanticError("La forma no tiene un tamaño (SIZE) definido.")
        if 'color' not in shape:
            raise SemanticError("La forma no tiene un color (COLOR) definido.")
        if 'repeat' not in shape:
            raise SemanticError("La forma no tiene un número de repeticiones (REPEAT) definido.")


                #//////////////

            if token.type == 'PATTERN':
                # Si ya hay una forma en progreso, agrégala a la lista
                if shape:
                    self.shapes.append(shape)
                    shape = {}  # Reinicia el diccionario para la nueva forma
                # Extraer el tipo de patrón (CIRCLE, DIAMOND, TRIANGLE, etc.)
                pattern_type = token.value.split()[1]
                shape['type'] = 'PATTERN'
                shape['pattern_type'] = pattern_type
            elif token.type == 'SIZE':
                shape['size'] = int(token.value.split()[1])  # Extraer el tamaño
            elif token.type == 'COLOR':
                shape['color'] = token.value.split()[1]  # Extraer el color
            elif token.type == 'REPEAT':
                shape['repeat'] = int(token.value.split()[1])  # Extraer las repeticiones
            elif token.type == 'POINTS':
                shape['points'] = int(token.value.split()[1]) #Extrae el numero de puntas
            elif token.type == 'PETALS':
                shape['petals'] = int(token.value.split()[1])
            elif token.type == 'LEVELS':
                shape['levels'] = int(token.value.split()[1])
            elif token.type == 'COUNT':
                shape['count'] = int(token.value.split()[1])
        if shape:  # Asegúrate de agregar la última forma procesada
            self.shapes.append(shape)

        return self.shapes
    
