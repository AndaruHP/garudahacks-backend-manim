from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
from dotenv import load_dotenv

load_dotenv()

class PerkalianSebagaiPenjumlahan(VoiceoverScene):
    def construct(self):
        # Gunakan Azure TTS dengan voice bahasa Indonesia
        self.set_speech_service(
            AzureService(
                voice="id-ID-GadisNeural",
                style="general",
                azure_key=os.getenv("AZURE_SUBSCRIPTION_KEY"),
                region=os.getenv("AZURE_SERVICE_REGION"),
            )
        )

        # Narasi pembuka
        with self.voiceover(text="Mari kita lihat bagaimana lima dikali lima dapat diilustrasikan sebagai penjumlahan berulang.") as tracker:
            self.wait(tracker.duration)

        # Tampilkan soal
        soal = MathTex("5 \\times 5 =").to_edge(UP)
        self.play(Write(soal))

        # Narasi menjelaskan perkalian
        with self.voiceover(text="Lima dikali lima artinya lima dijumlahkan sebanyak lima kali.") as tracker:
            self.wait(tracker.duration)

        # Penjumlahan bertahap: 5 + 5 + 5 + 5 + 5
        penjumlahan = MathTex("5", "+", "5", "+", "5", "+", "5", "+", "5").next_to(soal, DOWN)

        for i in range(0, 9, 2):  # Indeks angka: 0, 2, 4, 6, 8
            self.play(Write(penjumlahan[i]))
            if i < 8:
                self.play(Write(penjumlahan[i + 1]))
            self.wait(0.3)

        self.wait(0.5)

        # Narasi hasil akhir
        with self.voiceover(text="Jika kita jumlahkan semuanya, hasilnya adalah dua puluh lima.") as tracker:
            self.wait(tracker.duration)

        hasil = MathTex("= 25").next_to(penjumlahan, RIGHT)
        self.play(Write(hasil))
        self.wait(1)
