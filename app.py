import streamlit as st

st.set_page_config(page_title="ICD-10-AM Smart Coder", layout="centered")

st.title("Smart ICD-10-AM Code Assistant")
st.markdown("**Project by: BASSAM TAWFEEG**")

note = st.text_area("Enter doctor's note:")

if st.button("Suggest Code"):
    if "pneumonia" in note.lower():
        st.success("Suggested ICD-10-AM Code: J18.9 – Pneumonia, unspecified organism")
    elif "chest pain" in note.lower() and "diabetes" in note.lower():
        st.success("Suggested ICD-10-AM Code: I21.9 – Acute myocardial infarction")
    elif "abdominal pain" in note.lower():
        st.success("Suggested ICD-10-AM Code: K58.9 – Irritable bowel syndrome")
    else:
        st.warning("No code suggestion found for the entered note.")
