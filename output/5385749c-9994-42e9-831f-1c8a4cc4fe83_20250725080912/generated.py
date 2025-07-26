from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivideExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        division = MathTex('100', '\div', '50')
        self.play(Write(division))
        with self.voiceover("One hundred divided by fifty."):
            self.wait(2)
        result = MathTex('100', '\div', '50', '=', '2')
        with self.voiceover("Is equal to two."):
            self.play(Transform(division, result))
            self.wait(2)
        self.play(FadeOut(division))