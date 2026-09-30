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

# CATALOGO CON DESCRIZIONI DETTAGLIATE (ADATTE ANCHE PER TEEN E CREATOR)
AURASYNC_CATALOG = {
    "🌐 Bacheca Pubblica": [
        ("🌐 AuraFeed Community Wall", "Bacheca globale interattiva dove condividere post, idee e progetti con l'intera community in tempo reale."),
        ("⭐ Creator Hall of Fame", "La classifica d'onore che celebra i creatori di contenuti, prompt e moduli più votati della settimana."),
        ("🛒 Prompt & Template Market", "Il marketplace ufficiale per scambiare, vendere o scaricare prompt di IA e template di produttività."),
        ("🛡️ Moderation Guard", "Sistema di filtraggio e sicurezza automatizzato per mantenere un ambiente pulito, sicuro e rispettoso.")
    ],
    "🧠 Area 1: Core IA & Produttività": [
        ("1. AuraBot Universal Chat", "Assistente IA conversazionale avanzato per rispondere a qualsiasi domanda, risolvere dubbi o scrivere testi."),
        ("2. Branch Selector IA", "Strumento decisionale basato su alberi decisionali guidati dall'intelligenza artificiale per scelte complesse."),
        ("3. Voice & Persona Chameleon", "Cambia il tono di voce e la personalità dell'IA (da professore serio a coach motivazionale o amico ironico)."),
        ("4. AuraTwin Predittivo", "Simulatore di scenari futuri basato sulle tue abitudini e decisioni passate."),
        ("5. Prompt Engineering Studio", "Laboratorio avanzato per creare, testare e ottimizzare prompt perfetti per qualsiasi modello di IA."),
        ("6. Smart Summarizer", "Riassume istantaneamente articoli lunghi, PDF o documenti complessi in punti chiave immediati."),
        ("7. Global Trend Analyzer", "Analizzatore di tendenze globali dal web per scoprire cosa sta diventando virale in tempo reale."),
        ("8. Cognitive Flow Optimizer", "Ottimizzatore del flusso di lavoro per eliminare le distrazioni e massimizzare la concentrazione."),
        ("9. Task Automator AI", "Automatizza le attività ripetitive quotidiane trasformandole in flussi di lavoro gestiti dall'IA."),
        ("10. Data Cleanse Tool", "Pulisce, formatta e corregge set di dati disordinati in pochi secondi."),
        ("11. Multi-Language Translator Hub", "Traduttore multilingua avanzato con supporto a slang, modi di dire e traduzioni contestuali."),
        ("12. Code Snippet Generator", "Generatore di frammenti di codice in Python, JavaScript, HTML e altri linguaggi pronto all'uso."),
        ("13. API Connector Studio", "Pannello per connettere e testare API esterne e servizi web direttamente dall'app."),
        ("14. Document Semantic Search", "Ricerca semantica avanzata all'interno dei tuoi documenti personali per trovare subito i concetti chiave."),
        ("15. Context Memory Vault", "Memoria di contesto a lungo termine per ricordare preferenze, progetti e conversazioni passate.")
    ],
    "🚀 Area 2: Business & Growth": [
        ("61. Pitch Deck Generator AI", "Crea presentazioni aziendali e pitch vincenti per investitori strutturati dall'IA."),
        ("62. SWOT Matrix Analyzer", "Analizza punti di forza, debolezza, opportunità e minacce di qualsiasi progetto o idea imprenditoriale."),
        ("63. Business Model Canvas Builder", "Costruisci il modello di business perfetto definendo valore, clienti e flussi di ricavi."),
        ("64. Competitor Pricing Spy", "Analizza le strategie di prezzo dei concorrenti per posizionare al meglio il tuo prodotto."),
        ("65. HR Interview Simulator", "Simulatore di colloqui di lavoro con domande mirate e feedback dell'IA per migliorare le tue performance."),
        ("66. OKR & KPI Goal Tracker", "Traccia obiettivi aziendali e indicatori chiave di prestazione con grafici di crescita."),
        ("67. B2B Email Outreach Writer", "Scrive email commerciali e di contatto B2B altamente persuasive e ottimizzate per le risposte."),
        ("68. Legal Contract Draft AI", "Boze di contratti legali personalizzati generati dall'IA per accordi e collaborazioni rapide."),
        ("69. Crowdfunding Campaign Planner", "Pianificatore completo per campagne di crowdfunding di successo su Kickstarter o GoFundMe."),
        ("70. Brand Tone of Voice Designer", "Definisce e mantiene coerente la voce e lo stile comunicativo del tuo brand.")
    ],
    "💎 Area 3: Store, Wallet & Sicurezza": [
        ("46. Ruota della Fortuna Interattiva", "Minigioco quotidiano per testare la fortuna e vincere Gettoni d'Oro omaggio."),
        ("47. Streak & Habit Tracker", "Traccia le tue abitudini quotidiane e i giorni consecutivi di attività (streak) per restare motivato."),
        ("48. Digital Pet Companion", "Un cucciolo virtuale digitale che cresce, interagisce e si evolve in base alla tua attività nell'app."),
        ("49. Wallet Token Economy", "Gestione completa del portafoglio digitale e dei Gettoni d'Oro guadagnati nel sistema."),
        ("50. Stripe Checkout Integration", "Sistema sicuro integrato per acquisti e transazioni digitali protette."),
        ("51. Fair Use Policy Guard (FUP)", "Sistema di protezione e bilanciamento delle risorse per garantire un utilizzo equo della piattaforma."),
        ("52. Aura Security Hub", "Centro di controllo della sicurezza, crittografia e protezione dei dati personali."),
        ("53. Age Verification Guard", "Modulo di verifica dell'età e protezione dei minori per contenuti sicuri."),
        ("54. Admin Supreme Control Panel", "Pannello di controllo amministrativo avanzato per la gestione globale del sistema operativo."),
        ("55. AURA SOS Emergency Protocol", "Protocollo di emergenza rapida per bloccare sessioni o richiedere supporto immediato."),
        ("56. PWA Offline Sync", "Sincronizzazione offline per continuare a usare l'app anche senza connessione internet."),
        ("57. Data Privacy & GDPR Vault", "Cassaforte digitale per la gestione della privacy e la conformità alle normative europee GDPR."),
        ("58. User Feedback & Bug Reporter", "Invia segnalazioni di bug o suggerimenti direttamente agli sviluppatori."),
        ("59. Onboarding Interactive Guide", "Guida interattiva dettagliata per scoprire tutte le funzioni nascoste di AuraSync."),
        ("60. Custom Plugin Marketplace", "Marketplace per installare estensioni e plugin personalizzati creati dalla community.")
    ],
    "🌿 Area 4: Benessere, Fai-da-Te & Social": [
        ("16. AuraGreen Leaf Analyzer", "Analizza lo stato di salute delle tue piante di casa tramite foto e suggerisce cure."),
        ("17. Smart Watering Scheduler", "Pianificatore intelligente delle innaffiature basato sul clima e sul tipo di pianta."),
        ("18. Botanic Disease Tracker", "Identifica malattie delle piante e parassiti con rimedi biologici mirati."),
        ("19. AuraFix Hardware Diagnostic", "Diagnostica guasti domestici e malfunzionamenti di piccoli elettrodomestici o oggetti."),
        ("20. DIY Step-by-Step Guide", "Guide pratiche fai-da-te passo-passo per progetti di bricolage e creatività."),
        ("21. Tool Inventory Manager", "Gestisce l'inventario dei tuoi strumenti da lavoro, attrezzi o materiali hobbistici."),
        ("22. AuraPets Paws Health", "Monitoraggio della salute, benessere e vaccinazioni dei tuoi animali domestici."),
        ("23. Pet Nutrition Advisor", "Consigli nutrizionali personalizzati e diete equilibrate per cani, gatti e pet."),
        ("24. Behavioral Pet Tracker", "Traccia il comportamento e l'umore del tuo cucciolo per capirne i bisogni."),
        ("25. Eco-Friendly Habit Builder", "Costruttore di abitudini ecologiche per ridurre l'impronta di carbonio quotidiana."),
        ("26. Home Energy Auditor", "Analizzatore dei consumi energetici domestici per risparmiare sulla bolletta."),
        ("27. Waste Reduction Assistant", "Assistente per la riduzione degli sprechi alimentari e domestici."),
        ("28. Indoor Climate Optimizer", "Ottimizza temperatura, umidità e qualità dell'aria all'interno delle stanze."),
        ("29. Smart Grocery Planner", "Pianificatore intelligente della spesa per evitare sprechi e comprare il necessario."),
        ("30. Green Space Designer", "Progetta spazi verdi, balconi fioriti o giardini verticali personalizzati."),
        ("Social 1. Real-Time Viral Trend Radar", "Radar per creator e teen per scoprire trend e audio virali su TikTok e Instagram."),
        ("Social 2. AI Content Hook & Caption Generator", "Crea ganci (hook) irresistibili e didascalie accattivanti per i tuoi video e post social."),
        ("Social 3. Cross-Platform Video Script Writer", "Sceneggiatore automatico di script per Reel, TikTok, Shorts e video YouTube."),
        ("Social 4. Social Calendar & Timing Optimizer", "Pianifica i tuoi post social nei momenti esatti in cui il pubblico è più attivo."),
        ("Social 5. Competitor & Niche Analyzer", "Analizza i concorrenti di nicchia sui social per far crescere il tuo profilo.")
    ],
    "📖 Area 5: Famiglia, Memoria & Musica": [
        ("31. Bedtime Story AI", "Crea storie della buonanotte personalizzate con protagonisti i tuoi bambini e morali a scelta."),
        ("32. Moral Lesson Customizer", "Personalizza la morale e i valori educativi all'interno delle storie interattive."),
        ("33. Character Creator Studio", "Crea personaggi unici con caratteristiche, aspetto e voce per storie e giochi."),
        ("34. AuraSound Studio Lyrics", "Scrittore di testi musicali e canzoni originali in qualsiasi genere e stile."),
        ("35. Melody & Binaural Generator", "Generatore di melodie rilassanti e frequenze binaurali per studio e sonno."),
        ("36. Sleep & Focus Soundscapes", "Paesaggi sonori immersivi (pioggia, foresta, onde del mare) per concentrarsi o dormire."),
        ("37. Time Capsule Cloud", "Capsula del tempo digitale per salvare messaggi e foto da aprire in futuro."),
        ("38. Family Memory Vault", "Album di famiglia digitale sicuro per custodire ricordi preziosi e ricorrenze."),
        ("39. Future Letter Dispatcher", "Invia una lettera programmata a te stesso nel futuro (es. tra 5 anni)."),
        ("40. Daily Gratitude Journal", "Diario della gratitudine quotidiana per annotare pensieri positivi e benessere."),
        ("41. Mood Tracker Emotivo", "Traccia le tue emozioni quotidiane per comprendere meglio i tuoi stati d'animo."),
        ("42. Creative Writing Companion", "Compagno di scrittura creativa per sbloccare la creatività e scrivere romanzi o poesie."),
        ("43. Recipe & Cooking Assistant", "Ricettario intelligente che inventa ricette con gli ingredienti che hai in frigo."),
        ("44. Event Planner Familiare", "Organizzatore di feste, compleanni e cene di famiglia senza stress."),
        ("45. Digital Scrapbook Creator", "Crea collage digitali interattivi con ricordi di viaggi ed eventi speciali.")
    ],
    "🎨 Area 6: Design & UI/UX": [
        ("71. Color Palette Harmony AI", "Genera palette di colori armoniose e professionali per siti web, loghi e grafiche."),
        ("72. UI/UX Wireframe Planner", "Pianifica la struttura e i flussi di navigazione di app e interfacce digitali."),
        ("73. Logo Concept Generator", "Ideatore di concetti e stili visivi originali per loghi e brand identity."),
        ("74. Typography Pairer Pro", "Suggerisce abbinamenti tipografici perfetti per progetti di design e stampa."),
        ("75. AI Image Prompt Architect", "Costruisce prompt dettagliati e avanzati per generatori di immagini come Midjourney o DALL-E."),
        ("76. SVG Icon Code Creator", "Genera codice SVG pulito per icone vettoriali personalizzate."),
        ("77. UX Microcopy Writer", "Scrive testi brevi, intuitivi e ingaggianti per pulsanti, errori e interfacce utente."),
        ("78. Moodboard Visualizer", "Crea tavole d'ispirazione visiva per progetti creativi, design e moda."),
        ("79. Landing Page Structure Optimizer", "Ottimizza la struttura di una landing page per convertire al meglio i visitatori."),
        ("80. Accessibility (WCAG) Checker", "Verifica l'accessibilità e i contrasti di colore secondo gli standard WCAG per siti web.")
    ],
    "📊 Area 7: Data Science & Finanza": [
        ("81. Personal Budget Planner", "Gestisci entrate, spese e risparmi personali con grafici di bilancio chiari e intuitivi."),
        ("82. Crypto & Portfolio Tracker", "Monitora il portafoglio di criptovalute e investimenti finanziari in tempo reale."),
        ("83. CSV/Excel Data Cleaner", "Pulisci e unisci file di dati tabulari in formato CSV o Excel senza errori."),
        ("84. SQL Query Builder AI", "Genera query SQL complesse partendo da semplici richieste in linguaggio naturale."),
        ("85. Regex Pattern Generator", "Crea espressioni regolari (RegEx) per la ricerca e validazione di testi."),
        ("86. Tax & Expense Estimator", "Stima spese, tasse e costi previsti per liberi professionisti e piccoli progetti."),
        ("87. Statistical Data Interpreter", "Interpreta dati statistici complessi trasformandoli in report di facile lettura."),
        ("88. Loan & Mortgage Calculator", "Calcolatore di prestiti, mutui e piani di ammortamento con simulazione tassi."),
        ("89. JSON/XML Data Formatter", "Formatta, valida e converti strutture dati JSON e XML all'istante."),
        ("90. A/B Testing Statistical Calculator", "Calcolatore statistico per verificare i risultati di test A/B su conversioni e marketing.")
    ],
    "🧘 Area 8: Life Coaching & Mind": [
        ("91. Daily Habit Loop Builder", "Costruisci cicli di abitudini sane basati sulla psicologia comportamentale."),
        ("92. Guided Meditation Script Writer", "Scrive script personalizzati per meditazioni guidate e sessioni di rilassamento."),
        ("93. Procrastination Breaker", "Tecniche e prompt rapidi per sbloccare l'inerzia e iniziare subito a studiare o lavorare."),
        ("94. Sleep Cycle Optimizer", "Ottimizza i cicli di sonno per svegliarti riposato e pieno di energia."),
        ("95. Book Notes & Summarizer", "Riassunti e appunti dettagliati dei libri di crescita personale e saggistica più famosi."),
        ("96. Public Speaking Coach", "Allenatore virtuale per migliorare la parlata in pubblico, la sicurezza e la dizione."),
        ("97. Digital Detox Tracker", "Traccia e limita il tempo passato davanti agli schermi per staccare la spina."),
        ("98. Relationship & Empathy Advisor", "Consigli basati sull'intelligenza emotiva per migliorare i rapporti con gli altri."),
        ("99. Travel Itinerary Planner", "Pianificatore di viaggi su misura con tappe, attrazioni e consigli culturali."),
        ("100. Life Vision Board Generator", "Crea la tua bacheca dei sogni visiva per focalizzarti sui tuoi obiettivi di vita.")
    ],
    "🎒 Area 9: Teen & Youth Empowerment": [
        ("101. School Homework Helper", "Aiuto compiti interattivo per spiegare concetti difficili di matematica, storia e scienze in modo semplice."),
        ("102. Exam Anxiety & Study Planner", "Organizza il piano di studio e gestisce l'ansia da esame con tecniche di respirazione e focus."),
        ("103. Language & Slang Bridge", "Traduttore intergenerazionale e di slang giovanile per capire meme, espressioni e nuove lingue."),
        ("104. Future Career Explorer", "Esplora professioni innovative, lavori digitali e percorsi di studio ideali per il tuo futuro."),
        ("105. Creative Writing & Manga Plotter", "Crea trame, personaggi e sceneggiature per storie, fumetti, manga e racconti."),
        ("106. Gamer Strategy & Build Planner", "Pianifica strategie di gioco, build di personaggi e guide tattiche per i tuoi videogiochi preferiti."),
        ("107. Teen Mood & Vibe Journal", "Diario personale sicuro e privato dedicato ai ragazzi per esprimere pensieri, emozioni e musica del giorno."),
        ("108. Pocket Coding & Game Dev Coach", "Primo coach tascabile per imparare le basi della programmazione e dello sviluppo di videogiochi."),
        ("109. Music & Beat Maker Lyrist", "Scrivi barre, rime e testi rap/trap o pop su basi musicali generate dall'IA."),
        ("110. Pocket Finance for Teens", "Educazione finanziaria per ragazzi: impara a gestire la tua prima paga, risparmiare e investire."),
        ("111. DIY Creative Room Decor", "Idee fai-da-te e progetti creativi per arredare e personalizzare la tua stanza o camera."),
        ("112. Eco & Animal Activism Guide", "Guida pratica per iniziative ecologiche, protezione degli animali e attivismo giovanile."),
        ("113. Public Speaking & Debate Trainer", "Allenati a dibattere, argomentare le tue idee e parlare senza paura nei progetti scolastici."),
        ("114. Book & Comic Club Tracker", "Traccia le tue letture, manga, fumetti e libri preferiti condividendo recensioni."),
        ("115. Smart Sport & Workout Tracker", "Traccia allenamenti, esercizi a corpo libero, corsa e performance sportive personali."),
        ("116. DIY Cosplay & Prop Planner", "Pianificatore di progetti cosplay, costumi e oggetti di scena con materiali di recupero."),
        ("117. Friends & Hangout Event Planner", "Organizza uscite, feste e ritrovi con gli amici in modo semplice e coordinato."),
        ("118. Digital Safety & Privacy Guardian", "Guida alla sicurezza online, difesa da truffe, privacy sui social e cyberbullismo."),
        ("119. DIY Photography & Reel Editor", "Consigli di fotografia con smartphone e montaggio video per reel spettacolari."),
        ("120. Dream & Goal Board for Teens", "Crea la tua bacheca dei sogni e degli obiettivi futuri con immagini e motivazione.")
    ],
    "🎮 Area 10: 25 Giochi e Quiz per Tutti": [
        ("Game 1. Quiz di Cultura Generale IA", "Metti alla prova la tua cultura generale con domande generate dall'IA su ogni argomento."),
        ("Game 2. Rompicapo Logico Matematico", "Enigmi e problemi di logica pura per allenare la mente e il ragionamento."),
        ("Game 3. Indovina la Parola Segreta", "Classico gioco di parole nascoste con indizi progressivi per trovare la soluzione."),
        ("Game 4. Memory Test Cognitivo", "Esercizi di memoria visiva e sequenziale per testare le tue capacità cognitive."),
        ("Game 5. Test di Intuito e Psicologia", "Test divertenti di psicologia comportamentale e intuito per scoprire lati nascosti del carattere."),
        ("Game 6. Trivia su Cinema e Serie TV", "Quiz definitivo per veri esperti di film, attori e serie televisive cult."),
        ("Game 7. Calcolatore di Compatibilità Zodiacale", "Simuratore ironico e divertente di affinità di coppia e oroscopo."),
        ("Game 8. Indovinelli Storici", "Viaggia nel tempo risolvendo indovinelli e misteri legati a grandi personaggi storici."),
        ("Game 9. Test di Velocità di Reazione", "Metti alla prova i tuoi riflessi con un test di velocità millimetrica al tocco."),
        ("Game 10. Labirinto Testuale Decisionale", "Un'avventura testuale interattiva dove ogni tua scelta cambia il finale della storia."),
        ("Game 11. Quiz di Geografia Mondiale", "Indovina capitali, bandiere, monumenti e curiosità geografiche da tutto il mondo."),
        ("Game 12. Indovina il Brand o il Logo", "Riconosci loghi celebri e marchi famosi nascosti o stilizzati."),
        ("Game 13. Sfida di Calcolo Mentale Rapido", "Esercizi cronometrati di calcolo a mente per sfrecciare coi numeri."),
        ("Game 14. Quiz sui Misteri dello Spazio", "Domande e curiosità strabilianti su pianeti, buchi neri, galassie e universo."),
        ("Game 15. Test del QI Lirico e Musicale", "Completa i testi delle canzoni più famose e dimostra di conoscere ogni hit."),
        ("Game 16. Trova l'Intruso Logico", "Analizza quattro elementi e individua l'unico intruso basandoti sulla logica."),
        ("Game 17. Quiz sulla Tecnologia del Futuro", "Scopri quanto ne sai di intelligenza artificiale, robotica e gadget hi-tech."),
        ("Game 18. Indovina la Curiosità Biologica", "Quiz interattivo sui segreti più strani e affascinanti della natura e degli animali."),
        ("Game 19. Sfida di Riddle ed Enigmi", "Enigmi ingannevoli e rompicapo linguistici che metteranno a dura prova il tuo ingegno."),
        ("Game 20. Test di Creatività Espressiva", "Valuta la tua vena artistica e creativa attraverso scelte visive e verbali."),
        ("Game 21. Quiz sulle Lingue del Mondo", "Scopri parole intraducibili, modi di dire e curiosità linguistiche globali."),
        ("Game 22. Gioco della Torre di Hanoi IA", "Il celebre rompicapo matematico dei dischi da spostare con ottimizzazione IA."),
        ("Game 23. Test di Sopravvivenza in Natura", "Mettiti nei guai in scenari estremi e scegli come sopravvivere con l'intuito."),
        ("Game 24. Quiz sull'Economia e Finanza Base", "Impara i concetti base di soldi, risparmio ed economia divertendoti."),
        ("Game 25. Il Grande Quiz Finale di AuraSync", "La sfida finale che racchiude tutte le categorie per eleggere il campione supremo.")
    ]
}

# --- FLUSSO PRINCIPALE ---

if not st.session_state.tutorial_completed:
    # 1. LOADING & RUOTA DELLA FORTUNA INIZIALE (UNICA PRESENZA DELLA RUOTA)
    st.title("⚙️ Caricamento e Sincronizzazione in Corso...")
    st.markdown("### Benvenuto in AuraSync OS — L'Ecosistema Cognitivo per Tutti (anche Teen & Creator)")
    st.write("Fai girare la ruota integrata durante il caricamento per vincere i Gettoni d'Oro di benvenuto!")

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

    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        if st.button("🎡 Gira la Ruota di Caricamento!", type="primary", use_container_width=True):
            won = random.choice([1, 2, 3, 5, 10])
            st.session_state.wallet_tokens += won
            st.session_state.wheel_spun_today = True
            st.session_state.wheel_result_val = won
            st.balloons()
            st.success(f"🎉 Hai vinto {won} Gettoni d'Oro! Inizializzazione completata.")
            time.sleep(2)
            st.session_state.tutorial_completed = True
            st.rerun()

else:
    # --- 2. INTERFACCIA PRINCIPALE (SENZA RUOTA) ---
    
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
            st.header(f"🚀 Modulo Attivo: {st.session_state.active_app}")
            st.success(f"L'applicazione **{st.session_state.active_app}** è stata caricata con successo.")
            st.write("Ambiente operativo pronto per l'esecuzione e l'interazione avanzata.")
            
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
            st.info("• Tutti i 150 moduli (inclusa l'area Teen & Youth e Social) sono attivi.\n• Usa il pulsante in alto a destra (**>> 📁 Apri Menu File**) per accedere al menu visivo con descrizioni dettagliate e Ricerca Esterna IA.")
        
    else:
        # --- MENU FILE E MODULI CON RICERCA ESTERNA IA E DESCRIZIONI DETTAGLIATE ---
        st.header("📂 Menu Applicazioni - Vista a Icone e Dettagli")
        st.write(f"Gettoni nel Wallet: **{st.session_state.wallet_tokens} 🪙** | Esplora tutte le 150 applicazioni e giochi.")
        
        # BARRA DI RICERCA ESTERNA IA POTENZIATA
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

        # MOSTRA IL CATALOGO A ICONE E DETTAGLI SPECIFICI
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
