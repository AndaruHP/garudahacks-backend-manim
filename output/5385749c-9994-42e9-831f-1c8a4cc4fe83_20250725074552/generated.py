from manim import *

class DivisionScene(Scene):
    def construct(self):
        # Number to be divided
        dividend = 100
        # Number to divide by
        divisor = 10
        # Result of the division
        quotient = dividend / divisor

        # Create Text objects for each number
        dividend_text = Text(str(dividend), color=BLUE).scale(1.5)
        divisor_text = Text(str(divisor), color=GREEN).scale(1.5)
        division_symbol = Tex(r'$\div$', color=WHITE).scale(1.5)
        equals_symbol = Tex(r'=', color=WHITE).scale(1.5)
        quotient_text = Text(str(int(quotient)), color=YELLOW).scale(1.5) # Use int to avoid .0

        # Arrange the text objects horizontally
        group = VGroup(dividend_text, division_symbol, divisor_text, equals_symbol, quotient_text).arrange(RIGHT)

        # Display the objects
        self.play(Write(group))
        self.wait(2)

        # Example: Highlight the dividend and divisor
        rect_dividend = Rectangle(width=dividend_text.width + 0.2, height=dividend_text.height + 0.2, color=BLUE)
        rect_dividend.move_to(dividend_text.get_center())
        rect_divisor = Rectangle(width=divisor_text.width + 0.2, height=divisor_text.height + 0.2, color=GREEN)
        rect_divisor.move_to(divisor_text.get_center())

        self.play(Create(rect_dividend), Create(rect_divisor))
        self.wait(1)

        # Show an arrow and brief explanation
        arrow = Arrow(start=divisor_text.get_bottom(), end=quotient_text.get_top(), color=YELLOW)
        explanation = Text("How many groups of 10 are in 100?", color=WHITE).scale(0.7)
        explanation.next_to(arrow, DOWN)

        self.play(Create(arrow), Write(explanation))
        self.wait(3)

        # Clean up
        self.play(FadeOut(group, rect_dividend, rect_divisor, arrow, explanation))
        self.wait(1)
