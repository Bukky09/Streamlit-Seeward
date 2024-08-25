import streamlit as st

# Set the app title
st.title("Seeward Severity Score Calculator")
st.header('Input Values')
# Create input fields for the components
vulnerability_severity = st.number_input("Enter Vulnerability Severity (1-10):", min_value=1, max_value=10, step=1)
ease_of_resolution = st.number_input("Enter Ease of Resolution (1-10):", min_value=1, max_value=10, step=1)
exploit_difficulty = st.number_input("Enter Exploit Difficulty (1-10):", min_value=1, max_value=10, step=1)
epss = st.number_input("Enter EPSS (Exploit Prediction Scoring System) (1-10):", min_value=1, max_value=10, step=1)

# Set the weights for the components
st.sidebar.header("Set Weights")
weight_vs = st.sidebar.number_input("Enter Weight for Vulnerability Severity (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_er = st.sidebar.number_input("Enter Weight for Ease of Resolution (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_ed = st.sidebar.number_input("Enter Weight for Exploit Difficulty(0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_epss = st.sidebar.number_input("Enter Weight for EPSS (Exploit Prediction Scoring System) (0-1):", min_value=0.0, max_value=1.0, step=0.1)



# Calculate the Seeward Severity score when the button is clicked
if st.button("Calculate Seeward Severity"):
    seeward_severity = (vulnerability_severity * weight_vs) + (ease_of_resolution * weight_er) + (exploit_difficulty * weight_ed) + (epss * weight_epss)
    
    st.success(f"The Seeward Severity Score is: {seeward_severity:.2f}")


# Provide some guidance
st.subheader('INFORMATION')
if st.button('What is the Seeward Severity Score Formula ?'):

    st.write('Seeward Severity=(Vulnerability Severity x WeightVS) + (Ease of Resolution × WeightER) + (Exploit Difficulty x WeightED) + (EPSS * WeightEPSS).')
else:
    st.write('Click me to define Seeward Severity Score Formula.')
