
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class CalculateDivision(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AvaMultilingualNeural", 
                style="general", 
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"), 
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )
        
        # Create the division operation
        division_operation = MathTex('999', ' \div ', '1')
        with self.voiceover("Let's calculate 999 divided by 1."):
            self.play(Write(division_operation))
            self.wait(1)

        # Create the result
        result = MathTex('999')
        result.next_to(division_operation, DOWN, buff=1)

        # Transform the operation into the result
        with self.voiceover("When we divide any number by 1, the result is always the number itself. So, 999 divided by 1 equals 999."):
            self.play(Transform(division_operation, result))
            self.wait(2)

        # Remove the result from the screen
        with self.voiceover("Now, let's clear the screen."):
            self.play(FadeOut(division_operation))
            self.wait(1)
