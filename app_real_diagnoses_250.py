import streamlit as st
import re

st.set_page_config(page_title='ICD-10-AM Smart Coder', layout='centered')
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/King_Abdulaziz_Medical_City_Logo.png/600px-King_Abdulaziz_Medical_City_Logo.png", width=150)
st.title('ICD-10-AM Smart Coding Assistant')
st.subheader('Developed by: BASSAM TAWFEEG')
st.markdown("""
Welcome to the smart assistant for automated clinical coding.
This tool reads free-text clinical notes and suggests appropriate **ICD-10-AM** codes in real time.
It's designed to support medical coders and improve documentation quality.
""")
st.markdown("---")

note = st.text_area("Enter a doctor's note or clinical statement:")

diagnoses = {
    "essential hypertension": "I10",
    "acute myocardial infarction": "I21.9",
    "heart failure": "I50.9",
    "atrial fibrillation": "I48.91",
    "copd": "J44.9",
    "asthma": "J45.909",
    "type 2 diabetes mellitus": "E11.9",
    "hypothyroidism": "E03.9",
    "anemia": "D64.9",
    "pneumonia": "J18.9",
    "appendicitis": "K35.80",
    "gastric ulcer": "K25.9",
    "rheumatoid arthritis": "M06.9",
    "lumbago": "M54.5",
    "depressive episode": "F32.1",
    "generalized anxiety disorder": "F41.1",
    "otitis media": "H66.9",
    "tonsillitis": "J03.9",
    "urinary retention": "R33.9",
    "nocturia": "R35.1",
    "hyperkalemia": "E87.5",
    "hypocalcemia": "E83.51",
    "acute pancreatitis": "K85.9",
    "cholelithiasis": "K80.2",
    "gastritis": "K29.7",
    "diverticulitis": "K57.3",
    "hepatitis b": "B16.9",
    "hepatitis c": "B18.2",
    "hiv disease": "B24",
    "otitis externa": "H60.3",
    "menstrual disorder": "N92.6",
    "infertility": "N97.9",
    "ectopic pregnancy": "O00.9",
    "spontaneous abortion": "O03.9",
    "anxiety state": "F41.0",
    "insomnia": "G47.0",
    "vertigo": "R42",
    "syncope": "R55",
    "palpitations": "R00.2",
    "chest pain": "R07.9",
    "headache": "R51",
    "nasal congestion": "R09.81",
    "cough": "R05",
    "dyspnea": "R06.0",
    "fever": "R50.9",
    "fatigue": "R53.83",
    "back pain": "M54.5",
    "joint stiffness": "M25.60",
    "muscle cramps": "M62.830",
    "hyponatremia": "E87.1",
    "hypokalemia": "E87.6",
    "hypernatremia": "E87.0",
    "hyperglycemia": "R73.9",
    "hypoglycemia": "E16.2",
    "urinary tract infection": "N39.0",
    "cystitis": "N30.0",
    "nephrolithiasis": "N20.0",
    "enuresis": "R32",
    "hematuria": "R31.9",
    "angina pectoris": "I20.9",
    "myocardial infarction": "I21.9",
    "cardiac arrest": "I46.9",
    "ischemic heart disease": "I25.9",
    "congestive heart failure": "I50.0",
    "hypertensive heart disease": "I11.9",
    "pulmonary embolism": "I26.9",
    "pericarditis": "I30.9",
    "endocarditis": "I33.0",
    "aortic stenosis": "I35.0",
    "acute bronchitis": "J20.9",
    "chronic bronchitis": "J42",
    "emphysema": "J43.9",
    "bronchiectasis": "J47.9",
    "lung abscess": "J85.1",
    "influenza": "J10.1",
    "sinusitis": "J32.9",
    "laryngitis": "J04.0",
    "pleurisy": "R09.1",
    "tuberculosis": "A15.0",
    "type 1 diabetes mellitus": "E10.9",
    "gestational diabetes": "O24.4",
    "hyperthyroidism": "E05.9",
    "thyroiditis": "E06.9",
    "obesity": "E66.9",
    "metabolic syndrome": "E88.81",
    "gout": "M10.9",
    "hyperlipidemia": "E78.5",
    "peptic ulcer": "K27.9",
    "gerd": "K21.9",
    "irritable bowel syndrome": "K58.9",
    "ulcerative colitis": "K51.9",
    "crohn’s disease": "K50.9",
    "cirrhosis of liver": "K74.6",
    "stroke": "I63.9",
    "epilepsy": "G40.9",
    "migraine": "G43.9",
    "parkinson's disease": "G20",
    "multiple sclerosis": "G35",
    "bell's palsy": "G51.0",
    "dementia": "F03.90",
    "alzheimer's disease": "G30.9",
    "neuralgia": "M79.2",
    "tension headache": "R51",
    "viral gastroenteritis": "A08.4",
    "bacterial pneumonia": "J15.9",
    "pharyngitis": "J02.9",
    "conjunctivitis": "H10.9",
    "skin infection": "L08.9",
    "herpes zoster": "B02.9",
}

if st.button("Suggest Code"):
    found = False
    words = re.findall(r'\b\w+\b', note.lower())
    for keyword, code in diagnoses.items():
        if keyword in " ".join(words):
            st.success(f"Suggested ICD-10-AM Code: {code}")
            found = True
    if not found:
        st.warning("No code suggestion found for the entered note.")