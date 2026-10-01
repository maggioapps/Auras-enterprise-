import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync - 18+ Interactive OS v7.6",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inizializzazione dello State globale
if "active_view" not in st.session_state: 
    st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: 
    st.session_state.active_app = None
if "story_step" not in st.session_state: 
    st.session_state.story_step = 1
if "tension_score" not in st.session_state: 
    st.session_state.tension_score = 50
if "last_card" not in st.session_state: 
    st.session_state.last_card = "Clicca su 'Estrai Quesito' per iniziare."
if "magnetism_result" not in st.session_state: 
    st.session_state.magnetism_result = None

# CATALOGO DEI MODULI (Con chiavi univoche fisse)
CATALOGO_MODULI = {
    "Adult 1. Nocturne Noir: Visual Novel di Seduzione": {
        "cat": "🔥 Area 16: Adult & Advanced Interactive (18+)",
        "desc": "Thriller psicologico e romantico a bivi narrativi interattivi con tensione crescente."
    },
    "Adult 2. Red Secrets: Il Gioco delle Confidenze Profonde": {
        "cat": "🔥 Area 16: Adult & Advanced Interactive (18+)",
        "desc": "Domande, quiz e dilemmi ad alta tensione emotiva per sondare ogni inibizione."
    },
    "Adult 3. Chemistry & Magnetic Meter AI": {
        "cat": "🔥 Area 16: Adult & Advanced Interactive (18+)",
        "desc": "Simulatore in tempo reale di affinità, magnetismo e sintonia di coppia avanzata."
    },
    "Dating 1. AuraMatch: Swipe & Chat Reale": {
        "cat": "❤ Area 15: Dating & App di Incontri",
        "desc": "Esplora i profili, metti like e avvia una conversazione interattiva."
    },
    "Dating 2. Couple Chemistry & Compatibility Quiz": {
        "cat": "❤ Area 15: Dating & App di Incontri",
        "desc": "Test di compatibilità reale con punteggio di affinità dinamico."
    }
}

# --- GESTIONE INTERFACCIA DEL MODULO ATTIVO ---
def render_active_app_interface(app_name):
    st.subheader(f"🔥 Modulo Attivo: {app_name}")
    st.divider()

    # 1. VISUAL NOVEL (Adult 1)
    if "Nocturne Noir" in app_name:
        st.markdown("### 🍷 Nocturne Noir: Capitolo Interattivo")
        st.progress(st.session_state.tension_score / 100, text=f"Indice di Tensione e Magnetismo: {st.session_state.tension_score}%")
        
        if st.session_state.story_step == 1:
            st.info("Capitolo 1: L'Invito.\n\nTi trovi in un elegante club privato a luci soffuse. All'angolo del bancone, una figura misteriosa ti osserva attraverso lo specchio e fa scivolare un biglietto verso di te: 'Il coraggio è il prezzo di ogni emozione intensa.'")
            
            choice_1 = st.radio("Come rispondi alla provocazione?", [
                "1. Ti siedi accanto senza dire una parola, mantenendo lo sguardo fisso.",
                "2. Prendi il biglietto, scrivi una risposta sul retro e glielo rimandi indietro.",
                "3. Ignori il biglietto e ordini da bere voltandole le spalle."
            ], key="unique_r_choice_1")
            
            if st.button("Conferma Scelta ⚡", key="unique_btn_step_1"):
                if "1" in choice_1 or "2" in choice_1:
                    st.session_state.tension_score = min(100, st.session_state.tension_score + 25)
                    st.session_state.story_step = 2
                    st.success("La tensione sale visibilmente. La persona sorride in modo complice e si sposta più vicina.")
                else:
                    st.session_state.tension_score = max(0, st.session_state.tension_score - 15)
                    st.warning("L'atmosfera si raffredda, ma la curiosità nell'aria resta palpabile.")
                st.rerun()

        elif st.session_state.story_step == 2:
            st.info("Capitolo 2: Il Confronto Ravvicinato.\n\nOra la distanza tra di voi si è azzerata. Il rumore di fondo della sala sembra svanire mentre vi scambiate sussurri carichi di sottintesi.")
            
            choice_2 = st.radio("Qual è la tua mossa successiva?", [
                "1. Proponi di lasciare il locale per un luogo più intimo e riservato.",
                "2. Rompi il contatto fisico ma le sussurri una domanda spiazzante all'orecchio."
            ], key="unique_r_choice_2")
            
            if st.button("Procedi nel racconto 🔥", key="unique_btn_step_2"):
                st.session_state.tension_score = min(100, st.session_state.tension_score + 35)
                st.session_state.story_step = 3
                st.success("Hai sbloccato il livello massimo di sintonia narrativa di questa sessione.")
                st.rerun()
                
        else:
            st.success("🏆 Hai completato con successo il percorso narrativo ad alta tensione!")
            if st.button("Ricomincia Storia 🔄", key="unique_btn_restart_story"):
                st.session_state.story_step = 1
                st.session_state.tension_score = 50
                st.rerun()

    # 2. RED SECRETS (Adult 2)
    elif "Red Secrets" in app_name:
        st.markdown("### 💋 Red Secrets: Il Gioco delle Inibizioni")
        category_mode = st.selectbox("Seleziona il livello di intensità:", ["Confessioni e Misteri", "Sguardi e Scelte Forti", "Dilemmi di Coppia"], key="unique_red_mode")
        
        if st.button("Estrai Quesito 🃏", key="unique_btn_draw_card"):
            questions = {
                "Confessioni e Misteri": [
                    "Qual è il complimento più inaspettato e destabilizzante che tu abbia mai ricevuto?",
                    "Se potessi rielaborare un incontro passato eliminando ogni inibizione, cosa faresti diversamente?",
                    "Qual è il dettaglio fisico o caratteriale che ti attrae magneticamente in una persona?"
                ],
                "Sguardi e Scelte Forti": [
                    "Preferisci l'attesa logorante di un incontro o la sorpresa improvvisa di un avvicinamento?",
                    "Descrivi con tre aggettivi l'atmosfera perfetta per una notte senza regole.",
                    "Se dovessi cedere a un capriccio immediato in questo momento, quale sarebbe?"
                ],
                "Dilemmi di Coppia": [
                    "Quanto conta il fattore sorpresa e mistero per mantenere alta la tensione in un rapporto?",
                    "Qual è il limite che trovi più eccitante superare in una conversazione intima?"
                ]
            }
            st.session_state.last_card = random.choice(questions[category_mode])
            st.rerun()
            
        st.warning(f"🔥 **Quesito Estratto:**\n\n> *{st.session_state.last_card}*")

    # 3. CHEMISTRY & MAGNETIC METER (Adult 3)
    elif "Magnetic Meter" in app_name:
        st.markdown("### 🧪 Chemistry & Magnetic Meter AI")
        st.write("Analizzatore istantaneo del livello di compatibilità e magnetismo psicologico.")
        
        p1 = st.text_input("Inserisci il tuo nome o profilo:", key="unique_partner_1")
        p2 = st.text_input("Inserisci il nome o profilo del partner:", key="unique_partner_2")
        
        if st.button("Calcola Magnetismo ✨", key="unique_btn_calc_mag"):
            if p1.strip() and p2.strip():
                st.session_state.magnetism_result = random.randint(88, 99)
            else:
                st.warning("Inserisci entrambi i nomi per procedere al calcolo.")
                st.session_state.magnetism_result = None
                
        if st.session_state.magnetism_result:
            st.balloons()
            st.success(f"🔥 **Indice di Magnetismo Calcolato: {st.session_state.magnetism_result}%!**")
            st.info("I profili mostrano una forte polarizzazione e un'attrazione mentale e psicologica elevatissima. Sintonia profonda rilevata.")

    else:
        st.markdown(f"### ⚙️ Modulo: {app_name}")
        st.write("Modulo interattivo attivo e pronto all'uso.")
        if st.button("Esegui Test di Connessione ⚡", key="unique_generic_test"):
            st.success("Test completato con successo.")

    st.divider()
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🔙 Torna alla Bacheca Principale", key="unique_back_dash"):
            st.session_state.active_app = None
            st.rerun()
    with col_b2:
        if st.button("📂 Torna al Menu Principale", key="unique_back_menu"):
            st.session_state.active_view = "menu_file"
            st.session_state.active_app = None
            st.rerun()

# --- INTERFACCIA PRINCIPALE ---
top_col1, top_col2, top_col3 = st.columns([2, 1, 1])
with top_col1:
    st.title("🔥 AuraSync OS v7.6 - Stabile")
with top_col2:
    st.metric("👥 Stato", "Online")
with top_col3:
    st.write("") 
    if st.button(">> 📁 Menu App & 18+", type="secondary", use_container_width=True, key="unique_toggle_menu"):
        st.session_state.active_view = "menu_file" if st.session_state.active_view == "bacheca" else "bacheca"
        st.rerun()

st.divider()

if st.session_state.active_view == "bacheca":
    if st.session_state.active_app:
        render_active_app_interface(st.session_state.active_app)
    else:
        st.subheader("📦 Dashboard Principale")
        st.info("• Clicca sul pulsante in alto a destra (**>> 📁 Menu App & 18+**) per aprire il catalogo ed evitare qualsiasi errore di routing.")
else:
    st.header("📂 Catalogo Completo Selezionato")
    ai_query = st.text_input("🤖 Cerca nel catalogo:", placeholder="Es. nocturne, red secrets, chemistry...", key="unique_search_cat")
    st.divider()

    # Raggruppa per categoria per una visualizzazione ordinata
    categorie = {}
    for name, info in CATALOGO_MODULI.items():
        if not ai_query or ai_query.lower() in name.lower() or ai_query.lower() in info['desc'].lower():
            cat = info['cat']
            if cat not in categorie: categorie[cat] = []
            categorie[cat].append((name, info['desc']))

    for cat_name, items in categorie.items():
        st.subheader(cat_name)
        cols = st.columns(2)
        for idx, (file_name, file_desc) in enumerate(items):
            with cols[idx % 2]:
                st.markdown(f"""
                <div style="border: 1px solid #d0d0d0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #fafafa; min-height: 140px;">
                    <h4 style="margin-bottom: 5px; font-size: 15px;">⚡ {file_name}</h4>
                    <p style="font-size: 12px; color: #555; margin-bottom: 10px;">{file_desc}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # CHIAVE UNIVOCA ASSOLUTA basata sul nome esatto del modulo
                safe_key = f"btn_launch_exact_{file_name}"
                if st.button(f"🚀 Avvia Modulo", key=safe_key):
                    st.session_state.active_app = file_name
                    st.session_state.active_view = "bacheca"
                    st.rerun()
        st.divider()
    
    if st.button("🔙 Torna alla Bacheca Principale", key="unique_back_from_cat"):
        st.session_state.active_view = "bacheca"
        st.rerun()
