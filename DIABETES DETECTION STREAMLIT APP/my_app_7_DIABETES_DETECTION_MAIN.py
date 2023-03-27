# ############################################### #
# ######### IMPORTING REQ PACKAGES ############## #
# ############################################### #
# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# Importing Mini Apps
from my_app_7_DIABETES_DETECTION_EDA_APP import run_eda_app
from my_app_7_DIABETES_DETECTION_ML_APP import run_ml_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage Diabetes Risk Detection </h1>
		<h4 style="color:white;text-align:center;"> ML Classifier </h4>
		</div>
		"""

desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource 
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Dataset
				- ML Section: ML Predictor App
			"""


def main():
    # st.title('Main App')
    stc.html(html_temp)

    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')
        st.write(desc_temp)
    elif choice =='EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()
    else:
        st.subheader('About')


if __name__ == '__main__':
    main()