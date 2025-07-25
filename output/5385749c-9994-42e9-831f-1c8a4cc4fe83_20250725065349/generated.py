from manim import *

class SembilanKaliDua(Scene):
    def construct(self):
        # Teks Soal
        soal = Tex(r"9 \times 2 = ?", font_size=72)
        self.play(Write(soal))
        self.wait(1)

        # Representasi Visual
        boxes = VGroup(*[Square(side_length=1).set_fill(BLUE, opacity=0.5).set_stroke(width=2) for _ in range(9)])
        boxes.arrange(RIGHT, buff=0.5)
        boxes.move_to(UP * 1.5)
        self.play(Create(boxes))
        self.wait(1)

        boxes2 = VGroup(*[Square(side_length=1).set_fill(GREEN, opacity=0.5).set_stroke(width=2) for _ in range(9)])
        boxes2.arrange(RIGHT, buff=0.5)
        boxes2.move_to(DOWN * 0.5)
        self.play(Create(boxes2))
        self.wait(1)
        
        plus_sign = Tex("+").scale(2).move_to(LEFT * 4)
        arrow_up = Arrow(start=plus_sign.get_left() + LEFT * 0.5 + UP * 0.5, end=boxes.get_left(), buff=0.1)
        arrow_down = Arrow(start=plus_sign.get_left() + LEFT * 0.5 + DOWN * 0.5, end=boxes2.get_left(), buff=0.1)
        self.play(Create(plus_sign),Create(arrow_up),Create(arrow_down))
        self.wait(1)
        
        # Menghitung Hasil
        hasil = Tex("= 18", font_size=72)
        hasil.move_to(DOWN * 2.5)
        self.play(Write(hasil))
        self.wait(2)

        # Menghapus semua objek
        self.play(FadeOut(soal, boxes, boxes2, hasil, plus_sign, arrow_up, arrow_down))
        self.wait(1)