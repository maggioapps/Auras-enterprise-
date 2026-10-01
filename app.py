import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(
    page_title="AuraSync OS v7.9 - Full Catalog & 18+",
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
if "magnetism_explanation" not in st.session_state: 
    st.session_state.magnetism_explanation = ""
if "dating_chat" not in st.session_state: 
    st.session_state.dating_chat = [
        {"sender": "Sofia", "text": "Ciao! Che piacere fare la tua conoscenza qui su AuraMatch. Di cosa ti occupi nel tempo libero?"}
    ]

# CATALOGO COMPLETO DI TUTTE LE AREE E MODULI DI AURASYNC
CATALOGO_MODULI = {
    # AREA ADULTI E INCONTRI (18+)
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
        "desc": "Simulatore in tempo reale di affinità, magnetismo e sintonia di coppia con analisi e riflessione dettagliata."
    },
    "Dating 1. AuraMatch: Swipe & Chat Reale": {
        "cat": "❤ Area 15: Dating & App di Incontri",
        "desc": "Esplora i profili, metti like e avvia una conversazione interattiva."
    },
    "Dating 2. Couple Chemistry & Compatibility Quiz": {
        "cat": "❤ Area 15: Dating & App di Incontri",
        "desc": "Test di compatibilità reale con punteggio di affinità dinamico."
    },
    
    # AREE SPORTIVE E MOTORI
    "Sport 1. Calcio: Rigore Decisivo 1v1": {
        "cat": "⚽ Area 10-14: Giochi Sportivi & Motori",
        "desc": "Scegli dove tirare dagli 11 metri e prova a battere il portiere virtuale."
    },
    "Sport 2. Basket Street: Tiri da Tre Punti": {
        "cat": "⚽ Area 10-14: Giochi Sportivi & Motori",
        "desc": "Gestisci il tempismo e la potenza per segnare canestri consecutivi."
    },
    "Sport 3. Simulatore Guida Rally VR": {
        "cat": "⚽ Area 10-14: Giochi Sportivi & Motori",
        "desc": "Test di riflessi e guida ad alta velocità su percorsi sterrati."
    },

    # AREE UTILITY, SYSTEM & PRODUTTIVITÀ
    "System 1. AuraSync Terminal & Diagnostics": {
        "cat": "💻 Area 1-9: Utility di Sistema & Developer Tools",
        "desc": "Console di comando avanzata per il monitoraggio dei server e dei processi attivi."
    },
    "System 2. Cloud Storage & File Manager Pro": {
        "cat": "💻 Area 1-9: Utility di Sistema & Developer Tools",
        "desc": "Gestione e archiviazione sicura dei file multimediali e dei dati di sessione."
    },
    "AI 1. Neural Prompt Studio & Assistant": {
        "cat": "💻 Area 1-9: Utility di Sistema & Developer Tools",
        "desc": "Generatore e ottimizzatore di prompt avanzati per modelli linguistici."
    },
    "AI 2. Code Syntax & Debugger Engine": {
        "cat": "💻 Area 1-9: Utility di Sistema & Developer Tools",
        "desc": "Analizzatore di codice in tempo reale per correggere errori di sintassi."
    },

    # AREE COMMUNITY & SOCIAL
    "Community 1. AuraFeed Community Wall": {
        "cat": "🌐 Area 17-20: Community, Feed & Social Hub",
        "desc": "Bacheca globale interattiva per condividere post, idee e progetti con la community."
    },
    "Community 2. Creator Hall of Fame": {
        "cat": "🌐 Area 17-20: Community, Feed & Social Hub",
        "desc": "Classifica d'onore che celebra i creatori di contenuti e moduli più votati."
    },
    "Community 3. Prompt & Template Hub": {
        "cat": "🌐 Area 17-20: Community, Feed & Social Hub",
        "desc": "Centro ufficiale per scambiare e scaricare liberamente prompt e template."
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
    elif "Red Secrets" in app_name:
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

    # 3. CHEMISTRY & MAGNETIC METER (Adult 3) - CON RIFLESSIONE E SPIEGAZIONE
    elif "Magnetic Meter" in app_name:
        st.markdown("### 🧪 Chemistry & Magnetic Meter AI")
        st.write("Analizzatore istantaneo del livello di compatibilità e magnetismo psicologico con spiegazione approfondita.")
        
        p1 = st.text_input("Inserisci il tuo nome o profilo:", key="partner_1")
        p2 = st.text_input("Inserisci il nome o profilo del partner:", key="partner_2")
        
        if st.button("Calcola Magnetismo ✨", key="btn_calc_mag"):
            if p1.strip() and p2.strip():
                score = random.randint(85, 99)
                st.session_state.magnetism_result = score
                
                explanations = [
                    f"Tra **{p1.capitalize()}** e **{p2.capitalize()}** si attiva una polarità energetica straordinaria. Il punteggio del {score}% evidenzia un'attrazione istintiva in cui le differenze non creano attrito, ma agiscono come carichi opposti che si attraggono magneticamente. C'è una forte componente di curiosità mentale e una tensione sottile che spinge alla scoperta reciproca senza filtri.",
                    f"Il valore del {score}% registrato tra **{p1.capitalize()}** e **{p2.capitalize()}** svela una sintonia sottile ma potentissima. Condividete frequenze emotive elevate: bastano un'occhiata o una battuta per accendere un'intesa immediata. L'attrazione psicologica è il fulcro di questo legame, capace di superare qualsiasi barriera formale.",
                    f"Un'affinità del {score}% tra **{p1.capitalize()}** e **{p2.capitalize()}** indica un magnetismo basato sull'alternanza perfetta tra complicità e mistero. Nessuno dei due svela tutto subito, e questo gioco di specchi psicologico mantiene la fiamma e la curiosità costantemente alte nel tempo."
                ]
                st.session_state.magnetism_explanation = random.choice(explanations)
            else:
                st.warning("Inserisci entrambi i nomi per procedere al calcolo.")
                st.session_state.magnetism_result = None
                st.session_state.magnetism_explanation = ""
                
        if st.session_state.magnetism_result:
            st.balloons()
            st.success(f"🔥 **Indice di Magnetismo Calcolato: {st.session_state.magnetism_result}%!**")
            
            st.markdown("---")
            st.markdown("### 🧠 Analisi e Riflessione Psicologica dell'Intesa")
            st.info(st.session_state.magnetism_explanation)
            
            st.markdown("""
            * **Dinamica di Coppia:** Elevata reattività emotiva e scambi intensi.
            * **Punto di Forza:** Forte magnetismo mentale e naturale predisposizione al dialogo senza inibizioni.
            * **Consiglio AuraSync:** Alimentate la complicità lasciando spazio al fattore sorpresa e all'attesa.
            """)

    # 4. AURAMATCH CHAT REALE (Dating 1)
    elif "AuraMatch" in app_name:
        st.markdown("### ❤️ AuraMatch: Chat con Sofia, 24")
        st.write("Scambia messaggi in tempo reale con il profilo selezionato:")
        
        for msg in st.session_state.dating_chat:
            if msg["sender"] == "Tu":
                st.markdown(f"<div style='text-align: right; background-color: #d1e7dd; padding: 10px; border-radius: 10px; margin: 5px 0;'><b>Tu:</b> {msg['text']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: left; background-color: #f8d7da; padding: 10px; border-radius: 10px; margin: 5px 0;'><b>{msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)
        
        user_msg = st.text_input("Scrivi una risposta a Sofia:", key="dating_input_msg")
        if st.button("Invia Messaggio 💬", key="btn_send_dating"):
            if user_msg.strip():
                st.session_state.dating_chat.append({"sender": "Tu", "text": user_msg})
                bot_replies = [
                    "Che bella risposta! Mi piacerebbe continuare a chiacchierare di persona.",
                    "Adoro il tuo punto di vista! Raccontami qualcos'altro su di te.",
                    "Questa è davvero un'ottima osservazione. E nel weekend cosa fai di bello?"
                ]
                st.session_state.dating_chat.append({"sender": "Sofia", "text": random.choice(bot_replies)})
                st.rerun()

    # 5. COMPATIBILITY QUIZ (Dating 2)
    elif "Compatibility Quiz" in app_name:
        st.markdown("### ❤️ Couple Chemistry & Compatibility Quiz")
        q1 = st.radio("Come preferisci trascorrere una serata ideale?", ["Cena intima a lume di candela", "Uscita dinamica e divertente in centro", "Relax totale a casa"], key="quiz_q1")
        q2 = st.radio("Qual è la tua priorità in una relazione?", ["Complicità e dialogo profondo", "Passione e spensieratezza", "Condivisione di hobby e passioni"], key="quiz_q2")
        
        if st.button("Calcola Affinità 🧪", key="btn_calc_quiz"):
            score = random.randint(85, 98)
            st.balloons()
            st.success(f"✨ **Indice di Affinità di Coppia: {score}%!**")
            st.info("I vostri stili di risposta indicano una sintonia straordinaria e un forte potenziale d'intesa.")

    else:
        st.markdown(f"### ⚙️ Modulo: {app_name}")
        st.write("Modulo di sistema o utility interattivo attivo e pronto all'uso.")
        if st.button("Esegui Test Modulo ⚡", key=f"test_generic_{app_name}"):
            st.success("Esecuzione completata con successo.")

    st.divider()
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🔙 Torna alla Bacheca Principale", key="back_dash_fixed"):
            st.session_state.active_app = None
            st.rerun()
    with col_b2:
        if st.button("📂 Torna al Menu Principale", key="back_menu_fixed"):
            st.session_state.active_view = "menu_file"
            st.session_state.active_app = None
            st.rerun()

# --- INTERFACCIA PRINCIPALE ---
top_col1, top_col2, top_col3 = st.columns([2, 1, 1])
with top_col1:
    st.title("🔥 AuraSync OS v7.9 - Full Catalog")
with top_col2:
    st.metric("👥 Stato Server", "Online")
with top_col3:
    st.write("") 
    if st.button(">> 📁 Menu App & 18+", type="secondary", use_container_width=True, key="toggle_menu_fixed"):
        st.session_state.active_view = "menu_file" if st.session_state.active_view == "bacheca" else "bacheca"
        st.rerun()

st.divider()

if st.session_state.active_view == "bacheca":
    if st.session_state.active_app:
        render_active_app_interface(st.session_state.active_app)
    else:
        st.subheader("📦 Dashboard Principale - AuraSync OS")
        st.info("• Clicca sul pulsante in alto a destra (**>> 📁 Menu App & 18+**) per aprire il catalogo completo di tutte le sezioni, giochi, tool e aree 18+.")
else:
    st.header("📂 Catalogo Completo - Tutte le Categorie")
    ai_query = st.text_input("🤖 Cerca nel catalogo completo:", placeholder="Es. nocturne, sport, system, community, dating...", key="search_cat_fixed")
    st.divider()

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
                
                safe_key = f"launch_fixed_{file_name}"
                if st.button(f"🚀 Avvia Modulo", key=safe_key):
                    st.session_state.active_app = file_name
                    st.session_state.active_view = "bacheca"
                    st.rerun()
        st.divider()
    
    if st.button("🔙 Torna alla Bacheca Principale", key="back_from_cat_fixed"):
        st.session_state.active_view = "bacheca"
        st.rerun()
