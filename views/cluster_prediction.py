import streamlit as st
import requests



st.markdown("<h1 style='text-align: center;'>🤖 FideBot</h1>", unsafe_allow_html=True)

# Histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do usuário
if user_input := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Chamada à API Langflow
    url = "http://localhost:7860/api/v1/run/c98ac3ec-d8e7-40c1-a8c4-775661f756a5"
    payload = {
        "input_value": user_input,
        "output_type": "chat",
        "input_type": "chat"
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        output = response.json()

        # Acessar a resposta correta
        bot_reply = output["outputs"][0]["outputs"][0]["results"]["message"]["text"]

    except Exception as e:
        bot_reply = f"❌ Erro: {e}"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
