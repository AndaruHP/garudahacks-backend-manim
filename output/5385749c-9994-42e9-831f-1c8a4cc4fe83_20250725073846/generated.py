from manim import *

class DivisionExample(Scene):
    def construct(self):
        # Teks pembagian
        division_text = MathTex("100 \div 4").move_to(UP)
        self.play(Write(division_text))
        self.wait(1)

        # Representasi visual 100 sebagai 10 x 10 kotak
        grid = Square(side_length=4).get_grid(10, 10)
        grid.set_color(BLUE)
        grid.scale(0.2)

        self.play(Create(grid), run_time=2)
        self.wait(1)

        # Membagi menjadi 4 kelompok
        group1 = VGroup(*[grid[i] for i in range(25)])
        group2 = VGroup(*[grid[i] for i in range(25, 50)])
        group3 = VGroup(*[grid[i] for i in range(50, 75)])
        group4 = VGroup(*[grid[i] for i in range(75, 100)])

        self.play(
            group1.move_to(UP + LEFT * 2),
            group2.move_to(UP + RIGHT * 2),
            group3.move_to(DOWN + LEFT * 2),
            group4.move_to(DOWN + RIGHT * 2),
            run_time=2
        )
        self.wait(1)

        # Menghitung jumlah kotak di setiap kelompok
        count_text = MathTex("= 25").next_to(division_text, RIGHT)
        self.play(Write(count_text))

        self.wait(2)

        # Kotak yang merepresentasikan angka 25
        box25 = Square(side_length = 1).get_grid(5,5)
        box25.set_color(GREEN)
        box25.scale(0.3)
        box25.move_to(DOWN*2)

        self.play(Create(box25))

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)