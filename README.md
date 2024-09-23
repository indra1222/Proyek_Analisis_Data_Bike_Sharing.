**Proyek Analisis Data: Dataset Publik E-Commerce 📊**

Proyek ini adalah dashboard interaktif yang dikembangkan menggunakan Streamlit untuk menganalisis dataset e-commerce publik. Dashboard ini memungkinkan pengguna menjawab pertanyaan bisnis kunci terkait sebaran penjual berdasarkan lokasi geografis dan visualisasi data terkait.

### Detail Proyek
**Nama:** Indra Mauludani Efendi  
**Email:** indramauludani09@gmail.com  
**ID Dicoding:** indramauludani14  
**Streamlit:** [https://indramauludaniefendi.streamlit.app/](https://indramauludaniefendi.streamlit.app/)

### Pertanyaan Bisnis
1. Apakah terdapat hubungan antara harga produk (price) dan biaya pengiriman (freight_value)?
2. Bagaimana distribusi metode pembayaran yang digunakan oleh pelanggan, dan apakah metode pembayaran tertentu cenderung digunakan untuk transaksi dengan nilai yang lebih tinggi?

### Fitur Utama dan Penjelasannya

1. **Visualisasi Distribusi Penjual Berdasarkan Kota**  
   - **Penjelasan:**  
     Fitur ini menampilkan barplot yang menunjukkan jumlah penjual per kota. Anda dapat melihat kota-kota mana yang memiliki konsentrasi penjual terbanyak, yang dapat memberikan wawasan tentang lokasi geografis yang mendominasi penjualan.
   - **Implementasi di Streamlit:**
     ```python
     st.title('Distribusi Penjual Berdasarkan Kota')
     st.bar_chart(df['city'].value_counts())
     st.write('Grafik ini menunjukkan jumlah penjual di setiap kota.')
     ```

2. **Analisis Distribusi Penjual Berdasarkan Kode Pos**  
   - **Penjelasan:**  
     Fitur ini memberikan gambaran mengenai sebaran penjual berdasarkan kode pos. Histogram digunakan untuk melihat distribusi penjual di berbagai wilayah, yang dapat membantu dalam analisis lebih lanjut mengenai penetrasi pasar di area tertentu.
   - **Implementasi di Streamlit:**
     ```python
     st.title('Distribusi Penjual Berdasarkan Kode Pos')
     st.write('Histogram ini menunjukkan distribusi penjual di berbagai kode pos.')
     st.histogram(df['zip_code'], bins=50)
     ```

3. **Pembersihan Data**  
   - **Penjelasan:**  
     Pembersihan data dilakukan dengan menghapus duplikat dan nilai-nilai yang hilang. Ini adalah langkah penting dalam memastikan bahwa data yang digunakan untuk analisis bersih dan akurat. Dengan membersihkan data, kita dapat menghindari hasil analisis yang bias atau tidak tepat.
   - **Implementasi di Streamlit:**
     ```python
     st.write('Membersihkan data dengan menghapus duplikat dan nilai yang hilang...')
     df_cleaned = df.drop_duplicates().dropna()
     st.write('Data setelah pembersihan:', df_cleaned)
     ```

4. **Eksplorasi Data Lanjutan: Visualisasi Korelasi Antar Variabel**  
   - **Penjelasan:**  
     Fitur ini menggunakan heatmap untuk menampilkan korelasi antara variabel-variabel dalam dataset. Dengan visualisasi korelasi, pengguna dapat dengan cepat mengidentifikasi hubungan antara variabel, seperti hubungan antara harga produk dan biaya pengiriman.
   - **Implementasi di Streamlit:**
     ```python
     st.title('Korelasi Antar Variabel')
     correlation_matrix = df.corr()
     sns.heatmap(correlation_matrix, annot=True)
     st.pyplot()
     st.write('Heatmap di atas menunjukkan korelasi antar variabel dalam dataset.')
     ```

5. **Hubungan antara Harga Produk dan Biaya Pengiriman**  
   - **Penjelasan:**  
     Analisis ini mencari hubungan antara harga produk (`price`) dan biaya pengiriman (`freight_value`). Dengan melihat korelasi antara kedua variabel ini, kita dapat menyimpulkan apakah produk dengan harga lebih tinggi cenderung memiliki biaya pengiriman yang lebih tinggi.
   - **Implementasi di Streamlit:**
     ```python
     st.title('Hubungan antara Harga Produk dan Biaya Pengiriman')
     sns.scatterplot(x='price', y='freight_value', data=df)
     st.pyplot()
     st.write('Grafik ini menunjukkan hubungan antara harga produk dan biaya pengiriman.')
     ```

6. **Distribusi Metode Pembayaran**  
   - **Penjelasan:**  
     Fitur ini menganalisis distribusi metode pembayaran yang digunakan oleh pelanggan dan apakah metode pembayaran tertentu cenderung lebih sering digunakan untuk transaksi dengan nilai yang lebih tinggi. Analisis ini dapat memberikan wawasan tentang preferensi pelanggan dalam metode pembayaran dan hubungannya dengan nilai transaksi.
   - **Implementasi di Streamlit:**
     ```python
     st.title('Distribusi Metode Pembayaran')
     st.bar_chart(df['payment_method'].value_counts())
     st.write('Grafik ini menunjukkan distribusi metode pembayaran yang digunakan oleh pelanggan.')
     ```

### Setup Environment

#### Menggunakan Anaconda
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

#### Menggunakan Shell/Terminal
1. Buat folder proyek:
   ```bash
   mkdir proyek_ecommerce
   cd proyek_ecommerce
   ```
2. Inisialisasi virtual environment menggunakan `venv`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies dari file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Aplikasi Streamlit
Setelah semua dependensi terinstall, jalankan aplikasi dengan perintah berikut:
```bash
streamlit run dashboard.py
```
Aplikasi akan berjalan di browser dan bisa diakses melalui URL yang ditampilkan (biasanya `http://localhost:8501`).

### Teknologi yang Digunakan
- **Python:** Bahasa pemrograman utama.
- **Streamlit:** Framework untuk membuat aplikasi web berbasis data.
- **Pandas:** Untuk manipulasi dan analisis data.
- **Seaborn & Matplotlib:** Untuk visualisasi data.

### Struktur Direktori
```
proyek_ecommerce/
│
├── Dashboard.py            # File utama aplikasi Streamlit
├── README.md               # Dokumentasi proyek
├── requirements.txt        # Daftar dependensi Python
└── order_items_dataset.csv  # Dataset e-commerce (order items)
└── order_payment_dataset.csv # Dataset e-commerce (payment methods)
```

### Lisensi
Proyek ini tidak memiliki lisensi dan digunakan untuk keperluan edukasi.
