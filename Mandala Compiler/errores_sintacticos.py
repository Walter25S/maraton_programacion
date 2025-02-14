from compiler import Compiler
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer, SyntaxError
from semantic import SemanticAnalyzer

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

        # Continuar con el proceso...
        print("\n3. Realizando análisis semántico...")
        semantic_analyzer = SemanticAnalyzer(tokens)
        shapes = semantic_analyzer.analyze()
        
        print("\n4. Compilando mandala...")
        compiler = Compiler()
        compiler.compile(code)

    except SyntaxError as e:
        print(f"\n❌ Error Sintáctico en línea {e.line_number}: {e.message}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    # Test 1: Falta START
    codigo_sin_start = """
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_sin_start, "Error: Falta START")

    # Test 2: Falta END
    codigo_sin_end = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    """
    test_mandala_code(codigo_sin_end, "Error: Falta END")

    # Test 3: Tokens después de END
    codigo_post_end = """
    START
    PATTERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    PATTERN CIRCLE SIZE 30 COLOR #00FF00 REPEAT 2
    """
    test_mandala_code(codigo_post_end, "Error: Tokens después de END")

    # Test 4: Sin patrones entre START y END
    codigo_sin_patrones = """
    START
    END
    """
    test_mandala_code(codigo_sin_patrones, "Error: Sin patrones")

    # Test 5: Atributos en orden incorrecto
    codigo_orden_incorrecto = """
    START
    PATTERN CIRCLE COLOR #FF0000 SIZE 50 REPEAT 3
    END
    """
    test_mandala_code(codigo_orden_incorrecto, "Error: Orden incorrecto de atributos")

    # Test 6: Atributos duplicados
    codigo_atributos_duplicados = """
    START
    PATTERN CIRCLE SIZE 50 SIZE 30 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_atributos_duplicados, "Error: Atributos duplicados")