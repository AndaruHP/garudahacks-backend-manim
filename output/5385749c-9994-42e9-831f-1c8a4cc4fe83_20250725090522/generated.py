from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

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

        # Create the equation
        equation = MathTex('255', '\div', '5')

        # Display the equation
        with self.voiceover("Let's calculate 255 divided by 5."):
            self.play(Write(equation))
            self.wait(2)

        # Calculate the result
        result = MathTex('51')
        result.next_to(equation, RIGHT, buff=1)
        equals = MathTex('=')
        equals.next_to(equation, RIGHT)

        # Display the result
        with self.voiceover("255 divided by 5 equals 51."):
            self.play(Transform(equation, equals), FadeIn(result))
            self.wait(2)

        # Remove all mobjects
        self.play(FadeOut(equation), FadeOut(result))