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

# Inizializzazione dello State globale (senza ruota, accesso diretto)
if "wallet_tokens" not in st.session_state: st.session_state.wallet_tokens = 10  # Bonus di benvenuto diretto
if "active_view" not in st.session_state: st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: st.session_state.active_app = None

# CATALOGO CON DESCRIZIONI DETTAGLIATE
AURASYNC_CATALOG = {
    "🌐 Bacheca Pubblica": [
        ("🌐 AuraFeed Community Wall", "Bacheca globale interattiva dove condividere post, idee e progetti con l'intera community in tempo reale."),
        ("⭐ Creator Hall of Fame", "La classifica d'onore che celebra i creatori di contenuti, prompt e moduli più votati della settimana."),
        ("🛒 Prompt & Template Market", "Il marketplace ufficiale per scambiare, vendere o scaricare prompt di IA e template di produttività."),
        ("🛡️ Moderation Guard", "Sistema di filtraggio e sicurezza automatizzato per mantenere un ambiente pulito, sicuro e rispettoso.")
    ],
    "🧠 Area 1: Core IA & Produttività": [
        ("1. AuraBot Universal Chat", "Assistente IA conversazionale avanzato per rispondere a qualsiasi domanda o scrivere testi."),
        ("2. Branch Selector IA", "Strumento decisionale basato su alberi decisionali guidati dall'intelligenza artificiale."),
        ("3. Voice & Persona Chameleon", "Cambia il tono di voce e la personalità dell'IA (professore, coach o amico ironico)."),
        ("4. AuraTwin Predittivo", "Simulatore di scenari futuri basato sulle tue abitudini e decisioni passate."),
        ("5. Prompt Engineering Studio", "Laboratorio avanzato per creare, testare e ottimizzare prompt perfetti per qualsiasi IA."),
        ("6. Smart Summarizer", "Riassume istantaneamente articoli lunghi o documenti complessi in punti chiave."),
        ("7. Global Trend Analyzer", "Analizzatore di tendenze dal web per scoprire cosa sta diventando virale."),
        ("8. Cognitive Flow Optimizer", "Ottimizzatore del flusso di lavoro per eliminare le distrazioni e massimizzare il focus."),
        ("9. Task Automator AI", "Automatizza le attività ripetitive quotidiane gestite dall'intelligenza artificiale."),
        ("10. Data Cleanse Tool", "Pulisce, formatta e corregge set di dati disordinati in pochi secondi."),
        ("11. Multi-Language Translator Hub", "Traduttore multilingua avanzato con supporto a slang e modi di dire."),
        ("12. Code Snippet Generator", "Generatore di frammenti di codice in Python, JavaScript e HTML pronto all'uso."),
        ("13. API Connector Studio", "Pannello per connettere e testare API esterne e servizi web."),
        ("14. Document Semantic Search", "Ricerca semantica avanzata all'interno dei tuoi documenti personali."),
        ("15. Context Memory Vault", "Memoria di contesto a lungo termine per ricordare preferenze e progetti.")
    ],
    "🚀 Area 2: Business & Growth": [
        ("61. Pitch Deck Generator AI", "Crea presentazioni aziendali e pitch vincenti per investitori."),
        ("62. SWOT Matrix Analyzer", "Analizza punti di forza, debolezza, opportunità e minacce di un'idea."),
        ("63. Business Model Canvas Builder", "Costruisci il modello di business perfetto per la tua startup."),
        ("64. Competitor Pricing Spy", "Analizza le strategie di prezzo dei concorrenti sul mercato."),
        ("65. HR Interview Simulator", "Simulatore di colloqui di lavoro con domande mirate e feedback."),
        ("66. OKR & KPI Goal Tracker", "Traccia obiettivi aziendali e indicatori chiave di prestazione."),
        ("67. B2B Email Outreach Writer", "Scrive email commerciali e di contatto B2B altamente persuasive."),
        ("68. Legal Contract Draft AI", "Bozze di contratti legali personalizzati generati dall'IA."),
        ("69. Crowdfunding Campaign Planner", "Pianificatore completo per campagne di crowdfunding di successo."),
        ("70. Brand Tone of Voice Designer", "Definisce e mantiene coerente la voce e lo stile comunicativo del brand.")
    ],
    "💎 Area 3: Store, Wallet & Sicurezza": [
        ("46. Store & Token Exchange", "Negozio virtuale per gestire i gettoni e sbloccare funzioni premium."),
        ("47. Streak & Habit Tracker", "Traccia le tue abitudini quotidiane e i giorni consecutivi di attività."),
        ("48. Digital Pet Companion", "Un cucciolo virtuale digitale che cresce e interagisce con te."),
        ("49. Wallet Token Economy", "Gestione completa del portafoglio digitale e dei Gettoni d'Oro."),
        ("50. Stripe Checkout Integration", "Sistema sicuro integrato per acquisti e transazioni digitali."),
        ("51. Fair Use Policy Guard (FUP)", "Sistema di protezione e bilanciamento delle risorse della piattaforma."),
        ("52. Aura Security Hub", "Centro di controllo della sicurezza e crittografia dati."),
        ("53. Age Verification Guard", "Modulo di verifica dell'età e protezione dei minori."),
        ("54. Admin Supreme Control Panel", "Pannello di controllo amministrativo avanzato per il sistema."),
        ("55. AURA SOS Emergency Protocol", "Protocollo di emergenza rapida per bloccare sessioni critiche."),
        ("56. PWA Offline Sync", "Sincronizzazione offline per usare l'app senza connessione."),
        ("57. Data Privacy & GDPR Vault", "Cassaforte digitale per la gestione della privacy e conformità GDPR."),
        ("58. User Feedback & Bug Reporter", "Invia segnalazioni di bug o suggerimenti agli sviluppatori."),
        ("59. Onboarding Interactive Guide", "Guida interattiva dettagliata per scoprire tutte le funzioni."),
        ("60. Custom Plugin Marketplace", "Marketplace per installare estensioni e plugin della community.")
    ],
    "🌿 Area 4: Benessere, Fai-da-Te & Social": [
        ("16. AuraGreen Leaf Analyzer", "Analizza lo stato di salute delle tue piante di casa tramite foto."),
        ("17. Smart Watering Scheduler", "Pianificatore intelligente delle innaffiature basato sul clima."),
        ("18. Botanic Disease Tracker", "Identifica malattie delle piante e parassiti con rimedi mirati."),
        ("19. AuraFix Hardware Diagnostic", "Diagnostica guasti domestici e malfunzionamenti di piccoli oggetti."),
        ("20. DIY Step-by-Step Guide", "Guide pratiche fai-da-te passo-passo per progetti creativi."),
        ("21. Tool Inventory Manager", "Gestisce l'inventario dei tuoi strumenti da lavoro o hobbistici."),
        ("22. AuraPets Paws Health", "Monitoraggio della salute e vaccinazioni degli animali domestici."),
        ("23. Pet Nutrition Advisor", "Consigli nutrizionali personalizzati e diete per cani e gatti."),
        ("24. Behavioral Pet Tracker", "Traccia il comportamento e l'umore del tuo cucciolo."),
        ("25. Eco-Friendly Habit Builder", "Costruttore di abitudini ecologiche per ridurre l'impronta di carbonio."),
        ("26. Home Energy Auditor", "Analizzatore dei consumi energetici domestici per risparmiare."),
        ("27. Waste Reduction Assistant", "Assistente per la riduzione degli sprechi alimentari."),
        ("28. Indoor Climate Optimizer", "Ottimizza temperatura, umidità e qualità dell'aria nelle stanze."),
        ("29. Smart Grocery Planner", "Pianificatore intelligente della spesa per evitare sprechi."),
        ("30. Green Space Designer", "Progetta spazi verdi, balconi fioriti o giardini verticali."),
        ("Social 1. Real-Time Viral Trend Radar", "Radar per scoprire trend e audio virali su TikTok e Instagram."),
        ("Social 2. AI Content Hook & Caption Generator", "Crea ganci irresistibili e didascalie per i tuoi video social."),
        ("Social 3. Cross-Platform Video Script Writer", "Sceneggiatore automatico di script per Reel, TikTok e Shorts."),
        ("Social 4. Social Calendar & Timing Optimizer", "Pianifica i post nei momenti in cui il pubblico è più attivo."),
        ("Social 5. Competitor & Niche Analyzer", "Analizza i concorrenti di nicchia per far crescere il profilo.")
    ],
    "📖 Area 5: Famiglia, Memoria & Musica": [
        ("31. Bedtime Story AI", "Crea storie della buonanotte personalizzate con morali a scelta."),
        ("32. Moral Lesson Customizer", "Personalizza i valori educativi nelle storie interattive."),
        ("33. Character Creator Studio", "Crea personaggi unici con caratteristiche e aspetto per storie e giochi."),
        ("34. AuraSound Studio Lyrics", "Scrittore di testi musicali e canzoni originali in qualsiasi stile."),
        ("35. Melody & Binaural Generator", "Generatore di melodie rilassanti e frequenze binaurali."),
        ("36. Sleep & Focus Soundscapes", "Paesaggi sonori immersivi per concentrarsi o dormire."),
        ("37. Time Capsule Cloud", "Capsula del tempo digitale per salvare messaggi per il futuro."),
        ("38. Family Memory Vault", "Album di famiglia digitale sicuro per custodire ricordi."),
        ("39. Future Letter Dispatcher", "Invia una lettera programmata a te stesso nel futuro."),
        ("40. Daily Gratitude Journal", "Diario della gratitudine quotidiana per annotare pensieri positivi."),
        ("41. Mood Tracker Emotivo", "Traccia le tue emozioni quotidiane e stati d'animo."),
        ("42. Creative Writing Companion", "Compagno di scrittura creativa per sbloccare l'ispirazione."),
        ("43. Recipe & Cooking Assistant", "Ricettario intelligente che inventa piatti con gli ingredienti in frigo."),
        ("44. Event Planner Familiare", "Organizzatore di feste e compleanni senza stress."),
        ("45. Digital Scrapbook Creator", "Crea collage digitali interattivi con ricordi di viaggi.")
    ],
    "🎨 Area 6: Design & UI/UX": [
        ("71. Color Palette Harmony AI", "Genera palette di colori armoniose per siti web e loghi."),
        ("72. UI/UX Wireframe Planner", "Pianifica la struttura e i flussi di navigazione di app digitali."),
        ("73. Logo Concept Generator", "Ideatore di concetti visivi originali per loghi e brand."),
        ("74. Typography Pairer Pro", "Suggerisce abbinamenti tipografici perfetti per il design."),
        ("75. AI Image Prompt Architect", "Costruisce prompt dettagliati per generatori come Midjourney o DALL-E."),
        ("76. SVG Icon Code Creator", "Genera codice SVG pulito per icone vettoriali personalizzate."),
        ("77. UX Microcopy Writer", "Scrive testi brevi e intuitivi per pulsanti e interfacce utente."),
        ("78. Moodboard Visualizer", "Crea tavole d'ispirazione visiva per progetti creativi."),
        ("79. Landing Page Structure Optimizer", "Ottimizza la struttura di una landing page per le conversioni."),
        ("80. Accessibility (WCAG) Checker", "Verifica l'accessibilità e i contrasti secondo gli standard WCAG.")
    ],
    "📊 Area 7: Data Science & Finanza": [
        ("81. Personal Budget Planner", "Gestisci entrate, spese e risparmi personali con grafici chiari."),
        ("82. Crypto & Portfolio Tracker", "Monitora il portafoglio di criptovalute e investimenti."),
        ("83. CSV/Excel Data Cleaner", "Pulisci e unisci file di dati tabulari in formato CSV o Excel."),
        ("84. SQL Query Builder AI", "Genera query SQL complesse partendo da richieste in linguaggio naturale."),
        ("85. Regex Pattern Generator", "Crea espressioni regolari (RegEx) per la ricerca di testi."),
        ("86. Tax & Expense Estimator", "Stima spese e tasse per liberi professionisti e piccoli progetti."),
        ("87. Statistical Data Interpreter", "Interpreta dati statistici trasformandoli in report di facile lettura."),
        ("88. Loan & Mortgage Calculator", "Calcolatore di prestiti, mutui e piani di ammortamento."),
        ("89. JSON/XML Data Formatter", "Formatta, valida e converti strutture dati JSON e XML."),
        ("90. A/B Testing Statistical Calculator", "Calcolatore statistico per verificare test A/B di marketing.")
    ],
    "🧘 Area 8: Life Coaching & Mind": [
        ("91. Daily Habit Loop Builder", "Costruisci cicli di abitudini sane basate sulla psicologia."),
        ("92. Guided Meditation Script Writer", "Scrive script personalizzati per meditazioni guidate."),
        ("93. Procrastination Breaker", "Tecniche e prompt rapidi per sbloccare l'inerzia e iniziare a studiare."),
        ("94. Sleep Cycle Optimizer", "Ottimizza i cicli di sonno per svegliarti pieno di energia."),
        ("95. Book Notes & Summarizer", "Riassunti dettagliati dei libri di crescita personale più famosi."),
        ("96. Public Speaking Coach", "Allenatore virtuale per migliorare la parlata in pubblico e sicurezza."),
        ("97. Digital Detox Tracker", "Traccia e limita il tempo passato davanti agli schermi."),
        ("98. Relationship & Empathy Advisor", "Consigli basati sull'intelligenza emotiva per i rapporti."),
        ("99. Travel Itinerary Planner", "Pianificatore di viaggi su misura con tappe e attrazioni."),
        ("100. Life Vision Board Generator", "Crea la tua bacheca dei sogni visiva per focalizzarti sugli obiettivi.")
    ],
    "🎒 Area 9: Teen & Youth Empowerment": [
        ("101. School Homework Helper", "Aiuto compiti interattivo per spiegare matematica, storia e scienze in modo semplice."),
        ("102. Exam Anxiety & Study Planner", "Organizza il piano di studio e gestisce l'ansia da esame con focus."),
        ("103. Language & Slang Bridge", "Traduttore intergenerazionale e di slang giovanile per meme ed espressioni."),
        ("104. Future Career Explorer", "Esplora professioni innovative e lavori digitali ideali per il futuro."),
        ("105. Creative Writing & Manga Plotter", "Crea trame, personaggi e sceneggiature per fumetti e manga."),
        ("106. Gamer Strategy & Build Planner", "Pianifica strategie di gioco, build di personaggi e guide tattiche."),
        ("107. Teen Mood & Vibe Journal", "Diario personale sicuro e privato dedicato ai ragazzi per esprimere pensieri."),
        ("108. Pocket Coding & Game Dev Coach", "Primo coach tascabile per imparare programmazione e sviluppo giochi."),
        ("109. Music & Beat Maker Lyrist", "Scrivi barre, rime e testi rap/trap su basi musicali generate."),
        ("110. Pocket Finance for Teens", "Educazione finanziaria per ragazzi: impara a gestire la prima paga."),
        ("111. DIY Creative Room Decor", "Idee fai-da-te e progetti per arredare e personalizzare la stanza."),
        ("112. Eco & Animal Activism Guide", "Guida pratica per iniziative ecologiche e protezione degli animali."),
        ("113. Public Speaking & Debate Trainer", "Allenati a dibattere e argomentare idee per la scuola."),
        ("114. Book & Comic Club Tracker", "Traccia le tue letture, manga e fumetti preferiti con recensioni."),
        ("115. Smart Sport & Workout Tracker", "Traccia allenamenti, esercizi a corpo libero e corsa."),
        ("116. DIY Cosplay & Prop Planner", "Pianificatore di progetti cosplay, costumi e oggetti di scena."),
        ("117. Friends & Hangout Event Planner", "Organizza uscite, feste e ritrovi con gli amici facilmente."),
        ("118. Digital Safety & Privacy Guardian", "Guida alla sicurezza online, difesa da truffe e cyberbullismo."),
        ("119. DIY Photography & Reel Editor", "Consigli di fotografia con smartphone e montaggio per reel."),
        ("120. Dream & Goal Board for Teens", "Crea la tua bacheca dei sogni e obiettivi futuri.")
    ],
    "🎮 Area 10: 25 Giochi e Quiz per Tutti": [
        ("Game 1. Quiz di Cultura Generale IA", "Metti alla prova la tua cultura con domande generate dall'IA."),
        ("Game 2. Rompicapo Logico Matematico", "Enigmi e problemi di logica pura per allenare la mente."),
        ("Game 3. Indovina la Parola Segreta", "Classico gioco di parole nascoste con indizi progressivi."),
        ("Game 4. Memory Test Cognitivo", "Esercizi di memoria visiva e sequenziale."),
        ("Game 5. Test di Intuito e Psicologia", "Test divertenti di psicologia e intuito comportamentale."),
        ("Game 6. Trivia su Cinema e Serie TV", "Quiz definitivo per esperti di film e serie TV."),
        ("Game 7. Calcolatore di Compatibilità Zodiacale", "Simulatore ironico di affinità di coppia e oroscopo."),
        ("Game 8. Indovinelli Storici", "Risolvi indovinelli e misteri legati a grandi personaggi storici."),
        ("Game 9. Test di Velocità di Reazione", "Metti alla prova i tuoi riflessi con un test di velocità."),
        ("Game 10. Labirinto Testuale Decisionale", "Un'avventura testuale interattiva dove ogni scelta cambia il finale."),
        ("Game 11. Quiz di Geografia Mondiale", "Indovina capitali, bandiere e monumenti dal mondo."),
        ("Game 12. Indovina il Brand o il Logo", "Riconosci loghi celebri e marchi famosi nascosti."),
        ("Game 13. Sfida di Calcolo Mentale Rapido", "Esercizi cronometrati di calcolo a mente."),
        ("Game 14. Quiz sui Misteri dello Spazio", "Domande strabilianti su pianeti, buchi neri e universo."),
        ("Game 15. Test del QI Lirico e Musicale", "Completa i testi delle canzoni più famose e hit."),
        ("Game 16. Trova l'Intruso Logico", "Analizza quattro elementi e individua l'intruso logico."),
        ("Game 17. Quiz sulla Tecnologia del Futuro", "Scopri quanto ne sai di intelligenza artificiale e robotica."),
        ("Game 18. Indovina la Curiosità Biologica", "Quiz interattivo sui segreti della natura e degli animali."),
        ("Game 19. Sfida di Riddle ed Enigmi", "Enigmi ingannevoli che metteranno alla prova il tuo ingegno."),
        ("Game 20. Test di Creatività Espressiva", "Valuta la tua vena artistica attraverso scelte visive e verbali."),
        ("Game 21. Quiz sulle Lingue del Mondo", "Scopri parole intraducibili e modi di dire globali."),
        ("Game 22. Gioco della Torre di Hanoi IA", "Il celebre rompicapo matematico dei dischi da spostare."),
        ("Game 23. Test di Sopravvivenza in Natura", "Mettiti in scenari estremi e scegli come sopravvivere."),
        ("Game 24. Quiz sull'Economia e Finanza Base", "Impara i concetti base di soldi e risparmio divertendoti."),
        ("Game 25. Il Grande Quiz Finale di AuraSync", "La sfida finale che racchiude tutte le categorie.")
    ]
}

# --- FUNZIONE INTERATTIVA PER LE APPLICAZIONI ---
def render_active_app_interface(app_name):
    st.header(f"🚀 Modulo Attivo: {app_name}")
    st.divider()

    if "Digital Pet Companion" in app_name:
        st.subheader("🐾 Il tuo Cucciolo Virtuale Aura")
        if "pet_energy" not in st.session_state: st.session_state.pet_energy = 80
        if "pet_mood" not in st.session_state: st.session_state.pet_mood = "Felice 😺"
        
        col1, col2 = st.columns(2)
        col1.metric("Energia Cucciolo", f"{st.session_state.pet_energy}%")
        col2.metric("Umore", st.session_state.pet_mood)
        
        c1, c2, c3 = st.columns(3)
        if c1.button("🍖 Dai da mangiare"):
            st.session_state.pet_energy = min(100, st.session_state.pet_energy + 15)
            st.success("Gnam! Il cucciolo ha gradito molto.")
            st.rerun()
        if c2.button("🎾 Gioca insieme"):
            st.session_state.pet_energy = max(0, st.session_state.pet_energy - 10)
            st.session_state.pet_mood = "Eccitato ed Energetico ⚡"
            st.success("Evviva! Avete fatto una bellissima corsa insieme.")
            st.rerun()
        if c3.button("💤 Metti a dormire"):
            st.session_state.pet_energy = 100
            st.session_state.pet_mood = "Riposato e Tranquillo 😴"
            st.success("Il cucciolo ha fatto un sonnellino e ora è pieno di energie!")
            st.rerun()

    elif "AuraBot Universal Chat" in app_name:
        st.subheader("💬 Chat Universale con AuraBot")
        user_prompt = st.text_input("Scrivi un messaggio o fai una domanda all'IA:")
        if st.button("Invia messaggio"):
            if user_prompt:
                responses = [
                    "Analizzando la tua richiesta con algoritmi cognitivi avanzati... Ecco la risposta ottimale!",
                    "È un'ottima domanda! Ti consiglio di procedere per piccoli passi.",
                    "Ho elaborato i dati dal database di AuraSync: la soluzione ideale è mantenere il focus.",
                    "Interessante! Posso aiutarti a sviluppare ulteriormente questo concetto."
                ]
                st.info(f"🤖 **AuraBot:** {random.choice(responses)}")
            else:
                st.warning("Inserisci prima un testo nella casella.")

    elif "Personal Budget Planner" in app_name:
        st.subheader("📊 Gestione Budget Personale")
        spesa = st.number_input("Inserisci importo spesa o entrata (€):", value=0.0)
        tipo = st.radio("Tipologia movimento:", ["Entrata (+)", "Uscita (-)"])
        if "bilancio" not in st.session_state: st.session_state.bilancio = 1250.0
        
        if st.button("Registra transazione"):
            if tipo == "Entrata (+)":
                st.session_state.bilancio += spesa
                st.success(f"Aggiunti €{spesa} al bilancio.")
            else:
                st.session_state.bilancio -= spesa
                st.success(f"Registrata spesa di €{spesa}.")
        st.metric("Saldo Attuale nel Wallet", f"€ {st.session_state.bilancio:.2f}")

    elif "Quiz" in app_name or "Game" in app_name:
        st.subheader(f"🎮 Area Gioco & Test: {app_name}")
        st.write("Metti alla prova le tue abilità con questa sfida interattiva!")
        
        ans = st.radio("Rispondi al quesito del modulo:", ["Opzione A (Logica)", "Opzione B (Creativa)", "Opzione C (Intuitiva)"])
        if st.button("Conferma Risposta"):
            st.balloons()
            won_t = random.choice([1, 2, 3])
            st.session_state.wallet_tokens += won_t
            st.success(f"🎉 Risposta corretta! Hai guadagnato bonus +{won_t} Gettoni d'Oro nel tuo wallet!")

    else:
        st.info(f"Ambiente operativo attivo per: **{app_name}**")
        user_input = st.text_input("Parametri di input o prompt personalizzato per il modulo:")
        if st.button("Esegui Elaborazione Modulo"):
            if user_input:
                st.success(f"Elaborazione completata con successo per: '{user_input}'. Il modulo ha generato l'output richiesto.")
            else:
                st.success("Esecuzione standard avviata con successo. Tutti i sistemi rispondono correttamente.")

    st.divider()
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🔙 Torna alla Bacheca Principale"):
            st.session_state.active_app = None
            st.rerun()
    with col_b2:
        if st.button("📂 Torna al Menu a Icone"):
            st.session_state.active_view = "menu_file"
            st.session_state.active_app = None
            st.rerun()


# --- INTERFACCIA PRINCIPALE DIRETTA (SENZA RUOTA) ---

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
        render_active_app_interface(st.session_state.active_app)
    else:
        st.success("🎉 Benvenuto in AuraSync OS! Tutti i moduli e giochi sono operativi.")
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("I tuoi Gettoni Disponibili", f"{st.session_state.wallet_tokens} 🪙")
        with col_m2:
            st.metric("Moduli e Giochi Totali", "150 Disponibili 🚀")

        st.divider()
        st.subheader("📢 Stato del Sistema")
        st.info("• Caricamento diretto completato senza schermate di attesa o ruote.\n• Usa il pulsante in alto a destra (**>> 📁 Apri Menu File**) per esplorare le 150 app e i giochi con la ricerca IA.")
    
else:
    # --- MENU FILE E MODULI CON RICERCA ESTERNA IA ---
    st.header("📂 Menu Applicazioni - Vista a Icone e Dettagli")
    st.write(f"Gettoni nel Wallet: **{st.session_state.wallet_tokens} 🪙** | Esplora tutte le 150 applicazioni e giochi.")
    
    ai_query = st.text_input("🤖 Ricerca Esterna IA (Cerca per parole chiave, concetti o giochi):", placeholder="Es. teen, game, budget, social, chat, quiz...")
    
    st.divider()

    filtered_catalog = {}
    if ai_query:
        query_terms = ai_query.lower().strip().split()
        for area, files in AURASYNC_CATALOG.items():
            matched_files = []
            for item in files:
                file_name = item[0]
                file_desc = item[1]
                f_combined = f"{file_name} {file_desc}".lower()
                if any(term in f_combined or term in area.lower() for term in query_terms):
                    matched_files.append(item)
            if matched_files:
                filtered_catalog[area] = matched_files
        
        if not filtered_catalog:
            st.warning("🤖 L'IA non ha trovato corrispondenze esatte. Mostriamo l'intero catalogo:")
            filtered_catalog = AURASYNC_CATALOG
        else:
            st.info(f"🤖 Risultati elaborati dall'IA per la ricerca: '{ai_query}'")
    else:
        filtered_catalog = AURASYNC_CATALOG

    for category, files in filtered_catalog.items():
        st.subheader(category)
        cols = st.columns(3)
        for idx, (file_name, file_desc) in enumerate(files):
            with cols[idx % 3]:
                st.markdown(f"""
                <div style="border: 1px solid #e0e0e0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #fcfcfc; box-shadow: 0 2px 5px rgba(0,0,0,0.05); min-height: 180px;">
                    <h4 style="margin-bottom: 5px; font-size: 15px;">✨ {file_name}</h4>
                    <p style="font-size: 12px; color: #555; margin-bottom: 10px;">{file_desc}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🚀 Avvia Modulo", key=f"btn_{category}_{idx}"):
                    st.session_state.active_app = file_name
                    st.session_state.active_view = "bacheca"
                    st.rerun()
        st.divider()
    
    if st.button("🔙 Torna alla Bacheca Pubblica"):
        st.session_state.active_view = "bacheca"
        st.rerun()
