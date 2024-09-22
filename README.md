---

# Proyek Analisis Data: Dataset Publik E-Commerce 📊

Proyek ini adalah dashboard interaktif yang dikembangkan menggunakan **Streamlit** untuk menganalisis dataset e-commerce publik. Dashboard ini memungkinkan pengguna untuk menjawab pertanyaan bisnis kunci terkait sebaran penjual berdasarkan lokasi geografis dan visualisasi data yang terkait.

## Detail Proyek
- **Nama:** Indra Mauludani Efendi
- **Email:** [indramauludani09@gmail.com](mailto:indramauludani09@gmail.com)
- **ID Dicoding:** indramauludani14
- **Streamlit:** [https://proyeke-commercepublicdataset-tyfvuaglmp7h4i9nyjoiyr.streamlit.app/](https://proyeke-commercepublicdataset-tyfvuaglmp7h4i9nyjoiyr.streamlit.app/)

### Pertanyaan Bisnis
1. Bagaimana sebaran penjual berdasarkan kota?
2. Kota dan negara bagian mana yang memiliki jumlah penjual terbanyak?

## Fitur Utama
- **Visualisasi Distribusi Penjual Berdasarkan Kota**: Menggunakan *barplot* untuk menampilkan jumlah penjual per kota.
- **Analisis Distribusi Penjual Berdasarkan Kode Pos**: *Histogram* untuk melihat distribusi penjual di berbagai kode pos.
- **Pembersihan Data**: Deteksi dan penghapusan duplikat dan nilai-nilai yang hilang dari dataset.
- **Eksplorasi Data Lanjutan**: Visualisasi korelasi antar variabel menggunakan *heatmap*.

## Setup Environment

### Menggunakan Anaconda
1. Buat environment baru dengan Python 3.9:
   ```bash
   conda create --name proyek_ecommerce python=3.9
   ```
2. Aktifkan environment:
   ```bash
   conda activate proyek_ecommerce
   ```
3. Install dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

### Menggunakan Shell/Terminal
1. Buat folder proyek:
   ```bash
   mkdir proyek_ecommerce
   cd proyek_ecommerce
   ```
2. Inisialisasi virtual environment menggunakan **venv**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies dari file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi Streamlit
Setelah semua dependensi terinstall, Anda bisa menjalankan aplikasi dengan perintah berikut:

```bash
streamlit run dashboard.py
```

Aplikasi akan berjalan di browser dan bisa diakses melalui URL yang ditampilkan (biasanya `http://localhost:8501`).

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Framework untuk membuat aplikasi web berbasis data.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Seaborn & Matplotlib**: Untuk visualisasi data.

## Struktur Direktori
```plaintext
proyek_ecommerce/
│
├── Dashboard.py             # File utama aplikasi Streamlit
├── README.md              # File ini
├── requirements.txt       # Daftar dependensi Python
└── sellers_dataset.csv/   # Folder untuk menyimpan dataset (opsional)
└── Proyek_Analisis_Data
```

## Lisensi
Proyek ini tidak memiliki lisensi dan digunakan untuk keperluan edukasi.

--- 
