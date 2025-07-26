from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Title
        title = Tex("Menghitung 100 : 2").scale(1.5)
        self.play(Write(title))
        self.wait(1)

        # Equation setup
        equation = MathTex("100", ":", "2", "=", "?").shift(UP)
        self.play(Transform(title, equation))
        self.wait(1)

        # Visual representation (dots)
        dots = VGroup(*[Dot() for _ in range(100)]).arrange_in_grid(10, 10).scale(0.5).shift(DOWN)
        self.play(Create(dots))
        self.wait(1)

        # Grouping into two
        group1 = VGroup(*dots[:50]).set_color(BLUE)
        group2 = VGroup(*dots[50:]).set_color(GREEN)
        
        brace1 = Brace(group1, direction=DOWN, color=BLUE)
        brace2 = Brace(group2, direction=DOWN, color=GREEN)
        
        text1 = brace1.get_text("50", color=BLUE)
        text2 = brace2.get_text("50", color=GREEN)
        
        self.play(Create(brace1), Create(text1), Create(brace2), Create(text2))
        self.wait(1)

        # Answer
        answer = MathTex("100", ":", "2", "=", "50").shift(UP)
        self.play(Transform(equation, answer))
        self.wait(2)

        self.play(FadeOut(equation, dots, brace1, brace2, text1, text2))
        self.wait(1)