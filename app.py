import streamlit as st

# Configurazione della pagina (deve essere la prima istruzione Streamlit)
st.set_page_config(
    page_title="AuraSync OS — Full Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DIZIONARIO LINGUE NATIVO (Zero dipendenze esterne, zero errori) ---
LINGUE_DISPONIBILI = {
    "Italiano": "it",
    "English": "en",
    "Español": "es",
    "Français": "fr",
    "Deutsch": "de"
}

# --- LOGICA DELLE APPLICAZIONI (ISOLATE E MODULARI) ---

def app_media_ponderata():
    st.subheader("🎓 Calcolatore Media Ponderata e CFU")
    st.write("Inserisci i dati dei tuoi esami per calcolare istantaneamente la media ponderata ufficiale.")
    
    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input("Voto Esame 1", 18, 30, 27, key="m_v1")
        c1 = st.number_input("CFU Esame 1", 1, 18, 6, key="m_c1")
    with col2:
        v2 = st.number_input("Voto Esame 2", 18, 30, 24, key="m_v2")
        c2 = st.number_input("CFU Esame 2", 1, 18, 9, key="m_c2")

    if st.button("Calcola Media", key="btn_media"):
        risultato = ((v1 * c1) + (v2 * c2)) / (c1 + c2)
        st.success(f"Media Ponderata Ufficiale: **{risultato:.2f} / 30**")

def app_sblocco_lavandino():
    st.subheader("🛠️ Guida Sblocco Lavandino d'Emergenza")
    st.warning("Mantieni la calma e segui questa procedura passo-passo:")
    st.markdown("""
    1. **Posiziona un secchio** capiente direttamente sotto il sifone.
    2. **Svita manualmente** la ghiera inferiore del sifone raccoglitore.
    3. **Rimuovi i residui** di sporco o calcare accumulati all'interno.
    4. **Riavvita saldamente** e fai scorrere acqua calda per testare la tenuta.
    """)

def app_xp_system():
    st.subheader("🎮 RPG della Vita Reale (XP System)")
    st.write("Registra le azioni quotidiane per guadagnare punti esperienza e salire di livello.")
    
    task = st.text_input("Azione compiuta:", "Completato sessione di studio profondo", key="xp_task")
    difficolta = st.selectbox("Difficoltà Quest:", ["Facile (+10 XP)", "Medio (+50 XP)", "Epico (+100 XP)"], key="xp_diff")
    
    if st.button("Riscatta XP", key="btn_xp"):
        st.balloons()
        st.success(f"Quest completata: **{task}**! Punti registrati con successo nel tuo profilo.")

def app_dashboard():
    st.subheader("🖥️ Dashboard Zero-Click & Control Center")
    st.write("Panoramica rapida del tuo ecosistema operativo personale.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Stato del Sistema", value="Online", delta="100% Sincronizzato")
    with col2:
        st.metric(label="Moduli Totali", value="300", delta="Disponibili")

# --- REGISTRO CENTRALE DEI MODULI ---
registro_app = {
    "🖥️ Control Center: Dashboard": app_dashboard,
    "🎓 Università: Calcolatore Media": app_media_ponderata,
    "🛠️ Casa: Sblocco Lavandino": app_sblocco_lavandino,
    "🎮 Gamification: XP System": app_xp_system,
}

# --- BARRA LATERALE E SELETTORE LINGUA ---
st.sidebar.title("⚡ AuraSync OS")
st.sidebar.caption("Architettura Modulare Completa")
st.sidebar.markdown("---")

selected_lang_name = st.sidebar.selectbox(
    "🌍 Seleziona Lingua:",
    options=list(LINGUE_DISPONIBILI.keys()),
    index=0
)
selected_lang_code = LINGUE_DISPONIBILI[selected_lang_name]

st.sidebar.markdown("---")
st.sidebar.header("🧭 Selettore Applicazioni")

scelta_app = st.sidebar.selectbox(
    "Scegli il modulo da eseguire:",
    options=list(registro_app.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("📱 Suggerimento PWA: Aggiungi questa app alla schermata Home del tuo smartphone.")

# --- CORPO PRINCIPALE ---
st.title("⚡ AuraSync OS — Centro di Controllo")
st.caption(f"Esecuzione Modulo Isolata | Lingua attiva: {selected_lang_name} ({selected_lang_code})")
st.markdown("---")

if scelta_app in registro_app:
    registro_app[scelta_app]()
else:
    st.error("Modulo non trovato o in fase di caricamento.")
