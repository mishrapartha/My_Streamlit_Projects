
# Core Pkgs
import streamlit as st
import pandas as pd

# Load Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

# Load Dataset
@st.cache
def  load_data(data):
    df = pd.read_csv(data)
    return df


def run_eda_app():
    st.subheader('Exploratory Data Analysis')
    # df = pd.read_csv('data/diabetes_data_upload.csv')
    df = load_data('data/diabetes_data_upload.csv')
    df_encoded = load_data('data/diabetes_data_upload_clean.csv')
    freq_df = load_data('data/freqdist_of_age_data.csv')
    submenu = st.sidebar.selectbox("SubMenu", ['Descriptive', 'Plots'])

    if submenu == 'Descriptive':
        st.subheader('Data (First 5 entries)')
        st.dataframe(df.head())

        with st.expander('Complete Data'):
            st.dataframe(df)

        with st.expander('Data Types'):
            st.dataframe(df.dtypes)

        with st.expander('Descriptive Summary'):
            st.dataframe(df_encoded.describe())

        with st.expander('Class Distribution'):
            st.dataframe(df['class'].value_counts())

        with st.expander('Gender Distribution'):
            st.dataframe(df['Gender'].value_counts())

    elif submenu == 'Plots':
        st.subheader('Plots')

        # Layouts
        col1, col2 = st.columns([2, 1])

        with col1:
            # Gender Distribution
            with st.expander('Dist Plot of Gender'):
                # # Using Seaborn
                # fig = plt.figure()
                # sns.countplot(df, x='Gender')
                # st.pyplot(fig)

                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                # st.dataframe(gen_df)

                # Using PLotly
                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)

             # Class Distribution
            with st.expander('Dist Plot for Class'):
                # Using Seaborn
                fig = plt.figure()
                sns.countplot(df, x='class')
                st.pyplot(fig)

        with col2:
            with st.expander('Gender Distribution Table'):
                st.dataframe(gen_df)
            with st.expander('Class Distribution Table'):
                st.dataframe(df['class'].value_counts())

        # Freq Distribution of Age
        with st.expander('Frequency Distribution of Age'):
            p2 = px.bar(freq_df, x='Age', y='count')
            st.plotly_chart(p2)

        # Outlier Detection of Age
        with st.expander('Outlier Detection Plot'):
            fig = plt.figure()
            plt.title("Outliers for Age")
            sns.boxplot(df, x='Age')
            st.pyplot(fig)

            p3 = px.box(df, x='Age', color='Gender', title='Gender-wise Outlier Analysis')
            st.plotly_chart(p3)

        with st.expander("Correlation Plot"):
            corr_matrix = df_encoded.corr()
            fig = plt.figure(figsize=(20, 10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)

            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4, use_container_width=True)