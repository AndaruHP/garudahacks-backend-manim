from manim import *

class DivisionExample(Scene):
    def construct(self):
        # Number 100
        num100 = MathTex("100", color=BLUE).scale(2)
        self.play(Write(num100))
        self.wait(0.5)

        # Division symbol
        division_symbol = MathTex("\div", color=WHITE).scale(2)
        self.play(Transform(num100, num100.move_to(LEFT * 3)))
        self.play(Write(division_symbol.next_to(num100, RIGHT)))
        self.wait(0.5)

        # Number 5
        num5 = MathTex("5", color=GREEN).scale(2)
        self.play(Write(num5.next_to(division_symbol, RIGHT)))
        self.wait(0.5)

        # Equals symbol
        equals_symbol = MathTex("=", color=WHITE).scale(2)
        self.play(Write(equals_symbol.next_to(num5, RIGHT)))
        self.wait(0.5)

        # Result 20
        result = MathTex("20", color=YELLOW).scale(2)
        self.play(Write(result.next_to(equals_symbol, RIGHT)))
        self.wait(1)

        # Explanation (optional, but adds clarity)
        explanation = Tex("100 \"dibagi\" 5 sama dengan 20", color=WHITE).scale(0.8)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(2)
