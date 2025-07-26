from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class MultiplicationExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        multiplication = MathTex('5 \times 5 = 25')
        with self.voiceover('Lima dikali lima adalah dua puluh lima.'):
            self.play(Write(multiplication))
            self.wait(2)
        self.play(FadeOut(multiplication))