from compiler import Compiler
from lexical import LexicalAnalyzer
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
        print("¡Mandala compilado exitosamente!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    # Test 1: Círculo simple
    codigo_circulo = """
    START
    PATTERN CIRCLE SIZE 100 COLOR #FF0000 REPEAT 3
    END
    """
    test_mandala_code(codigo_circulo, "Patrón: CIRCLE")

    # Test 2: Diamante
    codigo_diamante = """
    START
    PATTERN DIAMOND SIZE 80 COLOR #00FF00 REPEAT 4
    END
    """
    test_mandala_code(codigo_diamante, "Patrón: DIAMOND")

    # Test 3: Triángulo
    codigo_triangulo = """
    START
    PATTERN TRIANGLE SIZE 90 COLOR #0000FF REPEAT 3
    END
    """
    test_mandala_code(codigo_triangulo, "Patrón: TRIANGLE")

    # Test 4: Cuadrado
    codigo_cuadrado = """
    START
    PATTERN SQUARE SIZE 70 COLOR #800080 REPEAT 4
    END
    """
    test_mandala_code(codigo_cuadrado, "Patrón: SQUARE")

    # Test 5: Estrella
    codigo_estrella = """
    START
    PATTERN STAR SIZE 85 COLOR #FFA500 REPEAT 3 POINTS 5
    END
    """
    test_mandala_code(codigo_estrella, "Patrón: STAR")

    # Test 6: Flor de Loto
    codigo_lotus = """
    START
    PATTERN LOTUS SIZE 95 COLOR #FF1493 REPEAT 2 PETALS 8
    END
    """
    test_mandala_code(codigo_lotus, "Patrón: LOTUS")

    # Test 7: Laberinto
    codigo_maze = """
    START
    PATTERN MAZE SIZE 75 COLOR #4B0082 REPEAT 2 LEVELS 4
    END
    """
    test_mandala_code(codigo_maze, "Patrón: MAZE")

    # Test 8: Pétalos Radiantes
    codigo_petals_radiate = """
    START
    PATTERN PETALS_RADIATE SIZE 90 COLOR #008B8B REPEAT 2 PETALS 12
    END
    """
    test_mandala_code(codigo_petals_radiate, "Patrón: PETALS_RADIATE")

    # Test 9: Puntos
    codigo_dots = """
    START
    PATTERN DOTS SIZE 85 COLOR #DC143C REPEAT 3 COUNT 16
    END
    """
    test_mandala_code(codigo_dots, "Patrón: DOTS")

    # Test 10: Yin Yang
    codigo_yinyang = """
    START
    PATTERN YINYANG SIZE 100 COLOR #000000 REPEAT 2
    END
    """
    test_mandala_code(codigo_yinyang, "Patrón: YINYANG")

    # Test 11: Mandala complejo con múltiples patrones
    codigo_complejo = """
    START
    PATTERN CIRCLE SIZE 150 COLOR #4B0082 REPEAT 3
    PATTERN STAR SIZE 120 COLOR #FF1493 REPEAT 2 POINTS 7
    PATTERN LOTUS SIZE 90 COLOR #00FF00 REPEAT 2 PETALS 6
    PATTERN DOTS SIZE 60 COLOR #0000FF REPEAT 3 COUNT 12
    END
    """
    test_mandala_code(codigo_complejo, "Mandala Complejo: Múltiples Patrones")