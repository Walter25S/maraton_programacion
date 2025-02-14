from compiler import Compiler
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer, SyntaxError
from semantic import SemanticAnalyzer, SemanticError

def test_mandala_code(code, test_name=""):
    """
    Función para probar código de mandala con manejo de errores
    """
    print(f"\n{'='*20} Test: {test_name} {'='*20}")
    print("Código a analizar:")
    print(code)
    print('-' * 50)

    try:
        # Análisis Léxico
        print("\n1. Realizando análisis léxico...")
        tokens = LexicalAnalyzer.lex(code)
        print("Tokens generados:")
        for token in tokens:
            print(f"  {token}")

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
        print("Formas validadas:")
        for shape in shapes:
            print(f"  {shape}")

        # Compilación y visualización
        print("\n4. Compilando y visualizando el mandala...")
        compiler = Compiler()
        compiler.compile(code)
        
    except SyntaxError as e:
        print(f"\n❌ Error Sintáctico: {e.message}")
        if hasattr(e, 'token'):
            print(f"Token problemático: {e.token}")
        if hasattr(e, 'line_number'):
            print(f"En la línea: {e.line_number}")
    except SemanticError as e:
        print(f"\n❌ Error Semántico: {e}")
    except Exception as e:
        print(f"\n❌ Error Inesperado: {str(e)}")

if __name__ == '__main__':
    # Test 1: Código válido básico
    codigo_valido = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_valido, "Código Válido Básico")

    # Test 2: Error sintáctico - Falta START
    codigo_sin_start = """
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_sin_start, "Código Sin START")

    # Test 3: Error sintáctico - Falta END
    codigo_sin_end = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    """
    test_mandala_code(codigo_sin_end, "Código Sin END")

    # Test 4: Error sintáctico - Atributos en orden incorrecto
    codigo_orden_incorrecto = """
    START
    PATTERN CIRCLE REPEAT 3 SIZE 50 COLOR #FF0000
    END
    """
    test_mandala_code(codigo_orden_incorrecto, "Atributos en Orden Incorrecto")

    # Test 5: Error sintáctico - Atributos duplicados
    codigo_atributos_duplicados = """
    START
    PATTERN CIRCLE SIZE 50 SIZE 30 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_atributos_duplicados, "Atributos Duplicados")

    # Test 6: Código complejo válido
    codigo_complejo = """
    START
    PATTERN STAR POINTS 5 SIZE 100 COLOR #FF0000 REPEAT 3
    PATTERN LOTUS PETALS 8 SIZE 80 COLOR #00FF00 REPEAT 2
    PATTERN MAZE LEVELS 3 SIZE 60 COLOR #FF00FF REPEAT 4
    PATTERN DIAMOND COLOR #FF0000 SIZE 200 REPEAT 2
    END
    """
    test_mandala_code(codigo_complejo, "Código Complejo Válido")

    # Test 7: Error sintáctico - Patrón sin atributos requeridos
    codigo_sin_atributos = """
    START
    PATTERN STAR POINTS 5
    END
    """
    test_mandala_code(codigo_sin_atributos, "Patrón Sin Atributos Requeridos")

    # Test 8: Error sintáctico - Tokens después de END
    codigo_post_end = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    PATTERN CIRCLE SIZE 30 COLOR #00FF00 REPEAT 2
    """
    test_mandala_code(codigo_post_end, "Tokens Después de END")

    # Test 9: Código con múltiples patrones y atributos específicos
    codigo_multiple = """
    START
    PATTERN YINYANG SIZE 100 COLOR #FF0000 REPEAT 2
    PATTERN DOTS COUNT 12 SIZE 80 COLOR #00FF00 REPEAT 3
    PATTERN PETALSRADIATE SIZE 60 COLOR #0000FF REPEAT 4
    END
    """
    test_mandala_code(codigo_multiple, "Múltiples Patrones")