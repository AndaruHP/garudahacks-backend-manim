from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivisionCalculation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        
        equation = MathTex('100', '\div', '25', '=', '?')
        self.play(Write(equation))
        self.wait(1)

        with self.voiceover("Let's calculate 100 divided by 25."):
            result = MathTex('100', '\div', '25', '=', '4')
            self.play(Transform(equation, result))
            self.wait(1)

        with self.voiceover("So, 100 divided by 25 equals 4."):
            self.wait(2)

        self.play(FadeOut(equation))