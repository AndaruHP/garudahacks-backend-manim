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

        # Create numbers
        num1 = MathTex("5")
        times = MathTex("\times")
        num2 = MathTex("8")
        equation = VGroup(num1, times, num2).arrange(RIGHT)

        with self.voiceover("Mari kita hitung 5 kali 8"):
            self.play(Write(equation))
            self.wait(2)

        result = MathTex("40")
        result.next_to(equation, RIGHT)

        with self.voiceover("Hasil dari 5 kali 8 adalah 40"):
            self.play(Transform(num2, result))
            self.wait(2)

        self.play(FadeOut(equation), FadeOut(result))