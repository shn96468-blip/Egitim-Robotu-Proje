# Bu dosya, sadece 7. Sınıfa kadar Türkçe konularını içerir.
KONULAR_TR = {
    "gerçek anlam": "⭐ Gerçek Anlam: Kelimenin akla gelen ilk anlamıdır.",
    "mecaz anlam": "Gerçek anlamdan tamamen uzaklaşan, soyut anlamdır.",
    "deyimler": "Genellikle mecaz anlamlı, kalıplaşmış söz gruplarıdır.",
    "neden sonuç cümleleri": "Kesinleşmiş bir sebep bildiren cümlelerdir.",
    "fiiller": "⭐ Fiiller: İş, oluş, hareket bildiren sözcüklerdir.",
    "zarflar": "Fiilleri, fiilimsileri, sıfatları etkileyen sözcüklerdir.",
    "yazım imla kuralları": "Kelimelerin doğru yazılışını kapsar.",
}

def konuyu_bul_tr(arama_terimi):
    if arama_terimi in KONULAR_TR:
        return f"🇹🇷 TÜRKÇE KONU ANLATIMI (7. Sınıfa Kadar):\n{KONULAR_TR[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız konuyu 7. Sınıf Türkçe sözlüğünde bulamadım."

def soru_cozumu_yap_tr(arama_termi):
    return "❓ Örnek Soru Çözümü (Türkçe): Çözüm için 7. Sınıf Türkçe Dil Bilgisi kuralları kullanıldı."