from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
from dotenv import load_dotenv

load_dotenv()

class MultiplicationAsAddition(VoiceoverScene):
    def construct(self):
        # Azure voice setup: AvaMultilingual
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION"),
            )
        )

        # Introduction
        with self.voiceover(text="Let's understand how five times five can be represented as repeated addition.") as tracker:
            self.wait(tracker.duration)

        # Equation at the top
        equation = MathTex("5 \\times 5 =").to_edge(UP)
        self.play(Write(equation))

        with self.voiceover(text="Five times five means we add the number five, five times.") as tracker:
            self.wait(tracker.duration)

        # Display: 5 + 5 + 5 + 5 + 5
        addition = MathTex("5", "+", "5", "+", "5", "+", "5", "+", "5").next_to(equation, DOWN)

        for i in range(0, 9, 2):  # Loop over numbers
            self.play(Write(addition[i]))
            if i < 8:
                self.play(Write(addition[i + 1]))
            self.wait(0.3)

        self.wait(0.5)

        # Narration for result
        with self.voiceover(text="And when we add them all together, the result is twenty five.") as tracker:
            self.wait(tracker.duration)

        result = MathTex("= 25").next_to(addition, RIGHT)
        self.play(Write(result))
        self.wait(1)
