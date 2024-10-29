from manim import *

class CubicBezier(Scene):
    def construct(self):
        # Define control points
        p0 = np.array([-3, 0, 0])   # Start control point
        p1 = np.array([-1, 2, 0])   # Intermediate control point
        p2 = np.array([1, 2, 0])    # Intermediate control point
        p3 = np.array([3, 0, 0])    # End control point
        
        # Create control points as colored dots
        point_0 = Dot(p0, color=BLUE)
        point_1 = Dot(p1, color=GREEN)
        point_2 = Dot(p2, color=RED)
        point_3 = Dot(p3, color=YELLOW)

        # Create labels for the control points
        label_0 = Tex(r"$P_0$", font_size=24).next_to(point_0, DOWN)
        label_1 = Tex(r"$P_1$", font_size=24).next_to(point_1, UP)
        label_2 = Tex(r"$P_2$", font_size=24).next_to(point_2, UP)
        label_3 = Tex(r"$P_3$", font_size=24).next_to(point_3, DOWN)

        self.play(Write(Tex(r"Cubic Bézier Curve", font_size=50).to_edge(UP)))

        # Add control points and relative labels
        self.play(DrawBorderThenFill(point_0), Write(label_0))
        self.play(DrawBorderThenFill(point_1), Write(label_1))
        self.play(DrawBorderThenFill(point_2), Write(label_2))
        self.play(DrawBorderThenFill(point_3), Write(label_3))

        # Create cubic Bézier curve
        bezier_curve = CubicBezier(p0, p1, p2, p3, color=RED)

        # Show control points
        self.play(Create(Line(point_0.get_center(), point_1.get_center(), color=WHITE, stroke_width=2)))
        self.play(Create(Line(point_1.get_center(), point_2.get_center(), color=WHITE, stroke_width=2)))
        self.play(Create(Line(point_2.get_center(), point_3.get_center(), color=WHITE, stroke_width=2)))

        # Add curve to the scene
        self.play(Create(bezier_curve))

# To execute the file, use this command
# manim -pql your_file_name.py your_class_name
# manim -pwl CubicBezier.py CubicBezier
