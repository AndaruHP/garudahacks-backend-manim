from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os


class MultiplyScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        
        number_5 = MathTex("5").scale(2)
        number_10 = MathTex("10").scale(2).next_to(number_5, RIGHT, buff=1)
        multiply_sign = MathTex("\times").scale(2).next_to(number_5, RIGHT)
        
        with self.voiceover("Ini adalah cara menghitung 5 kali 10."):
            self.play(Write(number_5))
            self.play(Write(multiply_sign))
            self.play(Write(number_10))

        with self.voiceover("5 kali 10 sama dengan 50."):
            result = MathTex("= 50").scale(2).next_to(number_10, RIGHT, buff=1)
            self.play(Write(result))

        self.wait(2)
        self.play(FadeOut(number_5), FadeOut(number_10), FadeOut(multiply_sign), FadeOut(result))