
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class DivisionScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural", 
                style="general", 
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"), 
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        division = MathTex('999', '\div', '999')
        with self.voiceover("Let's divide 999 by 999."):
            self.play(Write(division))
            self.wait(1)

        result = MathTex('1')
        with self.voiceover("Any number divided by itself is 1."):
            self.play(Transform(division, result))
            self.wait(1)

        self.play(FadeOut(division))
}
