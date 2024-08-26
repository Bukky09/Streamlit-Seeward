iimport streamlit as st

# Set the app title
st.title("Seeward Severity Score Calculator")
st.header('Input Values')

# Set the weights for the components
st.sidebar.header("Set Weights For Seeward Severity score")
weight_vs = st.sidebar.number_input("Enter Weight for Vulnerability Severity (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_er = st.sidebar.number_input("Enter Weight for Ease of Resolution (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_ed = st.sidebar.number_input("Enter Weight for Exploit Difficulty (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_epss = st.sidebar.number_input("Enter Weight for EPSS (Exploit Prediction Scoring System) (0-1):", min_value=0.0, max_value=1.0, step=0.1)

# Create input fields for the components
st.subheader("Ease Of Resolution")

response_time = st.number_input("Response Time:", min_value=1, max_value=10, step=1)
team_expertise = st.number_input("Team Expertise:", min_value=1, max_value=10, step=1)
impact_on_systems = st.number_input("Impact on Systems:", min_value=1, max_value=10, step=1)
communication_efficiency = st.number_input("Communication Efficiency:", min_value=1, max_value=10, step=1)
documentation_learning = st.number_input("Documentation and Learning:", min_value=1, max_value=10, step=1)
detection_time = 5
complexity_issue = 7
resource_availability = 6

st.sidebar.header("Set For Weights Ease of Resolution")
weight_detection_time = st.sidebar.number_input("Detection Time Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_complexity_issue = st.sidebar.number_input("Complexity of Issue Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_resource_availability = st.sidebar.number_input("Resource Availability Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_response_time = st.sidebar.number_input("Response Time Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_team_expertise = st.sidebar.number_input("Team Expertise Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_impact_on_systems = st.sidebar.number_input("Impact on Systems Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_communication_efficiency = st.sidebar.number_input("Communication Efficiency Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_documentation_learning = st.sidebar.number_input("Documentation and Learning Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)

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
# Display predefined values
st.write("Attack Vector = 5")
st.write("Attack Complexity = 6")
st.write("Privileges Required = 7")
st.write("Availability Of Exploit = 5")
st.write("Environmental Factors = 7")
st.write("Mitigations Defenses = 8")
st.write("Exploit Reliability = 6")

attack_vector = 5
attack_complexity = 6
privileges_required = 7
availability_of_exploit = 5
environmental_factors = 7
mitigations_defenses = 8
exploit_reliability = 6

st.sidebar.header("Set For Weights Exploit Difficulty")
weight_attack_vector = st.sidebar.number_input("Attack Vector Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_attack_complexity = st.sidebar.number_input("Attack Complexity Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_privileges_required = st.sidebar.number_input("Privileges Required Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_availability_of_exploit = st.sidebar.number_input("Availability of Exploit Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_environmental_factors = st.sidebar.number_input("Environmental Factors Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_mitigations_defenses = st.sidebar.number_input("Mitigations and Defenses Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_exploit_reliability = st.sidebar.number_input("Exploit Reliability Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)

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
st.write("CVSS Score = 5")
st.write("Affected Products Score = 6")
cvss = 5
affected_products_score = 6
recency_score = st.number_input("Recency Score:", min_value=1, max_value=10, step=1)
age_score = st.number_input("Age Score:", min_value=1, max_value=10, step=1)
exploit_weight = st.number_input("Exploit Weight:", min_value=1, max_value=10, step=1)

st.sidebar.header("Set For Weights Vulnerability Severity")
weight_cvss = st.sidebar.number_input("CVSS Score Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_affected_products_score = st.sidebar.number_input("Affected Products Score Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_recency_score = st.sidebar.number_input("Recency Score Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_age_score = st.sidebar.number_input("Age Score Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)
weight_exploit_weight = st.sidebar.number_input("Exploit Weight Weight (0-1):", min_value=0.0, max_value=1.0, step=0.1)

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
epss = st.number_input("Enter EPSS (Exploit Prediction Scoring System) (1-10):", min_value=1, max_value=10, step=1)

# Set the weights for the components

st.subheader("Seeeward Severity Score")

# Calculate the Seeward Severity score when the button is clicked
if st.button("Calculate Seeward Severity"):
    if (st.session_state.ease_of_resolution is not None and
        st.session_state.exploit_difficulty is not None and
        st.session_state.vulnerability_severity is not None):
        seeward_severity = (st.session_state.vulnerability_severity * weight_vs) + \
                           (st.session_state.ease_of_resolution * weight_er) + \
                           (st.session_state.exploit_difficulty * weight_ed) + \
                           (epss * weight_epss)
        st.success(f"The Seeward Severity Score is: {seeward_severity:.2f}")
    else:
        st.error("Please calculate both Ease of Resolution, Exploit Difficulty, and Vulnerability Severity scores first.")


# Provide some guidance
st.header('INFORMATION')
if st.button('What is the Seeward Severity Score Formula ?'):
    st.write('Seeward Severity = (Vulnerability Severity x WeightVS) + (Ease of Resolution × WeightER) + (Exploit Difficulty x WeightED) + (EPSS x WeightEPSS).')
else:
    st.write('Click me to define Seeward Severity Score Formula.')


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

if st.button('What is the Vulnerability Severity Score Formula ?'):
    st.write('Vulnerability Severity = (cvss * weight_cvss) + \
                                               (affected_products_score * weight_affected_products_score) + \
                                               (recency_score * weight_recency_score) + \
                                               (age_score * weight_age_score) + \
                                               (exploit_weight * weight_exploit_weight)')
else:
    st.write('Click me to define Vulnerability Severity Score Formula.') (Exploit Difficulty x WeightED) + (EPSS * WeightEPSS).')
else:
    st.write('Click me to define Seeward Severity Score Formula.')
