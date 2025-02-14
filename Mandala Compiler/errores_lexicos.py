#errores_lexicos.py

from compiler import Compiler
from lexical import LexicalAnalyzer, LexicalError
from sintactic import SintacticAnalyzer
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
        print("Tokens generados:")
        for token in tokens:
            print(f"  {token}")

        # Continuar con el resto del proceso...
        print("\n2. Realizando análisis sintáctico...")
        sintactic_analyzer = SintacticAnalyzer(tokens)
        sintactic_analyzer.parse()
        
        print("\n3. Realizando análisis semántico...")
        semantic_analyzer = SemanticAnalyzer(tokens)
        shapes = semantic_analyzer.analyze()
        
        print("\n4. Compilando mandala...")
        compiler = Compiler()
        compiler.compile(code)

    except LexicalError as e:
        print(f"\n❌ Error Léxico en línea {e.line_number}: {e.message}")
        if e.suggestion:
            print(f"Sugerencia: {e.suggestion}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    # Test 1: Error en PATTERN
    codigo_pattern_error = """
    START
    pattern CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_pattern_error, "Error en PATTERN (minúsculas)")

    # Test 2: Error en tipo de patrón
    codigo_tipo_error = """
    START
    PATTERN CIRCL SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_tipo_error, "Error en tipo de patrón")

    # Test 3: Error en atributo
    codigo_atributo_error = """
    START
    PATTERN CIRCLE size 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_atributo_error, "Error en atributo SIZE")

    # Test 4: Error en color hexadecimal
    codigo_color_error = """
    START
    PATTERN CIRCLE SIZE 50 COLOR FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_color_error, "Error en formato de color")

    # Test 5: Valor numérico inválido
    codigo_numero_error = """
    START
    PATTERN CIRCLE SIZE -50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_numero_error, "Error en valor numérico")

    # Test 6: Palabra mal escrita
    codigo_typo = """
    START
    PATERN CIRCLE SIZE 50 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_typo, "Error de escritura en PATTERN")