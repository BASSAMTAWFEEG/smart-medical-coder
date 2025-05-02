import streamlit as st

st.set_page_config(page_title='ICD-10-AM Smart Coder', layout='centered')
st.title('Smart ICD-10-AM Code Assistant')
st.markdown('**Project by: BASSAM TAWFEEG**')

note = st.text_area("Enter doctor's note:")

diagnoses = {
    "essential hypertension": "I10",
    "acute myocardial infarction": "I21.9",
    "heart failure": "I50.9",
    "atrial fibrillation": "I48.91",
    "coronary artery disease": "I25.10",
    "bradycardia": "R00.1",
    "tachycardia": "R00.0",
    "mitral valve prolapse": "I34.1",
    "aortic aneurysm": "I71.4",
    "pulmonary embolism": "I26.9",
    "migraine": "G43",
    "parkinson's disease": "G20",
    "unspecified dementia": "F03.90",
    "alzheimer's disease": "G30.9",
    "epilepsy": "G40.9",
    "stroke": "I63.9",
    "transient ischemic attack (tia)": "G45.9",
    "multiple sclerosis": "G35",
    "bell's palsy": "G51.0",
    "trigeminal neuralgia": "G50.0",
    "pneumonia": "J18.9",
    "asthma": "J45.909",
    "copd": "J44.9",
    "acute bronchitis": "J20.9",
    "shortness of breath": "R06.02",
    "wheezing": "R06.2",
    "hemoptysis": "R04.2",
    "chronic sinusitis": "J32.9",
    "allergic rhinitis": "J30.9",
    "pleural effusion": "J90",
    "type 2 diabetes mellitus": "E11.9",
    "hypothyroidism": "E03.9",
    "hyperthyroidism": "E05.9",
    "hyperlipidemia": "E78.5",
    "obesity": "E66.9",
    "polycystic ovary syndrome": "E28.2",
    "cushing's syndrome": "E24.9",
    "acromegaly": "E22.0",
    "goiter": "E04.9",
    "adrenal insufficiency": "E27.40",
    "anemia": "D64.9",
    "iron deficiency anemia": "D50.9",
    "vitamin b12 deficiency": "D51.0",
    "folate deficiency anemia": "D52.9",
    "thrombocytopenia": "D69.6",
    "leukopenia": "D72.819",
    "pancytopenia": "D61.818",
    "sickle cell disease": "D57.1",
    "hemophilia": "D66",
    "polycythemia vera": "D45"
}

if st.button("Suggest Code"):
    found = False
    for keyword, code in diagnoses.items():
        if keyword in note.lower():
            st.success(f"Suggested ICD-10-AM Code: {code}")
            found = True
    if not found:
        st.warning("No code suggestion found for the entered note.")
