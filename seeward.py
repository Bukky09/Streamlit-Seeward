import streamlit as st
import requests

# Set the app title
st.title("Seeward Severity Score Calculator")
st.header('Input Values')

# Set the weights for the components
st.sidebar.header(" Weights For Seeward Severity score")
weight_vs = st.sidebar.number_input("Enter Weight for Vulnerability Severity (1-10):", min_value=1, max_value=10, step=1)
weight_er = st.sidebar.number_input("Enter Weight for Ease of Resolution (1-10):", min_value=1, max_value=10, step=1)
weight_ed = st.sidebar.number_input("Enter Weight for Exploit Difficulty (1-10):", min_value=1, max_value=10, step=1)
weight_epss = st.sidebar.number_input("Enter Weight for EPSS (Exploit Prediction Scoring System) (1-10):", min_value=1, max_value=10, step=1)

# Create input fields for the components
st.subheader("Ease Of Resolution")
if st.button('What is the Ease of Resolution Formula ?'):
    st.write('Ease of Resolution = ((detection_time * weight_detection_time) + \
                                           (complexity_issue * weight_complexity_issue) + \
                                           (resource_availability * weight_resource_availability) + \
                                           (response_time * weight_response_time) + \
                                           (team_expertise * weight_team_expertise) + \
                                           (impact_on_systems * weight_impact_on_systems) + \
                                           (communication_efficiency * weight_communication_efficiency) + \
                                           (documentation_learning * weight_documentation_learning)')
else:
    st.write('Click me to define Ease of Resolution Score Formula.')
col_weights,col_factors =st.columns(2) 

with col_factors:
    st.write('Factors For Ease of Resolution') 
    response_time = st.number_input("Response Time:", min_value=1, max_value=10, step=1)
    team_expertise = st.number_input("Team Expertise:", min_value=1, max_value=10, step=1)
    impact_on_systems = st.number_input("Impact on Systems:", min_value=1, max_value=10, step=1)
    communication_efficiency = st.number_input("Communication Efficiency:", min_value=1, max_value=10, step=1)
    documentation_learning = st.number_input("Documentation and Learning:", min_value=1, max_value=10, step=1)
    detection_time =st.number_input('Detection time (Retrieve this from the CVE response):', min_value=5,max_value=5,step=1)
    complexity_issue = st.number_input('Complexity Issue (Retrieve this from the CVE response):', min_value=7,max_value=7,step=1)
    resource_availability =st.number_input('Resource Availability (Retrieve this from the CVE response):', min_value=8,max_value=8,step=1)
with col_weights:
    st.write('Weights For Ease of Resolution')
    weight_response_time = st.number_input("Response Time Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_team_expertise = st.number_input("Team Expertise Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_impact_on_systems = st.number_input("Impact on Systems Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_communication_efficiency = st.number_input("Communication Efficiency Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_documentation_learning = st.number_input("Documentation and Learning Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_detection_time = st.number_input("Detection Time Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_complexity_issue = st.number_input("Complexity of Issue Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_resource_availability = st.number_input("Resource Availability Weight (1-10):", min_value=1, max_value=10, step=1)

# Initialize session state for ease_of_resolution if not already set
if 'ease_of_resolution' not in st.session_state:
    st.session_state.ease_of_resolution = None

# Calculate the Ease of Resolution score when the button is clicked
if st.button("Calculate Ease Of Resolution"):
    st.session_state.ease_of_resolution = (detection_time * weight_detection_time) + \
                                           (complexity_issue * weight_complexity_issue) + \
                                           (resource_availability * weight_resource_availability) + \
                                           (response_time * weight_response_time) + \
                                           (team_expertise * weight_team_expertise) + \
                                           (impact_on_systems * weight_impact_on_systems) + \
                                           (communication_efficiency * weight_communication_efficiency) + \
                                           (documentation_learning * weight_documentation_learning)
    st.success(f"The Ease of Resolution Score is: {st.session_state.ease_of_resolution:.2f}")

st.subheader("Exploit Difficulty")
if st.button('What is the Exploit Difficulty Formula ?'):
    st.write('Exploit Difficulty = ((attack_vector * weight_attack_vector) + \
                                           (attack_complexity * weight_attack_complexity) + \
                                           (privileges_required * weight_privileges_required) + \
                                           (availability_of_exploit * weight_availability_of_exploit) + \
                                           (environmental_factors * weight_environmental_factors) + \
                                           (mitigations_defenses * weight_mitigations_defenses) + \
                                           (exploit_reliability * weight_exploit_reliability)')
else:
    st.write('Click me to define Exploit Difficulty Score Formula.')
# Display predefined values  
col_weights_ed, col_factors_ed = st.columns(2)
with col_factors_ed:
    st.write('Factors For Exploit Difficulty')
    st.number_input("Attack Vector (Retrieve this from the CVE response):", min_value=5,max_value=5,step=1)
    st.number_input("Attack Complexity (Retrieve this from the CVE response):", min_value=6,max_value=6,step=1)
    st.number_input("Privileges Required(Retrieve this from the CVE response):", min_value=7,max_value=7,step=1)
    st.number_input("Availability Of Exploit(Retrieve this from the CVE response):", min_value=5,max_value=5,step=1)
    st.number_input("Envi. Factors(Retrieve this from the CVE response):", min_value=7,max_value=7,step=1)
    st.number_input("Mitigations Defenses(Retrieve this from the CVE response):", min_value=8,max_value=8,step=1)
    st.number_input("Exploit Reliability( Retrieve this from the CVE response):", min_value=6,max_value=6,step=1)


attack_vector = 5
attack_complexity = 6
privileges_required = 7
availability_of_exploit = 5
environmental_factors = 7
mitigations_defenses = 8
exploit_reliability = 6

with col_weights_ed:
    st.write(" Weights For Exploit Difficulty")
    weight_attack_vector = st.number_input("Attack Vector Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_attack_complexity = st.number_input("Attack Complexity Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_privileges_required = st.number_input("Privileges Required Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_availability_of_exploit = st.number_input("Availability of Exploit Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_environmental_factors = st.number_input("Environmental Factors Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_mitigations_defenses = st.number_input("Mitigations and Defenses Weight (1-10):", min_value=1, max_value=10, step=1)
    weight_exploit_reliability = st.number_input("Exploit Reliability Weight (1-10):", min_value=1, max_value=10, step=1)

# Initialize session state for exploit_difficulty if not already set
if 'exploit_difficulty' not in st.session_state:
    st.session_state.exploit_difficulty = None

# Calculate the Exploit Difficulty score when the button is clicked
if st.button("Calculate Exploit Difficulty"):
    st.session_state.exploit_difficulty = (attack_vector * weight_attack_vector) + \
                                           (attack_complexity * weight_attack_complexity) + \
                                           (privileges_required * weight_privileges_required) + \
                                           (availability_of_exploit * weight_availability_of_exploit) + \
                                           (environmental_factors * weight_environmental_factors) + \
                                           (mitigations_defenses * weight_mitigations_defenses) + \
                                           (exploit_reliability * weight_exploit_reliability)
    st.success(f"The Exploit Difficulty Score is: {st.session_state.exploit_difficulty:.2f}")


st.subheader("Vulnerability Severity")

if st.button('What is the Vulnerability Severity Score Formula ?'):
    st.write('Vulnerability Severity = (cvss * weight_cvss) + \
                                               (affected_products_score * weight_affected_products_score) + \
                                               (recency_score * weight_recency_score) + \
                                               (age_score * weight_age_score) + \
                                               (exploit_weight * weight_exploit_weight)')
else:
    st.write('Click me to define Vulnerability Severity Score Formula.')

col_weights_vs, col_factors_vs = st.columns(2)

with col_factors_vs:
    st.write('Factors For Vulnerability Severity')
    st.number_input("CVSS Score( Retrieve this from the CVE response):", min_value=5,max_value=5,step=1)
    st.number_input("Affec. Prod. Score ( Retrieve this from the CVE response):", min_value=6,max_value=6,step=1)
    recency_score = st.number_input("Recency Score:", min_value=1, max_value=10, step=1)
    age_score = st.number_input("Age Score:", min_value=1, max_value=10, step=1)
    exploit_weight = st.number_input("Exploit Weight:", min_value=1, max_value=10, step=1)

cvss = 5
affected_products_score = 6

with col_weights_vs:
 st.write("Weights For Vulnerability Severity")
 weight_cvss = st.number_input("CVSS Score Weight (1-10):", min_value=1, max_value=10, step=1)
 weight_affected_products_score = st.number_input("Affected Products Score Weight (1-10):", min_value=1, max_value=10, step=1)
 weight_recency_score = st.number_input("Recency Score Weight (1-10):", min_value=1, max_value=10, step=1)
 weight_age_score = st.number_input("Age Score Weight (1-10):", min_value=1, max_value=10, step=1)
 weight_exploit_weight = st.number_input("Exploit Weight Weight (1-10):", min_value=1, max_value=10, step=1)

# Initialize session state for vulnerability_severity if not already set
if 'vulnerability_severity' not in st.session_state:
    st.session_state.vulnerability_severity = None

# Calculate the Vulnerability Severity score when the button is clicked
if st.button("Calculate Vulnerability Severity"):
    st.session_state.vulnerability_severity = (cvss * weight_cvss) + \
                                               (affected_products_score * weight_affected_products_score) + \
                                               (recency_score * weight_recency_score) + \
                                               (age_score * weight_age_score) + \
                                               (exploit_weight * weight_exploit_weight)
    st.success(f"The Vulnerability Severity Score is: {st.session_state.vulnerability_severity:.2f}")

# Vulnerability severity, and EPSS inputs
st.subheader("EPSS")
def fetch_epss_score(cve_id):
    # Define the API URL for fetching EPSS score
    epss_api_url = f"https://api.first.org/data/v1/epss?cve={cve_id}"

    # Make a GET request to the EPSS API
    epss_response = requests.get(epss_api_url)

    # Check if the response is successful
    if epss_response.status_code == 200:
        epss_data = epss_response.json()
        epss_score = epss_data['data'][0]['epss']
        return epss_score
    else:
        st.error("Failed to fetch EPSS score.")
        return None

# Example usage:
cve_id = "CVE-2023-0001"
epss = fetch_epss_score(cve_id)
st.write(f"EPSS score for {cve_id}: {epss}")
if epss is not None:
    epss = float(epss)  # Convert EPSS score to float

# Set the weights for the components

st.subheader("Seeeward Severity Score")
if st.button('What is the Seeward Severity Score Formula ?'):
    st.write('Seeward Severity = (Vulnerability Severity x WeightVS) + (Ease of Resolution × WeightER) + (Exploit Difficulty x WeightED) + (EPSS x WeightEPSS).')
else:
    st.write('Click me to define Seeward Severity Score Formula.')


# Calculate the Seeward Severity score when the button is clicked
if st.button("Calculate Seeward Severity"):
    if (st.session_state.ease_of_resolution is not None and
        st.session_state.exploit_difficulty is not None and
        st.session_state.vulnerability_severity is not None):
        
        # Ensure all variables are numbers
        seeward_severity = (float(st.session_state.vulnerability_severity) * weight_vs) + \
                           (float(st.session_state.ease_of_resolution) * weight_er) + \
                           (float(st.session_state.exploit_difficulty) * weight_ed) + \
                           (epss * weight_epss)
                           
        st.success(f"The Seeward Severity Score is: {seeward_severity:.2f}")
    else:
        st.error("Please calculate both Ease of Resolution, Exploit Difficulty, and Vulnerability Severity scores first.")
