import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync Enterprise OS", 
    page_icon="🧠", 
    layout="wide"
)

# --- MEMORIA UTENTI (Simulata) ---
if 'utenti_registrati' not in st.session_state:
    st.session_state.utenti_registrati = {"admin_principale": "TuaPasswordAdminSegreta123"}

if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None

# --- BARRA LATERALE: LOGIN E REGISTRAZIONE ---
st.sidebar.markdown("### 🔐 Area Personale & Admin")

if st.session_state.utente_corrente is None:
    azione = st.sidebar.radio("Scegli:", ["Accedi (Login)", "Crea Nuovo Account"])
    
    if azione == "Crea Nuovo Account":
        st.sidebar.subheader("Registrati")
        u_reg = st.sidebar.text_input("Username")
        p_reg = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Crea Account"):
            if u_reg and p_reg:
                if u_reg in st.session_state.utenti_registrati:
                    st.sidebar.error("Username già esistente!")
                else:
                    st.session_state.utenti_registrati[u_reg] = p_reg
                    st.sidebar.success("Account creato! Fai il login.")
            else:
                st.sidebar.warning("Compilare tutti i campi.")
    else:
        st.sidebar.subheader("Login")
        u_log = st.sidebar.text_input("Username")
        p_log = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Entra"):
            if u_log in st.session_state.utenti_registrati and st.session_state.utenti_registrati[u_log] == p_log:
                st.session_state.utente_corrente = u_log
                st.rerun()
            else:
                st.sidebar.error("Credenziali errate.")
else:
    st.sidebar.success(f"Benvenuto, {st.session_state.utente_corrente}!")
    if st.sidebar.button("Esci (Logout)"):
        st.session_state.utente_corrente = None
        st.rerun()

# Verifica se è l'amministratore
SEI_ADMIN = (st.session_state.utente_corrente == "admin_principale")
if SEI_ADMIN:
    st.sidebar.info("👑 Modalità Admin: Accesso Illimitato Attivo")

# --- PAGINA PRINCIPALE LIBERA A ICONE (IN ORDINE ALFABETICO) ---
st.title("🚀 AuraSync Enterprise - Dashboard Aperta")
st.write("Esplora liberamente tutte le sezioni, i modelli di Branch IA e i Trend di mercato organizzati in ordine alfabetico.")

st.markdown("---")

# Griglia di opzioni in ordine alfabetico rigoroso
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🤖 Branch IA")
    st.write("Libreria di modelli cognitivi avanzati suddivisi in 10 categorie (con modelli base gratuiti e opzioni pro).")
    if st.button("Apri Branch IA"):
        st.session_state.pagina_attiva = "BranchIA"
        st.rerun()

with col2:
    st.markdown("### 💎 Gettoni & Abbonamenti")
    st.write("Gestisci i tuoi piani di abbonamento, acquista gettoni o sblocca la licenza esclusiva.")
    if st.button("Apri Abbonamenti"):
        st.session_state.pagina_attiva = "Abbonamenti"
        st.rerun()

with col3:
    st.markdown("### 📈 Trend di Mercato")
    st.write("Analisi approfondite sui trend finanziari globali, crypto e social media in tempo reale.")
    if st.button("Apri Trend"):
        st.session_state.pagina_attiva = "Trend"
        st.rerun()

# Gestione della navigazione interna dopo il clic sulle icone
if 'pagina_attiva' not in st.session_state:
    st.session_state.pagina_attiva = "Home"

st.markdown("---")

if st.session_state.pagina_attiva == "BranchIA":
    if st.button("⬅️ Torna alla Home a Icone"):
        st.session_state.pagina_attiva = "Home"
        st.rerun()
    
    st.header("🤖 Sezione Modelli Branch IA")
    st.write("Le 10 categorie ufficiali (5 modelli gratuiti + modelli avanzati/master):")
    
    cat_ia_alfabetico = [
        "1. Analisi Cognitiva & Comportamentale",
        "2. Automazione Workflow & Agent Swarms",
        "3. Generazione Contenuti & Copywriting Multilingua",
        "4. Integrazione API & Cloud Deployment",
        "5. Modelli Predittivi & Machine Learning",
        "6. Ottimizzazione Token & Economia IA",
        "7. Sicurezza Informatica & Masking UI",
        "8. Simulazioni di Mercato & Game Theory",
        "9. Sviluppo Codice & Architettura Software",
        "10. 🔒 IL TUO BRANCH ESCLUSIVO AURA-SYNC (Master 100€ a prova)"
    ]
    
    scelta_ia = st.selectbox("Seleziona Categoria:", cat_ia_alfabetico)
    if "10. 🔒 IL TUO BRANCH ESCLUSIVO" in scelta_ia:
        if SEI_ADMIN:
            st.success("🔓 [ADMIN] Accesso Master sbloccato gratuitamente!")
        else:
            st.warning("⚠️️ Accesso protetto (100€ a prova).")
            st.markdown("[💳 SBLOCCA IL BRANCH PRINCIPALE (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    else:
        st.info(f"Categoria attiva: {scelta_ia}")
        st.write("• Modelli 1-5: 🟢 Gratuiti")
        st.write("• Modelli 6+: 💎 Avanzati (Richiedono gettoni o abbonamento)")

elif st.session_state.pagina_attiva == "Trend":
    if st.button("⬅️ Torna alla Home a Icone"):
        st.session_state.pagina_attiva = "Home"
        st.rerun()
        
    st.header("📈 Sezione Trend Finanziari & Social")
    st.write("Le 10 categorie di trend in ordine alfabetico:")
    
    cat_trend_alfabetico = [
        "1. Azioni Tech & Intelligenza Artificiale (Globali)",
        "2. Criptovalute & Tokenomics di Mercato",
        "3. E-commerce & Consumer Spending Analytics",
        "4. Forex & Macroeconomia Internazionale",
        "5. Green Energy & ESG Investment Trends",
        "6. Real Estate & Asset Digitali",
        "7. Sentiment Analysis delle community globali",
        "8. Social Media Viral Trends (TikTok, Instagram, X)",
        "9. Venture Capital & Startup Funding Trends",
        "10. 🔒 PREVISIONI MASTER PROPRIETARIE (Branch Esclusivo 100€)"
    ]
    
    scelta_tr = st.selectbox("Seleziona Trend:", cat_trend_alfabetico)
    if "10. 🔒 PREVISIONI MASTER" in scelta_tr and not SEI_ADMIN:
        st.warning("⚠️ Area riservata alle previsioni master proprietarie (100€ a prova).")
        st.markdown("[💳 ACCEDI AL TREND MASTER (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    else:
        st.success("📊 Analisi e dati sbloccati.")

elif st.session_state.pagina_attiva == "Abbonamenti":
    if st.button("⬅️ Torna alla Home a Icone"):
        st.session_state.pagina_attiva = "Home"
        st.rerun()
        
    st.header("💎 Vetrina Abbonamenti & Gettoni")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.subheader("🪙 Pacchetto Gettoni")
        st.write("15€ (50 Gettoni)")
        st.markdown("[ACQUISTA GETTONI](https://buy.stripe.com/tuo_link_gettoni)")
    with col_b:
        st.subheader("🚀 Abbonamento Pro")
        st.write("49€ / mese")
        st.markdown("[ABBONATI ORA](https://buy.stripe.com/tuo_link_abbonamento)")
    with col_c:
        st.subheader("👑 Licenza Master Branch")
        st.write("100€ / accesso")
        st.markdown("[SBLOCCA 100€ PROVA](https://buy.stripe.com/tuo_link_100_euro)")
