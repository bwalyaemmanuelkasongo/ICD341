import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set up the page configuration
st.set_page_config(page_title="ICD 341 Dashboard", layout="wide")

# Main title and description
st.title("📊 Interactive Statistical Dashboard")
st.write("Welcome to the Lab 17 Streamlit Dashboard by Bwalya Kasongo (202403418).")

# Create a sidebar for user controls
st.sidebar.header("Dashboard Controls")
mean_input = st.sidebar.slider("Select Mean", min_value=0, max_value=100, value=50)
std_input = st.sidebar.slider("Select Standard Deviation", min_value=1, max_value=20, value=10)
sample_size = st.sidebar.number_input("Sample Size", min_value=10, max_value=1000, value=100)

# Generate data based on user input
np.random.seed(42) # Ensure reproducibility
data = np.random.normal(loc=mean_input, scale=std_input, size=sample_size)
df = pd.DataFrame(data, columns=["Values"])

# Create two columns for layout
col1, col2 = st.columns(2)

# Left column: Data Summary
with col1:
    st.subheader("Data Summary")
    st.write(df.describe())

# Right column: Histogram
with col2:
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(df["Values"], bins=20, edgecolor="black", color="skyblue")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)