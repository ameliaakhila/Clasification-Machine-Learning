# 🍎 Belajar Klasifikasi Apel

Aplikasi **machine learning berbasis Streamlit** untuk memprediksi **kualitas apel** berdasarkan karakteristik fisik dan lingkungan seperti diameter, berat, kadar gula, warna, asal daerah, serta musim panen.  
Sistem ini menggunakan model **Logistic Regression** yang telah dilatih untuk melakukan klasifikasi secara otomatis.

---

## 🚀 Fitur Utama
- **Prediksi kualitas apel** berdasarkan 6 parameter input.
- **Antarmuka interaktif** dengan tampilan **modern bertema biru lembut**.
- **Model Machine Learning** terintegrasi secara langsung.
- **Visual efek** seperti animasi balon setelah prediksi berhasil 🎈.
- **Desain responsif & clean** menggunakan CSS kustom Streamlit.

---

## 🧠 Algoritma yang Digunakan
Model yang digunakan adalah **Logistic Regression**, salah satu algoritma *supervised learning* yang cocok untuk klasifikasi biner atau multikelas.  
Tahapan pelatihan model mencakup:
1. **Preprocessing data** menggunakan:
   - `StandardScaler` untuk fitur numerik.
   - `OneHotEncoder` untuk kategori nominal.
   - `OrdinalEncoder` untuk kategori ordinal seperti warna apel.
2. **Training dan evaluasi model** menggunakan metrik:
   - *Accuracy Score*
   - *Classification Report*
   - *Confusion Matrix*
3. Model kemudian disimpan ke file `model_klasifikasi_apel.joblib`.

---

## 📊 Dataset
Dataset yang digunakan bernama **apel_balance_500.csv**, berisi data karakteristik apel dengan beberapa kolom utama:
- `diameter` — ukuran apel dalam cm  
- `berat` — berat apel dalam gram  
- `kadar_gula` — kadar gula dalam persen  
- `warna` — kategori warna apel (`hijau`, `kuning`, `merah`)  
- `asal_daerah` — wilayah asal panen  
- `musim_panen` — waktu panen (`kemarau`, `hujan`)  
- `kualitas` — label target (misalnya `baik` / `buruk`)

---

## 🧩 Struktur Proyek
```

📂 klasifikasi-apel
├── app_streamlit.py                 # Aplikasi utama Streamlit
├── model_klasifikasi_apel.joblib    # Model Logistic Regression tersimpan
├── apel_balance_500.csv             # Dataset utama
├── train_model.py                   # Script untuk pelatihan model
└── README.md                        # Dokumentasi proyek

````

---

## 💻 Cara Menjalankan Aplikasi

### 1️⃣ Persiapkan lingkungan
Pastikan kamu sudah menginstal **Python 3.9+**

```bash
pip install streamlit scikit-learn pandas joblib
````

### 2️⃣ Jalankan aplikasi

```bash
streamlit run app_streamlit.py
```

### 3️⃣ Buka di browser

Streamlit akan menampilkan link lokal seperti:

```
http://localhost:8501
```

---

## 🎨 Tampilan Aplikasi

Tampilan dibuat **minimalis dan profesional** dengan tema **biru lembut** serta elemen interaktif.
Input diletakkan di **sidebar**, sementara hasil prediksi muncul dalam **kartu hasil (card)** di tengah halaman.

---

## 🧾 Contoh Prediksi

Misalnya kamu memasukkan:

* Diameter: `8.5 cm`
* Berat: `180 g`
* Kadar Gula: `14%`
* Warna: `merah`
* Asal Daerah: `Jawa Barat`
* Musim Panen: `kemarau`

Maka sistem akan menampilkan hasil seperti:

> 🍏 Model memprediksi **BAIK** dengan tingkat keyakinan **92.35%**

---

## 👩‍💻 Teknologi yang Digunakan

* **Python 3**
* **Streamlit**
* **scikit-learn**
* **pandas**
* **joblib**

---

## ❤️ Kontributor

Dibuat dengan 💙 oleh **Yang Mulia Ratu**
Mahasiswi yang memadukan *data science* dan *desain estetika* menjadi sistem pembelajaran yang interaktif 🍎✨

---

## 📜 Lisensi

Proyek ini bersifat **open-source** dan dapat digunakan untuk pembelajaran atau pengembangan lanjutan.
Lisensi: [MIT License](LICENSE)
