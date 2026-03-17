import streamlit as st
import pandas as pd
import joblib

# === Konfigurasi Halaman ===
st.set_page_config(
    page_title="Belajar Klasifikasi Apel",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# === CSS untuk tampilan clean & modern ===
st.markdown("""
    <style>
    /* Background lembut */
    .stApp {
        background: linear-gradient(145deg, #eaf3ff, #ffffff);
        color: #0d1a33;
        font-family: 'Poppins', sans-serif;
    }

    /* Judul */
    h1 {
        color: #003366;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    /* Subjudul / deskripsi */
    .subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #1a1a1a;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        border-right: 2px solid #cce0ff;
    }

    [data-testid="stSidebar"] h2 {
        color: #cce0ff;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Tombol Prediksi */
    div.stButton > button {
        background-color: #004080;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        width: 100%;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #0066cc;
        transform: scale(1.03);
    }

    /* Card Hasil */
    .result-card {
        background-color: #cce0ff;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        color: #003366;
        font-size: 1.25rem;
        font-weight: 600;
        box-shadow: 0px 4px 10px rgba(0, 64, 128, 0.15);
        margin-top: 20px;
        line-height: 1.7;
    }

    /* Footer */
    footer, .st-emotion-cache-17lntkn {
        text-align: center;
        font-size: 0.9rem;
        color: #336699;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# === Load Model ===
model = joblib.load("model_klasifikasi_apel.joblib")

# === Judul & Deskripsi ===
st.markdown("<h1>🍎 Belajar Klasifikasi Apel</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Aplikasi machine learning sederhana untuk memprediksi kualitas apel berdasarkan karakteristiknya.</p>", unsafe_allow_html=True)

# === Sidebar Input ===
st.sidebar.header("⚙️ Input Kriteria Apel")
diameter = st.sidebar.slider("Diameter (cm)", 5.0, 12.0, 8.0)
berat = st.sidebar.slider("Berat (gram)", 120.0, 300.0, 180.0)
kadar_gula = st.sidebar.slider("Kadar Gula (%)", 10.0, 18.0, 14.0)
warna = st.sidebar.selectbox("Warna", ["merah", "hijau", "kuning"])
asal_daerah = st.sidebar.selectbox("Asal Daerah", ["Jawa Barat", "Jawa Tengah", "Sumatera"])
musim_panen = st.sidebar.selectbox("Musim Panen", ["kemarau", "hujan"])

# === Tombol Prediksi ===
if st.button("🔍 Prediksi Kualitas Apel"):
    # Buat dataframe dari input user
    data_baru = pd.DataFrame(
        [[diameter, berat, kadar_gula, warna, asal_daerah, musim_panen]],
        columns=["diameter", "berat", "kadar_gula", "warna", "asal_daerah", "musim_panen"]
    )

    selected_columns = ["diameter", "berat", "kadar_gula", "warna", "asal_daerah", "musim_panen"]
    data_baru_selected = data_baru[selected_columns]

    # Prediksi
    prediksi = model.predict(data_baru_selected)[0]
    presentase = max(model.predict_proba(data_baru_selected)[0])

    # Tampilkan hasil dengan card rapi
    st.markdown(f"""
        <div class="result-card">
            🍏 <b>Prediksi:</b> {prediksi} <br>
            💡 <b>Tingkat Akurasi:</b> {presentase*100:.2f}%
        </div>
    """, unsafe_allow_html=True)
    st.balloons()

# === Footer ===
st.markdown("---")
st.markdown("<footer>💙 Dibuat dengan akal & logika by <b>Yang Mulia Ratu</b></footer>", unsafe_allow_html=True)
