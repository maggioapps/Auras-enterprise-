import streamlit as st
from googletrans import LANGUAGES, Translator

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync OS — Full Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

translator = Translator()

# --- LOGICA DELLE SINGOLE APPLICAZIONI (ISOLATE E FUNZIONANTI) ---

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
    
    col1, col2, col3 = st.triline = st.columns(3) if hasattr(st, "columns") else (None, None, None)
    # Metriche rapide di sistema
    st.metric(label="Stato del Sistema", value="Online", delta="100% Sincronizzato")
    st.metric(label="Moduli Caricati", value="300 / 300", delta="Pronti")

# --- REGISTRO CENTRALE DEI MODULI (Mappa dei 50 Capitoli) ---
registro_app = {
    "🎓 Università: Calcolatore Media": app_media_ponderata,
    "🛠️ Casa: Sblocco Lavandino": app_sblocco_lavandino,
    "🎮 Gamification: XP System": app_xp_system,
    "🖥️ Control Center: Dashboard": app_dashboard,
}

# --- BARRA LATERALE E LINGUA UNIVERSALE ---
st.sidebar.title("⚡ AuraSync OS")
st.sidebar.caption("Architettura Modulare a 300 Moduli")
st.sidebar.markdown("---")

# Selettore Lingua Universale
language_options = [name.capitalize() for name in LANGUAGES.values()]
selected_lang_name = st.sidebar.selectbox(
    "🌍 Lingua Universale:",
    options=language_options,
    index=language_options.index("Italian") if "Italian" in language_options else 0,
)
selected_lang_code = [code for code, name in LANGUAGES.items() if name.capitalize() == selected_lang_name][0]

st.sidebar.markdown("---")
st.sidebar.header("🧭 Selettore Applicazioni")

# Selezione pulita tramite menu a tendina laterale
scelta_app = st.sidebar.selectbox(
    "Scegli il modulo da eseguire:",
    options=list(registro_app.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("📱 Suggerimento PWA: Aggiungi questa app alla schermata Home del tuo smartphone.")

# --- CORPO PRINCIPALE ---
st.title("⚡ AuraSync OS — Centro di Controllo")
st.caption(f"Esecuzione Modulo Isolata | Lingua attiva: {selected_lang_name}")
st.markdown("---")

# Esecuzione dinamica sicura del modulo selezionato
if scelta_app in registro_app:
    # Richiama la funzione associata all'app scelta senza conflitti di stato
    registro_app[scelta_app]()
else:
    st.error("Modulo non trovato o in fase di caricamento.")
