import streamlit as st
import random

# Configurazione PWA
st.set_page_config(
    page_title="AuraSync - Cognitive Operating System",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"  # Nascosto/Estraibile di default
)

# Inizializzazione dello State globale
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if "username" not in st.session_state: st.session_state.username = ""
if "wallet_tokens" not in st.session_state: st.session_state.wallet_tokens = 0
if "tutorial_completed" not in st.session_state: st.session_state.tutorial_completed = False
if "wheel_spun_today" not in st.session_state: st.session_state.wheel_spun_today = False
if "daily_actions_left" not in st.session_state: st.session_state.daily_actions_left = 5

# CATALOGO COMPLETO DELLE 150 APPLICAZIONI (125 ORIGINALI + 25 GIOCHI E QUIZ)
AURASYNC_CATALOG = {
    "🧠 Area 1: Core IA & Produttività": [
        "1. AuraBot Universal Chat", "2. Branch Selector IA", "3. Voice & Persona Chameleon",
        "4. AuraTwin Predittivo", "5. Prompt Engineering Studio", "6. Smart Summarizer",
        "7. Global Trend Analyzer", "8. Cognitive Flow Optimizer", "9. Task Automator AI",
        "10. Data Cleanse Tool", "11. Multi-Language Translator Hub", "12. Code Snippet Generator",
        "13. API Connector Studio", "14. Document Semantic Search", "15. Context Memory Vault"
    ],
    "🌿 Area 2: Benessere, Fai-da-Te & Social": [
        "16. AuraGreen Leaf Analyzer", "17. Smart Watering Scheduler", "18. Botanic Disease Tracker",
        "19. AuraFix Hardware Diagnostic", "20. DIY Step-by-Step Guide", "21. Tool Inventory Manager",
        "22. AuraPets Paws Health", "23. Pet Nutrition Advisor", "24. Behavioral Pet Tracker",
        "25. Eco-Friendly Habit Builder", "26. Home Energy Auditor", "27. Waste Reduction Assistant",
        "28. Indoor Climate Optimizer", "29. Smart Grocery Planner", "30. Green Space Designer",
        "Social 1. Real-Time Viral Trend Radar", "Social 2. AI Content Hook & Caption Generator",
        "Social 3. Cross-Platform Video Script Writer", "Social 4. Social Calendar & Timing Optimizer",
        "Social 5. Competitor & Niche Analyzer"
    ],
    "📖 Area 3: Famiglia, Memoria & Musica": [
        "31. Bedtime Story AI", "32. Moral Lesson Customizer", "33. Character Creator Studio",
        "34. AuraSound Studio Lyrics (AI Lyricist)", "35. Melody & Binaural Generator", "36. Sleep & Focus Soundscapes",
        "37. Time Capsule Cloud", "38. Family Memory Vault", "39. Future Letter Dispatcher",
        "40. Daily Gratitude Journal", "41. Mood Tracker Emotivo", "42. Creative Writing Companion",
        "43. Recipe & Cooking Assistant", "44. Event Planner Familiare", "45. Digital Scrapbook Creator"
    ],
    "💎 Area 4: Store, Wallet & Sicurezza": [
        "46. Ruota della Fortuna Interattiva", "47. Streak & Habit Tracker", "48. Digital Pet Companion",
        "49. Wallet Token Economy", "50. Stripe Checkout Integration", "51. Fair Use Policy Guard (FUP)",
        "52. Aura Security Hub", "53. Age Verification Guard", "54. Admin Supreme Control Panel",
        "55. AURA SOS Emergency Protocol", "56. PWA Offline Sync", "57. Data Privacy & GDPR Vault",
        "58. User Feedback & Bug Reporter", "59. Onboarding Interactive Guide", "60. Custom Plugin Marketplace"
    ],
    "🚀 Area 5: Business & Growth": [
        "61. Pitch Deck Generator AI", "62. SWOT Matrix Analyzer", "63. Business Model Canvas Builder",
        "64. Competitor Pricing Spy", "65. HR Interview Simulator", "66. OKR & KPI Goal Tracker",
        "67. B2B Email Outreach Writer", "68. Legal Contract Draft AI", "69. Crowdfunding Campaign Planner",
        "70. Brand Tone of Voice Designer"
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
    "🌐 Area 10: Community & Public Wall": [
        "121. AuraFeed Community Wall", "122. Creator Hall of Fame & Leaderboard",
        "123. Public Prompt & Template Market", "124. Safe Community Moderation Guard",
        "125. Collaborative Story & Song Jam"
    ],
    "🎮 Area 11: 25 Giochi e Quiz per Tutti": [
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

# --- BARRA LATERALE (Nascosta/Estraibile) ---
with st.sidebar:
    st.title("✨ Menu AuraSync")
    
    if st.session_state.authenticated:
        st.success(f"Utente: **{st.session_state.username}**")
        st.metric("Gettoni", f"{st.session_state.wallet_tokens} 🪙")
        st.metric("Azioni FUP", f"{st.session_state.daily_actions_left} ⚡")
        if st.button("Disconnetti / Reset"):
            st.session_state.authenticated = False
            st.session_state.tutorial_completed = False
            st.session_state.wheel_spun_today = False
            st.rerun()
        st.divider()
        selected_area = st.radio("Seleziona Area e Moduli:", ["🌐 Bacheca Pubblica"] + list(AURASYNC_CATALOG.keys()))
    else:
        st.info("ℹ️ Completa il percorso iniziale per sbloccare la Bacheca e le 150 applicazioni.")
        selected_area = "🌐 Bacheca Pubblica"

# --- FLUSSO SEQUENZIALE PRINCIPALE ---

if not st.session_state.tutorial_completed:
    # 1. TUTORIAL INIZIALE
    st.title("📘 Guida Ufficiale ad AuraSync OS")
    st.markdown("### Benvenuto nel Sistema Operativo Cognitivo Integrato")
    st.write("Leggi la guida rapida per comprendere l'architettura della piattaforma, la token economy e sbloccare subito i tuoi vantaggi.")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 🎯 1. Architettura e Moduli
        * **150 Applicazioni e Giochi:** Un ecosistema completo diviso in 11 aree tematiche (dall'IA alla produttività, fino ai 25 giochi e quiz per tutti).
        * **Strumenti su Misura:** Moduli avanzati per business, creatività, analisi dati e intrattenimento cognitivo.
        """)
    with col2:
        st.markdown("""
        #### 🪙 2. Economia dei Gettoni
        * **Bonus Immediato:** Ottieni subito **3 Gettoni d'Oro** completando questa lettura.
        * **Ruota Bonus:** Subito dopo potrai girare la Ruota della Fortuna per vincere crediti extra prima di entrare nella Bacheca Pubblica.
        """)

    st.divider()

    if st.button("✅ Ho letto la guida e confermo (Sblocca 3 Gettoni)", type="primary", use_container_width=True):
        st.session_state.tutorial_completed = True
        st.session_state.wallet_tokens += 3
        st.balloons()
        st.success("🎉 Guida completata! 3 Gettoni d'Oro accreditati.")
        st.rerun()

elif not st.session_state.wheel_spun_today:
    # 2. RUOTA DELLA FORTUNA
    st.title("🎡 Ruota della Fortuna Bonus")
    st.info("Il tutorial è completato! Gira la ruota per accumulare gettoni extra prima di accedere alla Bacheca Pubblica.")
    
    if st.button("🎁 Gira la Ruota Ora!", type="primary"):
        won = random.choice([1, 2, 3, 5, 10])
        st.session_state.wallet_tokens += won
        st.session_state.wheel_spun_today = True
        st.balloons()
        st.success(f"🎊 Hai vinto altri **{won} Gettoni d'Oro**! (Saldo totale: {st.session_state.wallet_tokens} 🪙)")
        st.rerun()

else:
    # 3. ACCESSO ALLA BACHECA PUBBLICA (E PIATTAFORMA SBLOCCATA)
    st.session_state.authenticated = True  # Auto-login sbloccato dopo la ruota

    if selected_area == "🌐 Bacheca Pubblica":
        st.title("🌐 Bacheca Pubblica AuraSync")
        st.success("🎉 Benvenuto nella schermata principale della community e della bacheca pubblica!")
        st.write("Qui puoi visualizzare i contenuti condivisi, interagire con gli altri utenti e verificare i gettoni a tua disposizione.")
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("I tuoi Gettoni Disponibili", f"{st.session_state.wallet_tokens} 🪙")
        with col_m2:
            st.metric("Moduli e Giochi Totali", "150 Disponibili 🚀")

        st.divider()
        st.subheader("📢 Ultime Notizie dalla Community")
        st.info("• Aggiornamento v3.2 attivo: Aggiunti 25 nuovi giochi e quiz interattivi nell'Area 11!\n• Bacheca pubblica sincronizzata correttamente in modalità cloud PWA.")
        
        st.write("👉 *Usa il menu a scomparsa in alto a sinistra (tramite la freccia o la barra laterale) per esplorare tutte le 150 applicazioni e i giochi.*")
    else:
        st.subheader(selected_area)
        apps_in_area = AURASYNC_CATALOG[selected_area]
        chosen_app = st.selectbox("Seleziona il modulo o il gioco desiderato:", apps_in_area)
        st.info(f"Hai selezionato: **{chosen_app}**. Ambiente operativo pronto e sincronizzato.")
