import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync Enterprise", page_icon="📱", layout="wide"
)

# Inizializzazione dello stato della pagina
if "pagina_attiva" not in st.session_state:
    st.session_state["pagina_attiva"] = "Home"

# Funzione per tornare alla home
def vai_a_home():
    st.session_state["pagina_attiva"] = "Home"

# ----------------- HOME / MENU PRINCIPALE (Stile Telefono) -----------------
if st.session_state["pagina_attiva"] == "Home":
    st.title("AuraSync Enterprise - Hub IA, Trend & Gamification")
    st.write("Esplora liberamente la piattaforma: seleziona un'applicazione dal menu qui sotto.")
    st.divider()

    st.subheader("📲 Menu Principale")

    # Prima riga di "app" (3 colonne)
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🎡\n\nRuota della Fortuna", use_container_width=True):
            st.session_state["pagina_attiva"] = "Ruota"
            st.rerun()

    with col2:
        if st.button("🤖\n\nHub IA", use_container_width=True):
            st.session_state["pagina_attiva"] = "Hub IA"
            st.rerun()

    with col3:
        if st.button("📊\n\nTrend & Mercato", use_container_width=True):
            st.session_state["pagina_attiva"] = "Trend"
            st.rerun()

    # Seconda riga di "app" (3 colonne)
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("🎁\n\nArea Premi", use_container_width=True):
            st.session_state["pagina_attiva"] = "Premi"
            st.rerun()

    with col5:
        if st.button("⚙️\n\nProva Gratuita", use_container_width=True):
            st.session_state["pagina_attiva"] = "Prova"
            st.rerun()

    with col6:
        if st.button("👤\n\nIl mio Profilo", use_container_width=True):
            st.session_state["pagina_attiva"] = "Profilo"
            st.rerun()

# ----------------- SEZIONI INTERNE -----------------
elif st.session_state["pagina_attiva"] == "Ruota":
    st.header("🎡 La Ruota della Fortuna AuraSync")
    st.write("Gira la ruota per vincere gettoni e premi esclusivi!")
    # [Qui puoi inserire la logica o la grafica della ruota]
    st.write("*(Area Ruota della Fortuna attiva)*")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Hub IA":
    st.header("🤖 Hub Intelligenza Artificiale")
    st.write("Accedi agli strumenti di IA avanzati per il tuo business.")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Trend":
    st.header("📊 Trend & Mercato")
    st.write("Monitoraggio dei trend in tempo reale e analisi statistiche.")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Premi":
    st.header("🎁 Area Premi e Gettoni")
    st.write("Gestisci i tuoi gettoni d'oro e riscatta i premi vinti.")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Prova":
    st.header("⚙️ Prova Gratuita")
    st.write("Configura o attiva la tua prova gratuita completa della piattaforma.")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Profilo":
    st.header("👤 Il mio Profilo")
    st.write("Visualizza i tuoi dati personali, lo storico e i progressi.")
    st.divider()
    if st.button("🏠 Torna al Menu Principale"):
        vai_a_home()
        st.rerun()
