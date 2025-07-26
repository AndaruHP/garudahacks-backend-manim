from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivisionVoiceover(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        with self.voiceover("Mari kita hitung 999 dibagi 9."):
            equation = MathTex("999", "\div", "9")
            self.play(Write(equation))
            self.wait(2)
        with self.voiceover("Jadi, jika kita membagi 999 dengan 9, kita akan mendapatkan 111."):
            result = MathTex("111")
            result.next_to(equation, DOWN)
            self.play(Transform(equation, result))
            self.wait(2)
        self.play(FadeOut(equation))