
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivideScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        math_expression = MathTex("999 / 1 = ?")
        with self.voiceover("Let's divide 999 by 1."):
            self.play(Write(math_expression))
            self.wait(2)

        result = MathTex("999 / 1 = 999")
        with self.voiceover("If we divide any number by 1, the result is the number itself. So, 999 divided by 1 equals 999."):
            self.play(Transform(math_expression, result))
            self.wait(2)

        self.play(FadeOut(math_expression))
