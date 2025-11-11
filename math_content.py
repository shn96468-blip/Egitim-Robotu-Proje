# Bu dosya, sadece Matematik konularını ve fonksiyonlarını içerir.
KONULAR_MATH = {
    "doğal sayılar": "⭐ Doğal Sayılar: 0'dan başlayıp sonsuza giden pozitif tam sayılardır.",
    "tam sayılar": "Doğal sayılar, negatifleri ve sıfırdan oluşur.",
    "denklemler": "İki cebirsel ifadenin eşitliğini gösteren ifadelerdir. Bilinmeyeni (x) bulmayı amaçlar.",
    "fonksiyonlar": "Bir kümenin her elemanını, ikinci bir kümenin tek bir elemanına eşleyen kuraldır.",
    "trigonometri": "Üçgenlerin açıları ve kenarları arasındaki ilişkileri inceler.",
    "logaritma": "Üslü ifadelerin tersi işlemidir.",
    "türev": "Bir fonksiyonun belli bir noktadaki anlık değişim hızını bulur.",
    "integral": "Türevin tersi işlemidir. Eğriler altındaki alanı hesaplamakta kullanılır.",
}

def konuyu_bul_math(arama_terimi):
    if arama_terimi in KONULAR_MATH:
        return f"📐 MATEMATİK KONU ANLATIMI (12. Sınıf Kapsamlı):\n{KONULAR_MATH[arama_terimi]}"
    else:
        return "Üzgünüm, aradığınız konuyu Matematik sözlüğünde bulamadım."

def soru_cozumu_yap_math(arama_termi):
    return "❓ Örnek Soru Çözümü (Matematik): Gerekli limit/türev/integral kuralı kullanılarak çözüldü."