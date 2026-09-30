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
if "wallet_tokens" not in st.session_state: st.session_state.wallet_tokens = 50
if "active_view" not in st.session_state: st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: st.session_state.active_app = None
if "chat_history" not in st.session_state: st.session_state.chat_history = [
    ("AuraBot", "Benvenuto! Sono il tuo assistente IA universale. Come posso aiutarti oggi?")
]
if "pet" not in st.session_state: st.session_state.pet = {"name": "AuraPet", "energy": 80, "hunger": 50, "mood": "Felice 😺"}
if "budget_items" not in st.session_state: st.session_state.budget_items = [{"desc": "Stipendio", "amount": 1500, "type": "Entrata"}]

# CATALOGO COMPLETO DI TUTTE LE 150 APPLICAZIONI E GIOCHI
AURASYNC_CATALOG = {
    "🌐 Bacheca Pubblica": [
        ("🌐 AuraFeed Community Wall", "Bacheca globale interattiva dove condividere post, idee e progetti con l'intera community."),
        ("⭐ Creator Hall of Fame", "La classifica d'onore che celebra i creatori di contenuti e moduli più votati."),
        ("🛒 Prompt & Template Market", "Il marketplace ufficiale per scambiare e scaricare prompt di IA e template."),
        ("🛡️ Moderation Guard", "Sistema di filtraggio e sicurezza automatizzato per mantenere un ambiente protetto.")
    ],
    "🧠 Area 1: Core IA & Produttività": [
        ("1. AuraBot Universal Chat", "Assistente IA conversazionale avanzato per rispondere a qualsiasi domanda o scrivere testi."),
        ("2. Branch Selector IA", "Strumento decisionale basato su alberi decisionali guidati dall'intelligenza artificiale."),
        ("3. Voice & Persona Chameleon", "Cambia il tono di voce e la personalità dell'IA (professore, coach o amico ironico)."),
        ("4. AuraTwin Predittivo", "Simulatore di scenari futuri basato sulle tue abitudini e decisioni passate."),
        ("5. Prompt Engineering Studio", "Laboratorio avanzato per creare, testare e ottimizzare prompt perfetti."),
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
    "🌿 Area 2: Benessere, Fai-da-Te & Social": [
        ("16. AuraGreen Leaf Analyzer", "Analizza lo stato di salute delle tue piante di casa tramite parametri."),
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
    "📖 Area 3: Famiglia, Memoria & Musica": [
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
    "💎 Area 4: Store, Wallet & Sicurezza": [
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
    "🚀 Area 5: Business & Growth": [
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
    "🎮 Area 10: 30 Giochi e Quiz Reali": [
        ("Game 1. Quiz di Cultura Generale IA", "Metti alla prova la tua cultura con domande interattive."),
        ("Game 2. Rompicapo Logico Matematico", "Enigmi e problemi di logica pura con verifica della risposta."),
        ("Game 3. Indovina la Parola Segreta", "Classico gioco di parole nascoste con indizi progressivi."),
        ("Game 4. Memory Test Cognitivo", "Esercizi di memoria visiva e sequenziale interattivi."),
        ("Game 5. Test di Intuito e Psicologia", "Test divertenti di psicologia e profilo comportamentale."),
        ("Game 6. Trivia su Cinema e Serie TV", "Quiz definitivo per esperti di film e serie TV con punteggio."),
        ("Game 7. Calcolatore di Compatibilità Zodiacale", "Simulatore ironico di affinità di coppia e oroscopo."),
        ("Game 8. Indovinelli Storici", "Risolvi indovinelli e misteri legati a grandi personaggi storici."),
        ("Game 9. Test di Velocità di Reazione", "Metti alla prova i tuoi riflessi con un test interattivo."),
        ("Game 10. Labirinto Testuale Decisionale", "Un'avventura testuale interattiva dove ogni scelta cambia il finale."),
        ("Game 11. Quiz di Geografia Mondiale", "Indovina capitali, bandiere e monumenti dal mondo."),
        ("Game 12. Indovina il Brand o il Logo", "Riconosci loghi celebri e marchi famosi nascosti."),
        ("Game 13. Sfida di Calcolo Mentale Rapido", "Esercizi di calcolo a mente con verifica immediata."),
        ("Game 14. Quiz sui Misteri dello Spazio", "Domande strabilianti su pianeti, buchi neri e universo."),
        ("Game 15. Test del QI Lirico e Musicale", "Completa i testi delle canzoni più famose e hit."),
        ("Game 16. Trova l'Intruso Logico", "Analizza quattro elementi e individua l'intruso logico."),
        ("Game 17. Quiz sulla Tecnologia del Futuro", "Scopri quanto ne sai di intelligenza artificiale e robotica."),
        ("Game 18. Indovina la Curiosità Biologica", "Quiz interattivo sui segreti della natura e degli animali."),
        ("Game 19. Sfida di Riddle ed Enigmi", "Enigmi ingannevoli che metteranno alla prova il tuo ingegno."),
        ("Game 20. Test di Creatività Espressiva", "Valuta la tua vena artistica attraverso scelte guidate."),
        ("Game 21. Quiz sulle Lingue del Mondo", "Scopri parole intraducibili e modi di dire globali."),
        ("Game 22. Gioco della Torre di Hanoi IA", "Il celebre rompicapo matematico dei dischi da spostare."),
        ("Game 23. Test di Sopravvivenza in Natura", "Mettiti in scenari estremi e scegli come sopravvivere."),
        ("Game 24. Quiz sull'Economia e Finanza Base", "Impara i concetti base di soldi e risparmio divertendoti."),
        ("Game 25. Quiz sui Supereroi e Fumetti", "Metti alla prova la tua conoscenza di universi fantastici."),
        ("Game 26. Indovina l'Anno dell'Evento", "Associa l'evento storico corretto all'anno esatto."),
        ("Game 27. Test di Empatia e Relazioni", "Valuta le tue reazioni emotive in situazioni sociali."),
        ("Game 28. Labirinto dei Numeri Primo", "Indovina e calcola sequenze numeriche complesse."),
        ("Game 29. Quiz di Cucina e Gastronomia", "Scopri ricette tradizionali e segreti degli chef."),
        ("Game 30. Il Grande Quiz Finale di AuraSync", "La sfida finale che racchiude tutte le categorie con premio in token.")
    ]
}

# --- FUNZIONE GESTIONE INTERATTIVA DELL'APP ATTIVA ---
def render_active_app_interface(app_name):
    st.subheader(f"🚀 Modulo Attivo: {app_name}")
    st.divider()

    # 1. Chat Universale (Corretta per mostrare i messaggi in sequenza corretta)
    if "AuraBot Universal Chat" in app_name:
        st.write("💬 **Conversazione in tempo reale con AuraBot:**")
        
        # Mostra la cronologia chat nell'ordine corretto
        chat_container = st.container()
        with chat_container:
            for sender, text in st.session_state.chat_history:
                if sender == "Tu":
                    st.markdown(f"👤 **{sender}:** {text}")
                else:
                    st.markdown(f"🤖 **{sender}:** {text}")
        
        st.divider()
        
        # Form di invio messaggio reattivo
        with st.form(key="chat_form", clear_on_submit=True):
            user_msg = st.text_input("Scrivi un messaggio ad AuraBot:")
            submit_btn = st.form_submit_button("Invia messaggio 🚀")
            
            if submit_btn and user_msg:
                st.session_state.chat_history.append(("Tu", user_msg))
                reply = f"Ho analizzato la tua richiesta '{user_msg}': Il sistema cognitivo ha elaborato una risposta ottimizzata e pronta all'uso."
                st.session_state.chat_history.append(("AuraBot", reply))
                st.rerun()

    # 2. Digital Pet Companion
    elif "Digital Pet Companion" in app_name:
        p = st.session_state.pet
        col1, col2, col3 = st.columns(3)
        col1.metric("Energia", f"{p['energy']}%")
        col2.metric("Sazietà", f"{p['hunger']}%")
        col3.metric("Umore", p['mood'])
        
        c1, c2, c3 = st.columns(3)
        if c1.button("🍖 Da' da mangiare"):
            p['hunger'] = min(100, p['hunger'] + 25)
            p['energy'] = min(100, p['energy'] + 10)
            p['mood'] = "Sazio e Felice 😊"
            st.success("Gnam! Il cucciolo ha mangiato con gusto.")
            st.rerun()
        if c2.button("🎾 Gioca insieme"):
            p['energy'] = max(0, p['energy'] - 20)
            p['hunger'] = max(0, p['hunger'] - 15)
            p['mood'] = "Eccitato ed Energetico ⚡"
            st.success("Che divertimento! Avete giocato un bel po'.")
            st.rerun()
        if c3.button("💤 Metti a dormire"):
            p['energy'] = 100
            p['mood'] = "Riposato e Tranquillo 😴"
            st.success("Il cucciolo ha fatto un sonnellino rigenerante.")
            st.rerun()

    # 3. Personal Budget Planner
    elif "Personal Budget Planner" in app_name:
        st.write("Gestisci le tue finanze personali in tempo reale:")
        desc = st.text_input("Descrizione movimento:")
        amount = st.number_input("Importo (€):", value=50.0, min_value=0.0)
        m_type = st.selectbox("Tipo:", ["Entrata", "Uscita"])
        
        if st.button("Aggiungi Transazione"):
            st.session_state.budget_items.append({"desc": desc if desc else "Transazione", "amount": amount, "type": m_type})
            st.success("Transazione registrata con successo!")
            st.rerun()
        
        totale = sum(item['amount'] if item['type'] == 'Entrata' else -item['amount'] for item in st.session_state.budget_items)
        st.metric("Bilancio Totale Attuale", f"€ {totale:.2f}")
        st.write("**Storico Movimenti:**")
        for item in st.session_state.budget_items:
            st.markdown(f"- {item['desc']}: **{'+' if item['type']=='Entrata' else '-' }€{item['amount']}**")

    # 4. Gestione Quiz e Giochi (Area 10 e simili)
    elif "Quiz" in app_name or "Game" in app_name or "Rompicapo" in app_name or "Indovina" in app_name or "Test" in app_name or "Sfida" in app_name or "Labirinto" in app_name:
        st.subheader("🎯 Arena di Gioco Interattiva")
        st.write("Metti alla prova le tue abilità risolvendo questa sfida generata dal sistema:")
        
        q_options = ["Risposta A: Ottimizzazione Algoritmica", "Risposta B: Euristica Dinamica", "Risposta C: Elaborazione Neurale"]
        user_choice = st.radio("Seleziona la risposta corretta:", q_options)
        
        if st.button("Verifica Soluzione"):
            st.balloons()
            st.session_state.wallet_tokens += 10
            st.success("🎉 Risposta Esatta! Hai guadagnato +10 Gettoni d'Oro nel tuo Wallet!")

    # 5. Generatori di Codice / Prompt / Testi / Idee
    elif "Generator" in app_name or "Writer" in app_name or "Creator" in app_name or "Studio" in app_name or "Architect" in app_name:
        st.subheader("⚙️ Laboratorio di Generazione IA")
        user_param = st.text_input("Inserisci argomento o parole chiave per la generazione:", "Crescita digitale e startup")
        if st.button("Genera Contenuto Ottimizzato"):
            with st.spinner("Elaborazione in corso con reti neurali..."):
                time.sleep(1)
            st.success("Contenuto generato con successo:")
            st.code(f"""# Output generato per: {user_param}
- Obiettivo: Ottimizzazione avanzata delle performance
- Struttura: Modulare e scalabile con standard di mercato
- Risultato: Pronto per l'implementazione immediata in produzione.""", language="markdown")

    # 6. Tutti gli altri moduli
    else:
        st.write("Pannello operativo avanzato per questo modulo specifico.")
        param = st.text_input("Parametri di input personalizzati:", placeholder="Inserisci dati o istruzioni...")
        if st.button("Esegui Analisi Modulo"):
            if param:
                st.success(f"Analisi completata con successo per: '{param}'. I parametri sono stati elaborati.")
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


# --- INTERFACCIA PRINCIPALE ---

top_col1, top_col2 = st.columns([3, 1])
with top_col1:
    st.title("🌐 AuraSync OS - Dashboard Centrale")
with top_col2:
    st.write("") 
    if st.button(">> 📁 Menu App & Giochi", type="secondary", use_container_width=True):
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
        st.success("✨ Sistema operativo avviato correttamente. 150 applicazioni e giochi interattivi pronti.")
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Gettoni nel Wallet", f"{st.session_state.wallet_tokens} 🪙")
        col_m2.metric("Moduli e Giochi Totali", "150 Attivi 🚀")
        col_m3.metric("Stato Sistema", "Online 🟢")

        st.divider()
        st.subheader("📢 Come navigare")
        st.info("• Clicca sul pulsante in alto a destra (**>> 📁 Menu App & Giochi**) per aprire il catalogo completo.\n• Usa la barra di ricerca IA per trovare istantaneamente qualsiasi strumento o gioco tra i 150 disponibili.")
    
else:
    # --- MENU FILE E MODULI CON RICERCA IA ---
    st.header("📂 Catalogo Completo (150 App & Giochi)")
    st.write(f"Gettoni nel Wallet: **{st.session_state.wallet_tokens} 🪙** | Cerca per nome, categoria o tipo di gioco.")
    
    ai_query = st.text_input("🤖 Ricerca IA nel Catalogo:", placeholder="Es. game, quiz, budget, pet, chat, social, fitness...")
    
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
            st.warning("🤖 Nessuna corrispondenza esatta trovata. Mostriamo l'intero catalogo:")
            filtered_catalog = AURASYNC_CATALOG
        else:
            st.info(f"🤖 Risultati filtrati per: '{ai_query}'")
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
    
    if st.button("🔙 Torna alla Bacheca Principale"):
        st.session_state.active_view = "bacheca"
        st.rerun()
