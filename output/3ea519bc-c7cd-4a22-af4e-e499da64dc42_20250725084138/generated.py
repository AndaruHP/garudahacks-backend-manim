
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class Penjumlahan(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural", 
                style="general", 
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"), 
                region=os.getenv("AZURE_SERVICE_REGION")
            )
        )

        angka_satu = Text("5")
        angka_satu.to_edge(LEFT)
        operator = Text("+")
        operator.next_to(angka_satu, RIGHT)
        angka_dua = Text("10")
        angka_dua.next_to(operator, RIGHT)
        sama_dengan = Text("=")
        sama_dengan.next_to(angka_dua, RIGHT)
        hasil = Text("15")
        hasil.next_to(sama_dengan, RIGHT)

        with self.voiceover("Mari kita hitung 5 ditambah 10."):
            self.play(Write(angka_satu), Write(operator), Write(angka_dua))
            self.wait(2)

        with self.voiceover("Hasil dari 5 ditambah 10 adalah 15."):
            self.play(Write(sama_dengan), Write(hasil))
            self.wait(2)

        self.remove(angka_satu, operator, angka_dua, sama_dengan, hasil)
