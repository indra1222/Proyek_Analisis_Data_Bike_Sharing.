# Install Streamlit if you haven't already
# !pip install streamlit

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to create scatter plot for price vs freight_value
def plot_price_vs_freight(order_items_clean):
    st.subheader("Korelasi antara Harga Produk dan Biaya Pengiriman")
    correlation = order_items_clean[['price', 'freight_value']].corr()
    st.write("Korelasi antara harga dan biaya pengiriman:")
    st.write(correlation)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='price', y='freight_value', data=order_items_clean, color='#2ecc71')
    plt.title("Hubungan antara Harga Produk dan Biaya Pengiriman")
    plt.xlabel("Harga Produk")
    plt.ylabel("Biaya Pengiriman")
    st.pyplot(plt)

# Function to plot payment method distribution
def plot_payment_methods(order_payments_clean):
    st.subheader("Distribusi Metode Pembayaran")
    
    payment_method_freq = order_payments_clean['payment_type'].value_counts()
    st.write("Frekuensi metode pembayaran:")
    st.write(payment_method_freq)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=payment_method_freq.index, y=payment_method_freq.values, color='#2ecc71')
    plt.title("Distribusi Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

# Function to plot box plot for payment values per payment method
def plot_payment_values(order_payments_clean):
    st.subheader("Distribusi Nilai Pembayaran per Metode Pembayaran")
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='payment_type', y='payment_value', data=order_payments_clean, showfliers=False, color='#2ecc71')
    sns.stripplot(x='payment_type', y='payment_value', data=order_payments_clean, jitter=True, color='#2ecc71', alpha=0.6)
    plt.title("Distribusi Nilai Pembayaran per Metode Pembayaran dengan Distribusi Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Nilai Pembayaran")
    st.pyplot(plt)

# Main function to build the dashboard
def main():
    st.title("Proyek Analisis Data: E-commerce Dataset")
    st.markdown("""
        **Nama:** Indra Mauludani Efendi  
        **Email:** IndraMauludani09@gmail.com  
        **ID Dicoding:** indramauludani14
    """)
    
    # Load the datasets (use the cleaned datasets directly)
    order_items_clean = pd.read_csv('order_items_clean.csv')  # Replace with actual dataset
    order_payments_clean = pd.read_csv('order_payments_clean.csv')  # Replace with actual dataset
    
    # Display datasets
    st.subheader("Dataset Order Items")
    st.write(order_items_clean.head())
    
    st.subheader("Dataset Order Payments")
    st.write(order_payments_clean.head())
    
    # Display descriptive statistics
    st.subheader("Statistik Deskriptif")
    st.write("Statistik Deskriptif untuk Order Items:")
    st.write(order_items_clean.describe())
    
    st.write("Statistik Deskriptif untuk Order Payments:")
    st.write(order_payments_clean.describe())
    
    # Show correlation plot for price and freight_value
    plot_price_vs_freight(order_items_clean)
    
    # Show payment method distribution
    plot_payment_methods(order_payments_clean)
    
    # Show payment values per method
    plot_payment_values(order_payments_clean)

if __name__ == '__main__':
    main()
