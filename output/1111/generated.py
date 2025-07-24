from manim import *

class SolveEquation(Scene):
    def construct(self):
        equation = Tex("x + 1000 + 1 = 11 - 10")
        self.play(Write(equation))
        self.wait(1)

        equation_step1 = Tex("x + 1001 = 11 - 10")
        self.play(Transform(equation, equation_step1))
        self.wait(1)

        equation_step2 = Tex("x + 1001 = 1")
        self.play(Transform(equation, equation_step2))
        self.wait(1)

        equation_step3 = Tex("x = 1 - 1001")
        self.play(Transform(equation, equation_step3))
        self.wait(1)

        equation_step4 = Tex("x = -1000")
        self.play(Transform(equation, equation_step4))
        self.wait(2)
