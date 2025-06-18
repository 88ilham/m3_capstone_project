import pandas as pd
import streamlit as st
import pickle
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="🏡 Daegu Apartment Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
/* Main container */
.css-18e3th9 {
    padding: 2rem;
    background-color: #fafafa;
}

/* Sidebar */
.css-1d391kg {
    background-color: #f0f8ff;
    padding: 1.5rem;
    border-radius: 10px;
}

/* Headers */
h1, h2, h3 {
    color: #5a67d8 !important;
    font-family: 'Arial Rounded MT Bold', sans-serif;
}

/* Input widgets */
.stNumberInput>div>div>input, .stSelectbox>div>div>select {
    font-size: 16px !important;
    border-radius: 8px !important;
    border: 1px solid #cbd5e0 !important;
}

/* Prediction highlight */
.highlight-box {
    background-color: #ebf8ff;
    border-left: 5px solid #4299e1;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* Buttons and interactive elements */
.stButton>button {
    background-color: #667eea;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    border: none;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #5a67d8;
}

/* Custom emoji styling */
.emoji-feature {
    font-size: 1.5rem;
    margin-right: 0.5rem;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

# Function to format currency
def format_currency(amount):
    return f"💰 {int(amount):,} ₩"

def load_header_image():
    return None

# Main function
def user_input_feature():
    # Sidebar header
    st.sidebar.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #5a67d8;'>🏠 Apartment Features</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Input features
    with st.sidebar.expander("🏡 Basic Information", expanded=True):
        size = st.number_input(
            label="📏 Total Area (sq ft)", 
            min_value=135, 
            max_value=2337, 
            value=500,
            help="Enter the total area of the apartment"
        )
        
        yearbuilt = st.selectbox(
            label="📅 Year Built", 
            options=(1978, 1980, 1985, 1986, 1992, 1993, 1997, 2003, 2005, 2006, 
                    2007, 2008, 2009, 2013, 2014, 2015),
            help="When was the building constructed?"
        )
        
        hallwaytype = st.selectbox(
            label="🚪 Hallway Type", 
            options=('Corridor', 'Mixed', 'Terraced'),
            help="Type of hallway in the building"
        )
    
    with st.sidebar.expander("📍 Location Features", expanded=True):
        timetosubway = st.selectbox(
            label="🚇 Time to Subway", 
            options=('0-5min', '5min~10min', '10min~15min', '15min~20min', 'no_bus_stop_nearby'),
            help="Walking distance to nearest subway"
        )
        
        subwaystation = st.selectbox(
            label="🚉 Nearest Station", 
            options=('Bangoge', 'Banwoldang', 'Chil-sung-market', 'Daegu', 
                    'Kyungbuk_uni_hospital', 'Myung-duk', 'Sin-nam', 'no_subway_nearby'),
            help="Closest subway station"
        )
    
    with st.sidebar.expander("🏢 Building Amenities", expanded=True):
        numoffacilities = st.selectbox(
            label="🏋️‍♀️ Facilities in Building", 
            options=(1, 2, 3, 4, 5, 7, 8, 9, 10),
            help="Number of amenities in the apartment complex"
        )
        
        numofarking = st.selectbox(
            label="🅿️ Parking Spaces", 
            options=(0, 18, 56, 76, 79, 108, 181, 184, 203, 218, 400, 475, 524, 536, 605, 798, 930, 1174, 1270, 1321),
            help="Available parking spots"
        )
    
    with st.sidebar.expander("🌆 Neighborhood", expanded=True):
        numofuni = st.selectbox(
            label="🎓 Nearby Universities", 
            options=(0,1,2,3,4,5),
            help="Number of universities in the area"
        )
        
        numofpuboffice = st.selectbox(
            label="🏛️ Public Offices", 
            options=(0,1,2,3,4,5,7),
            help="Number of government offices nearby"
        )
        
        numofotherfacilities = st.selectbox(
            label="🏪 Other Facilities", 
            options=(0,1,2,5),
            help="Additional neighborhood amenities"
        )
    
    # Create DataFrame with input features
    df = pd.DataFrame({
        'TimeToSubway': [timetosubway],
        'SubwayStation': [subwaystation],
        'N_FacilitiesNearBy(PublicOffice)': [numofpuboffice],
        'N_SchoolNearBy(University)': [numofuni],
        'N_Parkinglot(Basement)': [numofarking],
        'YearBuilt': [yearbuilt],
        'Size(sqf)': [size],
        'HallwayType': [hallwaytype],
        'N_FacilitiesInApt': [numoffacilities],
        'N_FacilitiesNearBy(ETC)': [numofotherfacilities]
    })
    
    return df

def main():
    """Main function"""
    # Title
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #5a67d8;'>🏡 Daegu Apartment Price Predictor</h1>
        <p style='font-size: 1.1rem; color: #ffffff;'>
        Discover the best value of your apartment's ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Collect user input
    df_customer = user_input_feature()
    
    # Prediction section
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #5a67d8;'>✨ Price Prediction ✨</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Load pre-trained model
    try:
        model_loaded = pickle.load(open('final_model.sav', 'rb'))
        
        # Make prediction
        predicted_price = model_loaded.predict(df_customer)[0]
        
        # Create columns for better layout
        col1, col2 = st.columns([1, 1.2])
        
        # Display input features
        with col1:
            st.markdown("""
            📋 Apartment Details</h3>
            </div>
            """, unsafe_allow_html=True)
            
            features_display = df_customer.transpose()
            features_display.columns = ['Value']
            st.dataframe(features_display, use_container_width=True,
                        height=min(500, 35 * len(features_display)))
        
        # Display prediction
        with col2:
            st.markdown(f"""
            <div class='highlight-box'>
                <div style='text-align: center;'>
                    <h3 style='margin-top: 0; color: #2b6cb0;'>Estimated Value</h3>
                    <h1 style='color: #2c5282; margin: 1rem 0;'>{format_currency(predicted_price)}</h1>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Model performance metrics
            st.markdown("""
            <div style='margin-top: 1.5rem;'>
                <h3 style='color: #4a5568;'>📊 Model Confidence</h3>
                <div style='display: flex; gap: 1rem; margin-top: 1rem;'>
                    <div style='flex: 1; background-color: #ebf8ff; padding: 1rem; border-radius: 8px;'>
                        <p style='margin: 0; font-weight: bold; color: #2b6cb0;'>Accuracy</p>
                        <p style='margin: 0.5rem 0 0; font-size: 1.2rem; color: #2b6cb0'>80.5%</p>  <!-- Changed color -->
                    </div>
                    <div style='flex: 1; background-color: #fff5f5; padding: 1rem; border-radius: 8px;'>
                        <p style='margin: 0; font-weight: bold; color: #c53030;'>Avg Error</p>
                        <p style='margin: 0.5rem 0 0; font-size: 1.2rem; color: #c53030'>±37,816 ₩</p>  <!-- Added color -->
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Disclaimer and additional info
        st.markdown("""
            <div style='border: 1px solid #718096; padding: 1rem; border-radius: 8px; margin-top: 1.5rem;'>
                <h3 style='color: #363942; margin-top: 0;'>💡 Disclaimer</h3>
                <ul style='color: #ffffff;'>
                    <li>This estimate is based on current market trends</li>
                    <li>For precise valuation, consult with local real estate experts</li>
                    <li>Prices may vary based on property condition and timing</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("""
        ❌ Oops! We couldn't find the prediction model. 
        Please make sure 'final_model.sav' is in the right place.
        """)
    except Exception as e:
        st.error(f"""
        🛑 Something went wrong!
        Error: {str(e)}
        """)

# Run the app
if __name__ == '__main__':
    main()
