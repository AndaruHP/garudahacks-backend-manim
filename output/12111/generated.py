from manim import *

class SolveEquation(Scene):
    def construct(self):
        # Define the equation
        equation = Tex(r"x + 1000 + 1 = 11 - 10")
        self.play(Write(equation))
        self.wait(1)

        # Simplify the equation
        simplified_equation1 = Tex(r"x + 1001 = 1")
        self.play(TransformMatchingTex(equation, simplified_equation1))
        self.wait(1)

        # Isolate x
        isolate_x = Tex(r"x = 1 - 1001")
        self.play(TransformMatchingTex(simplified_equation1, isolate_x))
        self.wait(1)

        # Final solution
        solution = Tex(r"x = -1000")
        self.play(TransformMatchingTex(isolate_x, solution))
        self.wait(2)

        # Highlight the solution
        box = SurroundingRectangle(solution, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(1)

        # Display final answer with explanation
        final_answer = VGroup(
            Tex(r"\text{Therefore,}"),
            Tex(r"x = -1000")
        ).arrange(DOWN)
        self.play(Transform(VGroup(box, solution), final_answer))

        self.wait(3)
