import streamlit as st
from PIL import Image
import os
import base64

# Fungsi untuk memuat gambar dari path lokal
def muat_gambar(path_gambar):
    if os.path.exists(path_gambar):
        return Image.open(path_gambar)
    return None

# Fungsi untuk memutar musik dengan tag HTML
def putar_musik(file_audio):
    path_file_audio = file_audio
    with open(path_file_audio, "rb") as f:
        data = f.read()
        data_b64 = base64.b64encode(data).decode()
        html_audio = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{data_b64}" type="audio/mp3">
            Browser Anda tidak mendukung elemen audio.
        </audio>
        """
        st.markdown(html_audio, unsafe_allow_html=True)

st.set_page_config(page_title="Kejutan untuk Magdala", page_icon="🎂", layout="wide")

# Confetti animation CSS
st.markdown("""
<style>
    .confetti {
        position: absolute;
        top: 0;
        left: 50%;
        width: 10px;
        height: 10px;
        background-color: #ff6f91;
        border-radius: 50%;
        animation: confettiFall 5s infinite ease-in-out;
        animation-delay: calc(var(--i) * -0.3s);
    }

    @keyframes confettiFall {
        0% { transform: translateY(0) rotate(0); }
        100% { transform: translateY(100vh) rotate(720deg); }
    }
</style>
""", unsafe_allow_html=True)

# Add confetti elements in HTML
st.markdown("""
<div class="confetti" style="--i:1;"></div>
<div class="confetti" style="--i:2;"></div>
<div class="confetti" style="--i:3;"></div>
<div class="confetti" style="--i:4;"></div>
<div class="confetti" style="--i:5;"></div>
""", unsafe_allow_html=True)


# Gaya CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Raleway:wght@400;700&display=swap');

    body {
        background: #FFE0F7 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cg fill='%23FFB6C1' fill-opacity='0.4'%3E%3Cpath d='M10 0l5 20H5l5-20zM50 30a3 3 0 0 0 0-6 3 3 0 0 0 0 6zM0 60h40v4H0v-4zM0 52h30v4H0v-4zm20-16h20v4H20v-4zM0 48h40v4H0v-4zm60-22a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM40 38a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM70 38a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-30 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-30 4a5 5 0 0 0-10 0h10zm10 0a5 5 0 0 1-10 0h10zM60 0a5 5 0 0 0-10 0h10zm10 0a5 5 0 0 1-10 0h10zM60 50a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM70 50a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM20 0l5 20H15l5-20zm43 64v-4h-4v4h-4v4h4v4h4v-4h4v-4h-4z'/%3E%3C/g%3E%3C/svg%3E") !important;
        background-attachment: fixed !important;
    }
    .stApp {
        background: transparent !important;
    }
    .main {
        background: rgba(255, 235, 240, 0.9) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        padding: 30px !important;
        color: #e06f8b !important;
        border: 2px solid #ff6f91;
        box-shadow: 0 0 20px rgba(255, 112, 145, 0.5);
    }
    h1 {
        font-family: 'Pacifico', cursive !important;
        color: #ff4081 !important;
        text-shadow: 2px 2px 4px #ff77a9;
    }
    .font-besar {
        font-family: 'Raleway', sans-serif !important;
        font-size: 36px !important;
        font-weight: 700;
        color: #ffa07a;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .font-hasil {
        font-size: 28px !important;
        color: #f49ac2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background-color: #ff77a9;
        color: #fff;
        font-family: 'Pacifico', cursive !important;
        font-size: 24px;
        padding: 12px 30px;
        border-radius: 30px;
        border: 2px solid #ffa07a;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #ff4081;
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 20px rgba(255,112,145,0.4);
    }
    .kontainer-gambar {
        text-align: center;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
        100% {
            transform: scale(1);
        }
    }
    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-20px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    .balon {
        position: fixed;
        z-index: -1;
        animation: float 6s ease-in-out infinite;
    }
    .balon-1 { top: 10%; left: 10%; }
    .balon-2 { top: 20%; right: 20%; animation-delay: 1s; }
    .balon-3 { bottom: 15%; left: 15%; animation-delay: 2s; }
    .balon-4 { bottom: 25%; right: 10%; animation-delay: 3s; }
</style>
""", unsafe_allow_html=True)

# Tambahkan balon-balon sebagai elemen latar belakang
st.markdown("""
    <div class="balon balon-1">🎈</div>
    <div class="balon balon-2">🎉</div>
    <div class="balon balon-3">🎊</div>
    <div class="balon balon-4">🎁</div>
""", unsafe_allow_html=True)

# Inisialisasi state sesi
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1

def halaman_berikutnya():
    st.session_state.halaman += 1

def mulai_ulang():
    st.session_state.halaman = 1


def tampilkan_halaman_1():
    putar_musik(r'C:\autodidak\kado\audio.mp3')  # Putar musik di halaman 1
    st.markdown("<h1 class='animated-text' style='text-align: center; animation: pulse 2s infinite;'>🎉 Kejutan Spesial di Dalam 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<p class='font-besar' style='text-align: center;'>Apakah kamu siap untuk perjalanan ajaib?</p>", unsafe_allow_html=True)
    if st.button("Klik untuk Memulai"):
        halaman_berikutnya()

def tampilkan_halaman_2():
    putar_musik(r'C:\autodidak\kado\audio.mp3')  # Putar musik di halaman 2
    st.markdown("""
        <style>
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.6; }
                100% { opacity: 1; }
            }
            .judul {
                font-size: 40px;
                color: #ff69b4;
                font-family: 'Courier New', Courier, monospace;
                text-align: center;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .sub-judul {
                font-size: 30px;
                color: #ff4500;
                font-family: 'Lucida Handwriting', cursive;
                text-align: center;
                margin-bottom: 10px;
            }
            .animasi {
                font-size: 28px;
                color: #1e90ff;
                font-family: 'Comic Sans MS', cursive;
                text-align: center;
                animation: pulse 2s infinite;
                margin-bottom: 10px;
            }
            .isi {
                font-size: 20px;
                color: #000000;
                font-family: 'Arial', sans-serif;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='judul'>Hallo sayang💖</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-judul'>🎂Selamat Ulang Tahun ke-21 Yah!!!🎂</p>", unsafe_allow_html=True)
    st.markdown("<p class='animasi'>Magdala Nurrahma</p>", unsafe_allow_html=True)
    st.markdown("<p class='animasi'>09 September 2003</p>", unsafe_allow_html=True)
    st.markdown("<p class='isi'>Hari dimana dilahirkannya wanita tangguh dan hebat yang akan membawa kebahagiaan ke dunia ini.</p>", unsafe_allow_html=True)
    
    if st.button("Lanjut ke Ucapan"):
        halaman_berikutnya()



def tampilkan_halaman_3():
    putar_musik(r'C:\autodidak\kado\audio.mp3')  # Putar musik di halaman 3
    st.markdown("""
        <style>
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.6; }
                100% { opacity: 1; }
            }
            .judul {
                font-size: 38px;
                color: #6a0dad;
                font-family: 'Georgia', serif;
                text-align: center;
                font-weight: bold;
                margin-bottom: 20px;
                animation: pulse 2s infinite;
            }
            .ucapan {
                font-size: 24px;
                color: #2e8b57;
                font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
                text-align: center;
                margin-bottom: 20px;
                background-color: #f0f8ff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .penutup {
                font-size: 22px;
                color: #dc143c;
                font-family: 'Brush Script MT', cursive;
                text-align: center;
                margin-top: 20px;
                font-style: italic;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='judul'>✨ Doaku Untukmu ✨</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='ucapan'>
            Semoga di umur yang ke-21 ini diberikan umur yang panjang dan sehat selalu.
            Serta diikuti segala hal baik, baik itu pencapaian, rezeki, dan kesuksesan.
            Semoga kamu terus tumbuh, berkembang, dan menginspirasi orang-orang di sekitarmu.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='penutup'>~ Dariku yang selalu bersamamu</p>", unsafe_allow_html=True)

    if st.button("Lihat kejuatn terakhir!"):
        halaman_berikutnya()


def tampilkan_halaman_4():
    putar_musik(r'C:\autodidak\kado\audio.mp3')  # Putar musik di halaman 4
    st.markdown("""
        <style>
            .judul { font-size: 40px; color: #ff6347; text-align: center; font-weight: bold; animation: pulse 2s infinite; margin-bottom: 20px; }
            .ucapan { font-size: 26px; color: #4682b4; text-align: center; margin-bottom: 30px; }
            .caption { font-size: 32px; color: #ff1493; text-align: center; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='judul'>🌟 Kejutan Terakhir 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<p class='ucapan'>Terima kasih telah menjadi bagian dari perjalanan ini!</p>", unsafe_allow_html=True)
    
    gambar = muat_gambar(r'C:\autodidak\kado\foto.jpg')
    if gambar:
        st.image(gambar, use_column_width=True)
        st.markdown("<p class='caption'>I love you💓</p>", unsafe_allow_html=True)
    
    if st.button("Selesai"):
        st.write("Terima kasih telah menikmati kejutan ini!")
    
    if st.button("Mulai Ulang"):
        mulai_ulang()


# Logika untuk menampilkan halaman
if st.session_state.halaman == 1:
    tampilkan_halaman_1()
elif st.session_state.halaman == 2:
    tampilkan_halaman_2()
elif st.session_state.halaman == 3:
    tampilkan_halaman_3()
else:
    tampilkan_halaman_4()