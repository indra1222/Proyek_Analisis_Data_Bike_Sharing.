import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned datasets
order_items_clean = pd.read_csv('order_items_dataset.csv')  # Adjust the path to your dataset
order_payments_clean = pd.read_csv('order_payments_dataset.csv')  # Adjust the path to your dataset

# Title of the app
st.title('E-commerce Data Analysis')

# Introduction
st.markdown("""
This application provides insights into e-commerce data, focusing on two business questions:
1. Is there a relationship between product price and shipping cost?
2. What is the distribution of payment methods, and do certain payment methods tend to be used for higher-value transactions?
""")

# Sidebar for user selection
st.sidebar.header('Choose an analysis to display')

# Question 1: Correlation between price and freight_value
if st.sidebar.checkbox('Show Correlation between Product Price and Shipping Cost'):
    st.subheader('Relationship between Product Price and Shipping Cost')

    # Calculate correlation
    correlation = order_items_clean[['price', 'freight_value']].corr()
    st.write('Correlation matrix:')
    st.dataframe(correlation)

    # Scatter plot for price vs freight_value
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='price', y='freight_value', data=order_items_clean, color='#2ecc71')
    plt.title("Relationship between Product Price and Shipping Cost")
    plt.xlabel("Product Price")
    plt.ylabel("Shipping Cost")
    st.pyplot(plt)

    st.markdown(f"**Insight:** The correlation between product price and shipping cost is {correlation.loc['price', 'freight_value']:.2f}. A strong positive correlation suggests that higher-priced products often have higher shipping costs.")

# Question 2: Distribution of payment methods
if st.sidebar.checkbox('Show Payment Method Distribution'):
    st.subheader('Distribution of Payment Methods')

    # Payment method frequency
    payment_method_freq = order_payments_clean['payment_type'].value_counts()
    st.write('Frequency of Payment Methods:')
    st.dataframe(payment_method_freq)

    # Bar plot for payment method distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(x=payment_method_freq.index, y=payment_method_freq.values, color='#2ecc71')
    plt.title("Distribution of Payment Methods")
    plt.xlabel("Payment Method")
    plt.ylabel("Frequency")
    st.pyplot(plt)

    # Boxplot for payment value per payment method
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='payment_type', y='payment_value', data=order_payments_clean, showfliers=False, color='#2ecc71')
    sns.stripplot(x='payment_type', y='payment_value', data=order_payments_clean, jitter=True, color='#2ecc71', alpha=0.6)
    plt.title("Payment Value Distribution per Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Payment Value")
    st.pyplot(plt)

    st.markdown("**Insight:** The boxplot shows that high-value transactions tend to be done using credit cards. This information can help in targeting promotions for high-value transactions.")

# Display conclusion
st.subheader("Conclusion")
st.markdown("""
1. **Product Price vs Shipping Cost:** There is a strong positive correlation between product price and shipping cost. This suggests that higher-priced products tend to have higher shipping costs.
2. **Payment Method Preferences:** Credit card is the most frequently used payment method, and it is preferred for higher-value transactions. Offering more payment options like installment plans for credit cards could encourage customers to make larger purchases.
""")
