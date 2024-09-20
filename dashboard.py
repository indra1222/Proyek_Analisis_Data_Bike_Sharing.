import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title and project info using Streamlit
st.title('Proyek Analisis Data: E-Commerce Public Dataset')
st.write("""
- **Nama:** Indra Mauludani Efendi
- **Email:** indramauludani09@gmail.com
- **ID Dicoding:** indramauludani14
- **Pertanyaan Bisnis:**
   - Apa saja kategori yang memiliki rata-rata produk terberat, dan seberapa besar pengaruh dimensi produk terhadap bobotnya?
   - Bagaimana korelasi panjang deskripsi produk dan jumlah foto produk dengan berat dan ukuran produk?
""")

# Define the dataset
data = {
    'product_id': ["1e9e8ef04dbcff4541ed26657ea517e5", "3aa071139cb16b67ca9e5dea641aaa2f",
                   "96bd76ec8810374ed1b65e291975717f", "cef67bcfe19066a932b7673e239eb23d",
                   "9dc1a7de274444849c219cff195d0b71"],
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
df_cleaned = df.dropna().drop_duplicates()

# Visualizations
st.subheader('Distribusi Berat Produk per Kategori')
fig1, ax1 = plt.subplots()
sns.boxplot(x='product_category_name', y='product_weight_g', data=df_cleaned)
ax1.set_title('Distribusi Berat Produk per Kategori')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

st.subheader('Panjang Deskripsi Produk vs Berat Produk')
fig2, ax2 = plt.subplots()
sns.scatterplot(x='product_description_length', y='product_weight_g', hue='product_category_name', data=df_cleaned)
ax2.set_title('Panjang Deskripsi Produk vs Berat Produk')
st.pyplot(fig2)

st.subheader('Jumlah Foto Produk vs Berat Produk')
fig3, ax3 = plt.subplots()
sns.scatterplot(x='product_photos_qty', y='product_weight_g', hue='product_category_name', data=df_cleaned)
ax3.set_title('Jumlah Foto Produk vs Berat Produk')
st.pyplot(fig3)

# Conclusion Section
st.subheader('Kesimpulan')
st.write("""
- Kategori seperti **"esporte_lazer"** dan **"utilidades_domesticas"** cenderung memiliki produk yang lebih berat.
- Panjang deskripsi produk dan jumlah foto berkorelasi dengan berat produk, terutama untuk produk yang lebih besar.
""")

# Additional controls and widgets could be added here for interactive analysis
