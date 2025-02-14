from compiler import Compiler
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer, SemanticError


if __name__ == '__main__':
    example_code = """
    START
   
    
     PATTERN YINYANG SIZE 100 COLOR #FF0000 REPEAT 5
   
    END
    """
    example_code2 = """
    START
    PATTERN YINYANG SIZE 5 COLOR #FF0000 REPEAT 5
    PATTERN MAZE LEVELS 3 SIZE 50 COLOR #000000 REPEAT 3
    PATTERN LOTUS PETALS 12 SIZE 200 COLOR #FF69B4 REPEAT 5
    PATTERN CIRCLE SIZE 30 COLOR #00FF00 REPEAT 10
    PATTERN DIAMOND COLOR #FF0000 SIZE 50 REPEAT 2
    PATTERN STAR POINTS 7 SIZE 100 COLOR #00FF00 REPEAT 10
    PATTERN TRIANGLE COLOR #0000FF SIZE 40 REPEAT 4
    END
    """
    tokens = LexicalAnalyzer.lex(example_code2)
    sintactic_analyzer = SintacticAnalyzer(tokens)
    sintactic_analyzer.parse()

    # Semantic Analysis
    semantic_analyzer = SemanticAnalyzer(tokens)
    try:
        shapes = semantic_analyzer.analyze()
        print("Formas válidas:", shapes)
    except SemanticError as e:
        print(f"Error semántico: {e}")

    compiler = Compiler()
    compiler.compile(example_code)

    
   