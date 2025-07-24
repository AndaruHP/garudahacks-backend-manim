from manim import *

class SolveEquation(Scene):
    def construct(self):
        # Persamaan awal
        equation = MathTex("x + 1000 + 1 = 11 - 10")
        self.play(Write(equation))
        self.wait(1)

        # Kelompokkan konstanta
        equation_simplified = MathTex("x + 1001 = 1")
        self.play(TransformMatchingTex(equation, equation_simplified))
        self.wait(1)

        # Kurangkan 1001 dari kedua sisi
        minus_1001 = MathTex("-1001")
        self.play(Write(minus_1001.move_to(UP*2))) #Menambahkan tulisan -1001
        self.wait(0.5)
        equation_minus_1001_left = MathTex("x + 1001 - 1001 = 1 - 1001")

        self.play(TransformMatchingTex(equation_simplified, equation_minus_1001_left))

        self.wait(1)

        # Sederhanakan lagi
        equation_solved = MathTex("x = -1000")
        self.play(TransformMatchingTex(equation_minus_1001_left, equation_solved))
        self.wait(2)

        self.play(FadeOut(equation_solved))
        self.play(FadeOut(minus_1001))


        # Menampilkan cara pengerjaan lain yang lebih detail

        equation = MathTex("x + 1000 + 1 = 11 - 10").move_to(UP*3)
        self.play(Write(equation))

        equation_step1 = MathTex("x + 1001 = 11 - 10").move_to(UP*2)
        self.play(Write(equation_step1))

        equation_step2 = MathTex("x + 1001 = 1").move_to(UP*1)
        self.play(Write(equation_step2))

        equation_step3 = MathTex("x = 1 - 1001").move_to(DOWN*0)
        self.play(Write(equation_step3))

        equation_step4 = MathTex("x = -1000").move_to(DOWN*1)
        self.play(Write(equation_step4))

        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects]) #Membersihkan semua objek di layar
