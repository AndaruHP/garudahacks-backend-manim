from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Soal Pembagian
        division_problem = MathTex("100", ":", "2", "=", "?")
        self.play(Write(division_problem))
        self.wait(1)

        # Geser soal ke atas
        self.play(division_problem.animate.to_edge(UP))

        # Visualisasi 100 objek (misalnya lingkaran)
        num_circles = 100
circles = VGroup(*[Circle(radius=0.1).move_to(np.array([np.random.uniform(-4, 4), np.random.uniform(-2, 2), 0])) for _ in range(num_circles)])
        self.play(Create(circles))
        self.wait(1)

        # Membuat dua grup
        group1 = VGroup(*circles[:50])
group2 = VGroup(*circles[50:])

        # Menggeser kedua grup
group1_target = group1.copy().arrange(buff=0.2).move_to(LEFT * 3 + DOWN * 1)
group2_target = group2.copy().arrange(buff=0.2).move_to(RIGHT * 3 + DOWN * 1)

        self.play(Transform(group1, group1_target), Transform(group2, group2_target))
        self.wait(1)

        # Menghitung jumlah objek di setiap grup
        result = MathTex("50")
result.move_to(division_problem[4].get_center() + DOWN * 2)

        # Menampilkan jawaban
        self.play(Write(result))

        # Mengganti tanda tanya dengan jawaban
        self.play(Transform(division_problem[4], result.copy().move_to(division_problem[4].get_center())))
        self.wait(2)
