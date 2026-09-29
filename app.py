import streamlit as st
import random

# Configurazione PWA
st.set_page_config(
    page_title="AuraSync - Cognitive Operating System",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inizializzazione dello State globale
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if "username" not in st.session_state: st.session_state.username = ""
if "wallet_tokens" not in st.session_state: st.session_state.wallet_tokens = 0
if "pet_health" not in st.session_state: st.session_state.pet_health = 100
if "tutorial_completed" not in st.session_state: st.session_state.tutorial_completed = False
if "wheel_spun_today" not in st.session_state: st.session_state.wheel_spun_today = False
if "daily_actions_left" not in st.session_state: st.session_state.daily_actions_left = 5

# CATALOGO CENTRALE DELLE 125 APPLICAZIONI DI AURASYNC
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
    ]
}

# --- BARRA LATERALE ---
with st.sidebar:
    st.title("✨ AuraSync PWA")
    
    if st.session_state.authenticated:
        st.success(f"Utente: **{st.session_state.username}**")
        st.metric("Gettoni", f"{st.session_state.wallet_tokens} 🪙")
        st.metric("Azioni FUP", f"{st.session_state.daily_actions_left} ⚡")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.tutorial_completed = False
            st.session_state.wheel_spun_today = False
            st.rerun()
        st.divider()
        selected_area = st.radio("Seleziona Area:", ["🏠 Dashboard Centrale"] + list(AURASYNC_CATALOG.keys()))
    else:
        st.info("ℹ️ Segui il tutorial vocale e il video prima di accedere.")
        selected_area = "🏠 Dashboard Centrale"

# --- FLUSSO PRE-LOGIN: 1. VOCE PARLANTE E VIDEO -> 2. RUOTA -> 3. LOGIN ---

if not st.session_state.tutorial_completed:
    st.title("🎬 Video Tutorial Ufficiale (Mappatura 125 App)")
    st.warning("🎧 **Voce Guida Attiva:** Clicca sul pulsante qui sotto per ascoltare la spiegazione vocale e sbloccare **3 Gettoni d'Oro omaggio**!")

    # Sintesi vocale integrata del browser in Italiano (Voce parlante reale)
    st.markdown("""
        <div style="padding: 20px; background: rgba(0, 200, 255, 0.08); border-radius: 12px; border: 1px solid rgba(0, 200, 255, 0.2); margin-bottom: 20px;">
            <p style="font-size: 1.1em; color: #00bcd4; font-weight: bold; margin-bottom: 8px;">🎙️ Sintesi Vocale in Italiano:</p>
            <button onclick="
                const utterance = new SpeechSynthesisUtterance('Benvenuta in AuraSync! Ti guiderò attraverso la mappatura completa delle nostre centoventicinque mini applicazioni, suddivise in dieci aree strategiche. Guarda il video qui sotto per scoprire come sfruttare al massimo ogni funzione.');
                utterance.lang = 'it-IT';
                utterance.rate = 1.0;
                window.speechSynthesis.speak(utterance);
            " style="background-color: #00bcd4; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer;">
                🔊 Ascolta la Voce Guida
            </button>
            <p style="font-style: italic; color: #e0e0e0; margin-top: 12px;">
            "Benvenuta in AuraSync! Ti guiderò attraverso la mappatura completa delle nostre 125 mini-applicazioni cognitive, 
            suddivise in 10 aree strategiche..."
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Video dimostrativo
    st.video("https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4")

    st.markdown("""
    ### 🗺️ Le 10 Aree Principali Illustrate:
    * **Area 1-3:** IA & Produttività, Benessere & Fai-da-te, Famiglia & Musica.
    * **Area 4-6:** Store/Wallet, Business & Growth, Design & UI/UX.
    * **Area 7-10:** Data Science, Life Coaching, Teen Empowerment e Community Wall.
    """)
    
    if st.button("✅ Ho completato la visione e l'ascolto (Ricevi 3 Gettoni)", type="primary"):
        st.session_state.tutorial_completed = True
        st.session_state.wallet_tokens += 3
        st.balloons()
        st.success("🎉 Fantastico! Tutorial completato. 3 Gettoni d'Oro accreditati.")
        st.rerun()

elif not st.session_state.wheel_spun_today:
    # FASE 2: Ruota della Fortuna
    st.title("🎡 Ruota della Fortuna Bonus")
    st.info("Il tutorial è completato! Gira la ruota per vincere gettoni extra prima di effettuare il login.")
    
    if st.button("🎁 Gira la Ruota Ora!", type="primary"):
        won = random.choice([1, 2, 3, 5, 10])
        st.session_state.wallet_tokens += won
        st.session_state.wheel_spun_today = True
        st.balloons()
        st.success(f"🎊 Hai vinto altri **{won} Gettoni d'Oro**! (Totale: {st.session_state.wallet_tokens})")
        st.rerun()

elif not st.session_state.authenticated:
    # FASE 3: Schermata di Login finale
    st.title("🔐 Accesso a AuraSync PWA")
    st.success(f"Ottimo! Hai completato il tutorial e la ruota. Possiedi **{st.session_state.wallet_tokens} Gettoni d'Oro** omaggio.")
    st.write("Inserisci il tuo username per entrare nella dashboard e sbloccare tutte le 125 mini-applicazioni.")
    
    with st.form("login_form"):
        username_input = st.text_input("Scegli il tuo Username:")
        submit_login = st.form_submit_button("Entra nella Piattaforma 🚀", type="primary")
        
        if submit_login:
            if username_input.strip():
                st.session_state.authenticated = True
                st.session_state.username = username_input.strip()
                st.rerun()
            else:
                st.error("Inserisci un username valido per continuare.")

else:
    # FASE 4: Piattaforma pienamente sbloccata
    if selected_area == "🏠 Dashboard Centrale":
        st.subheader(f"Bentornato, {st.session_state.username}! 🌟")
        st.write("Tutti i sistemi di AuraSync sono attivi. Scegli un'area dal menu laterale per esplorare le 125 mini-applicazioni.")
        st.metric("I tuoi Gettoni Disponibili", f"{st.session_state.wallet_tokens} 🪙")
    else:
        st.subheader(selected_area)
        apps_in_area = AURASYNC_CATALOG[selected_area]
        chosen_app = st.selectbox("Seleziona la Mini-Applicazione:", apps_in_area)
        st.info(f"Hai selezionato: **{chosen_app}**. Modulo pronto per l'esecuzione.")
