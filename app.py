Non cdimport streamlit as st

# Configurazione della pagina principale
st.set_page_config(
    page_title="AuraSync - Cognitive Operating System", 
    page_icon="🧠", 
    layout="wide"
)

# --- 1. MEMORIA E DATABASE UTENTI SIMULATO ---
if 'utenti_registrati' not in st.session_state:
    st.session_state.utenti_registrati = {"admin_principale": "TuaPasswordAdminSegreta123"}

if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None

if 'wallet_oro' not in st.session_state:
    st.session_state.wallet_oro = 10  # Bonus onboarding iniziale
if 'wallet_platino' not in st.session_state:
    st.session_state.wallet_platino = 3
if 'streak_giorni' not in st.session_state:
    st.session_state.streak_giorni = 1
if 'pet_health' not in st.session_state:
    st.session_state.pet_health = 100 

# --- 2. BARRA LATERALE: ACCOUNT, WALLET, ABBONAMENTI & ADMIN ---
st.sidebar.markdown("### 🔐 AuraSync Security Hub")

if st.session_state.utente_corrente is None:
    azione_acc = st.sidebar.radio("Accesso:", ["Accedi (Login)", "Crea Nuovo Account"])
    
    if azione_acc == "Crea Nuovo Account":
        st.sidebar.subheader("Registrazione PWA")
        u_reg = st.sidebar.text_input("Scegli Username")
        p_reg = st.sidebar.text_input("Scegli Password", type="password")
        eta_reg = st.sidebar.number_input("Età", min_value=1, max_value=120, value=25)
        if st.sidebar.button("Registrati Ora"):
            if u_reg and p_reg:
                if u_reg in st.session_state.utenti_registrati:
                    st.sidebar.error("Username già in uso!")
                else:
                    st.session_state.utenti_registrati[u_reg] = {"pass": p_reg, "eta": eta_reg}
                    st.sidebar.success("Account creato con successo! Fai il login.")
            else:
                st.sidebar.warning("Compila tutti i campi.")
    else:
        st.sidebar.subheader("Login Utente")
        u_log = st.sidebar.text_input("Username")
        p_log = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Entra"):
            db_user = st.session_state.utenti_registrati.get(u_log)
            pass_valida = False
            eta_utente = 25
            
            if isinstance(db_user, dict) and db_user.get("pass") == p_log:
                pass_valida = True
                eta_utente = db_user.get("eta", 25)
            elif u_log == "admin_principale" and p_log == "TuaPasswordAdminSegreta123":
                pass_valida = True
                eta_utente = 30
                
            if pass_valida:
                st.session_state.utente_corrente = u_log
                st.session_state.utente_eta = eta_utente
                st.rerun()
            else:
                st.sidebar.error("Credenziali non valide!")
else:
    st.sidebar.success(f"Benvenuto, **{st.session_state.utente_corrente}**!")
    st.sidebar.markdown(f"🪙 **Oro:** {st.session_state.wallet_oro} | 💎 **Platino:** {st.session_state.wallet_platino}")
    st.sidebar.markdown(f"🔥 **Streak:** {st.session_state.streak_giorni} giorni | 🐾 **Pet Health:** {st.session_state.pet_health}%")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💳 Abbonamenti & Store Stripe")
    st.sidebar.markdown("[🪙 Acquista Gettoni](https://buy.stripe.com/tuo_link_gettoni)")
    st.sidebar.markdown("[⭐ Abbonamento Full Access (49€)](https://buy.stripe.com/tuo_link_abbonamento)")
    st.sidebar.markdown("[🚀 Licenza Master Branch (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    st.sidebar.markdown("---")
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.utente_corrente = None
        st.rerun()

SEI_ADMIN = (st.session_state.utente_corrente == "admin_principale")
ETA_UTENTE = st.session_state.get('utente_eta', 25)
IS_MAGGIORENNE = (SEI_ADMIN or ETA_UTENTE >= 18)

if SEI_ADMIN:
    st.sidebar.info("👑 **Modalità Admin Suprema:** Risorse illimitate e sbloccate.")

# --- 3. INTESTAZIONE CON BOTTONE SOS ROSSO IN ALTO A DESTRA ---
col_head1, col_head2 = st.columns([4, 1])

with col_head1:
    st.title("🚀 AuraSync - Cognitive Operating System")

with col_head2:
    st.markdown("<br>", unsafe_allow_html=True) 
    if st.button("🚨 AURA SOS", type="primary", use_container_width=True):
        st.error("⚡ **EMERGENZA ATTIVATA!** Protocollo di crisi avviato in background. Risoluzione immediata in corso...")

st.write("Piattaforma SaaS PWA globale. Esplora liberamente i moduli specialistici, i tool di intelligenza artificiale e le funzioni dirompenti.")

st.markdown("---")

# --- 4. RUOTA DELLA FORTUNA SEMPRE VISIBILE NELLA HOME ---
with st.container():
    st.markdown("### 🎡 Ruota della Fortuna & Bonus Giornaliero (Loot Table)")
    st.write("Gira la ruota in primo piano per riscuotere subito i tuoi gettoni bonus!")
    
    col_rf1, col_rf2 = st.columns([2, 3])
    with col_rf1:
        if st.button("✨ Gira la Ruota Ora (Bonus +3 Oro)", type="primary", use_container_width=True):
            st.session_state.wallet_oro += 3
            st.success("🎉 Hai vinto **3 Gettoni d'Oro** accreditati nel wallet!")
            st.rerun()
    with col_rf2:
        st.info(f"🪙 Il tuo saldo attuale è di **{st.session_state.wallet_oro} Gettoni d'Oro** e **{st.session_state.wallet_platino} Monete Platino**.")

st.markdown("---")
st.subheader("🗂️ Indice Generale delle Opzioni (In ordine alfabetico)")

# Gestione della navigazione a schede tramite session_state
if 'modulo_attivo' not in st.session_state:
    st.session_state.modulo_attivo = "Home"

if st.session_state.modulo_attivo == "Home":
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("### 🤖 AuraBot & Modelli IA")
        st.write("Libreria completa di Branch IA e Trend globali suddivisa in 10 categorie.")
        if st.button("Apri AuraBot & Modelli"):
            st.session_state.modulo_attivo = "ModelliIA"
            st.rerun()
            
        st.markdown("### 🌿 AuraGreen & Botanica")
        st.write("Pollice verde digitale, diagnosi piante tramite foto e gestione orto/giardino.")
        if st.button("Apri AuraGreen"):
            st.session_state.modulo_attivo = "AuraGreen"
            st.rerun()

        st.markdown("### 👨‍👩‍👧‍👦 AuraKids & Paws (0-18)")
        st.write("Nutrizione, svezzamento, supporto emotivo e scolastico diviso per fasce d'età.")
        if st.button("Apri AuraKids"):
            st.session_state.modulo_attivo = "AuraKids"
            st.rerun()

    with c2:
        st.markdown("### 🛠️ AuraFix & Meccanica")
        st.write("Guide di riparazione fai-da-te per casa, auto e bici con calcolo risparmio.")
        if st.button("Apri AuraFix"):
            st.session_state.modulo_attivo = "AuraFix"
            st.rerun()

        st.markdown("### 🐾 AuraPets & Paws")
        st.write("Companion empatico per animali domestici, guide all'addestramento e salute.")
        if st.button("Apri AuraPets"):
            st.session_state.modulo_attivo = "AuraPets"
            st.rerun()

        if IS_MAGGIORENNE:
            st.markdown("### 💬 AuraMatch (Incontri 18+)")
            st.write("Matchmaking basato sulla compatibilità neurale e profili cognitivi.")
            if st.button("Apri AuraMatch"):
                st.session_state.modulo_attivo = "AuraMatch"
                st.rerun()

    with c3:
        st.markdown("### 🚨 AuraTwin & Extra")
        st.write("Aura Twin, Capsula del tempo e favole dinamiche della buonanotte.")
        if st.button("Apri Funzioni Extra"):
            st.session_state.modulo_attivo = "Extra"
            st.rerun()

        if IS_MAGGIORENNE:
            st.markdown("### 🎰 AuraSlots (Mini-Casinò 18+)")
            st.write("Arcade virtuale con micro-puntate in Gettoni e Bonus Game di Platino.")
            if st.button("Apri AuraSlots"):
                st.session_state.modulo_attivo = "AuraSlots"
                st.rerun()

        st.markdown("### 💎 Token Economy & Store")
        st.write("Gestione wallet, conversione Oro/Platino, ruota bonus e abbonamenti Stripe.")
        if st.button("Apri Wallet & Store"):
            st.session_state.modulo_attivo = "WalletStore"
            st.rerun()

else:
    if st.button("⬅️ Torna alla Home Principale"):
        st.session_state.modulo_attivo = "Home"
        st.rerun()
    st.markdown("---")

    # --- ROUTING DEI MODULI SPECIALISTICI ---
    
    if st.session_state.modulo_attivo == "ModelliIA":
        st.header("🤖 Libreria Modelli Branch IA & Trend Globali")
        tab_ia1, tab_ia2 = st.tabs(["🤖 Branch IA (10 Categorie)", "📈 Trend Finanziari & Social (10 Categorie)"])
        
        with tab_ia1:
            cats_ia = [
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
            sel_cat_ia = st.selectbox("Seleziona Categoria IA:", cats_ia)
            if "10. 🔒 IL TUO BRANCH ESCLUSIVO" in sel_cat_ia and not SEI_ADMIN:
                st.warning("⚠️ Branch Master proprietario protetto. Richiede licenza di prova da 100€.")
                st.markdown("[💳 SBLOCCA IL BRANCH PRINCIPALE (100€)](https://buy.stripe.com/tuo_link_100_euro)")
            else:
                st.success(f"Accesso consentito a: {sel_cat_ia}")
                st.write("• Modelli 1-5: 🟢 Gratuiti")
                st.write("• Modelli 6+: 💎 Avanzati (Richiedono 1 Moneta Platino)")

        with tab_ia2:
            cats_tr = [
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
            sel_cat_tr = st.selectbox("Seleziona Trend:", cats_tr)
            if "10. 🔒 PREVISIONI MASTER" in sel_cat_tr and not SEI_ADMIN:
                st.warning("⚠️ Previsioni master proprietarie protette (100€ a prova).")
                st.markdown("[💳 ACCEDI AL TREND MASTER (100€)](https://buy.stripe.com/tuo_link_100_euro)")
            else:
                st.success(f"Analisi di mercato attiva per: {sel_cat_tr}")

    elif st.session_state.modulo_attivo == "AuraGreen":
        st.header("🌿 AuraGreen & Botanica Digitale")
        st.write("Diagnosi intelligente dello stato di salute delle piante tramite caricamento fotografico e consigli colturali.")
        foto_pianta = st.file_uploader("Carica una foto della pianta malata o da analizzare", type=["jpg", "png", "jpeg"])
        if foto_pianta:
            st.image(foto_pianta, width=300)
            if st.button("Diagnostica con IA"):
                st.success("🌱 Diagnosi completata: Carenza di azoto rilevata. Piano di concimazione organica generato!")

    elif st.session_state.modulo_attivo == "AuraKids":
        st.header("👨‍👩‍👧‍👦 AuraKids & Paws (Fascia 0-18 Anni)")
        eta_bambino = st.slider("Seleziona la fascia d'età del minore:", 0, 18, 5)
        st.info(f"Stai visualizzando i protocolli nutrizionali, svezzamento e gestione emotiva dedicati all'età di {eta_bambino} anni.")
        st.write("• Guida pedagogica personalizzata")
        st.write("• Supporto compiti e gestione capricci")

    elif st.session_state.modulo_attivo == "AuraFix":
        st.header("🛠️ AuraFix & Meccanica Pratica")
        st.write("Guide passo-passo per la manutenzione e la riparazione fai-da-te.")
        problema = st.text_input("Cosa devi riparare? (es. rubinetto che perde, catena bici, lavatrice)")
        if st.button("Genera Guida di Riparazione"):
            if problema:
                st.success(f"🔧 Guida generata per: {problema}. Risparmio stimato: ~85€!")
            else:
                st.warning("Inserisci il problema da risolvere.")

    elif st.session_state.modulo_attivo == "AuraPets":
        st.header("🐾 AuraPets & Paws - Companion Empatico")
        specie = st.selectbox("Animale domestico:", ["Cane", "Gatto", "Altro"])
        st.write(f"Gestione avanzata della salute, comportamento e piano alimentare per il tuo {specie}.")

    elif st.session_state.modulo_attivo == "AuraMatch" and IS_MAGGIORENNE:
        st.header("💬 AuraMatch - Incontri e Connessioni Protette (18+)")
        st.write("Sistema di matchmaking basato sulla compatibilità neurale dei moduli cognitivi.")
        st.info("💡 Usa 1 Gettone d'Oro per inviare un messaggio prioritario (Aura Spark).")

    elif st.session_state.modulo_attivo == "Extra":
        st.header("🚨 Funzioni Extra di Dirompente Genialità")
        col_ex1, col_ex2 = st.columns(2)
        with col_ex1:
            st.subheader("🤖 Aura Twin")
            st.write("Il tuo gemello digitale ha preparato 3 bozze di lavoro per te questa mattina.")

        with col_ex2:
            st.subheader("⏳ Capsula del Tempo")
            st.write("Archivia ricordi e strategie con sblocco a data futura.")
            
            st.subheader("📖 Favole Dinamiche della Buonanotte")
            if st.button("Genera Favola Interattiva"):
                st.success("✨ C'era una volta... (Scheda da colorare pronta nel repository download).")

    elif st.session_state.modulo_attivo == "AuraSlots" and IS_MAGGIORENNE:
        st.header("🎰 AuraSlots & Micro-Puntate (Mezzo Gettone)")
        st.write("Arcade virtuale con puntate frazionate (0.5 gettoni). Assenza totale di denaro reale.")
        st.info(f"🪙 Gettoni disponibili: {st.session_state.wallet_oro}")
        
        if st.button("Gira la Slot (Puntata: 0.5 Gettoni)"):
            st.success("🎰 Risultato: Vincita parziale accreditata!")

    elif st.session_state.modulo_attivo == "WalletStore":
        st.header("💎 Token Economy, Ruota Bonus & Abbonamenti")
        
        col_w1, col_w2 = st.columns(2)
        with col_w1:
            st.subheader("🪙 Portafoglio Virtuale")
            st.write(f"• **Gettoni d'Oro:** {st.session_state.wallet_oro}")
            st.write(f"• **Monete Platino:** {st.session_state.wallet_platino}")
            if st.button("🔄 Converti 3 Oro in 1 Platino"):
                if st.session_state.wallet_oro >= 3:
                    st.session_state.wallet_oro -= 3
                    st.session_state.wallet_platino += 1
                    st.success("Conversione riuscita!")
                else:
                    st.error("Gettoni d'Oro insufficienti!")

        with col_w2:
            st.subheader("🎡 Ruota della Fortuna (Loot Table)")
            if st.button("Gira la Ruota Bonus (Store)"):
                st.session_state.wallet_oro += 2
                st.success("🎉 Hai vinto 2 Gettoni d'Oro bonus!")

        st.markdown("---")
        st.subheader("💳 Listino Prezzi & Abbonamenti Stripe")
        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            st.write("**Pass Giornaliero / Gettoni**")
            st.markdown("[ACQUISTA GETTONI](https://buy.stripe.com/tuo_link_gettoni)")
        with sc2:
            st.write("**Abbonamento Full Access**")
            st.markdown("[ABBONATI PRO (49€)](https://buy.stripe.com/tuo_link_abbonamento)")
        with sc3:
            st.write("**Licenza Master Branch**")
            st.markdown("[SBLOCCA 100€ PROVA](https://buy.stripe.com/tuo_link_100_euro)")
