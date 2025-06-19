import streamlit as st
from mapping_cv import mapping_cv

st.title("🧠 Générateur Automatique de CV Word")

uploaded_file = st.file_uploader("Upload ton CV (PDF)", type=["pdf"])

if uploaded_file:
    if "output_bytes" not in st.session_state:
        with st.spinner("Traitement en cours..."):
            output = mapping_cv(file=uploaded_file)
            if output:
                st.session_state.output_bytes = output
                st.success("✅ CV généré avec succès !")
            else:
                st.error("Une erreur est survenue lors du traitement.")

    if "output_bytes" in st.session_state:
        st.download_button(
            label="📥 Télécharger le CV Word",
            data=st.session_state.output_bytes,
            file_name="cv_final.docx"
        )
