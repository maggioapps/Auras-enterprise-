import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync Enterprise", page_icon="📱", layout="wide"
)

st.title("AuraSync Enterprise - Hub IA, Trend & Gamification")
st.write(
    "Esplora liberamente la piattaforma, fai una prova gratuita o gira la ruota dei premi!"
)

st.divider()

# Schermata iniziale stile Menu del Telefono (Griglia di icone/pulsanti)
st.subheader("Menu Principale")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎡\n\nRuota della Fortuna", use_container_width=True):
        st.session_state["pagina_attiva"] = "Ruota"

with col2:
    if st.button("🤖\n\nHub IA", use_container_width=True):
        st.session_state["pagina_attiva"] = "Hub IA"

with col3:
    if st.button("📊\n\nTrend & Mercato", use_container_width=True):
        st.session_state["pagina_attiva"] = "Trend"

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("🎁\n\nArea Premi", use_container_width=True):
        st.session_state["pagina_attiva"] = "Premi"

with col5:
    if st.button("⚙️\n\nProva Gratuita", use_container_width=True):
        st.session_state["pagina_attiva"] = "Prova"

with col6:
    if st.button("👤\n\nIl mio Profilo", use_container_width=True):
        st.session_state["pagina_attiva"] = "Profilo"

# Gestione della navigazione in base al pulsante cliccato
if "pagina_attiva" not in st.session_state:
    st.session_state["pagina_attiva"] = "Home"

if st.session_state["pagina_attiva"] == "Ruota":
    st.header("La Ruota della Fortuna AuraSync")
    st.write("Gira la ruota per vincere gettoni e premi esclusivi!")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()

elif st.session_state["pagina_attiva"] == "Hub IA":
    st.header("Hub Intelligenza Artificiale")
    st.write("Accedi agli strumenti di IA avanzati.")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()

elif st.session_state["pagina_attiva"] == "Trend":
    st.header("Trend & Mercato")
    st.write("Analisi dei trend in tempo reale.")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()

elif st.session_state["pagina_attiva"] == "Premi":
    st.header("Area Premi e Gettoni")
    st.write("Gestisci i tuoi gettoni d'oro.")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()

elif st.session_state["pagina_attiva"] == "Prova":
    st.header("Prova Gratuita")
    st.write("Attiva la tua prova gratuita completa.")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()

elif st.session_state["pagina_attiva"] == "Profilo":
    st.header("Il mio Profilo")
    st.write("Visualizza i tuoi dati e progressi.")
    if st.button("Indietro al Menu"):
        st.session_state["pagina_attiva"] = "Home"
        st.rerun()
