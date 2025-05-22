import streamlit as st
from datetime import datetime
import pandas as pd

tab1, tab2 = st.tabs(['🗒️ Caderno', '📌 Notas Guardadas'])

# Inicializa o estado das notas
if 'notes' not in st.session_state:
    st.session_state['notes'] = []

# Garante que todas as notas são dicionários válidos
notas_validas = []
for note in st.session_state['notes']:
    if isinstance(note, dict):
        note.setdefault("data", "")
        note.setdefault("titulo", "")
        note.setdefault("categoria", "Outro")
        note.setdefault("conteudo", "")
        notas_validas.append(note)
st.session_state['notes'] = notas_validas

with tab1:
    st.header("📝 Caderno de Notas")

    title = st.text_input("Título da nota")
    category = st.selectbox("Assunto / Categoria", ["Cliente", "Produto", "Ideia", "Outro"])
    note_input = st.text_area("Escreve a tua nota:", placeholder="Ex: Ideia sobre um cliente, algo que não queiras esquecer, etc.")

    if st.button("Guardar nota"):
        if title.strip() and note_input.strip():
            st.session_state['notes'].append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "titulo": title.strip(),
                "categoria": category,
                "conteudo": note_input.strip()
            })
            st.success("✅ Nota guardada com sucesso!")
        else:
            st.warning("⚠️ Título e conteúdo são obrigatórios para guardar.")

with tab2:
    st.header("📌 Notas Guardadas")

    if st.session_state['notes']:
        df_notes = pd.DataFrame(st.session_state['notes'])

        # Filtros (mantido igual)
        with st.expander("🔍 Filtrar notas"):
            categoria_filtro = st.multiselect("Filtrar por categoria", df_notes['categoria'].unique())
            data_min = st.date_input("A partir de:", value=None)
            data_max = st.date_input("Até:", value=None)

        df_filtrado = df_notes.copy()
        if categoria_filtro:
            df_filtrado = df_filtrado[df_filtrado['categoria'].isin(categoria_filtro)]
        if data_min:
            df_filtrado = df_filtrado[df_filtrado['data'] >= str(data_min)]
        if data_max:
            df_filtrado = df_filtrado[df_filtrado['data'] <= str(data_max)]

        # --- NOVO LAYOUT AQUI ---
        cols = st.columns(1)  # 1 coluna por nota (pode ajustar)
        for idx, (_, row) in enumerate(df_filtrado.iterrows()):
            with cols[0].container(border=True):  # Cria um retângulo
                st.markdown(f"""
                <style>
                .note-box {{
                    padding: 10px;
                    border-radius: 8px;
                    background-color: #f0f2f6;
                }}
                </style>
                <div class="note-box">
                    <h3 style="color: #2e86de;">🗂️ {row['titulo']}</h3>
                    <p><b>📅 Data:</b> {row['data']}</p>
                    <p><b>🏷️ Categoria:</b> {row['categoria']}</p>
                    <p>{row['conteudo']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Botão para apagar (opcional)
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button(f"Apagar nota {idx + 1}", key=f"del_{idx}"):
                    st.session_state['notes'].pop(idx)
                    st.rerun()
            st.write("")  # Espaço entre notas

        # Download (mantido igual)
        st.download_button(
            label="⬇️ Fazer download das notas (CSV)",
            data=df_filtrado.to_csv(index=False).encode('utf-8'),
            file_name="notas_fidebot.csv",
            mime="text/csv"
        )
    else:
        st.info("Ainda não guardaste nenhuma nota. Escreve algo no caderno!")