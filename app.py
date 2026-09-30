import streamlit as st
import random
import time

# Configurazione PWA
st.set_page_config(
    page_title="AuraSync - Cognitive Operating System",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inizializzazione dello State globale
if "tutorial_completed" not in st.session_state: st.session_state.tutorial_completed = False
if "wheel_spun_today" not in st.session_state: st.session_state.wheel_spun_today = False
if "wallet_tokens" not in st.session_state: st.session_state.wallet_tokens = 0
if "wheel_result_val" not in st.session_state: st.session_state.wheel_result_val = None
if "active_view" not in st.session_state: st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: st.session_state.active_app = None

# CATALOGO COMPLETO DELLE 150 APPLICAZIONI (Ordinate per importanza)
AURASYNC_CATALOG = {
    "🌐 Bacheca Pubblica": [
        "🌐 AuraFeed Community Wall", "⭐ Creator Hall of Fame", "🛒 Prompt & Template Market", "🛡️ Moderation Guard"
    ],
    "🧠 Area 1: Core IA & Produttività": [
        "1. AuraBot Universal Chat", "2. Branch Selector IA", "3. Voice & Persona Chameleon",
        "4. AuraTwin Predittivo", "5. Prompt Engineering Studio", "6. Smart Summarizer",
        "7. Global Trend Analyzer", "8. Cognitive Flow Optimizer", "9. Task Automator AI",
        "10. Data Cleanse Tool", "11. Multi-Language Translator Hub", "12. Code Snippet Generator",
        "13. API Connector Studio", "14. Document Semantic Search", "15. Context Memory Vault"
    ],
    "🚀 Area 2: Business & Growth": [
        "61. Pitch Deck Generator AI", "62. SWOT Matrix Analyzer", "63. Business Model Canvas Builder",
        "64. Competitor Pricing Spy", "65. HR Interview Simulator", "66. OKR & KPI Goal Tracker",
        "67. B2B Email Outreach Writer", "68. Legal Contract Draft AI", "69. Crowdfunding Campaign Planner",
        "70. Brand Tone of Voice Designer"
    ],
    "💎 Area 3: Store, Wallet & Sicurezza": [
        "46. Ruota della Fortuna Interattiva", "47. Streak & Habit Tracker", "48. Digital Pet Companion",
        "49. Wallet Token Economy", "50. Stripe Checkout Integration", "51. Fair Use Policy Guard (FUP)",
        "52. Aura Security Hub", "53. Age Verification Guard", "54. Admin Supreme Control Panel",
        "55. AURA SOS Emergency Protocol", "56. PWA Offline Sync", "57. Data Privacy & GDPR Vault",
        "58. User Feedback & Bug Reporter", "59. Onboarding Interactive Guide", "60. Custom Plugin Marketplace"
    ],
    "🌿 Area 4: Benessere, Fai-da-Te & Social": [
        "16. AuraGreen Leaf Analyzer", "17. Smart Watering Scheduler", "18. Botanic Disease Tracker",
        "19. AuraFix Hardware Diagnostic", "20. DIY Step-by-Step Guide", "21. Tool Inventory Manager",
        "22. AuraPets Paws Health", "23. Pet Nutrition Advisor", "24. Behavioral Pet Tracker",
        "25. Eco-Friendly Habit Builder", "26. Home Energy Auditor", "27. Waste Reduction Assistant",
        "28. Indoor Climate Optimizer", "29. Smart Grocery Planner", "30. Green Space Designer",
        "Social 1. Real-Time Viral Trend Radar", "Social 2. AI Content Hook & Caption Generator",
        "Social 3. Cross-Platform Video Script Writer", "Social 4. Social Calendar & Timing Optimizer",
        "Social 5. Competitor & Niche Analyzer"
    ],
    "📖 Area 5: Famiglia, Memoria & Musica": [
        "31. Bedtime Story AI", "32. Moral Lesson Customizer", "33. Character Creator Studio",
        "34. AuraSound Studio Lyrics", "35. Melody & Binaural Generator", "36. Sleep & Focus Soundscapes",
        "37. Time Capsule Cloud", "38. Family Memory Vault", "39. Future Letter Dispatcher",
        "40. Daily Gratitude Journal", "41. Mood Tracker Emotivo", "42. Creative Writing Companion",
        "43. Recipe & Cooking Assistant", "44. Event Planner Familiare", "45. Digital Scrapbook Creator"
    ],
    "🎨 Area 6: Design & UI/UX": [
        "71. Color Palette Harmony AI", "72. UI/UX Wireframe Planner", "73. Logo Concept Generator",
        "74. Typography Pairer Pro", "75. AI Image Prompt Architect", "76. SVG Icon Code Creator",
        "77. UX Microcopy Writer", "78. Moodboard Visualizer", "79. Landing Page Structure Optimizer",
        "80. Accessibility (WCAG) Checker"
    ],
    "📊 Area 7: Data Science & Finanza": [
        "81. Personal Budget Planner", "82. Crypto & Portfolio Tracker", "83. CSV/Excel Data Cleaner",
        "84. SQL Query Builder AI", "85. Regex Pattern Generator", "86. Tax & Expense Estimator",
        "87. Statistical Data Interpreter", "88. Loan & Mortgage Calculator", "89. JSON/XML Data Formatter",
        "90. A/B Testing Statistical Calculator"
    ],
    "🧘 Area 8: Life Coaching & Mind": [
        "91. Daily Habit Loop Builder", "92. Guided Meditation Script Writer", "93. Procrastination Breaker",
        "94. Sleep Cycle Optimizer", "95. Book Notes & Summarizer", "96. Public Speaking Coach",
        "97. Digital Detox Tracker", "98. Relationship & Empathy Advisor", "99. Travel Itinerary Planner",
        "100. Life Vision Board Generator"
    ],
    "🎒 Area 9: Teen & Youth Empowerment": [
        "101. School Homework Helper", "102. Exam Anxiety & Study Planner", "103. Language & Slang Bridge",
        "104. Future Career Explorer", "105. Creative Writing & Manga Plotter", "106. Gamer Strategy & Build Planner",
        "107. Teen Mood & Vibe Journal", "108. Pocket Coding & Game Dev Coach", "109. Music & Beat Maker Lyrist",
        "110. Pocket Finance for Teens", "111. DIY Creative Room Decor", "112. Eco & Animal Activism Guide",
        "113. Public Speaking & Debate Trainer", "114. Book & Comic Club Tracker", "115. Smart Sport & Workout Tracker",
        "116. DIY Cosplay & Prop Planner", "117. Friends & Hangout Event Planner", "118. Digital Safety & Privacy Guardian",
        "119. DIY Photography & Reel Editor", "120. Dream & Goal Board for Teens"
    ],
    "🎮 Area 10: 25 Giochi e Quiz per Tutti": [
        "Game 1. Quiz di Cultura Generale IA", "Game 2. Rompicapo Logico Matematico",
        "Game 3. Indovina la Parola Segreta", "Game 4. Memory Test Cognitivo",
        "Game 5. Test di Intuito e Psicologia", "Game 6. Trivia su Cinema e Serie TV",
        "Game 7. Calcolatore di Compatibilità Zodiacale", "Game 8. Indovinelli Storici",
        "Game 9. Test di Velocità di Reazione", "Game 10. Labirinto Testuale Decisionale",
        "Game 11. Quiz di Geografia Mondiale", "Game 12. Indovina il Brand o il Logo",
        "Game 13. Sfida di Calcolo Mentale Rapido", "Game 14. Quiz sui Misteri dello Spazio",
        "Game 15. Test del QI Lirico e Musicale", "Game 16. Trova l'Intruso Logico",
        "Game 17. Quiz sulla Tecnologia del Futuro", "Game 18. Indovina la Curiosità Biologica",
        "Game 19. Sfida di Riddle ed Enigmi", "Game 20. Test di Creatività Espressiva",
        "Game 21. Quiz sulle Lingue del Mondo", "Game 22. Gioco della Torre di Hanoi IA",
        "Game 23. Test di Sopravvivenza in Natura", "Game 24. Quiz sull'Economia e Finanza Base",
        "Game 25. Il Grande Quiz Finale di AuraSync"
    ]
}

# --- FLUSSO PRINCIPALE ---

if not st.session_state.tutorial_completed:
    # 1. TUTORIAL SPECIFICO (20 SECONDI)
    st.title("📘 Manuale Operativo Ufficiale - AuraSync OS")
    st.markdown("### Benvenuto nel Sistema Operativo Cognitivo Integrato")
    
    st.write("""
    Questo sistema è progettato per offrirti un controllo totale su **150 moduli avanzati, strumenti di IA e giochi interattivi**. 
    Ecco come è strutturata la tua esperienza:
    
    * **🪙 Wallet e Gettoni d'Oro:** All'avvio riceverai gettoni omaggio che potrai incrementare tramite la Ruota della Fortuna per sbloccare funzionalità premium.
    * **📂 Menu a Icone e Dettagli:** Cliccando sulle frecce in alto a destra `(>> 📁 Apri Menu File)` si aprirà la pagina interattiva con tutte le 150 applicazioni disposte a icona, complete di dettagli e pulsanti di avvio rapido.
    * **🔍 Barra di Ricerca Interna:** Trova istantaneamente qualsiasi applicazione digitando una parola chiave nel menu.
    """)
    
    st.info("⏳ **Il tutorial avanzato si chiuderà automaticamente tra 20 secondi** accreditando subito **3 Gettoni d'Oro** nel tuo wallet...")

    bar = st.progress(0)
    status_placeholder = st.empty()

    for i in range(20):
        status_placeholder.text(f"Chiusura automatica tra {20 - i} secondi...")
        bar.progress((i + 1) * 5)
        time.sleep(1)

    st.session_state.tutorial_completed = True
    st.session_state.wallet_tokens += 3
    st.rerun()

elif not st.session_state.wheel_spun_today:
    # 2. RUOTA DELLA FORTUNA CON CHIUSURA E APERTURA AUTOMATICA DELLA BACHECA
    st.title("🎡 Ruota della Fortuna Rotonda")
    st.write("Il tutorial è stato completato! Premi **START** per far girare la ruota. Si chiuderà automaticamente aprendo la Bacheca.")

    st.markdown("""
    <style>
    .wheel-outer {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
    }
    .wheel-pointer {
        width: 0; height: 0; 
        border-left: 15px solid transparent;
        border-right: 15px solid transparent;
        border-bottom: 25px solid #ff4b4b;
        margin-bottom: -10px;
        z-index: 10;
    }
    .wheel {
        width: 260px; height: 260px;
        border-radius: 50%;
        border: 8px solid #222;
        background: conic-gradient(
            #00bcd4 0deg 72deg,
            #4caf50 72deg 144deg,
            #ffeb3b 144deg 216deg,
            #ff9800 216deg 288deg,
            #e91e63 288deg 360deg
        );
    }
    </style>
    <div class="wheel-outer">
        <div class="wheel-pointer"></div>
        <div class="wheel"></div>
    </div>
    """, unsafe_allow_html=True)

    col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
    with col_b2:
        if st.button("🚀 START - Gira la Ruota!", type="primary", use_container_width=True):
            won = random.choice([1, 2, 3, 5, 10])
            st.session_state.wallet_tokens += won
            st.session_state.wheel_spun_today = True
            st.session_state.wheel_result_val = won
            st.balloons()
            st.success(f"🎉 Hai vinto {won} Gettoni d'Oro! Apertura Bacheca in corso...")
            time.sleep(2.5)
            st.rerun()

else:
    # --- 3. INTERFACCIA PRINCIPALE ---
    
    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        st.title("🌐 Bacheca Pubblica AuraSync")
    with top_col2:
        st.write("") 
        if st.button(">> 📁 Apri Menu File", type="secondary", use_container_width=True):
            if st.session_state.active_view == "bacheca":
                st.session_state.active_view = "menu_file"
            else:
                st.session_state.active_view = "bacheca"
            st.rerun()

    st.divider()

    if st.session_state.active_view == "bacheca":
        if st.session_state.active_app:
            # Se un'app è stata avviata dal menu a icone
            st.header(f"🚀 Modulo Attivo: {st.session_state.active_app}")
            st.success(f"L'applicazione **{st.session_state.active_app}** è stata caricata con successo nell'area di lavoro.")
            st.write("Ambiente operativo pronto per l'elaborazione dei dati e l'interazione cognitiva.")
            
            col_back1, col_back2 = st.columns(2)
            with col_back1:
                if st.button("🔙 Torna alla Bacheca Principale"):
                    st.session_state.active_app = None
                    st.rerun()
            with col_back2:
                if st.button("📂 Torna al Menu a Icone"):
                    st.session_state.active_view = "menu_file"
                    st.session_state.active_app = None
                    st.rerun()
        else:
            st.success("🎉 Benvenuto nella schermata principale della community e della bacheca pubblica!")
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric("I tuoi Gettoni Disponibili", f"{st.session_state.wallet_tokens} 🪙")
            with col_m2:
                st.metric("Moduli e Giochi Totali", "150 Disponibili 🚀")

            st.divider()
            st.subheader("📢 Ultime Notizie dalla Community")
            st.info("• Aggiornamento attivo: Tutti i 150 moduli e giochi sono sincronizzati.\n• Usa il pulsante in alto a destra (**>> 📁 Apri Menu File**) per accedere al menu visivo a icone con dettagli e ricerca.")
        
    else:
        # --- MENU FILE E MODULI A ICONE E DETTAGLI (TUTTI E 150) ---
        st.header("📂 Menu Applicazioni - Vista a Icone e Dettagli")
        st.write(f"Gettoni nel Wallet: **{st.session_state.wallet_tokens} 🪙** | Esplora le 150 applicazioni suddivise per area.")
        
        # BARRA DI RICERCA INTERNA
        search_query = st.text_input("🔍 Cerca tra tutte le 150 applicazioni e giochi:", placeholder="Scrivi ad esempio 'Chat', 'Budget', 'Game', 'Eco'...")
        
        st.divider()

        if search_query:
            st.subheader(f"Risultati della ricerca per: '{search_query}'")
            found_items = []
            for area, files in AURASYNC_CATALOG.items():
                for f in files:
                    if search_query.lower() in f.lower():
                        found_items.append((area, f))
            
            if found_items:
                st.write(f"Trovati **{len(found_items)}** moduli corrispondenti:")
                cols = st.columns(3)
                for idx, (area, file_name) in enumerate(found_items):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #fafafa;">
                            <h4>🧩 {file_name}</h4>
                            <p style="font-size: 12px; color: #666;">Categoria: {area}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button(f"Avvia ➔ {file_name[:15]}...", key=f"search_{idx}"):
                            st.session_state.active_app = file_name
                            st.session_state.active_view = "bacheca"
                            st.rerun()
            else:
                st.warning("Nessun file trovato con questa parola chiave.")
        else:
            # MOSTRA PER CATEGORIE SOTTO FORMA DI GRIGLIA A ICONE E DETTAGLI
            for category, files in AURASYNC_CATALOG.items():
                st.subheader(category)
                cols = st.columns(3)
                for idx, file_item in enumerate(files):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div style="border: 1px solid #e0e0e0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #fcfcfc; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                            <h4 style="margin-bottom: 5px; font-size: 16px;">✨ {file_item}</h4>
                            <p style="font-size: 12px; color: #555; margin-bottom: 10px;">Modulo operativo integrato e pronto all'uso in ambiente AuraSync.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button(f"🚀 Avvia Modulo", key=f"btn_{category}_{idx}"):
                            st.session_state.active_app = file_item
                            st.session_state.active_view = "bacheca"
                            st.rerun()
                st.divider()
        
        if st.button("🔙 Torna alla Bacheca Pubblica"):
            st.session_state.active_view = "bacheca"
            st.rerun()
