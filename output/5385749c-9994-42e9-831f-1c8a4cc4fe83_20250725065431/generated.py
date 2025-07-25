from manim import *

class SembilanKaliDua(Scene):
    def construct(self):
        # Visualisasi perkalian sebagai penjumlahan berulang
        teks_perkalian = MathTex("9 \times 2 = ").to_edge(UP)
        self.play(Write(teks_perkalian))

        sembilan_plus_sembilan = MathTex("9 + 9 = ").next_to(teks_perkalian, DOWN, buff=0.5)
        self.play(Write(sembilan_plus_sembilan))

        hasil = MathTex("18").next_to(sembilan_plus_sembilan, RIGHT)
        self.play(Write(hasil))

        self.wait(2)

        # Alternatif: Visualisasi array 9x2
        self.play(
            FadeOut(teks_perkalian),
            FadeOut(sembilan_plus_sembilan),
            FadeOut(hasil)
        )

        dots = VGroup(*[Dot(point=[x, y, 0]) for x in range(2) for y in range(9)])
        dots.arrange_in_grid(rows=9, cols=2, buff=(DEFAULT_BUFF/5))
        self.play(Create(dots))

        teks_array = Text("9 baris, 2 kolom").next_to(dots, DOWN)
        self.play(Write(teks_array))

        kotak = SurroundingRectangle(dots, color=YELLOW, buff=0.1)
        self.play(Create(kotak))
        self.wait(2)

        jumlah_titik = MathTex("Jumlah \: Titik = 18").next_to(kotak, DOWN)
        self.play(Write(jumlah_titik))

        self.wait(3)
