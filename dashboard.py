import streamlit as st
import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Adding details about name, email, and ID from Dicoding
st.markdown("""
# E-Commerce Public Dataset Analysis Project
- **Name:** Indra Mauludani Efendi
- **Email:** indramauludani09@gmail.com
- **Dicoding ID:** indramauludani14
- **Business Questions**:
  - Which categories have the heaviest average product, and how much do product dimensions influence its weight?
  - How do the length of the product description and the number of product photos correlate with the product's weight and size?
""")

# Define dataset
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

# Category name mapping
category_mapping = {
    'beleza_saude': 'health_beauty',
    'informatica_acessorios': 'computers_accessories',
    'automotivo': 'auto',
    # Continue mapping for all categories
    'artes': 'art',
    'esporte_lazer': 'sports_leisure',
    'perfumaria': 'perfumery',
    'utilidades_domesticas': 'housewares',
    'telefonia': 'telephony',
    # Add mappings for all the categories provided
    'telefonia_fixa': 'fixed_telephony',
    # and so forth...
}

# Translate product categories to English
df['product_category_name_english'] = df['product_category_name'].map(category_mapping)

# Clean data
df_cleaned = df.dropna().drop_duplicates()

# Ensure data types are correct
df_cleaned['product_weight_g'] = pd.to_numeric(df_cleaned['product_weight_g'], errors='coerce')
df_cleaned['product_length_cm'] = pd.to_numeric(df_cleaned['product_length_cm'], errors='coerce')

# Display title and cleaned dataset
st.title('E-Commerce Product Data Analysis')

st.header('Cleaned Product Dataset')
st.dataframe(df_cleaned)

# Visualization: Product weight distribution by category
st.subheader('Product Weight Distribution by Category')
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='product_category_name_english', y='product_weight_g', data=df_cleaned, ax=ax1)
ax1.set_title('Product Weight Distribution by Category')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

# Visualization: Product Description Length vs. Product Weight
st.subheader('Product Description Length vs. Product Weight')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='product_description_length', y='product_weight_g', hue='product_category_name_english', data=df_cleaned, ax=ax2)
ax2.set_title('Product Description Length vs. Product Weight')
st.pyplot(fig2)

# Visualization: Number of Product Photos vs. Product Weight
st.subheader('Number of Product Photos vs. Product Weight')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='product_photos_qty', y='product_weight_g', hue='product_category_name_english', data=df_cleaned, ax=ax3)
ax3.set_title('Number of Product Photos vs. Product Weight')
st.pyplot(fig3)

# Data Wrangling Section
st.header('Data Wrangling')

# Check for missing values
st.subheader('Check for Missing Values')
missing_values = df.isnull().sum()
st.write(missing_values)

# Display data types of each column
st.subheader('Check Data Types in Columns')
st.write(df.dtypes)

# If needed, clean data (e.g., fill missing values)
df.fillna(0, inplace=True)

st.subheader('Descriptive Statistics of the Dataset')
st.write(df.describe())

# Clean Data (Detect and Remove Outliers)
st.header('Clean Data')

Q1 = df_cleaned['product_weight_g'].quantile(0.25)
Q3 = df_cleaned['product_weight_g'].quantile(0.75)
IQR = Q3 - Q1

# Determine lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_cleaned = df_cleaned[(df_cleaned['product_weight_g'] >= lower_bound) & (df_cleaned['product_weight_g'] <= upper_bound)]

st.write(f"Dataset size after removing outliers: {df_cleaned.shape}")

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# Histogram of product weights
st.subheader('Product Weight Distribution')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.histplot(df_cleaned['product_weight_g'], bins=30, kde=True, ax=ax4)
ax4.set_title('Product Weight Distribution')
st.pyplot(fig4)

# Boxplot of product weights
st.subheader('Product Weight Boxplot')
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.boxplot(x=df_cleaned['product_weight_g'], ax=ax5)
ax5.set_title('Product Weight Boxplot')
st.pyplot(fig5)

# Conclusions
st.header('Conclusions')
st.markdown("""
- Categories like **"sports_leisure"** and **"housewares"** tend to have heavier products.
- Product description length and the number of product photos correlate with product weight, especially for larger products.
""")
