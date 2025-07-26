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

        # create number 5
        number_5 = MathTex('5')
        number_5.shift(2*LEFT)

        # create multiplication symbol
        mul_symbol = MathTex('\times')

        # create number 6
        number_6 = MathTex('6')
        number_6.shift(2*RIGHT)

        # create equal symbol
        equal_symbol = MathTex('=')
        equal_symbol.shift(4*RIGHT)

        # create result
        result = MathTex('30')
        result.shift(6*RIGHT)

        with self.voiceover("Kita akan menghitung 5 dikalikan dengan 6."):
            self.play(Write(number_5), Write(mul_symbol), Write(number_6))
            self.wait(1)
        with self.voiceover("Hasil dari 5 dikalikan dengan 6 adalah 30."):
            self.play(Write(equal_symbol), Write(result))
            self.wait(1)

        # remove objects
        self.play(FadeOut(number_5), FadeOut(mul_symbol), FadeOut(number_6), FadeOut(equal_symbol), FadeOut(result))