import streamlit as st
import pandas as pd


# Tambahkan detail nama, email, dan ID Dicoding
st.markdown("""
# Proyek Analisis Data: E-Commerce Public Dataset
- **Nama:** [Indra Mauludani Efendi]
- **Email:** [Indramauludani09@gmail.com]
- **ID Dicoding:** [indramauludani14]
- **Pertanyaan bisnis** 
-   Apa saja kategori yang memiliki rata-rata produk terberat, dan seberapa besar pengaruh dimensi produk terhadap bobotnya?
-    Bagaimana korelasi panjang deskripsi produk dan jumlah foto produk dengan berat dan ukuran produk?
""")

# Definisikan dataset
data = {
    'product_id': ["1e9e8ef04dbcff4541ed26657ea517e5", "3aa071139cb16b67ca9e5dea641aaa2f", "96bd76ec8810374ed1b65e291975717f", "cef67bcfe19066a932b7673e239eb23d", "9dc1a7de274444849c219cff195d0b71"],
    'product_category_name': ['perfumaria', 'artes', 'esporte_lazer', 'bebes', 'utilidades_domesticas'],
    'product_name_length': [40, 44, 46, 27, 37],
    'product_description_length': [287, 276, 250, 261, 402],
    'product_photos_qty': [1, 1, 1, 1, 4],
    'product_weight_g': [225, 1000, 154, 371, 625],
    'product_length_cm': [16, 30, 18, 26, 20],
    'product_height_cm': [10, 18, 9, 4, 17],
    'product_width_cm': [14, 20, 15, 26, 13]
}

df = pd.DataFrame(data)

# Bersihkan data
df_cleaned = df.dropna().drop_duplicates()

# Pastikan tipe data sesuai
df_cleaned['product_weight_g'] = pd.to_numeric(df_cleaned['product_weight_g'], errors='coerce')
df_cleaned['product_length_cm'] = pd.to_numeric(df_cleaned['product_length_cm'], errors='coerce')

# Tampilkan judul dan dataset yang sudah dibersihkan
st.title('Analisis Data Produk E-Commerce')

st.header('Dataset Produk yang Sudah Dibersihkan')
st.dataframe(df_cleaned)

# Visualisasi distribusi berat produk per kategori
st.subheader('Distribusi Berat Produk per Kategori')
sns.set_style("whitegrid")
sns.boxplot(x='product_category_name', y='product_weight_g', data=df_cleaned)
st.pyplot()

# Visualisasi Panjang Deskripsi Produk vs Berat Produk
st.subheader('Panjang Deskripsi Produk vs Berat Produk')
sns.scatterplot(x='product_description_length', y='product_weight_g', hue='product_category_name', data=df_cleaned)
st.pyplot()

# Visualisasi Jumlah Foto Produk vs Berat Produk
st.subheader('Jumlah Foto Produk vs Berat Produk')
sns.scatterplot(x='product_photos_qty', y='product_weight_g', hue='product_category_name', data=df_cleaned)
st.pyplot()

# Data Wrangling Section
st.header('Data Wrangling')

# Cek apakah ada nilai yang hilang
st.subheader('Cek Nilai Hilang')
missing_values = df.isnull().sum()
st.write(missing_values)

# Tampilkan tipe data pada setiap kolom
st.subheader('Cek Tipe Data pada Kolom')
st.write(df.dtypes)

# Jika perlu, bersihkan data (contoh: mengisi nilai yang hilang)
df.fillna(0, inplace=True)

st.subheader('Statistik Deskriptif dari Dataset')
st.write(df.describe())

# Cleaning Data (Deteksi dan Hapus Outlier)
st.header('Cleaning Data')

Q1 = df_cleaned['product_weight_g'].quantile(0.25)
Q3 = df_cleaned['product_weight_g'].quantile(0.75)
IQR = Q3 - Q1

# Tentukan batas bawah dan atas
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Hapus outlier
df_cleaned = df_cleaned[(df_cleaned['product_weight_g'] >= lower_bound) & (df_cleaned['product_weight_g'] <= upper_bound)]

st.write(f"Ukuran dataset setelah menghapus outlier: {df_cleaned.shape}")

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# Histogram berat produk
st.subheader('Distribusi Berat Produk')
sns.histplot(df_cleaned['product_weight_g'], bins=30, kde=True)
st.pyplot()

# Boxplot berat produk
st.subheader('Boxplot Berat Produk')
sns.boxplot(x=df_cleaned['product_weight_g'])
st.pyplot()

# Kesimpulan
st.header('Kesimpulan')
st.markdown("""
- Kategori seperti **"esporte_lazer"** dan **"utilidades_domesticas"** cenderung memiliki produk yang lebih berat.
- Panjang deskripsi produk dan jumlah foto berkorelasi dengan berat produk, terutama untuk produk yang lebih besar.
""")
