from manim import *

class SembilanKaliDua(Scene):
    def construct(self):
        angka_sembilan = MathTex("9", color=BLUE)
        angka_dua = MathTex("2", color=RED)
        kali = MathTex("\\times")
        sama_dengan = MathTex("=")
        delapan_belas = MathTex("18", color=GREEN)

        group = VGroup(angka_sembilan, kali, angka_dua, sama_dengan, delapan_belas).arrange(RIGHT)

        self.play(Write(angka_sembilan))
        self.play(Write(kali))
        self.play(Write(angka_dua))
        self.play(Write(sama_dengan))

        self.wait(0.5)

        self.play(Write(delapan_belas))

        self.wait(2)

        #Visualisasi lain (optional):

        dots = VGroup(*[Dot(point=RIGHT*x + UP*y) for x in range(2) for y in range(9)])
        dots.arrange_in_grid(rows=9, buff=0.25)
        dots.scale(0.5)
        dots.to_edge(DOWN)

        self.play(TransformFromCopy(group, dots))

        self.wait(2)
