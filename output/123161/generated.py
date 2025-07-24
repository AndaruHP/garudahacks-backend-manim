from manim import *

class AlgebraProblem(Scene):
    def construct(self):
        # Define the equation
        equation_text = Tex('x + 5 + 1 = 11 - 10')
        self.play(Write(equation_text))
        self.wait(1)

        # Simplify the equation
        simplified_left = Tex('x + 6 = 11 - 10')
        self.play(Transform(equation_text, simplified_left))
        self.wait(1)

        simplified_right = Tex('x + 6 = 1')
        self.play(Transform(equation_text, simplified_right))
        self.wait(1)

        # Isolate x
        isolate_x = Tex('x = 1 - 6')
        self.play(Transform(equation_text, isolate_x))
        self.wait(1)

        # Solve for x
        solution = Tex('x = -5')
        self.play(Transform(equation_text, solution))
        self.wait(2)

        # Show the solution
        solution_box = SurroundingRectangle(solution, color=GREEN, buff=0.2)
        self.play(Create(solution_box))
        self.wait(2)

        self.play(FadeOut(equation_text, solution_box))
        self.wait(1)



if __name__ == "__main__":
    import os

    script_name = os.path.basename(__file__)
    command_line = f"manim -pql {script_name} AlgebraProblem"
    os.system(command_line)