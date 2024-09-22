import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from io import StringIO  # Import StringIO

# Title of the Streamlit app
st.title("Proyek Analisis Data: E-Commerce Public Dataset")

st.markdown("""
- **Nama:** Indra Mauludani Efendi
- **Email:** Indramauludani09@gmail.com
- **ID Dicoding:** indramauludani14
""")

st.header("1. Menentukan Pertanyaan Bisnis")
st.markdown("""
- Bagaimana sebaran penjual berdasarkan kota?
- Kota dan negara bagian mana yang memiliki jumlah penjual terbanyak?
""")

## Data Wrangling

### Gathering Data
# Dataset path (update with the actual file path)
file_path = 'sellers_dataset.csv'

try:
    # Load the dataset
    data_penjual = pd.read_csv(file_path)

    # Display the dataset
    st.write("Data Penjual:")
    st.dataframe(data_penjual)

    ## Assessing Data
    st.subheader("Assessing Data")

    # Using StringIO to capture dataset information
    buffer = StringIO()
    data_penjual.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)  # Display the captured dataset information using Streamlit text element

    # Descriptive statistics
    st.subheader("Descriptive Statistics")
    st.write(data_penjual.describe())

    # Check for missing values and duplicates
    st.subheader("Checking Missing Values and Duplicates")
    missing_values = data_penjual.isnull().sum()
    st.write("Missing Values:", missing_values)
    duplicated_values = data_penjual.duplicated().sum()
    st.write("Duplicate Values:", duplicated_values)

    # Drop duplicates
    data_penjual = data_penjual.drop_duplicates()

    ## Exploratory Data Analysis (EDA)
    st.header("2. Exploratory Data Analysis (EDA)")

    # Visualize distribution of zip codes
    st.subheader("Distribusi Kode Pos Penjual")
    plt.figure(figsize=(10,6))
    sns.histplot(data_penjual['seller_zip_code_prefix'], bins=30, kde=True, color='blue')
    plt.title('Distribusi Kode Pos Penjual')
    plt.xlabel('Kode Pos')
    plt.ylabel('Jumlah Penjual')
    st.pyplot(plt)

    ## Pertanyaan 1:
    st.subheader("Pertanyaan 1: Bagaimana sebaran penjual berdasarkan kota?")

    # Count sellers per city
    city_distribution = data_penjual['seller_city'].value_counts().head(10)
    st.write(city_distribution)

    # Visualize distribution of sellers per city
    plt.figure(figsize=(10,6))
    sns.barplot(x=city_distribution.values, y=city_distribution.index, palette='viridis')
    plt.title('Top 10 Kota dengan Jumlah Penjual Terbanyak')
    plt.xlabel('Jumlah Penjual')
    plt.ylabel('Kota')
    st.pyplot(plt)

    ## Pertanyaan 2:
    st.subheader("Pertanyaan 2: Kota dan negara bagian mana yang memiliki jumlah penjual terbanyak?")

    # Combine city and state for analysis
    data_penjual['city_state'] = data_penjual['seller_city'] + ', ' + data_penjual['seller_state']
    city_state_distribution = data_penjual['city_state'].value_counts().head(10)
    st.write(city_state_distribution)

    # Visualize distribution of sellers by city and state
    plt.figure(figsize=(10,6))
    sns.barplot(x=city_state_distribution.values, y=city_state_distribution.index, palette='plasma')
    plt.title('Top 10 Kombinasi Kota dan Negara Bagian dengan Penjual Terbanyak')
    plt.xlabel('Jumlah Penjual')
    plt.ylabel('Kota, Negara Bagian')
    st.pyplot(plt)

    st.subheader("**Conclusion**")
    st.markdown("""
    - Sebaran penjual berdasarkan kota menunjukkan sebagian besar penjual berada di kota besar seperti Sao Paulo dan Rio de Janeiro.
    - Sao Paulo mendominasi sebagai kota dengan jumlah penjual terbanyak.
    """)

except FileNotFoundError:
    st.error("File dataset tidak ditemukan. Pastikan file berada pada jalur yang benar.")
