import streamlit as st
import pandas as pd
import os  # For checking file existence

# Título da página
st.title("Sugestões")

# Selecionar nome
name = st.selectbox("Seleciona o teu nome:", ["", "Diana", "Jorge", "Francisco", "Catarina", "Pedro", "Joana", "Margarida", "Beatriz", "Teresa"])

# Selecionar o assunto da sugestão
subject = st.selectbox(
    "Seleciona o assunto:",
    ["", "Erros Fidebot", "Ideias", "Outros"]
)

# Caixa de texto para a sugestão
suggestion = st.text_area("Escreve a tua sugestão:")

# Submit Button
if st.button("Submeter"):
    # Validation
    if not name:
        st.error("Por favor seleciona o teu nome.")
    elif not subject:
        st.error("Por favor seleciona o assunto.")
    elif not suggestion.strip():
        st.error("Por favor escreve a tua sugestão.")
    else:
        # Process and save the suggestion
        st.success("Obrigada pela tua sugestão! 😉")
        st.write("### Summary of Your Input:")
        st.write(f"- **Nome:** {name}")
        st.write(f"- **Assunto:** {subject}")
        st.write(f"- **Sugestão:** {suggestion}")

        # Prepare data
        data = {
            "Nome": [name],
            "Assunto": [subject],
            "Sugestão": [suggestion]
        }
        df = pd.DataFrame(data)

        # Check if the file already exists
        file_path = "suggestions.csv"
        if not os.path.isfile(file_path):
            # File doesn't exist, create it with a header
            df.to_csv(file_path, mode="w", index=False, header=True)
        else:
            # File exists, append without header
            df.to_csv(file_path, mode="a", index=False, header=False)
