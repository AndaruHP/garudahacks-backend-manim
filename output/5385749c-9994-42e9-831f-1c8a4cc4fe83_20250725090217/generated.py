from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivideNumbers(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        equation = MathTex("999", "\div", "999")
        result = MathTex("= 1")
        result.next_to(equation, RIGHT)

        with self.voiceover("Let's divide 999 by 999."):
            self.play(Write(equation))
            self.wait(1)

        with self.voiceover("Any number divided by itself is 1."):
            self.play(Transform(equation[2], result))
            self.wait(1)

        self.play(FadeOut(equation), FadeOut(result))