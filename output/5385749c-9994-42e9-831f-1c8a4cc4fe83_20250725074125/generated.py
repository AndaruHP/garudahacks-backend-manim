from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Problem statement
        problem = MathTex("100 \div 4 = ?")
        self.play(Write(problem))
        self.wait(1)

        # Showing 100 as a collection of dots
        dots = VGroup(*[Dot(point=i * RIGHT * 0.1 + j * DOWN * 0.1) for i in range(10) for j in range(10)])
        dots.move_to(DOWN * 1.5)
        dots.set_color(BLUE)
        self.play(FadeIn(dots))
        self.wait(1)

        # Grouping the dots into 4 groups
        group1 = VGroup(*dots[:25]).set_color(YELLOW).move_to(LEFT * 2 + UP * 1.5)
        group2 = VGroup(*dots[25:50]).set_color(GREEN).move_to(RIGHT * 2 + UP * 1.5)
        group3 = VGroup(*dots[50:75]).set_color(ORANGE).move_to(LEFT * 2 + DOWN * 1.5)
        group4 = VGroup(*dots[75:]).set_color(PURPLE).move_to(RIGHT * 2 + DOWN * 1.5)

        self.play(
            Transform(dots[:25], group1),
            Transform(dots[25:50], group2),
            Transform(dots[50:75], group3),
            Transform(dots[75:], group4)
        )
        self.wait(1)

        # Counting the dots in one group
        num_dots = MathTex("25").next_to(group1, UP)
        self.play(Write(num_dots))
        self.wait(1)

        # Showing the answer
        answer = MathTex("100 \div 4 = 25").move_to(UP * 2)
        self.play(Transform(problem, answer))
        self.wait(2)
