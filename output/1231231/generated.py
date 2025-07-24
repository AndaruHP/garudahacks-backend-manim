from manim import *

class SolveEquation(Scene):
    def construct(self):
        # Persamaan awal
        equation = Tex("x + 5 + 1 = 11 - 10")
        self.play(Write(equation))
        self.wait(1)

        # Langkah 1: Sederhanakan kedua sisi
        step1 = Tex("x + 6 = 1")
        self.play(TransformMatchingTex(equation, step1))
        self.wait(1)

        # Langkah 2: Kurangi 6 dari kedua sisi
        step2 = Tex("x + 6 - 6 = 1 - 6")
        self.play(TransformMatchingTex(step1, step2))
        self.wait(1)

        # Langkah 3: Sederhanakan lagi
        step3 = Tex("x = -5")
        self.play(TransformMatchingTex(step2, step3))
        self.wait(1)

        # Kotak di sekitar jawaban
        box = SurroundingRectangle(step3)
        self.play(Create(box))
        self.wait(2)