import streamlit as st
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="Aviso Importante", layout="centered")

# Data limite (01 de abril às 23:59:59)
data_fim = datetime(2026, 4, 1, 0, 0, 0)
agora = datetime.now()

if agora < data_fim:
    st.title("🚨 Mudamos de site!")

    st.write(
        """
        Para evitar confusões com outros projetos da ufrj, este site será **desativado em breve**.
        
        👉 Acesse o novo site:
        """
    )

    st.markdown(
        '<a href="https://ufrjmapas.streamlit.app" target="_blank">'
        '🔗 https://ufrjmapas.streamlit.app'
        '</a>',
        unsafe_allow_html=True
    )

    st.divider()
    st.warning("💣 Esta mensagem vai se autodestruir em:")

    countdown_placeholder = st.empty()

    # Countdown ao vivo
    if True:
        agora = datetime.now()
        restante = data_fim - agora

        #if restante.total_seconds() <= 0:
        #    break

        dias = restante.days
        horas, resto = divmod(restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        countdown_placeholder.markdown(
            f"⏳ **{dias} dias, {horas:02d}:{minutos:02d}**"
        )

                

else:
    # Conteúdo após o prazo (opcional)
    st.title("Não há mais nada aqui")
    st.write("Nada")
    st.markdown(
        """
        <iframe width="560" height="315"
        src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&controls=1"
        title="YouTube video player"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True
    )

