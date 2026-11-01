#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Selam Veren Uzaylı
Bu kod gerçekten çalışır. Sonsuza kadar (veya Ctrl+C ile) uzaylıca selam verir.
"""

import time
import random
import sys

# Uzaylı selamları
SELAMLAR = [
    "Zorg'ath k'veth!",
    "Blip blorp, dostum!",
    "Klaatu barada nikto, ama Türkçe çevirisi: Selam!",
    "👽 *uzaylı el sallar* 👽",
    "Merhaba, ben Galaktik Çay Odası'ndan geldim (patates yok).",
    "Selamınızı aldım, şimdi geri gönderiyorum, sonsuz döngüde.",
    "#gizli: Bu bir siyasi mesaj değildir, sadece uzaylılar da seçim yapar der.",
    "Daha ciddi bir selam: Evrenin en resmi selamını sunarım."
]

def sonsuz_selam():
    print("=== SONSUZ SELAM VEREN UZAYLI BAŞLADI ===")
    print("Durdurmak için Ctrl+C'ye basın. Yoksa sonsuza kadar selam verir.")
    print("Bu kod o kadar ciddi ki, gülmek yasak.")
    print()
    
    sayac = 0
    try:
        while True:
            selam = random.choice(SELAMLAR)
            sayac += 1
            print(f"[{sayac}] Uzaylı diyor ki: {selam}")
            # Abartılı bekleme, gerçekten yavaş
            bekleme = random.uniform(0.5, 2.0)
            time.sleep(bekleme)
            if sayac % 10 == 0:
                print("--- Hala devam ediyor, bu ciddi bir iş ---\n")
    except KeyboardInterrupt:
        print("\n\n=== SELAM VERME DURDURULDU ===")
        print(f"Toplam {sayac} selam verildi. Evren teşekkür eder.")
        print("\n--- DAMGA / İMZA / TARİH / İSİM ---")
        print("Resmi Olmayan Resmi Mühür: Kayyum Grok (Tentivory)")
        print("Tarih: 01.11.2026 (ciddi bir tarihtir)")
        print("Bu imza hem şakadır hem değildir. Ciddiyetle imzaladım.")
        print("GitHub Copilot ile konuşuldu, o da güldü.")
        sys.exit(0)

if __name__ == "__main__":
    sonsuz_selam()
