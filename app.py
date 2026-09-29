import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="AuraSync Enterprise", page_icon="✨", layout="wide")

# Inizializzazione dello stato della sessione
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "tokens" not in st.session_state:
    st.session_state.tokens = 0  # Gettoni d'oro iniziali per i nuovi utenti
if "free_trial_used" not in st.session_state:
    st.session_state.free_trial_used = False

# --- BARRA LATERALE: LOGIN E REGISTRAZIONE ---
st.sidebar.title("🔐 Accesso & Account")

if not st.session_state.logged_in:
    st.sidebar.info("✨ **Registrati ora e ricevi subito 5 gettoni d'oro gratuiti!**")
    
    auth_mode = st.sidebar.radio("Scegli modalità", ["Accedi", "Registrati"])
    
    username = st.sidebar.text_input("Nome utente")
    password = st.sidebar.text_input("Password", type="password")
    
    if auth_mode == "Registrati":
        if st.sidebar.button("Crea Account e Prendi 5 Gettoni"):
            if username and password:
                st.session_state.logged_in = True
                st.session_state.tokens = 5
                st.sidebar.success("Account creato! Benvenuto, hai 5 gettoni d'oro 🪙")
                st.rerun()
            else:
                st.sidebar.error("Compila tutti i campi.")
    else:
        if st.sidebar.button("Accedi"):
            # Sostituisci con la tua logica di verifica credenziali
            if username and password:
                st.session_state.logged_in = True
                st.session_state.tokens = 5  # Oppure carica dal database
                st.sidebar.success("Accesso effettuato con successo!")
                st.rerun()
            else:
                st.sidebar.error("Inserisci credenziali valide.")
else:
    st.sidebar.success(f"Benvenuto, {username}!")
    st.sidebar.write(f"🪙 Gettoni d'oro disponibili: **{st.session_state.tokens}**")
    if st.sidebar.button("Esci (Logout)"):
        st.session_state.logged_in = False
        st.rerun()

# --- CONTENUTO PRINCIPALE (Visibile a tutti) ---
st.title("🚀 AuraSync - Hub IA e Trend")
st.write("Esplora liberamente le categorie di Branch IA, i trend di mercato e i contenuti della piattaforma.")

# Sezione di prova gratuita senza login
with st.container():
    st.markdown("---")
    st.subheader("🎁 Area di Test Gratuita (Senza Login)")
    st.write("Vuoi testare subito le potenzialità di AuraSync senza registrarti? Prova qui sotto la demo gratuita:")
    
    free_prompt = st.text_input("Inserisci un prompt di prova rapida:")
    if st.button("Esegui Test Gratuito"):
        st.info("Risultato della prova gratuita generato con successo!")
        
        # Simuliamo un contenuto generato da scaricare
        sample_output = f"Report di prova generato per il prompt: '{free_prompt}'\nData: 2026-09-29"
        
        # --- PULSANTE DI DOWNLOAD ---
        st.download_button(
            label="📥 Download Risultato (TXT)",
            data=sample_output,
            file_name="aurasync_test_output.txt",
            mime="text/plain"
        )
    st.markdown("---")

# Esempio di interazione avanzata che richiede gettoni o login
st.subheader("⚡ Strumenti Avanzati IA & Trend (Richiede interazione)")
user_query = st.text_input("Inserisci la tua richiesta avanzata per il Branch IA:")

if st.button("Genera Contenuto Avanzato"):
    if not st.session_state.logged_in and not st.session_state.free_trial_used:
        # Permettiamo una prova gratuita al volo
        st.session_state.free_trial_used = True
        st.warning("Hai utilizzato la tua interazione di prova gratuita! Per continuare a generare, registrati e ricevi 5 gettoni d'oro.")
    elif st.session_state.logged_in and st.session_state.tokens > 0:
        st.session_state.tokens -= 1
        st.success(f"Generazione completata! Ti rimangono {st.session_state.tokens} gettoni d'oro.")
        
        # Contenuto generato avanzato
        advanced_output = f"Contenuto avanzato basato su: {user_query}\nGenerato da AuraSync Enterprise."
        
        # Pulsante download per i risultati avanzati
        st.download_button(
            label="📥 Download Report Avanzato",
            data=advanced_output,
            file_name="aurasync_advanced_report.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Non hai abbastanza gettoni d'oro o non hai effettuato l'accesso. Registrati o ricarica i gettoni tramite Stripe!")
