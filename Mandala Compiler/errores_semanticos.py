from compiler import Compiler
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer, SemanticError

def test_mandala_code(code, test_name=""):
    print(f"\n{'='*20} Test: {test_name} {'='*20}")
    print("Código a analizar:")
    print(code)
    print('-' * 50)

    try:
        # Análisis Léxico
        print("\n1. Realizando análisis léxico...")
        tokens = LexicalAnalyzer.lex(code)
        print("Análisis léxico completado exitosamente")

        # Análisis Sintáctico
        print("\n2. Realizando análisis sintáctico...")
        sintactic_analyzer = SintacticAnalyzer(tokens)
        sintactic_analyzer.parse()
        print("Análisis sintáctico completado exitosamente")

        # Análisis Semántico
        print("\n3. Realizando análisis semántico...")
        semantic_analyzer = SemanticAnalyzer(tokens)
        shapes = semantic_analyzer.analyze()
        print("Análisis semántico completado exitosamente")

        print("\n4. Compilando mandala...")
        compiler = Compiler()
        compiler.compile(code)

    except SemanticError as e:
        print(f"\n❌ Error Semántico: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    # Test 1: Patrón no reconocido
    codigo_patron_invalido = """
    START
    PATTERN HEXAGON SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_patron_invalido, "Error: Patrón no reconocido")

    # Test 2: Falta atributo requerido para STAR
    codigo_sin_points = """
    START
    PATTERN STAR SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_sin_points, "Error: Falta POINTS en STAR")

    # Test 3: Falta atributo requerido para LOTUS
    codigo_sin_petals = """
    START
    PATTERN LOTUS SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_sin_petals, "Error: Falta PETALS en LOTUS")

    # Test 4: Falta atributo requerido para MAZE
    codigo_sin_levels = """
    START
    PATTERN MAZE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_sin_levels, "Error: Falta LEVELS en MAZE")

    # Test 5: Valor inválido para POINTS
    codigo_points_invalido = """
    START
    PATTERN STAR SIZE 50 COLOR #FF0000 REPEAT 3 POINTS 2
    END
    """
    test_mandala_code(codigo_points_invalido, "Error: POINTS debe ser >= 3")

    # Test 6: Valor inválido para PETALS
    codigo_petals_invalido = """
    START
    PATTERN LOTUS SIZE 50 COLOR #FF0000 REPEAT 3 PETALS 0
    END
    """
    test_mandala_code(codigo_petals_invalido, "Error: PETALS debe ser > 0")

    # Test 7: Atributo no permitido para el patrón
    codigo_atributo_no_permitido = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3 POINTS 5
    END
    """
    test_mandala_code(codigo_atributo_no_permitido, "Error: POINTS no permitido en CIRCLE")