import streamlit as st
import time

# --- YÖNETİCİ GİRİŞİ AYARLARI VE OTURUM BAŞLATMA ---
ADMIN_PASSWORD = "123"
MOCK_USERS = [
    {"username": "ali", "email": "ali@okul.com", "password_hash": "a123"},
    {"username": "ayse", "email": "ayse@okul.com", "password_hash": "a456"},
]

# OTURUM DURUMU BAŞLANGIÇ DEĞERLERİ
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
if 'show_user_login' not in st.session_state:
    st.session_state['show_user_login'] = False
if 'show_user_register' not in st.session_state:
    st.session_state['show_user_register'] = False
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#1E90FF' # Varsayılan Tema Rengi
if 'announcement' not in st.session_state:
    st.session_state['announcement'] = "🤖 Eğitim robotu aktif! Yeni konuları keşfetmeye başlayın."
if 'announcement_color' not in st.session_state:
    st.session_state['announcement_color'] = 'warning'
if 'registration_allowed' not in st.session_state:
    st.session_state['registration_allowed'] = True
if 'user_login_allowed' not in st.session_state:
    st.session_state['user_login_allowed'] = True
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'secilen_ders' not in st.session_state:
    st.session_state['secilen_ders'] = None
if 'show_kanka_chat' not in st.session_state:
    st.session_state['show_kanka_chat'] = False
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = False
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


# --- DERS FONKSİYONLARI YEDEK TANIMLARI (SIMÜLASYON) ---
def konuyu_bul_yedek(ders, konu): 
    return f"🤖 İçerik dosyaları yüklenmediği için {ders} dersi **'{konu}'** konusu hakkında genel bilgi veriyorum: Bu bir simülasyon cevabıdır. Gerçek bir AI, burada detaylı konu anlatımı yapacaktır."
    
def soru_cozumu_yap_yedek(ders, soru): 
    return f"🤖 İçerik dosyaları yüklenmediği için {ders} dersi **'{soru}'** sorusu çözülemiyor. Bu bir simülasyon cevabıdır. Gerçek bir AI, burada adım adım çözüm sunacaktır."

konuyu_bul_tr = lambda konu: konuyu_bul_yedek("Türkçe", konu)
soru_cozumu_yap_tr = lambda soru: soru_cozumu_yap_yedek("Türkçe", soru)
konuyu_bul_eng = lambda konu: konuyu_bul_yedek("İngilizce", konu)
soru_cozumu_yap_eng = lambda soru: soru_cozumu_yap_yedek("İngilizce", soru)
konuyu_bul_math = lambda konu: konuyu_bul_yedek("Matematik", konu)
soru_cozumu_yap_math = lambda soru: soru_cozumu_yap_yedek("Matematik", soru)
konuyu_bul_history = lambda konu: konuyu_bul_yedek("Tarih", konu)
soru_cozumu_yap_history = lambda soru: soru_cozumu_yap_yedek("Tarih", soru)
konuyu_bul_religion = lambda konu: konuyu_bul_yedek("Din K.", konu)
soru_cozumu_yap_religion = lambda soru: soru_cozumu_yap_yedek("Din K.", soru)


# --- SAYFA VE SİMGE AYARLARI (Gelişmiş Simge Kullanıldı) ---
st.set_page_config(
    page_title="Eğitim Robotu | Yusuf Efe Şahin",
    layout="wide",
    page_icon="🤖" # Projenizi profesyonel gösteren simge!
)

# --- GİRİŞ/ÇIKIŞ VE YÖNETİCİ FONKSİYONLARI ---
def attempt_admin_login(password):
    if password == ADMIN_PASSWORD:
        st.session_state['admin_mode'] = True
        st.session_state['show_admin_login'] = False
        st.rerun()
    else:
        st.error("Hatalı yönetici şifresi.")

def admin_logout():
    st.session_state['admin_mode'] = False
    st.rerun()

def user_login(username, password):
    if not st.session_state['user_login_allowed']:
        st.error("Üye girişi şu anda bakımdadır. Lütfen daha sonra tekrar deneyin.")
        return

    for user in MOCK_USERS:
        if user["username"] == username and user["password_hash"] == password:
            st.session_state['user_logged_in'] = True
            st.session_state['current_user'] = username
            st.session_state['show_user_login'] = False
            st.success(f"Hoş geldiniz, {username.upper()}!")
            time.sleep(1)
            st.rerun()
            return
    st.error("Kullanıcı adı veya şifre yanlış.")

def user_logout():
    st.session_state['user_logged_in'] = False
    st.session_state['current_user'] = None
    st.rerun()

def toggle_admin_login_panel():
    st.session_state['show_admin_login'] = not st.session_state['show_admin_login']
    st.session_state['show_user_login'] = False
    st.session_state['show_user_register'] = False

def toggle_user_login_panel():
    if st.session_state['user_login_allowed']:
        st.session_state['show_user_login'] = not st.session_state['show_user_login']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_register'] = False
    else:
        st.sidebar.error("Üye girişi şu anda bakımdadır.")

def toggle_user_register_panel():
    if st.session_state['registration_allowed']:
        st.session_state['show_user_register'] = not st.session_state['show_user_register']
        st.session_state['show_admin_login'] = False
        st.session_state['show_user_login'] = False
    else:
        st.sidebar.error("Yeni kayıtlar şu anda kapalıdır.")

def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistemimiz simülasyon modunda olduğundan, şifre sıfırlama linki kayıtlı e-posta adresinize gönderilmiştir.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili 'admin@robot.com' adresine gönderildi.")
    else:
        user_email = "kayıtlı_eposta_adresi"
        for user in MOCK_USERS:
            if user["username"] == email_or_username:
                user_email = user["email"]
                break

        st.sidebar.success(f" Kullanıcı şifresi sıfırlama linki '{user_email}' adresine gönderildi.")


# --- METİN OKUMA FONKSİYONU (SESLENDİRME) ---
def metin_oku(text):
    clean_text = text.replace('"', '').replace('\n', ' ')
    js_code = f"""
    <script>
        var utterance = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(utterance);
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)


# --- SOHBET VE ÇEVİRİ MANTIKLARI ---
basit_sozluk = {
    "merhaba": "Hello", "selam": "Hi", "teşekkürler": "Thanks", "sağol": "Thanks",
    "elma": "Apple", "armut": "Pear", "kedi": "Cat", "köpek": "Dog",
    "apple": "Elma", "pear": "Armut", "cat": "Kedi", "dog": "Köpek",
    "again": "Tekrar / Yine",
    "teach": "Öğretmek", "study": "Çalışmak", "kitap": "Book", "kalem": "Pen"
}

def general_chat_kanka(kullanici_mesaji):
    mesaj_lower = kullanici_mesaji.lower().strip()

    # Kanka Sohbeti Mantığı
    if "merhaba" in mesaj_lower or "selam" in mesaj_lower or "kanka" in mesaj_lower:
        cevap = "Selam! Ben senin yapay zeka kankanım. Ders mi çalışalım yoksa güncel bir konudan mı konuşalım?"
    elif "nasılsın" in mesaj_lower:
        cevap = "Çok iyi çalışıyorum, teşekkür ederim! Peki sen nasılsın, dersler nasıl gidiyor?"
    elif "teşekkür" in mesaj_lower or "sağol" in mesaj_lower:
        cevap = "Rica ederim, ne zaman istersen buradayım!"
    elif "ders" in mesaj_lower or "çalışmak" in mesaj_lower or "ödev" in mesaj_lower:
        cevap = "Harika! Hangi dersle ilgili bir sorunun var? Veya hangi konudan başlayayım?"
    else:
        cevap = f"Anladım, '{kullanici_mesaji}' ilginç bir konu! Ama biliyorsun, benim uzmanlık alanım eğitim. Ders kartlarından birini seçerek ilerleyelim mi?"

    return cevap

def instant_translate(kelime_veya_cumle):
    mesaj_lower = kelime_veya_cumle.lower().strip()

    if mesaj_lower in basit_sozluk: # Türkçe'den İngilizce'ye
         return f"'{kelime_veya_cumle.title()}' kelimesinin İngilizce karşılığı: **{basit_sozluk[mesaj_lower]}**."
    elif mesaj_lower in [v.lower() for v in basit_sozluk.values()]: # İngilizce'den Türkçe'ye
        tr_karsilik = next(k for k, v in basit_sozluk.items() if v.lower() == mesaj_lower)
        return f"'{kelime_veya_cumle.title()}' kelimesinin Türkçe karşılığı: **{tr_karsilik}**."
    else:
        # Google Translate Simülasyonu
        return f"'{kelime_veya_cumle}' ifadesi için hazır çeviri bulamadım. Bu uzunluğu çevirmek için gerçek bir dil modeline ihtiyacım var. (Simülasyon)"

# --- TEMA RENGİ VE MÜZİK KONTROLÜ ---
app_color_display = st.session_state.get('app_color', '#1E90FF') 

# CSS ile Başlık ve Vurgu Rengini Ayarlama
if st.session_state['admin_mode']:
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: {st.session_state["app_color"]};}}</style>', unsafe_allow_html=True)
else:
    # Öğrenci modunda başlık rengini kontrast için beyaz yapalım
    st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)


# --- MÜZİK ÇALMA MANTIĞI (Yönetici açarsa uygulama genelinde çalar) ---
if st.session_state['music_enabled'] and st.session_state['music_url']:
    # HTML audio etiketi ile arkaplan müziği çalma
    st.markdown(f"""
        <audio autoplay loop>
          <source src="{st.session_state['music_url']}" type="audio/mp3">
          Tarayıcınız ses çalmayı desteklemiyor.
        </audio>
        """,
        unsafe_allow_html=True
    )
    # Öğrenci modunda çalma uyarısı
    if not st.session_state['admin_mode']:
        st.info("🎵 Sitemizin fon müziği çalıyor! (Sesi kısabilirsiniz)")
# --------------------------------------------------

# --- ANA ROBOT GÖVDESİ ---
st.title("📚 Çok Dersli Eğitim Robotu")

# SADECE ÖĞRENCİ MODUNDA İSE GÖSTER
if not st.session_state['admin_mode']:

    # 2. KARŞILAMA VE DUYURU
    st.markdown("---")
    # Duyuru Mesajı Rengine Göre Kutu Çizdirme
    if st.session_state['announcement_color'] == 'warning':
        st.warning(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'info':
        st.info(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'success':
        st.success(f"📣 DUYURU: {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'error':
        st.error(f"📣 DUYURU: {st.session_state['announcement']}")

    # Renkli Karşılama Mesajı
    st.markdown(f"✨ Merhaba! Ben sizin <span style='color:{app_color_display}'>kişisel eğitim robotunuz</span>.", unsafe_allow_html=True)
    st.markdown("Aşağıdan dersinizi ve yapmak istediğiniz işlemi seçerek hemen bilgi almaya başlayın.")
    st.markdown("---")


    # 3. DERS SEÇİMİ (KARTLAR ŞEKLİNDE)
    st.header("📚 Ders Seçimi")

    # 4'erli iki satır oluşturuyoruz.
    col_din, col_fen, col_eng, col_mat = st.columns(4)
    col_tarih, col_tr, col_cevir, col_bos = st.columns(4)

    DERSLER = [
        {"isim": "Din Kültürü", "simgesi": "🕌", "kolon": col_din},
        {"isim": "Fen Bilimleri", "simgesi": "🔬", "kolon": col_fen},
        {"isim": "İngilizce", "simgesi": "🇬🇧", "kolon": col_eng},
        {"isim": "Matematik", "simgesi": "📐", "kolon": col_mat},
        {"isim": "Tarih", "simgesi": "🏛️", "kolon": col_tarih},
        {"isim": "Türkçe", "simgesi": "🇹🇷", "kolon": col_tr},
        {"isim": "Anlık Çeviri", "simgesi": "🔄", "kolon": col_cevir},
    ]

    # Ders Kartlarını Çizdirme
    for ders in DERSLER:
        with ders["kolon"]:
            if st.button(f"{ders['simgesi']} {ders['isim']}", key=f"btn_{ders['isim']}", use_container_width=True):
                st.session_state['secilen_ders'] = ders['isim']
                st.rerun()

    st.markdown("---")

    secilen_ders = st.session_state['secilen_ders']

    if secilen_ders:
        st.subheader(f"✅ Seçili İşlem: {secilen_ders}")

        # ANLIK ÇEVİRİ MODU
        if secilen_ders == "Anlık Çeviri":
            st.header("🔄 Anlık Kelime ve Kısa Cümle Çevirisi")
            st.info("Türkçe veya İngilizce bir kelime/kısa cümle girin, anında çevireyim. (Basit Sözlük Simülasyonu)")

            cevirilecek_metin = st.text_input("Çevirilecek Kelime/Cümle:")
            if st.button("Çevir"):
                if cevirilecek_metin:
                    cevap = instant_translate(cevirilecek_metin)
                    st.success(cevap)
                else:
                    st.error("Lütfen çevrilecek bir kelime veya cümle giriniz.")


        # DERS İŞLEM MODU
        else:
            islem_modu = st.radio(
                "Şimdi yapmak istediğiniz işlemi seçin:",
                ("Detaylı Konu Anlatımı", "Soru Çözümü", "Kelime Bilgisi"),
                horizontal=True
            )

            konu_adi = st.text_input(f"Aradığınız Konu Adını veya Soruyu Giriniz:")

            if st.button("Başlat"):
                if konu_adi:

                    konu_adi_lower = konu_adi.lower().strip()
                    konu_icerigi = "Üzgünüm, aradığınız konuyu/kelimeyi bulamadım."

                    # --- ANA MANTIK (Fonksiyon Çağrıları) ---
                    if islem_modu == "Kelime Bilgisi":
                        if secilen_ders == "Türkçe":
                            konu_icerigi = konuyu_bul_eng(konu_adi_lower)
                        elif secilen_ders == "İngilizce":
                            konu_icerigi = konuyu_bul_tr(konu_adi_lower)
                        else:
                            st.warning("Bu mod sadece Türkçe ve İngilizce derslerinde desteklenmektedir.")
                            konu_icerigi = "Geçersiz Mod Seçimi."

                    else:
                        if secilen_ders == "Türkçe":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_tr(konu_adi_lower)

                        elif secilen_ders == "İngilizce":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_eng(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_eng(konu_adi_lower)

                        elif secilen_ders == "Matematik":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_math(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_math(konu_adi_lower)

                        elif secilen_ders == "Tarih":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_history(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_history(konu_adi_lower)

                        elif secilen_ders == "Din Kültürü":
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_religion(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_religion(konu_adi_lower)

                        elif secilen_ders == "Fen Bilimleri":
                            st.warning("Fen Bilimleri içeriği Türkçe modülü ile simüle edilmiştir.")
                            if islem_modu == "Soru Çözümü":
                                konu_icerigi = soru_cozumu_yap_tr(konu_adi_lower)
                            else:
                                konu_icerigi = konuyu_bul_tr(konu_adi_lower)


                    # --- SONUÇ YAZDIRMA ---
                    if "Geçersiz Mod Seçimi" not in konu_icerigi:
                        st.success(f"İşte '{konu_adi.upper()}' için cevap/açıklama:")

                        # Konuşma Özelliği (Metin Okuma)
                        col_yazi, col_ses = st.columns([4, 1])
                        with col_yazi:
                            st.markdown(konu_icerigi)
                        with col_ses:
                            if st.button("🎤 Seslendir", key="seslendir_konu_anlatimi"):
                                metin_oku(konu_icerigi)

                    else:
                        st.warning(konu_icerigi)

                else:
                    st.error("Lütfen bir konu adı veya kelime giriniz.")

    # 4. KANKA CHATBOTU (Floating Chat Özelliği)
    kanka_toggle_js = f"""
<div style='position: fixed; right: 20px; bottom: 20px; z-index: 9999;'>
    <button onclick="parent.window.location.href = '?show_kanka_chat={not st.session_state['show_kanka_chat']}'"
            style="background-color: #FFC000; color: black; border: none; padding: 10px 15px; border-radius: 25px; box-shadow: 2px 2px 5px rgba(0,0,0,0.5); font-weight: bold; cursor: pointer;">
        🤖 KANKA'ya Sor
    </button>
</div>
"""

    if not st.session_state['admin_mode']:
        st.markdown(kanka_toggle_js, unsafe_allow_html=True)

    # Kanka Chat'i açma/kapama mantığı (URL'den kontrol)
    if 'show_kanka_chat' in st.query_params:
        try:
            st.session_state['show_kanka_chat'] = st.query_params['show_kanka_chat'].lower() == 'true'
        except:
            st.session_state['show_kanka_chat'] = False

    if st.session_state['show_kanka_chat']:
        st.header("💬 KANKA Sohbet Alanı")

        # Sohbet geçmişini çizdirme
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.markdown(chat["user"])
            with st.chat_message("robot"):
                col_yazi_chat, col_ses_chat = st.columns([4, 1])
                with col_yazi_chat:
                    st.markdown(chat["robot"])
                with col_ses_chat:
                    if st.button("🎤 Seslendir", key=f"seslendir_kanka_chat_{id(chat)}"):
                        metin_oku(chat["robot"])

        kanka_mesaji = st.chat_input("Kanka'ya mesajınızı girin:", key="kanka_chat_input")

        if kanka_mesaji:
            robot_cevap = general_chat_kanka(kanka_mesaji)
            st.session_state.chat_history.append({"user": kanka_mesaji, "robot": robot_cevap})
            st.rerun()

        if st.session_state.chat_history and st.button("Kanka Sohbetini Temizle"):
            st.session_state.chat_history = []
            st.rerun()

    st.markdown("---")

# --- YÖNETİCİ GİRİŞİ (SIDEBAR) ---
st.sidebar.title("Kullanıcı İşlemleri")

# Yönetici Girişi ve Ayarlar
if st.session_state['admin_mode']:
    st.sidebar.subheader("⚙️ Yönetici Ayarları")

    # TEMA RENGİ DEĞİŞTİRME
    new_color = st.sidebar.color_picker(
        "Uygulama Tema Rengini Seçin:", 
        st.session_state['app_color']
    )
    if new_color != st.session_state['app_color']:
        st.session_state['app_color'] = new_color
        st.rerun()
    
    # MÜZİK KONTROLÜ (URL ile şarkı açma özelliği)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎶 Müzik ve Ses Ayarları (URL ile)")
    
    MUSIC_OPTIONS = {
        "Ders Çalışma Müzik 1 (Varsayılan)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Piyano Melodisi": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Özel Şarkı Linki Gir": "CUSTOM_URL", 
        "Müzik Kapalı": ""
    }

    yeni_music_izin = st.sidebar.checkbox("Fon Müziğini Aç", st.session_state['music_enabled'])
    if yeni_music_izin != st.session_state['music_enabled']:
        st.session_state['music_enabled'] = yeni_music_izin
        st.rerun()

    secilen_sarki_adi = st.sidebar.selectbox(
        "Çalınacak Şarkıyı Seçin:",
        options=list(MUSIC_OPTIONS.keys())
    )
    
    yeni_url = MUSIC_OPTIONS[secilen_sarki_adi]
    
    if secilen_sarki_adi == "Özel Şarkı Linki Gir":
        custom_url_input = st.sidebar.text_input("Şarkınızın MP3 Linkini Buraya Yapıştırın:", key="custom_music_url_input", value=st.session_state['music_url'] if st.session_state['music_url'] not in MUSIC_OPTIONS.values() else "")
        if custom_url_input:
             yeni_url = custom_url_input
        else:
             st.sidebar.warning("Lütfen geçerli bir MP3 linki girin.")
             yeni_url = ""

    if yeni_url != st.session_state['music_url']:
        st.session_state['music_url'] = yeni_url
        if st.session_state['music_enabled']:
             st.rerun()
        
    st.sidebar.caption("Müzik açıldığında, hem yönetici hem de öğrenci modunda çalacaktır.")
    st.sidebar.markdown("---")

    # DUYURU AYARLARI
    st.sidebar.subheader("📢 Duyuru Paneli")
    new_announcement = st.sidebar.text_area("Duyuru Metni:", value=st.session_state['announcement'])
    new_announcement_color = st.sidebar.selectbox("Duyuru Kutusu Rengi:", ["warning", "info", "success", "error"], index=["warning", "info", "success", "error"].index(st.session_state['announcement_color']))
    if new_announcement != st.session_state['announcement'] or new_announcement_color != st.session_state['announcement_color']:
        st.session_state['announcement'] = new_announcement
        st.session_state['announcement_color'] = new_announcement_color
        st.rerun()
    
    # SİSTEM KONTROLLERİ
    st.sidebar.subheader("🚨 Sistem Kontrolleri")
    st.session_state['registration_allowed'] = st.sidebar.checkbox("Üye Kaydı Açık", st.session_state['registration_allowed'])
    st.session_state['user_login_allowed'] = st.sidebar.checkbox("Üye Girişi Açık", st.session_state['user_login_allowed'])

    st.sidebar.markdown("---")
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=admin_logout)
else:
    # Öğrenci Modunda Yönetici Giriş Butonu
    st.sidebar.button("🔒 Yönetici Girişi", on_click=toggle_admin_login_panel)

    # YÖNETİCİ GİRİŞ FORMU
    if st.session_state['show_admin_login']:
        with st.sidebar.form("admin_login_form"):
            admin_pass = st.text_input("Yönetici Şifresi", type="password", key="admin_pass_input")
            col1, col2 = st.columns(2)
            with col1:
                st.form_submit_button("Giriş Yap", on_click=attempt_admin_login, args=(admin_pass,))
            with col2:
                if st.form_submit_button("Şifremi Unuttum"):
                    forgot_password_simulation("Yönetici Mail Adresi", is_admin=True)

# Üye Girişi ve Kayıt Simülasyonu
if st.session_state['user_logged_in']:
    st.sidebar.success(f"Giriş Yapıldı: {st.session_state['current_user'].upper()}")
    st.sidebar.button("🚪 Üye Çıkışı", on_click=user_logout)
else:
    # ÜYE GİRİŞİ BUTONU VE FORMU
    st.sidebar.button("👤 Üye Girişi", on_click=toggle_user_login_panel)
    if st.session_state['show_user_login']:
        with st.sidebar.form("user_login_form"):
            user_name = st.text_input("Kullanıcı Adı")
            user_pass = st.text_input("Şifre", type="password")
            col1, col2 = st.columns(2)
            with col1:
                st.form_submit_button("Giriş Yap", on_click=user_login, args=(user_name, user_pass))
            with col2:
                if st.form_submit_button("Şifremi Unuttum"):
                     forgot_password_simulation(user_name or "Bilinmiyor", is_admin=False)
        st.sidebar.caption("Demo Hesaplar: ali/a123, ayse/a456")

    # ÜYE KAYIT BUTONU VE FORMU
    if st.session_state['registration_allowed']:
        st.sidebar.button("📝 Kaydol", on_click=toggle_user_register_panel)
        if st.session_state['show_user_register']:
            with st.sidebar.form("user_register_form"):
                reg_user = st.text_input("Kullanıcı Adı (Kaydol)")
                reg_email = st.text_input("E-posta Adresi")
                reg_pass = st.text_input("Şifre Belirle", type="password")
                if st.form_submit_button("Hesap Oluştur (Simülasyon)"):
                    st.info(f"Kayıt işlemi başarıyla simüle edildi! Lütfen giriş yapın.")
                    st.session_state['show_user_register'] = False
                    st.rerun()
    else:
        st.sidebar.error("Yeni kayıtlar şu anda kapalıdır.")

st.sidebar.markdown("---")
st.sidebar.title("⭐ Geri Bildirim")

# Geri bildirim formu
with st.sidebar.form("geri_bildirim_formu", clear_on_submit=True):
    st.sidebar.write("Uygulamayı geliştirmemiz için bize düşüncelerinizi gönderin.")
    feedback_konu = st.selectbox("Konu:", ["Genel Öneri", "Hata Bildirimi", "Yeni Ders İsteği", "Teşekkür"])
    feedback_mesaj = st.text_area("Mesajınız:")

    submitted = st.form_submit_button("Gönder")
    if submitted:
        st.sidebar.success(f"Geri bildiriminiz başarıyla iletildi! Konu: {feedback_konu}")

st.sidebar.markdown("---")
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin")

# --- SAYFA ALTI BİLGİ VE DURUM ÇUBUĞU ---
st.markdown("---")
st.caption(f"© 2024 Çok Dersli Eğitim Robotu - Geliştirici: Yusuf Efe Şahin")
st.markdown(f"API Durumu: 🟢 Aktif | Versiyon: 2.0 (Yeni ve Temiz Kurulum)")

col_tech, col_stats = st.columns([1, 1])

with col_tech:
    st.markdown("Kullanılan Teknoloji: **Streamlit, Python, Session State**")

with col_stats:
    st.progress(95, text="Uygulama Hazırlık Oranı: %95 (Tüm Modüller Tamam)")