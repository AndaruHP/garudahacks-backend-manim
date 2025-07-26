from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Text objects
        dividend = MathTex("100", color=BLUE)
        divisor = MathTex("2", color=RED)
        division_sign = MathTex("\div", color=WHITE)
        equals_sign = MathTex("=", color=WHITE)
        quotient = MathTex("50", color=GREEN)

        # Arrange the objects
        group = VGroup(dividend, division_sign, divisor, equals_sign, quotient).arrange(RIGHT)

        # Animations
        self.play(Write(dividend), Write(division_sign), Write(divisor))
        self.wait(1)
        self.play(Write(equals_sign))
        self.wait(0.5)
        self.play(Write(quotient))
        self.wait(2)

        # Alternative visual representation (optional)
        rectangles = VGroup(*[Rectangle(width=0.5, height=1) for _ in range(100)])
        rectangles.arrange_in_grid(rows=10, cols=10, buff=0.1)
        rectangles.scale(0.2)

        group2 = VGroup(*[VGroup(*rectangles[i:i+2]) for i in range(0, 100, 2)])
        group2.arrange_in_grid(rows=5, cols=10, buff=0.2)
        group2.move_to(DOWN * 2.5)

        fifty_rects = VGroup(*[Rectangle(width=0.5, height=1) for _ in range(50)])
        fifty_rects.arrange_in_grid(rows=5, cols=10, buff=0.1)
        fifty_rects.scale(0.4)
        fifty_rects.move_to(DOWN*2.5)
        fifty_rects.set_color(GREEN)

        self.play(
            TransformFromCopy(dividend, rectangles),
            FadeOut(group, shift=UP)
        )

        self.wait(1)
        self.play(TransformMatchingShapes(rectangles, fifty_rects))

        self.wait(2)
