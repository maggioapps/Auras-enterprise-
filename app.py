import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync Enterprise OS", 
    page_icon="🧠", 
    layout="wide"
)

# --- MEMORIA DEI DATI UTENTI NEL COMPUTER (Simulata) ---
if 'utenti_registrati' not in st.session_state:
    # Utente Admin predefinito di sistema
    st.session_state.utenti_registrati = {"admin_principale": "TuaPasswordAdminSegreta123"}

if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None

# --- BARRA LATERALE: GESTIONE ACCOUNT & LOGIN ---
st.sidebar.markdown("### 🔐 Accesso Account AuraSync")

# Se non sei loggato, mostra scelta tra Login e Registrazione
if st.session_state.utente_corrente is None:
    azione_account = st.sidebar.radio("Scegli:", ["Accedi (Login)", "Crea Nuovo Account"])
    
    if azione_account == "Crea Nuovo Account":
        st.sidebar.subheader("📝 Registrati")
        nuovo_user = st.sidebar.text_input("Scegli Username")
        nuova_pass = st.sidebar.text_input("Scegli Password", type="password")
        if st.sidebar.button("Registrati Ora"):
            if nuovo_user and nuova_pass:
                if nuovo_user in st.session_state.utenti_registrati:
                    st.sidebar.error("Questo username esiste già!")
                else:
                    st.session_state.utenti_registrati[nuovo_user] = nuova_pass
                    st.sidebar.success("Account creato! Ora fai il Login.")
            else:
                st.sidebar.warning("Inserisci tutti i dati.")
                
    else:
        st.sidebar.subheader("🔑 Login Utente")
        user_input = st.sidebar.text_input("Username")
        pass_input = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Entra nell'App"):
            # Controllo credenziali
            if user_input in st.session_state.utenti_registrati and st.session_state.utenti_registrati[user_input] == pass_input:
                st.session_state.utente_corrente = user_input
                st.rerun()
            else:
                st.sidebar.error("Username o password errati!")

else:
    # Se l'utente è loggato
    st.sidebar.success(f"Benvenuto, **{st.session_state.utente_corrente}**!")
    if st.sidebar.button("🚪 Esci (Logout)"):
        st.session_state.utente_corrente = None
        st.rerun()

# --- VERIFICA SE SEI L'AMMINISTRATORE ---
# Cambia 'admin_principale' con il nome utente esatto che usi per loggarti come admin!
SEI_ADMIN = (st.session_state.utente_corrente == "admin_principale")

if SEI_ADMIN:
    st.sidebar.markdown("---")
    st.sidebar.info("👑 **Modalità Admin attiva**: Funzioni illimitate e sbloccate.")

# --- SEZIONE PRINCIPALE DELL'APP (Visibile solo se loggati) ---
if st.session_state.utente_corrente is None:
    st.title("🔒 AuraSync - Area Protetta")
    st.warning("Per accedere alla piattaforma, ai modelli IA e ai trend, devi effettuare l'accesso o creare un account personale dalla barra laterale.")
else:
    # Menu di navigazione dell'app
    sezione = st.sidebar.selectbox("Scegli Sezione:", [
        "🏠 Home (Pagina Libera)", 
        "🤖 Modelli Branch IA (10 Categorie)", 
        "📈 Trend Finanziari & Social (10 Categorie)", 
        "💎 Abbonamenti & Gettoni (Stripe)"
    ])

    if sezione == "🏠 Home (Pagina Libera)":
        st.title("🚀 Benvenuto in AuraSync, " + st.session_state.utente_corrente + "!")
        st.success("La tua dashboard personale è attiva.")
        st.write("Usa il menu a sinistra per navigare tra i modelli avanzati e i trend di mercato.")

    elif sezione == "🤖 Modelli Branch IA (10 Categorie)":
        st.title("🤖 Libreria Modelli Branch IA")
        
        categorie_ia = [
            "1. Analisi Cognitiva & Comportamentale",
            "2. Sviluppo Codice & Architettura Software",
            "3. Automazione Workflow & Agent Swarms",
            "4. Sicurezza Informatica & Masking UI",
            "5. Ottimizzazione Token & Economia IA",
            "6. Generazione Contenuti & Copywriting Multilingua",
            "7. Modelli Predittivi & Machine Learning",
            "8. Integrazione API & Cloud Deployment",
            "9. Simulazioni di Mercato & Game Theory",
            "10. 🔒 IL TUO BRANCH ESCLUSIVO AURA-SYNC (Master 100€ a prova)"
        ]
        
        cat_scelta = st.selectbox("Seleziona Categoria IA:", categorie_ia)
        
        if "10. 🔒 IL TUO BRANCH ESCLUSIVO" in cat_scelta:
            if SEI_ADMIN:
                st.success("🔓 [ADMIN] Accesso illimitato al tuo branch master personale concesso!")
                st.write("Qui gestisci il codice proprietario in totale libertà.")
            else:
                st.warning("⚠️ Questo è un branch master proprietario protetto. Richiede la licenza di test da 100€.")
                st.markdown("[💳 SBLOCCA IL BRANCH PRINCIPALE (100€)](https://buy.stripe.com/tuo_link_100_euro)")
        else:
            st.info(f"Stai esplorando: **{cat_scelta}**")
            if SEI_ADMIN:
                st.success("🟢 [ADMIN] Tutti i modelli avanzati di questa categoria sono gratuiti e illimitati per te.")
            else:
                st.write("• **Modelli 1 a 5:** 🟢 *Gratuiti*")
                st.write("• **Modelli 6+:** 💎 *Avanzati a pagamento (Richiedono gettoni o abbonamento)*")

    elif sezione == "📈 Trend Finanziari & Social (10 Categorie)":
        st.title("📈 Analisi Trend Finanziari & Social")
        
        categorie_trend = [
            "1. Azioni Tech & Intelligenza Artificiale (Globali)",
            "2. Criptovalute & Tokenomics di Mercato",
            "3. Social Media Viral Trends (TikTok, Instagram, X)",
            "4. Forex & Macroeconomia Internazionale",
            "5. E-commerce & Consumer Spending Analytics",
            "6. Venture Capital & Startup Funding Trends",
            "7. Real Estate & Asset Digitali",
            "8. Sentiment Analysis delle community globali",
            "9. Green Energy & ESG Investment Trends",
            "10. 🔒 PREVISIONI MASTER PROPRIETARIE (Branch Esclusivo 100€)"
        ]
        
        trend_scelto = st.selectbox("Seleziona Categoria Trend:", categorie_trend)
        
        if "10. 🔒 PREVISIONI MASTER" in trend_scelto and not SEI_ADMIN:
            st.warning("⚠️ Area riservata alle previsioni master proprietarie (100€ a prova).")
            st.markdown("[💳 ACCEDI AL TREND MASTER (100€)](https://buy.stripe.com/tuo_link_100_euro)")
        else:
            st.success("📊 Dati e analisi dei trend sbloccati.")

    elif sezione == "💎 Abbonamenti & Gettoni (Stripe)":
        st.title("💎 Gestione Abbonamenti e Tariffe")
        if SEI_ADMIN:
            st.info("ℹ️ Pannello di controllo pagamenti visibile agli utenti standard.")
            
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("🪙 Pacchetto Gettoni")
            st.write("15€ (50 Gettoni)")
            st.markdown("[ACQUISTA GETTONI](https://buy.stripe.com/tuo_link_gettoni)")
        with col2:
            st.subheader("🚀 Abbonamento Pro")
            st.write("49€ / mese")
            st.markdown("[ABBONATI ORA](https://buy.stripe.com/tuo_link_abbonamento)")
        with col3:
            st.subheader("👑 Licenza Master Branch")
            st.write("100€ / accesso")
            st.markdown("[SBLOCCA 100€ PROVA](https://buy.stripe.com/tuo_link_100_euro)")
