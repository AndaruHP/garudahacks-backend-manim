from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Title
        title = Text("100 : 20 = ?", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Method 1: Repeated Subtraction
        subtraction_title = Text("Cara 1: Pengurangan Berulang", font_size=36).to_edge(LEFT + UP)
        self.play(Transform(title, subtraction_title))

        hundred = MathTex("100", color=YELLOW).shift(UP * 1.5)
        minus_twenty_1 = MathTex("- 20", color=RED).next_to(hundred, DOWN)
        eighty = MathTex("80", color=YELLOW).next_to(minus_twenty_1, DOWN)
        minus_twenty_2 = MathTex("- 20", color=RED).next_to(eighty, DOWN)
        sixty = MathTex("60", color=YELLOW).next_to(minus_twenty_2, DOWN)
        minus_twenty_3 = MathTex("- 20", color=RED).next_to(sixty, DOWN)
        forty = MathTex("40", color=YELLOW).next_to(minus_twenty_3, DOWN)
        minus_twenty_4 = MathTex("- 20", color=RED).next_to(forty, DOWN)
        twenty = MathTex("20", color=YELLOW).next_to(minus_twenty_4, DOWN)
        minus_twenty_5 = MathTex("- 20", color=RED).next_to(twenty, DOWN)
        zero = MathTex("0", color=YELLOW).next_to(minus_twenty_5, DOWN)

        self.play(Write(hundred))
        self.play(Write(minus_twenty_1), Write(eighty))
        self.play(Write(minus_twenty_2), Write(sixty))
        self.play(Write(minus_twenty_3), Write(forty))
        self.play(Write(minus_twenty_4), Write(twenty))
        self.play(Write(minus_twenty_5), Write(zero))
        self.wait(2)

        count_text = Text("Kita mengurangkan 20 sebanyak 5 kali.", font_size=30).to_edge(DOWN)
        self.play(Write(count_text))
        self.wait(2)

        # Method 2: Definition of Division
        definition_title = Text("Cara 2: Definisi Pembagian", font_size=36).to_edge(LEFT + UP)
        self.play(Transform(title, definition_title), FadeOut(hundred, minus_twenty_1, eighty, minus_twenty_2, sixty, minus_twenty_3, forty, minus_twenty_4, twenty, minus_twenty_5, zero, count_text))
        self.wait(1)

        division_equation = MathTex("100 : 20 = x").shift(UP)
        meaning_equation = MathTex("20 \times x = 100").next_to(division_equation, DOWN)

        self.play(Write(division_equation))
        self.wait(1)
        self.play(Write(meaning_equation))
        self.wait(2)

        x_equals_5 = MathTex("x = 5").next_to(meaning_equation, DOWN)
        self.play(Write(x_equals_5))
        self.wait(2)

        # Final Answer
        final_answer = MathTex("100 : 20 = 5", color=GREEN).to_edge(DOWN)
        self.play(Transform(division_equation, final_answer), FadeOut(meaning_equation, x_equals_5))
        self.wait(3)
