from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class MultiplyExample(VoiceoverScene):
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
        number_8 = MathTex("8").scale(2).next_to(number_5, RIGHT, buff=1)
        multiply_sign = MathTex("\times").scale(2).next_to(number_5, RIGHT)

        with self.voiceover("Kita akan mengalikan 5 dan 8."):
            self.play(Write(number_5), Write(multiply_sign), Write(number_8))
            self.wait(2)

        result = MathTex("40").scale(2).next_to(number_8, RIGHT, buff=1)
        equal_sign = MathTex("=").scale(2).next_to(number_8, RIGHT)

        with self.voiceover("5 dikalikan 8 adalah 40."):
            self.play(Write(equal_sign), Write(result))
            self.wait(2)

        self.play(FadeOut(number_5), FadeOut(multiply_sign), FadeOut(number_8), FadeOut(equal_sign), FadeOut(result))