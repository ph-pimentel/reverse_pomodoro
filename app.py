import streamlit as st
from main import register_time, total_work_month, best_time_month

st.set_page_config(
    page_title="HabAnt",
    page_icon="🐜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>

    .stApp {
        background-color: #eeeeee;
        color: #353935;
    }

    </style>
""", unsafe_allow_html=True)

PATH = "dados.json"
MONTHS = {
    "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
    "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
    "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
}
CONSULTAS = {"Total do mês", "Melhor tempo"}

# Sidebar
st.sidebar.title('Menu')
opcao_menu = st.sidebar.radio(
    "Selecione uma opção:",
    ["Registro de Tempo", "Consultas"]
)

if opcao_menu == "Registro de Tempo":
    st.title("Registro de Tempo")
    st.write("Insira os minutos e segundos trabalhados na sessão.")

    col1, col2 = st.columns(2)
    minutos = col1.number_input("Minutos", min_value=0, value=0)
    segundos = col2.number_input("Segundos", min_value=0, max_value=59, value=0)

    if st.button("Registrar Tempo"):
        msg = register_time(PATH, MONTHS, minutos, segundos)
        st.success(msg)

elif opcao_menu == "Consultas":
    st.title("Consultas")
    st.write("Insira os minutos e segundos trabalhados na sessão.")

    consulta_select = st.selectbox("Tipo de Consulta:", CONSULTAS)
    mes_selecionado = st.selectbox("Escolha um Mês:", list(MONTHS.values()))

    if consulta_select == "Total do mês":
        if st.button("Ver Total do Mês"):
            resultado = total_work_month(PATH, MONTHS, mes_selecionado)
            st.info(resultado)
    else:
        if st.button("Ver Melhor Tempo"):
            resultado_best = best_time_month(PATH, MONTHS, mes_selecionado)
            st.info(resultado_best)