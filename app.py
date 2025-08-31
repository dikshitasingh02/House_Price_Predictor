import pandas as pd
import pickle as pk
import streamlit as st

# Load model & data
model = pk.load(open('D:/house_price_prediction/house_prediction_model.pkl', 'rb'))
data = pd.read_csv('D:/house_price_prediction/Cleaned_data.csv')

# Page config
st.set_page_config(page_title="🏠 Bangalore House Price Predictor", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .prediction-box {
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    label {
        font-weight: 500 !important;
        color: #2c3e50 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🏠 Bangalore House Price Predictor</div>", unsafe_allow_html=True)

# Layout for inputs
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        loc = st.selectbox('📍 Location', sorted(data['location'].unique()))
        sqft = st.number_input('📏 Total Sqft', min_value=300.0, step=50.0)
        beds = st.number_input('🛏️ Bedrooms', min_value=1, step=1)

    with col2:
        bath = st.number_input('🛁 Bathrooms', min_value=1, step=1)
        balc = st.number_input('🌿 Balconies', min_value=0, step=1)

# Predict button
if st.button('🔮 Predict Price', use_container_width=True):
    input_df = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                            columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])
    output = model.predict(input_df)
    price = round(output[0] * 100000, 2)

    # Prediction box
    st.markdown(f"""
        <div class='prediction-box'>
            <h3 style='text-align:center; color:#27ae60;'>Estimated Price</h3>
            <h2 style='text-align:center; color:#2c3e50;'>₹ {price:,.0f}</h2>
        </div>
    """, unsafe_allow_html=True)
