---

# Proyek Analisis Data: E-Commerce Public Dataset 📊

Proyek ini merupakan dashboard interaktif yang dibuat menggunakan **Streamlit** untuk melakukan analisis dataset e-commerce publik. Melalui aplikasi ini, Anda dapat menjawab beberapa pertanyaan bisnis terkait produk-produk dalam kategori yang berbeda, serta menampilkan visualisasi data yang relevan.

## Detail Proyek
- **Nama:** Indra Mauludani Efendi
- **Email:** indramauludani09@gmail.com
- **ID Dicoding:** indramauludani14

### Pertanyaan Bisnis
1. Apa saja kategori yang memiliki rata-rata produk terberat, dan seberapa besar pengaruh dimensi produk terhadap bobotnya?
2. Bagaimana korelasi panjang deskripsi produk dan jumlah foto produk dengan berat dan ukuran produk?

## Fitur Utama
- **Visualisasi Kategori Produk Berdasarkan Berat**: Menggunakan *boxplot* untuk menunjukkan distribusi berat produk per kategori.
- **Analisis Panjang Deskripsi vs Berat Produk**: *Scatter plot* untuk melihat hubungan antara panjang deskripsi produk dan beratnya.
- **Analisis Jumlah Foto vs Berat Produk**: *Scatter plot* untuk memvisualisasikan korelasi antara jumlah foto produk dan berat produk.
- **Pembersihan Data**: Deteksi dan penghapusan outlier pada kolom berat produk.
- **Eksplorasi Data**: Histogram dan boxplot untuk mengeksplorasi distribusi berat produk.

## Setup Environment

### Menggunakan Anaconda
1. Buat environment baru dengan Python 3.9:
   ```bash
   conda create --name main-ds python=3.9
   ```
2. Aktifkan environment:
   ```bash
   conda activate main-ds
   ```
3. Install dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

### Menggunakan Shell/Terminal
1. Buat folder proyek:
   ```bash
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   ```
2. Inisialisasi virtual environment menggunakan **Pipenv**:
   ```bash
   pipenv install
   pipenv shell
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

Aplikasi akan berjalan di browser, dan bisa diakses melalui URL yang ditampilkan (biasanya `http://localhost:8501`).

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Framework untuk membuat aplikasi web berbasis data.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Seaborn & Matplotlib**: Untuk visualisasi data.

## Struktur Direktori
```bash
proyek_analisis_data/
│
├── dashboard.py            # File utama aplikasi Streamlit
├── README.md               # File ini
├── requirements.txt        # Daftar dependensi Python
└── data/                   # Folder untuk menyimpan dataset (opsional)
```

## Lisensi
Proyek ini tidak memiliki lisensi dan digunakan untuk keperluan edukasi.

