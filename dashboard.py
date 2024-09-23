# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data (assuming you have already cleaned these)
order_items_clean = pd.read_csv('order_items_clean.csv')  # Path to your cleaned data
order_payments_clean = pd.read_csv('order_payments_clean.csv')  # Path to your cleaned data

# Streamlit Application Title
st.title("E-Commerce Data Analysis")

# Section 1: Data Display
st.subheader("Dataset Order Items - Cleaned")
st.write(order_items_clean.head())

st.subheader("Dataset Order Payments - Cleaned")
st.write(order_payments_clean.head())

# Section 2: Question 1 - Price vs Freight Value Correlation
st.subheader("Pertanyaan 1: Apakah terdapat hubungan antara harga produk dan biaya pengiriman?")

# Calculate correlation
correlation = order_items_clean[['price', 'freight_value']].corr()
st.write("Korelasi antara harga dan biaya pengiriman:", correlation)

# Scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='price', y='freight_value', data=order_items_clean, color='#2ecc71', ax=ax)
plt.title("Hubungan antara Harga Produk dan Biaya Pengiriman")
plt.xlabel("Harga Produk")
plt.ylabel("Biaya Pengiriman")
st.pyplot(fig)

# Insight for Question 1
st.write("Insight: Korelasi yang dihasilkan menunjukkan adanya hubungan yang kuat antara harga produk dan biaya pengiriman.")

# Section 3: Question 2 - Payment Method Distribution
st.subheader("Pertanyaan 2: Bagaimana distribusi metode pembayaran yang digunakan oleh pelanggan?")

# Payment method frequency
payment_method_freq = order_payments_clean['payment_type'].value_counts()
st.write("Frekuensi metode pembayaran:")
st.write(payment_method_freq)

# Bar plot for payment method distribution
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=payment_method_freq.index, y=payment_method_freq.values, color='#2ecc71', ax=ax)
plt.title("Distribusi Metode Pembayaran")
plt.xlabel("Metode Pembayaran")
plt.ylabel("Frekuensi")
st.pyplot(fig)

# Box plot with strip plot for payment value distribution
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='payment_type', y='payment_value', data=order_payments_clean, showfliers=False, color='#2ecc71', ax=ax)
sns.stripplot(x='payment_type', y='payment_value', data=order_payments_clean, jitter=True, color='#2ecc71', alpha=0.6, ax=ax)
plt.title("Distribusi Nilai Pembayaran per Metode Pembayaran")
plt.xlabel("Metode Pembayaran")
plt.ylabel("Nilai Pembayaran")
st.pyplot(fig)

# Insight for Question 2
st.write("Insight: Analisis ini menunjukkan bahwa metode pembayaran kartu kredit mendominasi transaksi dengan nilai yang lebih tinggi.")

# Section 4: Conclusion
st.subheader("Kesimpulan")
st.write("""
Dari hasil korelasi dan analisis, terdapat hubungan yang kuat antara harga produk dan biaya pengiriman. 
Korelasi ini menunjukkan bahwa produk dengan harga yang lebih tinggi cenderung memiliki biaya pengiriman yang lebih besar. 
Distribusi metode pembayaran juga mengindikasikan bahwa kartu kredit adalah metode yang paling sering digunakan, terutama untuk transaksi bernilai tinggi.
""")
