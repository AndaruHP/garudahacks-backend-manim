from manim import *

class SembilanKaliLima(Scene):
    def construct(self):
        # Visualisasi Perkalian sebagai Penjumlahan Berulang
        sembilan = Tex('9', color=BLUE).scale(2)
        kali = Tex('$\times$', color=WHITE).scale(2)
        lima = Tex('5', color=GREEN).scale(2)
        sama_dengan = Tex('=', color=WHITE).scale(2)
        tanda_tanya = Tex('?', color=YELLOW).scale(2)

        group_awal = VGroup(sembilan, kali, lima, sama_dengan, tanda_tanya).arrange(RIGHT)

        self.play(Write(group_awal))
        self.wait(1)

        self.play(
            group_awal.animate.to_edge(UP)
        )

        sembilan_grup = VGroup(*[Tex('9', color=BLUE) for _ in range(5)]).arrange(RIGHT).scale(1.5).next_to(group_awal, DOWN, buff=1)
        plus_signs = VGroup(*[Tex('+', color=WHITE) for _ in range(4)]).scale(1.5)
        for i, plus_sign in enumerate(plus_signs):
            plus_sign.move_to(sembilan_grup[i].get_right() + RIGHT*0.2)

        self.play(Write(sembilan_grup))
        self.play(Write(plus_signs))
        self.wait(1)

        sama_dengan_bawah = Tex('=', color=WHITE).scale(1.5).next_to(sembilan_grup, DOWN, buff=0.5)
        self.play(Write(sama_dengan_bawah))

        empat_lima = Tex('45', color=YELLOW).scale(2).next_to(sama_dengan_bawah, RIGHT, buff=0.5)
        self.play(Write(empat_lima))
        self.wait(2)

        #Highlight jawaban akhir
        self.play(
            Indicate(empat_lima, color=RED, scale_factor=1.2)
        )
        self.wait(2)

        kotak = SurroundingRectangle(empat_lima, color=RED, buff=0.2)
        self.play(Create(kotak))
        self.wait(2)

        #Ganti tanda tanya di atas dengan jawaban
        self.play(
            ReplacementTransform(tanda_tanya, empat_lima.copy().scale(0.7).move_to(tanda_tanya.get_center()))
        )
        self.wait(3)
