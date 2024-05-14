
import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

warnings.filterwarnings("ignore", message="Trying to unpickle estimator")

st.set_page_config(page_title="Crop Prediction", page_icon="https://i.ibb.co/R6kwPmM/download.jpg", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
    loaded_model = pickle.load(open(modelfile, 'rb'))
    return loaded_model

# def set_bg_hack_url():    
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url("https://i.ibb.co/XC1c7tR/Picture1.jpg");
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

def main():
    # background image
    # set_bg_hack_url()
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:center;">  Crop Prediction using ML 🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
 

    col = st.columns(1)[0]

    with col:
        st.subheader("Find out the most suitable crop to grow in your farm 👨‍🌾")
    
        # Input fields for features
        N = st.number_input("**Nitrogen (10-200):**", 10, 200, step=1, format='%d', key='N')
        P = st.number_input("**Phosphorus (10-100):**", 10, 100, step=1, format='%d', key='P')
        K = st.number_input("**Potassium (10-450):**", 10, 450, step=1, format='%d', key='K')
        temp = st.number_input("**Temperature (10-35°C):**", 10, 35, format="%d", key='temp')
        humidity = st.number_input("**Humidity (30-60%):**", 30, 60, format="%d", key='humidity')
        ph = st.number_input("**Ph (5-8):**", 5.0, 8.0, format="%.2f", key='ph')
        rainfall = st.number_input("**Rainfall (30-290 cm):**", 30.0, 290.0, format="%.2f", key='rainfall')

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)
        
        crop_images = {
        "rice": "https://i.ibb.co/zGpNC8S/rice.jpg",
        "maize": "https://i.ibb.co/ZHS5HWy/maize.jpg",
        "wheat":"https://i.ibb.co/XkSD2vs/wheat.jpg",
        "millets":"https://i.ibb.co/stp3TwX/millet.jpg",
        "finger millets":"https://i.ibb.co/fX9x6z4/finger-m.jpg",
        "sorghum":"https://i.ibb.co/DMxhxwc/sorghum.jpg",
        "lady finger":"https://i.ibb.co/NYx2r0X/ladyf.jpg",
        "cauliflower":"https://i.ibb.co/W05pyt4/ca.jpg",
        "carrot":"https://i.ibb.co/b6trR9C/carot.jpg",
        "bottle gourd":"https://i.ibb.co/C1qhDYd/bg.jpg",
        "brinjal":"https://i.ibb.co/5sLbsJQ/binjal.jpg",
        "tomato":"https://i.ibb.co/m8C3Z15/tm.jpg",
        "chilli":"https://i.ibb.co/w7t8yWd/chilli.jpg",
        "papaya": "https://i.ibb.co/ZNvpLT4/papaya.jpg",
        "watermelon": "https://i.ibb.co/6Z7qz8W/watermelon.jpg",
        "banana": "https://i.ibb.co/WW3N4RV/banana.jpg",
        "yellow lentil":"https://i.ibb.co/MZZ7BzK/yl.jpg" ,
        "black lentil": "https://i.ibb.co/hLsBVQF/bl.jpg",
        "red lentil": "https://i.ibb.co/qBKbgB9/red-lentils.jpg",
        "groundnut":"https://i.ibb.co/88XvJpG/gn.jpg",
        "soyabean":"https://i.ibb.co/j6kTfnG/soyaben.jpg",
        "kidneybeans": "https://i.ibb.co/dKM2kHy/kb.jpg",
        "chickpea":"https://i.ibb.co/hc6z7Vh/ck.jpg",
        # Add more crop-image pairs as needed
            }
        
        if st.button('Predict'):
            loaded_model = load_model("E:\\Crop Prediction\\overall_model.pkl")
            prediction = loaded_model.predict(single_pred)
            col.markdown("<h2 style='color: black;'>Results 🔍</h2>", unsafe_allow_html=True)
            predicted_crop = prediction.item().title()
            col.markdown(f"<p style='font-size: 24px; color: black; font-weight: bold;'>{prediction.item().title()} are recommended by the A.I for your farm.</font>", unsafe_allow_html=True)
            if predicted_crop in crop_images:
                st.image(crop_images[predicted_crop], use_column_width=True, caption=predicted_crop)

            

    #code for html ☘️ 🌾 🌳 👨‍🌾  🍃
    hide_menu_style = """
    <style>
      
       
    .block-container {padding: 2rem 1rem 3rem;}
    
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
       <style>
   .block-container {padding: 2rem 1rem 3rem;}
        #MainMenu {visibility: hidden;}
     
      </style>
       """

st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()








