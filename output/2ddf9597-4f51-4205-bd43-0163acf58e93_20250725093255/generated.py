from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class AdditionScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural", 
                style="general", 
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"), 
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        equation = MathTex('5', '+', '4', '=', '9')
        with self.voiceover("Hasil dari penjumlahan 5 dan 4 adalah 9."):
            self.play(Write(equation))
            self.wait(3)
        self.play(FadeOut(equation))