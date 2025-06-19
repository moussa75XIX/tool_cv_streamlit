import streamlit as st
from mapping_cv import mapping_cv

st.title("🧠 Générateur Automatique de CV Word")

uploaded_file = st.file_uploader("Upload ton CV (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Traitement en cours..."):
        output_bytes = mapping_cv(file=uploaded_file)

        if output_bytes:
            st.success("✅ CV généré avec succès !")
            st.download_button(
                label="📥 Télécharger le CV Word",
                data=output_bytes,
                file_name="cv_final.docx"
            )
        else:
            st.error("Une erreur est survenue lors du traitement.")