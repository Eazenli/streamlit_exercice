import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(
    "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# Add the title
st.title("Automobile Data Analysis")
st.write("This application allows you to visualize correlations and distributions by regions.")

# Continent filtering
st.sidebar.header("Region Filter")
option = st.sidebar.radio("Select a region :", data['continent'].unique())

if option:
    st.write("______")
    st.subheader(f"Analysis for the region {option} : ")
    data_option = data[data["continent"] == option]
    st.dataframe(data_option)

    # Correlation Matrix
    st.write("### Correlation Matrix")
    plt.figure(figsize=(8, 6))
    sns.heatmap(data_option.corr(numeric_only=True),
                annot=True,
                center=0,
                cmap=sns.color_palette("vlag", as_cmap=True)
                )
    st.pyplot(plt.gcf())
    plt.clf()  # Close the figure after the display
    st.write("The heatmap shows the strength and direction of correlations between variables.\n"
             "\n Values close to 1 indicate strong positive correlation, while values close to -1 indicate strong negative correlation.")

    # Scatterplot
    st.write('___')
    select_x = st.selectbox("Select X-axis column:",
                            data_option.columns.tolist())
    select_y = st.selectbox("Select Y-axis column:",
                            data_option.columns.tolist())
    st.write(
        f"### Scatterplot Between Two Variables: {select_x} and {select_y}")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=data_option,
        x=select_x,
        y=select_y,
        color="lightcoral",
        alpha=0.5)
    st.pyplot(plt.gcf())
    plt.clf()
    # Histogram for a variable
    st.write('___')
    st.write("### Variable Distribution")
    variable = st.selectbox("Select a variable for the distribution histogram",
                            data_option.columns)
    plt.figure(figsize=(8, 6))
    sns.set(style="white")
    sns.histplot(data=data_option[variable],
                 kde=True, bins=20, color="lightcoral")
    st.pyplot(plt.gcf())
    plt.clf()  # Close the figure after the display
