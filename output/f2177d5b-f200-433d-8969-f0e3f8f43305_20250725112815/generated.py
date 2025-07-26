from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class FractionCalculation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        # Membuat objek MathTex
        fraction = MathTex("5 / 8")
        # Menampilkan objek MathTex dengan animasi Write
        with self.voiceover("Mari kita hitung 5 dibagi 8."):
            self.play(Write(fraction))
            self.wait(2)

        # Menghitung hasil pembagian
        result = 5 / 8
        result_text = MathTex(str(result))
        # Mengganti objek MathTex fraction dengan result_text
        with self.voiceover("Hasilnya adalah " + str(result) + "."):
            self.play(Transform(fraction, result_text))
            self.wait(2)

        # Menghapus objek MathTex dari layar
        self.play(FadeOut(fraction))