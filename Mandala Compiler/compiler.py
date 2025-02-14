#compiler.py
import tkinter as tk
import math

from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer

class Compiler:
    def compile(self, code: str):
        tokens = LexicalAnalyzer.lex(code)
        sintactic_analyzer = SintacticAnalyzer(tokens)
        sintactic_analyzer.parse()
        semantic_analyzer = SemanticAnalyzer(tokens)
        shapes = semantic_analyzer.analyze()  # Obtener las formas
        self.draw_mandala(shapes)  # Dibujar el mandala
    

   

    def draw_mandala(self, shapes):
        root = tk.Tk()
        root.title("Mandala Compiler")
        canvas = tk.Canvas(root, width=500, height=500, bg='white')
        canvas.pack()
        center_x, center_y = 250, 250

        for shape in shapes:
            if 'type' not in shape:  # Verifica si la clave 'type' existe
                continue  # Si no existe, omite esta forma

            size = shape.get('size', 50)  # Tamaño predeterminado
            color = shape.get('color', '#000000')  # Color predeterminado (negro)
            repeat = shape.get('repeat', 1)  # Repeticiones predeterminadas

            if shape['type'] == 'PATTERN' and shape['pattern_type'] == 'CIRCLE':
                for i in range(repeat):
                    offset = i * 10
                    canvas.create_oval(center_x - size - offset, center_y - size - offset,
                                    center_x + size + offset, center_y + size + offset,
                                    outline=color, width=2)

            elif shape['type'] == 'PATTERN':
                pattern_type = shape.get('pattern_type', 'DIAMOND')  # Tipo de patrón predeterminado

                if pattern_type == 'DIAMOND':
                    for i in range(repeat):
                        offset = i * 10
                        points = [
                            center_x, center_y - size - offset,
                            center_x - size - offset, center_y,
                            center_x, center_y + size + offset,
                            center_x + size + offset, center_y
                        ]
                        canvas.create_polygon(points, outline=color, fill='', width=2)

                elif pattern_type == 'TRIANGLE':
                    for i in range(repeat):
                        offset = i * 10
                        points = [
                            center_x, center_y - size - offset,
                            center_x - size - offset, center_y + size + offset,
                            center_x + size + offset, center_y + size + offset
                        ]
                        canvas.create_polygon(points, outline=color, fill='', width=2)

                elif pattern_type == 'SQUARE':
                    for i in range(repeat):
                        offset = i * 10
                        canvas.create_rectangle(center_x - size - offset, center_y - size - offset,
                                                center_x + size + offset, center_y + size + offset,
                                                outline=color, width=2)

                elif pattern_type == 'STAR':
                    points_count = shape.get('points', 5)  # Número de puntas predeterminado
                    for i in range(repeat):
                        offset = i * 10
                        points = []
                        for j in range(points_count * 2):
                            angle = (j * 360) / (points_count * 2)
                            radius = size + offset if j % 2 == 0 else (size + offset) / 2
                            x = center_x + radius * math.cos(math.radians(angle))
                            y = center_y + radius * math.sin(math.radians(angle))
                            points.extend([x, y])
                        canvas.create_polygon(points, outline=color, fill='', width=2)

                elif pattern_type == 'LOTUS':
                    petals_count = shape.get('petals', 8)  # Número de pétalos predeterminado
                    for i in range(repeat):
                        offset = i * 10
                        for j in range(petals_count):
                            angle = (j * 360) / petals_count
                            # Coordenadas del pétalo
                            x1 = center_x + (size + offset) * math.cos(math.radians(angle - 10))
                            y1 = center_y + (size + offset) * math.sin(math.radians(angle - 10))
                            x2 = center_x + (size + offset) * math.cos(math.radians(angle + 10))
                            y2 = center_y + (size + offset) * math.sin(math.radians(angle + 10))
                            # Dibujar el pétalo
                            canvas.create_oval(x1, y1, x2, y2, outline=color, width=2)


                elif pattern_type == 'MAZE':
                    levels = shape.get('levels', 3)  # Número de niveles predeterminado
                    for i in range(repeat):
                        offset = i * 10
                        for j in range(levels):
                            radius = size + (j * 20)  # Aumentar el tamaño para cada nivel
                            # Dibujar el círculo del laberinto
                            canvas.create_oval(center_x - radius - offset, center_y - radius - offset,
                                            center_x + radius + offset, center_y + radius + offset,
                                            outline=color, width=2)
                            # Dibujar líneas verticales y horizontales para simular el laberinto
                            if j > 0:  # No dibujar líneas en el primer nivel
                                # Línea vertical
                                canvas.create_line(center_x - radius - offset, center_y,
                                                center_x + radius + offset, center_y,
                                                fill=color, width=2)
                                # Línea horizontal
                                canvas.create_line(center_x, center_y - radius - offset,
                                                center_x, center_y + radius + offset,
                                                fill=color, width=2)
                                
                elif pattern_type == 'PETALSRADIATE':
                    petals_count = shape.get('petals', 8)  # Número de pétalos predeterminado
                    for i in range(repeat):
                        offset = i * 10
                        for j in range(petals_count):
                            angle = (j * 360) / petals_count
                            # Coordenadas del pétalo
                            x1 = center_x
                            y1 = center_y
                            x2 = center_x + (size + offset) * math.cos(math.radians(angle))
                            y2 = center_y + (size + offset) * math.sin(math.radians(angle))
                            # Dibujar el pétalo como una línea que irradia desde el centro
                            canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
                
                elif pattern_type == 'DOTS':
                    dots_count = shape.get('count', 12)  # Número de puntos predeterminado
                    for i in range(repeat):
                        offset = i * 10
                        for j in range(dots_count):
                            angle = (j * 360) / dots_count
                            # Coordenadas del punto
                            x = center_x + (size + offset) * math.cos(math.radians(angle))
                            y = center_y + (size + offset) * math.sin(math.radians(angle))
                            # Dibujar el punto
                            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline=color)

                elif pattern_type == 'YINYANG':
                    for i in range(repeat):
                        offset = i * 10
                        # Dibujar el círculo exterior
                        canvas.create_oval(center_x - size - offset, center_y - size - offset,
                                        center_x + size + offset, center_y + size + offset,
                                        outline=color, width=2)
                        # Dibujar la mitad superior (yin)
                        canvas.create_arc(center_x - size - offset, center_y - size - offset,
                                        center_x + size + offset, center_y + size + offset,
                                        start=0, extent=180, outline=color, fill='black', width=2)
                        # Dibujar la mitad inferior (yang)
                        canvas.create_arc(center_x - size - offset, center_y - size - offset,
                                        center_x + size + offset, center_y + size + offset,
                                        start=180, extent=180, outline=color, fill='white', width=2)
                        # Dibujar los círculos pequeños
                        small_size = (size + offset) // 4
                        # Círculo pequeño en la parte superior (yin)
                        canvas.create_oval(center_x - small_size, center_y - (size + offset) // 2 - small_size,
                                        center_x + small_size, center_y - (size + offset) // 2 + small_size,
                                        outline=color, fill='white', width=2)
                        # Círculo pequeño en la parte inferior (yang)
                        canvas.create_oval(center_x - small_size, center_y + (size + offset) // 2 - small_size,
                                        center_x + small_size, center_y + (size + offset) // 2 + small_size,
                                        outline=color, fill='black', width=2)


        root.mainloop()
        
        