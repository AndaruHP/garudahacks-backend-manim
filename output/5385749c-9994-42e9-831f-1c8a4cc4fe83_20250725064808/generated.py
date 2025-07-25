from manim import *

class SembilanKaliDua(Scene):
    def construct(self):
        # Teks penjelasan
        teks_penjelasan = Tex(r"9 \times 2 = ?", font_size=72)
        self.play(Write(teks_penjelasan))
        self.wait(1)

        # Representasi visual: 9 kelompok berisi 2 objek
        kelompok = []
        for i in range(9):
            objek_1 = Dot(color=BLUE, radius=0.2).move_to(UP + LEFT*2 + RIGHT*i*0.8)
            objek_2 = Dot(color=GREEN, radius=0.2).move_to(DOWN + LEFT*2+ RIGHT*i*0.8)
            kelompok.append(VGroup(objek_1, objek_2))

        self.play(*[Create(g) for g in kelompok])
        self.wait(1)
        # Menghitung total objek
        total_objek = 18
        teks_total = Tex(f"Total: {total_objek}", font_size=72).move_to(DOWN*2)

        self.play(Write(teks_total))
        self.wait(1)

        # Jawaban
        jawaban = Tex(r"9 \times 2 = 18", font_size=72).move_to(UP*2)
        self.play(Transform(teks_penjelasan, jawaban))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
