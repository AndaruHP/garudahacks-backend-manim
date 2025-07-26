from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class CalculateDivision(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        equation = MathTex("1000 : 50 = ?")

        with self.voiceover("Let's calculate 1000 divided by 50."):
            self.play(Write(equation))
            self.wait(2)

        answer = MathTex("1000 : 50 = 20")

        with self.voiceover("So, 1000 divided by 50 equals 20."):
            self.play(Transform(equation, answer))
            self.wait(2)

        self.play(FadeOut(equation))