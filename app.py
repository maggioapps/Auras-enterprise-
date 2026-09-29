import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync Enterprise OS", 
    page_icon="🧠", 
    layout="wide"
)

# --- MEMORIA DEI DATI UTENTI ---
if 'utenti_registrati' not in st.session_state:
    st.session_state.utenti_registrati = {"admin_principale": "TuaPasswordAdminSegreta123"}

if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None

if 'gettoni' not in st.session_state:
    st.session_state.gettoni = 0

if 'prova_gratis_fatta' not in st.session_state:
    st.session_state.prova_gratis_fatta = False

# --- BARRA LATERALE: LOGIN E REGISTRAZIONE ---
st.sidebar.markdown("### 🔐 Accesso Account AuraSync")

if st.session_state.utente_corrente is None:
    st.sidebar.info("✨ **Registrati ora e ricevi subito 5 gettoni d'oro!**")
    azione = st.sidebar.radio("Scegli:", ["Accedi (Login)", "Registrati"])
    
    if azione == "Registrati":
        nuovo_user = st.sidebar.text_input("Scegli Username")
        nuova_pass = st.sidebar.text_input("Scegli Password", type="password")
        if st.sidebar.button("Crea Account"):
            if nuovo_user and nuova_pass:
                if nuovo_user in st.session_state.utenti_registrati:
                    st.sidebar.error("Username già esistente!")
                else:
                    st.session_state.utenti_registrati[nuovo_user] = nuova_pass
                    st.session_state.utente_corrente = nuovo_user
                    st.session_state.gettoni = 5
                    st.sidebar.success("Registrato! Hai ricevuto 5 gettoni d'oro 🪙")
                    st.rerun()
            else:
                st.sidebar.warning("Compila tutti i campi.")
    else:
        user_in = st.sidebar.text_input("Username")
        pass_in = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Entra"):
            if user_in in st.session_state.utenti_registrati and st.session_state.utenti_registrati[user_in] == pass_in:
                st.session_state.utente_corrente = user_in
                st.session_state.gettoni = 5
                st.rerun()
            else:
                st.sidebar.error("Credenziali errate.")
else:
    st.sidebar.success(f"Benvenuto, **{st.session_state.utente_corrente}**!")
    st.sidebar.write(f"🪙 Gettoni: **{st.session_state.gettoni}**")
    if st.sidebar.button("Logout"):
        st.session_state.utente_corrente = None
        st.rerun()

SEI_ADMIN = (st.session_state.utente_corrente == "admin_principale")

# --- INTERFACCIA PRINCIPALE (Completamente Libera, niente Area Protetta) ---
st.title("🚀 AuraSync Enterprise - Hub IA, Trend & Gamification")
st.write("Esplora liberamente la piattaforma, fai una prova gratuita o gira la ruota dei premi!")

# Menu di navigazione principale aperto a tutti
sezione = st.selectbox("Scegli Sezione:", [
    "🎡 Ruota della Fortuna & Premi", 
    "🎁 Prova Gratuita (Senza Registrazione)", 
    "🤖 Modelli Branch IA (10 Categorie)", 
    "📈 Trend Finanziari & Social (10 Categorie)", 
    "💎 Abbonamenti & Gettoni (Stripe)"
])

if sezione == "🎡 Ruota della Fortuna & Premi":
    st.title("🎡 La Ruota della Fortuna AuraSync")
    st.write("Gira la ruota per vincere gettoni e premi esclusivi!")
    
    # Controllo prima di riscattare i premi della ruota
    if st.session_state.utente_corrente is None:
        st.warning("⚠️ **Registrati per avere 5 gettoni d'oro o fai la tua prova gratuita completa!**")
    
    if st.button("🌀 Gira la Ruota"):
        if st.session_state.utente_corrente is None:
            st.error("🔒 Impossibile riscattare il premio: **Registrati per avere 5 gettoni d'oro o fai la tua prova gratuita completa!**")
        else:
            premio = random.choice([1, 2, 5, 10, "Accesso VIP"])
            st.success(f"🎉 Hai vinto: **{premio}**!")
            if premio != "Accesso VIP":
                st.session_state.gettoni += int(premio)
                st.info((f"🪙 Ora hai {st.session_state.gettoni} gettoni."))

elif sezione == "🎁 Prova Gratuita (Senza Registrazione)":
    st.title("🎁 Area di Prova Gratuita Completa")
    st.write("Testa subito le potenzialità di AuraSync senza alcun impegno.")
    
    input_prova = st.text_input("Inserisci un comando di test per l'IA:")
    if st.button("Esegui Test Gratuito"):
        risultato_prova = f"Risultato elaborato per il test: '{input_prova}'\nStato: Test Gratuito completato."
        st.success("Test eseguito con successo!")
        st.write(risultato_prova)
        
        # Pulsante di download
        st.download_button(
            label="📥 Download Risultato Test",
            data=risultato_prova,
            file_name="aurasync_prova_gratis.txt",
            mime="text/plain"
        )
        
        st.session_state.prova_gratis_fatta = True

    # A fine prova compare esattamente la scritta richiesta
    if st.session_state.prova_gratis_fatta and st.session_state.utente_corrente is None:
        st.markdown("---")
        st.error("✨ **Registrati per avere 5 gettoni d'oro!** (Usa la barra laterale a sinistra per creare il tuo account in un click).")

elif sezione == "🤖 Modelli Branch IA (10 Categorie)":
    st.title("🤖 Libreria Modelli Branch IA (10 Categorie)")
    
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
    
    if "10. 🔒 IL TUO BRANCH ESCLUSIVO" in cat_scelta and not SEI_ADMIN:
        st.warning("⚠️ Area protetta del branch master proprietario.")
        st.markdown("[💳 SBLOCCA IL BRANCH PRINCIPALE (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    else:
        st.info(f"Stai consultando: **{cat_scelta}**")
        prompt_model = st.text_input("Prompt:")
        if st.button("Genera Contenuto IA"):
            output_ia = f"Output generato per [{cat_scelta}] con prompt: {prompt_model}"
            st.success("Generato!")
            st.write(output_ia)
            st.download_button("📥 Download Output", output_ia, "ia_output.txt", "text/plain")

elif sezione == "📈 Trend Finanziari & Social (10 Categorie)":
    st.title("📈 Analisi Trend Finanziari & Social (10 Categorie)")
    st.success("Tutti i trend di mercato sono liberamente esplorabili.")
    
    trend_scelto = st.selectbox("Seleziona Trend:", [
        "1. Azioni Tech & IA", "2. Criptovalute", "3. Social Media Viral Trends", 
        "4. Forex & Macro", "5. E-commerce", "6. Startup Funding", 
        "7. Real Estate", "8. Sentiment Analysis", "9. Green Energy", "10. 🔒 PREVISIONI MASTER 100€"
    ])
    
    if "10. 🔒 PREVISIONI MASTER" in trend_scelto and not SEI_ADMIN:
        st.warning("Area riservata alle previsioni master.")
        st.markdown("[💳 ACCEDI AL TREND MASTER (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    else:
        report_t = f"Analisi dettagliata del trend: {trend_scelto}"
        st.write(report_t)
        st.download_button("📥 Download Report Trend", report_t, "trend_report.txt", "text/plain")

elif sezione == "💎 Abbonamenti & Gettoni (Stripe)":
    st.title("💎 Gestione Abbonamenti e Gettoni")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🪙 Gettoni")
        st.write("15€ (50 Gettoni)")
        st.markdown("[ACQUISTA](https://buy.stripe.com/tuo_link_gettoni)")
    with col2:
        st.subheader("🚀 Pro")
        st.write("49€ / mese")
        st.markdown("[ABBONATI](https://buy.stripe.com/tuo_link_abbonamento)")
    with col3:
        st.subheader("👑 Master")
        st.write("100€ / accesso")
        st.markdown("[SBLOCCA](https://buy.stripe.com/tuo_link_100_euro)")
