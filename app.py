import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync - 18+ Interactive OS v7.5",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inizializzazione robusta dello State globale (Previene crash e reset)
if "active_view" not in st.session_state: 
    st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: 
    st.session_state.active_app = None
if "story_step" not in st.session_state: 
    st.session_state.story_step = 1
if "tension_score" not in st.session_state: 
    st.session_state.tension_score = 50
if "last_card" not in st.session_state: 
    st.session_state.last_card = "Clicca su 'Estrai Carta' per iniziare."
if "magnetism_result" not in st.session_state: 
    st.session_state.magnetism_result = None

# CATALOGO DEI MODULI ATTIVI
AURASYNC_CATALOG = {
    "🔥 Area 16: Adult & Advanced Interactive (18+)": [
        ("Adult 1. Nocturne Noir: Visual Novel di Seduzione", "Thriller psicologico e romantico a bivi narrativi interattivi con tensione crescente."),
        ("Adult 2. Red Secrets: Il Gioco delle Confidenze Profonde", "Domande, quiz e dilemmi ad alta tensione emotiva per sondare ogni inibizione."),
        ("Adult 3. Chemistry & Magnetic Meter AI", "Simulatore in tempo reale di affinità, magnetismo e sintonia di coppia avanzata."),
        ("Adult 4. Roleplay Studio: Scenari di Fascino e Mistero", "Generatore di ambientazioni e ruoli interattivi guidati.")
    ],
    "❤ Area 15: Dating & App di Incontri": [
        ("Dating 1. AuraMatch: Swipe & Chat Reale", "Esplora i profili, metti like e avvia una conversazione interattiva."),
        ("Dating 2. Couple Chemistry & Compatibility Quiz", "Test di compatibilità reale con punteggio di affinità dinamico.")
    ]
}

# --- GESTIONE INTERFACCIA DEL MODULO ATTIVO ---
def render_active_app_interface(app_name):
    st.subheader(f"🔥 Modulo Attivo: {app_name}")
    st.divider()

    # 1. VISUAL NOVEL (Adult 1)
    if "Adult 1" in app_name or "Nocturne Noir" in app_name:
        st.markdown("### 🍷 Nocturne Noir: Capitolo Interattivo")
        
        # Barra di progresso dinamica collegata allo state
        st.progress(st.session_state.tension_score / 100, text=f"Indice di Tensione e Magnetismo: {st.session_state.tension_score}%")
        
        if st.session_state.story_step == 1:
            st.info("Capitolo 1: L'Invito.\n\nTi trovi in un elegante club privato a luci soffuse. All'angolo del bancone, una figura misteriosa ti osserva attraverso lo specchio e fa scivolare un biglietto verso di te: 'Il coraggio è il prezzo di ogni emozione intensa.'")
            
            choice_1 = st.radio("Come rispondi alla provocazione?", [
                "1. Ti siedi accanto senza dire una parola, mantenendo lo sguardo fisso.",
                "2. Prendi il biglietto, scrivi una risposta sul retro e glielo rimandi indietro.",
                "3. Ignori il biglietto e ordini da bere voltandole le spalle."
            ], key="r_choice_1")
            
            if st.button("Conferma Scelta ⚡", key="btn_step_1"):
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
            ], key="r_choice_2")
            
            if st.button("Procedi nel racconto 🔥", key="btn_step_2"):
                st.session_state.tension_score = min(100, st.session_state.tension_score + 35)
                st.session_state.story_step = 3
                st.success("Hai sbloccato il livello massimo di sintonia narrativa di questa sessione.")
                st.rerun()
                
        else:
            st.success("🏆 Hai completato con successo il percorso narrativo ad alta tensione!")
            if st.button("Ricomincia Storia 🔄", key="btn_restart_story"):
                st.session_state.story_step = 1
                st.session_state.tension_score = 50
                st.rerun()

    # 2. RED SECRETS (Adult 2)
    elif "Adult 2" in app_name or "Red Secrets" in app_name:
        st.markdown("### 💋 Red Secrets: Il Gioco delle Inibizioni")
        category_mode = st.selectbox("Seleziona il livello di intensità:", ["Confessioni e Misteri", "Sguardi e Scelte Forti", "Dilemmi di Coppia"], key="red_mode")
        
        if st.button("Estrai Quesito 🃏", key="btn_draw_card"):
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
    elif "Adult 3" in app_name or "Chemistry" in app_name:
        st.markdown("### 🧪 Chemistry & Magnetic Meter AI")
        st.write("Analizzatore istantaneo del livello di compatibilità e magnetismo psicologico.")
        
        p1 = st.text_input("Inserisci il tuo nome o profilo:", key="partner_1")
        p2 = st.text_input("Inserisci il nome o profilo del partner:", key="partner_2")
        
        if st.button("Calcola Magnetismo ✨", key="btn_calc_mag"):
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
        st.write(f"⚙️ **Modulo {app_name} pronto e operativo.**")
        if st.button("Esegui Test ⚡", key="btn_generic_test"):
            st.success("Operazione completata con successo.")

    st.divider()
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🔙 Torna alla Bacheca Principale", key="back_dash"):
            st.session_state.active_app = None
            st.rerun()
    with col_b2:
        if st.button("📂 Torna al Menu Principale", key="back_menu"):
            st.session_state.active_view = "menu_file"
            st.session_state.active_app = None
            st.rerun()

# --- INTERFACCIA PRINCIPALE / CATALOGO ---
top_col1, top_col2, top_col3 = st.columns([2, 1, 1])
with top_col1:
    st.title("🔥 AuraSync OS v7.5 - Interattivo Stabile")
with top_col2:
    st.metric("👥 Protocolli Protetti", "Attivi")
with top_col3:
    st.write("") 
    if st.button(">> 📁 Menu App & 18+", type="secondary", use_container_width=True, key="toggle_menu"):
        st.session_state.active_view = "menu_file" if st.session_state.active_view == "bacheca" else "bacheca"
        st.rerun()

st.divider()

if st.session_state.active_view == "bacheca":
    if st.session_state.active_app:
        render_active_app_interface(st.session_state.active_app)
    else:
        st.subheader("📦 Dashboard Principale - Moduli Selezionati 18+")
        st.info("• Clicca sul pulsante in alto a destra (**>> 📁 Menu App & 18+**) per aprire il catalogo completo e avviare i moduli.")
else:
    st.header("📂 Catalogo Completo Selezionato")
    ai_query = st.text_input("🤖 Cerca nel catalogo:", placeholder="Es. nocturne, red secrets, chemistry...", key="search_cat")
    st.divider()

    for category, files in AURASYNC_CATALOG.items():
        st.subheader(category)
        cols = st.columns(2)
        for idx, (file_name, file_desc) in enumerate(files):
            with cols[idx % 2]:
                st.markdown(f"""
                <div style="border: 1px solid #d0d0d0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #fafafa; min-height: 150px;">
                    <h4 style="margin-bottom: 5px; font-size: 15px;">⚡ {file_name}</h4>
                    <p style="font-size: 12px; color: #555; margin-bottom: 10px;">{file_desc}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🚀 Avvia Modulo", key=f"btn_launch_{category}_{idx}"):
                    st.session_state.active_app = file_name
                    st.session_state.active_view = "bacheca"
                    st.rerun()
        st.divider()
    
    if st.button("🔙 Torna alla Bacheca Principale", key="back_from_cat"):
        st.session_state.active_view = "bacheca"
        st.rerun()
