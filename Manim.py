from manim import *

class QuadraticBezier(Scene):
    def construct(self):
        # Definisci i punti di controllo
        p0 = np.array([-3, 0, 0])  # Punto di partenza
        p1 = np.array([-1, 2, 0])    # Punto di controllo
        p2 = np.array([1, 2, 0])    # Punto di arrivo
        p3 = np.array([3, 0, 0])    # Punto di arrivo
        
        # Crea i punti come cerchi
        point_0 = Dot(p0, color=BLUE)
        point_1 = Dot(p1, color=GREEN)
        point_2 = Dot(p2, color=RED)
        point_3 = Dot(p3, color=YELLOW)

        # Crea le etichette per i punti
        label_0 = Tex(r"$P_0$", font_size=24).next_to(point_0, DOWN)
        label_1 = Tex(r"$P_1$", font_size=24).next_to(point_1, UP)
        label_2 = Tex(r"$P_2$", font_size=24).next_to(point_2, UP)
        label_3 = Tex(r"$P_3$", font_size=24).next_to(point_3, DOWN)

        self.play(Write(Tex(r"Curva di Bézier Cubica", font_size=50).to_edge(UP)))

        # Aggiungi i punti e le etichette alla scena
        self.play(DrawBorderThenFill(point_0), Write(label_0))
        self.play(DrawBorderThenFill(point_1), Write(label_1))
        self.play(DrawBorderThenFill(point_2), Write(label_2))
        self.play(DrawBorderThenFill(point_3), Write(label_3))

        # Crea la curva di Bézier quadratica
        bezier_curve = CubicBezier(p0, p1, p2, p3, color=RED)

        # Mostra i punti di controllo
        self.play(Create(Line(point_0.get_center(), point_1.get_center(), color=WHITE, stroke_width=2)))
        self.play(Create(Line(point_1.get_center(), point_2.get_center(), color=WHITE, stroke_width=2)))
        self.play(Create(Line(point_2.get_center(), point_3.get_center(), color=WHITE, stroke_width=2)))

        # Aggiungi la curva alla scena
        self.play(Create(bezier_curve))

# Per eseguire il file, usa il seguente comando nel terminale
# manim -pql your_file_name.py QuadraticBezier
