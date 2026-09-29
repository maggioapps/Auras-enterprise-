import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="AuraSync Enterprise", page_icon="📱", layout="wide")

# Stile CSS per trasformare i pulsanti in veri "blocchi app" in stile smartphone
st.markdown("""
    <style>
    /* Stile generale per i pulsanti principali */
    div.stButton > button {
        width: 100%;
        height: 120px;
        background-color: #f8f9fa;
        color: #212529;
        border: 2px solid #e9ecef;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #e2e6ea;
        border-color: #adb5bd;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione dello stato della pagina
if "pagina_attiva" not in st.session_state:
    st.session_state["pagina_attiva"] = "Home"

def vai_a_home():
    st.session_state["pagina_attiva"] = "Home"

# ----------------- HOME / MENU PRINCIPALE (Stile Telefono) -----------------
if st.session_state["pagina_attiva"] == "Home":
    st.title("AuraSync Enterprise")
    st.write("📲 **Menu Principale** - Seleziona un'applicazione:")
    st.divider()

    # Prima riga (3 app)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎡\n\nRuota della Fortuna"):
            st.session_state["pagina_attiva"] = "Ruota"
            st.rerun()
    with col2:
        if st.button("🤖\n\nHub IA"):
            st.session_state["pagina_attiva"] = "Hub IA"
            st.rerun()
    with col3:
        if st.button("📊\n\nTrend & Mercato"):
            st.session_state["pagina_attiva"] = "Trend"
            st.rerun()

    st.write("") # Spaziatura

    # Seconda riga (3 app)
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("🎁\n\nArea Premi"):
            st.session_state["pagina_attiva"] = "Premi"
            st.rerun()
    with col5:
        if st.button("⚙️\n\nProva Gratuita"):
            st.session_state["pagina_attiva"] = "Prova"
            st.rerun()
    with col6:
        if st.button("👤\n\nIl mio Profilo"):
            st.session_state["pagina_attiva"] = "Profilo"
            st.rerun()

# ----------------- SEZIONI INTERNE -----------------
elif st.session_state["pagina_attiva"] == "Ruota":
    st.header("🎡 La Ruota della Fortuna AuraSync")
    st.write("Gira la ruota per vincere gettoni e premi esclusivi!")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Hub IA":
    st.header("🤖 Hub Intelligenza Artificiale")
    st.write("Accedi agli strumenti di IA avanzati.")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Trend":
    st.header("📊 Trend & Mercato")
    st.write("Monitoraggio dei trend in tempo reale.")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Premi":
    st.header("🎁 Area Premi e Gettoni")
    st.write("Gestisci i tuoi gettoni d'oro.")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Prova":
    st.header("⚙️ Prova Gratuita")
    st.write("Attiva la tua prova gratuita.")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

elif st.session_state["pagina_attiva"] == "Profilo":
    st.header("👤 Il mio Profilo")
    st.write("Visualizza i tuoi dati personali.")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()
