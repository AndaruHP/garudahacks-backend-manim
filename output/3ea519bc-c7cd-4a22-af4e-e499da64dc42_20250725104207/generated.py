from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class MultiplicationScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        # Membuat objek teks untuk angka 6 dan 7
        number_6 = MathTex("6")
        number_7 = MathTex("7")
        multiply_sign = MathTex("\times")

        # Mengatur posisi objek teks
        number_6.to_edge(LEFT)
        number_7.to_edge(RIGHT)
        multiply_sign.next_to(number_6, RIGHT)
        multiply_sign.next_to(number_7, LEFT)

        # Menampilkan objek teks
        with self.voiceover("Kita akan mengalikan angka 6 dan 7."):
            self.play(Write(number_6), Write(number_7), Write(multiply_sign))
            self.wait(1)

        # Menghitung hasil
        result = MathTex("42")
        result_line = Line(number_6.get_bottom(), number_7.get_bottom()).next_to(number_6, DOWN)
        result.next_to(result_line, DOWN)

        # Menampilkan hasil
        with self.voiceover("Hasil dari 6 dikali 7 adalah 42."):
            self.play(ShowCreation(result_line), Write(result))
            self.wait(2)

        # Menghapus semua objek
        self.play(FadeOut(number_6), FadeOut(number_7), FadeOut(multiply_sign), FadeOut(result_line), FadeOut(result))