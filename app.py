import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(page_title="AuraSync Enterprise", page_icon="📱", layout="wide")

# Stile CSS per i pulsanti a blocco stile smartphone
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 110px;
        background-color: #f8f9fa;
        color: #212529;
        border: 2px solid #e9ecef;
        border-radius: 20px;
        font-size: 16px;
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

# Inizializzazione dello stato
if "pagina_attiva" not in st.session_state:
    st.session_state["pagina_attiva"] = "Home"
if "gettoni" not in st.session_state:
    st.session_state["gettoni"] = 5

def vai_a_home():
    st.session_state["pagina_attiva"] = "Home"

# ----------------- HOME / MENU PRINCIPALE (Stile Telefono) -----------------
if st.session_state["pagina_attiva"] == "Home":
    st.title("AuraSync Enterprise - Hub IA, Trend & Gamification")
    st.write(f"🪙 **I tuoi Gettoni:** {st.session_state['gettoni']} | Scegli un'applicazione dal menu:")
    st.divider()

    # Prima riga di app
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

    st.write("")

    # Seconda riga di app
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

# ----------------- 1. RUOTA DELLA FORTUNA -----------------
elif st.session_state["pagina_attiva"] == "Ruota":
    st.header("🎡 La Ruota della Fortuna AuraSync")
    st.write("Gira la ruota per vincere gettoni e premi esclusivi! (Costo: 1 gettone)")
    
    if st.button("🔄 Gira la Ruota!"):
        if st.session_state["gettoni"] > 0:
            st.session_state["gettoni"] -= 1
            vincita = random.choice([0, 1, 3, 5, 10])
            st.session_state["gettoni"] += vincita
            if vincita > 0:
                st.success(f"🎉 Complimenti! Hai vinto {vincita} gettoni!")
            else:
                st.warning("Ops! Questa volta è andata male, riprova!")
        else:
            st.error("Non hai abbastanza gettoni per girare la ruota!")

    st.write(f"🪙 Gettoni attuali: {st.session_state['gettoni']}")
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

# ----------------- 2. HUB IA -----------------
elif st.session_state["pagina_attiva"] == "Hub IA":
    st.header("🤖 Hub Intelligenza Artificiale")
    st.write("Accedi agli strumenti di IA avanzati per generare testi, immagini e strategie.")
    
    prompt_ia = st.text_input("Scrivi qui il comando o la richiesta per l'IA:")
    if st.button("Genera Risposta IA"):
        if prompt_ia:
            st.info(f"💡 Risposta elaborata dall'IA per: '{prompt_ia}' -> Questa è una simulazione avanzata della piattaforma AuraSync IA.")
        else:
            st.warning("Inserisci prima un testo o una richiesta.")

    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

# ----------------- 3. TREND & MERCATO -----------------
elif st.session_state["pagina_attiva"] == "Trend & Mercato":
    st.header("📊 Trend & Mercato")
    st.write("Monitoraggio in tempo reale dei trend di mercato e delle opportunità digitali.")
    st.metric(label="Crescita Trend IA", value="+45.2%", delta="5.4% rispetto a ieri")
    
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

# ----------------- 4. AREA PREMI -----------------
elif st.session_state["pagina_attiva"] == "Premi":
    st.header("🎁 Area Premi e Gettoni")
    st.write(f"I tuoi gettoni disponibili: **{st.session_state['gettoni']} 🪙**")
    st.write("Riscatta i tuoi premi esclusivi accumulando gettoni con la Ruota della Fortuna!")
    
    if st.button("Riscatta Buono Sconto (10 gettoni)"):
        if st.session_state["gettoni"] >= 10:
            st.session_state["gettoni"] -= 10
            st.success("🎁 Premio riscattato con successo! Controlla la tua email.")
        else:
            st.error("Ti servono almeno 10 gettoni per questo premio.")

    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

# ----------------- 5. PROVA GRATUITA -----------------
elif st.session_state["pagina_attiva"] == "Prova":
    st.header("⚙️ Prova Gratuita")
    st.write("La tua prova gratuita completa della piattaforma AuraSync Enterprise è attiva.")
    st.success("Stai utilizzando tutte le funzioni sbloccate senza limitazioni.")
    
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()

# ----------------- 6. PROFILO -----------------
elif st.session_state["pagina_attiva"] == "Profilo":
    st.header("👤 Il mio Profilo")
    st.write("Gestisci le tue impostazioni personali e visualizza i tuoi progressi.")
    st.text_input("Nome Utente", value="Utente AuraSync")
    st.text_input("Email", value="maggioapps@example.com")
    st.write(f"🪙 Gettoni nel saldo: {st.session_state['gettoni']}")
    
    st.divider()
    if st.button("🏠 Torna alla Home"):
        vai_a_home()
        st.rerun()
