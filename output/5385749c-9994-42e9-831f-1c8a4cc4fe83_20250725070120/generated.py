from manim import *

class SembilanKaliEmpat(Scene):
    def construct(self):
        # Visualisasi perkalian sebagai penjumlahan berulang
        sembilan = Tex('9').move_to(LEFT * 2 + UP)
        kali = Tex(r'$\times$').move_to(LEFT * 1.5 + UP)
        empat = Tex('4').move_to(LEFT + UP)
        sama_dengan = Tex('=').move_to(LEFT * 0.5 + UP)
        hasil = Tex('?').move_to(RIGHT + UP)

        self.play(Create(sembilan), Create(kali), Create(empat), Create(sama_dengan), Create(hasil))
        self.wait(1)

        # Membuat 4 kelompok berisi 9 objek
        kelompok = []
        for i in range(4):
            dots = VGroup(*[Dot(point=[x, -i, 0]) for x in range(i*2, i*2+9)])
            kelompok.append(dots)
            self.play(Create(dots))

        self.wait(2)

        jumlah = 36
        jumlah_tex = Tex(str(jumlah)).move_to(RIGHT + UP)
        self.play(Transform(hasil, jumlah_tex))
        self.wait(2)

        # Menambahkan penjelasan visual (opsional)
        penjelasan = Tex('9 + 9 + 9 + 9 = 36').move_to(DOWN)
        self.play(Create(penjelasan))

        self.wait(3)
