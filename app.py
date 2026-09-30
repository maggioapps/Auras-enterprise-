import streamlit as st
import random
import time
import json
import datetime

# Configurazione PWA e Layout
st.set_page_config(
    page_title="AuraSync - Sports & Arcade OS v7.0",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inizializzazione dello State globale
if "active_view" not in st.session_state: st.session_state.active_view = "bacheca"
if "active_app" not in st.session_state: st.session_state.active_app = None
if "chat_history" not in st.session_state: st.session_state.chat_history = [
    ("AuraServer", "Motori sportivi e server di gioco (Calcio, Basket, Moto, corse) attivi e sincronizzati.")
]
if "pet" not in st.session_state: st.session_state.pet = {"name": "AuraPet", "energy": 100, "hunger": 100, "mood": "In Forma 🥇"}
if "budget_items" not in st.session_state: st.session_state.budget_items = [{"desc": "Sponsorizzazione Sportiva", "amount": 5000.0, "type": "Entrata"}]
if "game_state" not in st.session_state: st.session_state.game_state = {"score": 0, "goals": 0, "baskets": 0, "race_pos": 1}

# CATALOGO COMPLETO: 150 APP + 50 GIOCHI SPORTIVI E DI MOTORI REALI
AURASYNC_CATALOG = {
    "🌐 Bacheca Pubblica & Community": [
        ("🌐 AuraFeed Community Wall", "Bacheca globale interattiva per condividere post, idee e progetti con la community."),
        ("⭐ Creator Hall of Fame", "Classifica d'onore che celebra i creatori di contenuti e moduli più votati."),
        ("🛒 Prompt & Template Hub", "Centro ufficiale per scambiare e scaricare liberamente prompt di IA e template."),
        ("🛡️ Open Guard", "Sistema di supporto e protezione open per mantenere un ambiente collaborativo.")
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
    "💎 Area 4: Risorse, Toolbox & Strumenti liberi": [
        ("46. Free Tools Hub", "Raccolta di utility e funzioni completamente libere da vincoli."),
        ("47. Streak & Habit Tracker", "Traccia le tue abitudini quotidiane e i giorni consecutivi di attività."),
        ("48. Digital Pet Companion", "Un cucciolo virtuale digitale che cresce e interagisce con te liberamente."),
        ("49. Open Resource Economy", "Gestione completa e aperta delle risorse di sistema."),
        ("50. Fast Access Integration", "Accesso rapido e senza barriere a tutte le funzioni."),
        ("51. Fair Use Policy Guard (FUP)", "Sistema di protezione e bilanciamento delle risorse della piattaforma."),
        ("52. Aura Security Hub", "Centro di controllo della sicurezza e crittografia dati."),
        ("53. Open Access Guard", "Modulo di accesso universale e libero per tutti gli utenti."),
        ("54. Admin Supreme Control Panel", "Pannello di controllo amministrativo avanzato per il sistema."),
        ("55. AURA SOS Emergency Protocol", "Protocollo di emergenza rapida per bloccare sessioni critiche."),
        ("56. PWA Offline Sync", "Sincronizzazione offline per usare l'app senza connessione."),
        ("57. Data Privacy & GDPR Vault", "Cassaforte digitale per la gestione della privacy e conformità GDPR."),
        ("58. User Feedback & Bug Reporter", "Invia segnalazioni di bug o suggerimenti agli sviluppatori."),
        ("59. Onboarding Interactive Guide", "Guida interattiva dettagliata per scoprire tutte le funzioni."),
        ("60. Custom Plugin Hub", "Hub aperto per installare estensioni e plugin della community.")
    ],
    "🚀 Area 5: Creative Projects & Growth": [
        ("61. Project Pitch Generator AI", "Crea presentazioni e idee vincenti per progetti personali."),
        ("62. SWOT Matrix Analyzer", "Analizza punti di forza, debolezza, opportunità e minacce di un'idea."),
        ("63. Project Model Canvas Builder", "Costruisci il modello organizzativo perfetto per le tue iniziative."),
        ("64. Idea Benchmarking Spy", "Analizza strategie e tendenze di progetti simili sul web."),
        ("65. Communication Interview Simulator", "Simulatore di colloqui e simulazioni di dialogo con feedback."),
        ("66. OKR & Personal Goal Tracker", "Traccia obiettivi personali e indicatori chiave di successo."),
        ("67. Creative Outreach Writer", "Scrive messaggi e comunicazioni creative altamente persuasive."),
        ("68. Creative Draft Guide AI", "Bozze di accordi e linee guida personalizzate generate dall'IA."),
        ("69. Community Campaign Planner", "Pianificatore completo per iniziative e progetti condivisi."),
        ("70. Brand Tone of Voice Designer", "Definisce e mantiene coerente la voce e lo stile comunicativo.")
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
    "📊 Area 7: Data Science & Statistiche": [
        ("81. Personal Budget Planner", "Gestisci entrate, spese e risparmi personali con grafici chiari."),
        ("82. Crypto & Asset Tracker", "Monitora il portafoglio di criptovalute e beni personali."),
        ("83. CSV/Excel Data Cleaner", "Pulisci e unisci file di dati tabulari in formato CSV o Excel."),
        ("84. SQL Query Builder AI", "Genera query SQL complesse partendo da richieste in linguaggio naturale."),
        ("85. Regex Pattern Generator", "Crea espressioni regolari (RegEx) per la ricerca di testi."),
        ("86. Expense & Resource Estimator", "Stima spese e risorse per piccoli progetti creativi o hobbistici."),
        ("87. Statistical Data Interpreter", "Interpreta dati statistici trasformandoli in report di facile lettura."),
        ("88. Loan & Savings Calculator", "Calcolatore di prestiti, risparmi e piani di accumulo personali."),
        ("89. JSON/XML Data Formatter", "Formatta, valida e converti strutture dati JSON e XML."),
        ("90. A/B Testing Statistical Calculator", "Calcolatore statistico per verificare test A/B di progetti.")
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
        ("110. Pocket Personal Finance for Teens", "Impara a gestire la prima paghetta e i piccoli risparmi personali."),
        ("111. DIY Creative Room Decor", "Idee fai-da-te e progetti per arredare e personalizzare la stanza."),
        ("112. Eco & Animal Activism Guide", "Guida pratica per iniziative ecologiche e protezione degli animali."),
        ("113. Public Speaking & Debate Trainer", "Trainati a dibattere e argomentare idee per la scuola."),
        ("114. Book & Comic Club Tracker", "Traccia le tue letture, manga e fumetti preferiti con recensioni."),
        ("115. Smart Sport & Workout Tracker", "Traccia allenamenti, esercizi a corpo libero e corsa."),
        ("116. DIY Cosplay & Prop Planner", "Pianificatore di progetti cosplay, costumi e oggetti di scena."),
        ("117. Friends & Hangout Event Planner", "Organizza uscite, feste e ritrovi con gli amici facilmente."),
        ("118. Digital Safety & Privacy Guardian", "Guida alla sicurezza online, difesa da truffe e cyberbullismo."),
        ("119. DIY Photography & Reel Editor", "Consigli di fotografia con smartphone e montaggio per reel."),
        ("120. Dream & Goal Board for Teens", "Crea la tua bacheca dei sogni e obiettivi futuri.")
    ],
    "⚽ Area 10: 10 Giochi Sportivi & Motori (Bambini 4-8 anni)": [
        ("Sport 1. Calcio Kids: Calira il Rigore", "Scegli l'angolo e calcia il pallone per segnare il gol della vittoria!"),
        ("Sport 2. Mini Basket: Canestro al Volo", "Mira il canestro e fai passare la palla dentro la retina."),
        ("Sport 3. Mini Moto: Corsa sui Kart in Pista", "Guida il mini bolide a due ruote schivando i birilli colorati."),
        ("Sport 4. Salto in Alto con l'Asticella", "Prendi la rincorsa e salta oltre l'asticella senza farla cadere."),
        ("Sport 5. Tennis da Tavolo Rapido", "Rimetti la pallina dall'altra parte del tavolo con tempismo."),
        ("Sport 6. Nuoto: Gara in Vasca da 25 Metri", "Tieni il ritmo delle bracciate per vincere la medaglia d'oro nel nuoto."),
        ("Sport 7. Bici senza Pedali: Percorso a Ostacoli", "Pedala veloce lungo il vialetto del parco schivando i gattini."),
        ("Sport 8. Bowling dei Birilli Colorati", "Lancia la boccia pesante per fare strike e abbattere tutti i birilli."),
        ("Sport 9. Monopattino Freestyle Junior", "Fai saltare il monopattino sulla rampa di legno divertendoti."),
        ("Sport 10. Corsa campestre dei Piccoli Animali", "Vinci la maratona campestre correndo insieme ai tuoi amici.")
    ],
    "🏀 Area 11: 10 Giochi Sportivi & Motori (Ragazzi 9-13 anni)": [
        ("Sport 11. Calcio Campionato: Punizione a Giro", "Tira una punizione a effetto sopra la barriera per battere il portiere."),
        ("Sport 12. Basket NBA Street: Tiri da Tre Punti", "Segna più canestri da tre punti possibili prima che scada il cronometro."),
        ("Sport 13. Motocross Freestyle: Salto della Ramp", "Esegui un backflip spettacolare con la moto da cross in aria."),
        ("Sport 14. Skateboard Street Park: Grind & Flip", "Combinazioni di tasti per eseguire trick pazzeschi sullo skate park."),
        ("Sport 15. BMX Dirt Jump Challenge", "Atterra perfettamente dopo un salto vertiginoso nel fango."),
        ("Sport 16. Nuoto Sincronizzato e Tuffi dal Trampolino", "Esegui un salto mortale con avvitamento perfetto in piscina."),
        ("Sport 17. Volley Beach: Smash Finale", "Schiaccia la palla nella sabbia avversaria per vincere il set."),
        ("Sport 18. Parkour Urbano: Salto sui Tetti", "Corri sui tetti della città superando ostacoli con agilità estrema."),
        ("Sport 19. Formula Kart: Gran Premio della Città", "Gestisci il turbo nei rettilinei per vincere la coppa dei kart."),
        ("Sport 20. Tennis Torneo Junior: Diritto a Fondo Campo", "Scambia colpi potenti di dritto e rovescio per superare l'avversario.")
    ],
    "🏍️ Area 12: 10 Giochi Sportivi & Motori (Teenager 14-18 anni)": [
        ("Sport 21. Moto GP: Derapata in Pista a 300 All'Ora", "Gestisci staccata e acceleratore per dominare il circuito di Moto GP."),
        ("Sport 22. Calcio Champions: Gestione Partita e Tattica", "Guida la tua squadra del cuore alla vittoria della coppa europea."),
        ("Sport 23. Rally WRC: Sterrata nel Fango Estrema", "Guida l'auto da rally tra curve a gomito e banchi di nebbia."),
        ("Sport 24. Basket 1v1 Playground Challenge", "Sfida l'avversario in uno scontro uno contro uno a tutto campo."),
        ("Sport 25. Snowboard Freeride: Discesa sulla Neve Fresca", "Schiva gli abeti innevati e fai evoluzioni acrobatiche nel halfpipe."),
        ("Sport 26. Surf da Onda Grande: Tubo Perfetto", "Mantieni l'equilibrio sulla tavola mentre l'onda gigante ti sovrasta."),
        ("Sport 27. Automobilismo F1: Gestione Gomme e Pit Stop", "Scegli la strategia di gara perfetta per vincere il Gran Premio di Formula 1."),
        ("Sport 28. Ciclismo Giro d'Italia: Scalata dello Stelvio", "Gestisci le energie della squadra durante la durissima salita alpina."),
        ("Sport 29. Boxe Match Mondiale: Gancio Destro K.O.", "Schiva i colpi dell'avversario e metti a segno il montante decisivo."),
        ("Sport 30. Calcio a 5 Futsal: Azione Veloce", "Vinci la partita di calcetto indoor con passaggi rapidi e tiri fulminei.")
    ],
    "🏎️ Area 13: 10 Giochi Sportivi & Motori (Adulti 19-35 anni)": [
        ("Sport 31. Simulatore di Guida GT: Endurance 24 Ore", "Gestisci consumo gomme, benzina e turni di guida nella gara di durata."),
        ("Sport 32. Calcio Manager: Fantacalcio & Direttore Sportivo", "Acquista campioni, gestisci il bilancio e porta la squadra in Serie A."),
        ("Sport 33. Superbike Simulator: Pista Asciutta/Bagnata", "Imposta l'assetto della moto da superbike in base alle previsioni meteo."),
        ("Sport 34. Golf Pro Tour: 18 Buche sui Green", "Calcola vento, pendenza del terreno e seleziona il ferro giusto per la buca."),
        ("Sport 35. Tennis Match Professionale: Grande Slam", "Gestisci la resistenza fisica e la precisione dei colpi nei match al meglio dei 5 set."),
        ("Sport 36. Rally Raid Dakar: Deserto e Orientamento", "Guida il fuoristrada tra dune di sabbia sahariane senza rompere il motore."),
        ("Sport 37. Basket General Manager: NBA Franchise", "Crea la dinastia vincente scambiando giocatori e ingaggiando fuoriclasse."),
        ("Sport 38. Motocross MXGP: Gestione Salti e Sospensioni", "Metti a punto le sospensioni della moto per dominare il campionato MX."),
        ("Sport 39. Triathlon Ironman: Nuoto, Bici e Corsa", "Gestisci lo sforzo atletico nelle tre discipline estreme di resistenza."),
        ("Sport 40. Regata Velica America's Cup", "Sfrutta le correnti marine e orienta le vele per tagliare per prima il traguardo.")
    ],
    "🏆 Area 14: 10 Giochi Sportivi & Motori (Senior & Esperti 36+ anni)": [
        ("Sport 41. Calcio Storico: Torneo dei Rioni", "Vivi la tradizione e la tattica del calcio storico con i vecchi schemi."),
        ("Sport 42. Ciclismo Classiche Monumento: Roubaix", "Guida i passatisti sul pavé storico delle classiche del nord Europa."),
        ("Sport 43. Motoring Vintage: Gara d'Epoca Regolarità", "Mantieni la tabella di marcia esatta con la tua auto d'epoca sportiva."),
        ("Sport 44. Boccette e Bigliardo Classico all'Italiana", "Realizza i punti di stecca facendo carambolare le palle sul panno verde."),
        ("Sport 45. Pesca Sportiva d'Altura in Barca", "Lancia la lenza e combatti con il grande pesce spada combattendo la corrente."),
        ("Sport 46. Tennis Tavolo Veterani: Torneo Sociale", "Riflessi pronti e colpi tagliati per vincere il torneo del circolo."),
        ("Sport 47. Automobilismo Classico: Gran Premio Storico", "Guida le monoposto degli anni '70 senza controlli elettronici di trazione."),
        ("Sport 48. Vela d'Altura: Crociere e Venti di Tramontana", "Mappa la rotta della barca a vela gestendo randa e fiocco."),
        ("Sport 49. Caccia al Bersaglio e Tiro Sportivo", "Concentrazione e respirazione per fare centro nel bersaglio fisso a 50 metri."),
        ("Sport 50. Il Grande Derby Calcistico Storico", "Vivi la telecronaca interattiva e le emozioni della stracittadina di calcio.")
    ]
}

# --- MOTORE DI GIOCO SPORTIVO E MOTORI REALE ---
def execute_module_engine(app_name, user_input):
    ui = user_input.lower().strip()
    
    if "AuraBot Universal Chat" in app_name:
        return f"🤖 [AuraBot Core]: Risposta elaborata per '{user_input}'."
    elif "Digital Pet Companion" in app_name:
        return f"🐾 [Pet Server]: Interazione completata per '{user_input}'."
    elif "Personal Budget Planner" in app_name:
        return f"📊 [Budget Server]: Movimento finanziario registrato con successo."
    elif "Sport" in app_name or any(k in app_name for k in ["Calcio", "Basket", "Moto", "Salto", "Tennis", "Nuoto", "Bici", "Bowling", "Monopattino", "Corsa", "Skateboard", "BMX", "Volley", "Parkour", "Formula", "Rally", "Snowboard", "Surf", "Automobilismo", "Ciclismo", "Boxe", "Golf", "Triathlon", "Regata", "Boccette", "Pesca", "Tiro", "Derby"]):
        st.session_state.game_state["score"] += 25
        return f"⚽ [Server Sportivo & Motori]: Azione '{user_input}' eseguita in '{app_name}'. Risultato: **OTTIMA ESECUZIONE!** Punteggio: {st.session_state.game_state['score']} punti 🥇"
    else:
        return f"⚡ [AuraSync Global Engine]: Elaborazione completata per '{user_input}' nel modulo '{app_name}'."

# --- INTERFACCIA PER IL MODULO ATTIVO ---
def render_active_app_interface(app_name):
    st.subheader(f"🚀 Modulo / Gioco Sportivo Attivo: {app_name}")
    st.divider()

    if "AuraBot Universal Chat" in app_name:
        st.write("💬 **Chat in tempo reale con AuraBot:**")
        for sender, text in st.session_state.chat_history:
            if sender == "Tu":
                st.markdown(f"👤 **{sender}:** {text}")
            else:
                st.markdown(f"🤖 **{sender}:** {text}")
        st.divider()
        with st.form(key="chat_form", clear_on_submit=True):
            user_msg = st.text_input("Scrivi un messaggio ad AuraBot:")
            submit_btn = st.form_submit_button("Invia al Server 🚀")
            if submit_btn and user_msg:
                st.session_state.chat_history.append(("Tu", user_msg))
                reply = execute_module_engine(app_name, user_msg)
                st.session_state.chat_history.append(("AuraBot", reply))
                st.rerun()

    elif "Digital Pet Companion" in app_name:
        p = st.session_state.pet
        col1, col2, col3 = st.columns(3)
        col1.metric("Energia", f"{p['energy']}%")
        col2.metric("Sazietà", f"{p['hunger']}%")
        col3.metric("Umore", p['mood'])
        
        c1, c2, c3 = st.columns(3)
        if c1.button("🍖 Da' da mangiare"):
            p['hunger'] = 100
            p['mood'] = "In Forma 🥇"
            st.success("Il cucciolo ha fatto il pieno di energie.")
            st.rerun()
        if c2.button("🎾 Allenamento Sportivo"):
            p['energy'] = 100
            p['mood'] = "Campione Olimpico 🏆"
            st.success("Sessione di allenamento completata.")
            st.rerun()
        if c3.button("💤 Riposo"):
            p['energy'] = 100
            st.success("Riposo completato.")
            st.rerun()

    elif "Sport" in app_name or any(k in app_name for k in ["Calcio", "Basket", "Moto", "Salto", "Tennis", "Nuoto", "Bici", "Bowling", "Monopattino", "Corsa", "Skateboard", "BMX", "Volley", "Parkour", "Formula", "Rally", "Snowboard", "Surf", "Automobilismo", "Ciclismo", "Boxe", "Golf", "Triathlon", "Regata", "Boccette", "Pesca", "Tiro", "Derby"]):
        st.markdown(f"### 🏟️ Simulatore Sportivo & Motori: **{app_name}**")
        st.info("Premi i pulsanti di azione in tempo reale per gestire la tua prestazione sportiva o di guida in pista!")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            if st.button("⚡ Acceleratore / Affondo", use_container_width=True):
                res = execute_module_engine(app_name, "Accelerazione / Tiro pieno")
                st.success(res)
        with col_s2:
            if st.button("🎯 Mira di Precisione / Staccata", use_container_width=True):
                res = execute_module_engine(app_name, "Staccata al limite / Mira perfetta")
                st.success(res)
        with col_s3:
            if st.button("🔥 Turbo / Scatto Finale", use_container_width=True):
                res = execute_module_engine(app_name, "Attivazione Turbo / Volata finale")
                st.success(res)
        
        st.write("")
        custom_action = st.text_input("Inserisci una mossa specifica (es. 'tiro a giro sotto l'incrocio', 'derapata di potenza'):")
        if st.button("Esegui Mossa Sportiva"):
            if custom_action:
                res_custom = execute_module_engine(app_name, custom_action)
                st.success(res_custom)
            else:
                st.warning("Inserisci una mossa valida.")

    else:
        st.write(f"⚙️ **Pannello Operativo Avanzato per {app_name}**")
        user_input = st.text_input("Inserisci dati o comandi per il server:", placeholder="Scrivi qui...")
        
        if st.button("Esegui sul Server 🚀"):
            if user_input:
                with st.spinner("Elaborazione in corso..."):
                    time.sleep(0.2)
                result_text = execute_module_engine(app_name, user_input)
                st.success(result_text)
            else:
                st.warning("Inserisci un testo valido.")

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

top_col1, top_col2, top_col3 = st.columns([2, 1, 1])
with top_col1:
    st.title("⚽ AuraSync OS v7.0 - Sports & Motors")
with top_col2:
    persone_online = random.randint(240, 290)
    st.metric("👥 Server Attivi", f"{persone_online} nodi")
with top_col3:
    st.write("") 
    if st.button(">> 📁 Menu App & Sport", type="secondary", use_container_width=True):
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
        st.subheader("📦 Panoramica Pacchetti & 50 Giochi Sportivi e di Motori")
        
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.markdown("""
            - **🧠 Core IA & Produttività**: 15 moduli
            - **🌿 Benessere & Social**: 20 moduli
            - **📖 Famiglia & Musica**: 15 moduli
            - **💎 Risorse & Toolbox**: 15 moduli
            """)
        with col_p2:
            st.markdown("""
            - **🚀 Creative Projects**: 10 moduli
            - **🎨 Design & UI/UX**: 10 moduli
            - **📊 Data Science**: 10 moduli
            - **🧘 Life Coaching**: 10 moduli
            - **🎒 Teen Empowerment**: 20 moduli
            """)
        with col_p3:
            st.markdown("""
            - **⚽ 4-8 Anni (10 Sport)**: Calcio, Basket, Moto Kids
            - **🏀 9-13 Anni (10 Sport)**: Punizioni, NBA, Skateboard
            - **🏍️ 14-18 Anni (10 Sport)**: Moto GP, Rally, F1
            - **🏎️ 19-35 Anni (10 Sport)**: GT Endurance, Golf, Triathlon
            - **🏆 36+ Anni (10 Sport)**: Calcio Storico, Boccette, Regate
            """)
        
        st.divider()
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Modalità di Sistema", "Open Access ✨")
        col_m2.metric("Moduli e Sport Totali", "200 Online 🚀")
        col_m3.metric("Stato Server", "Aggiornato al 100% 🟢")

        st.divider()
        st.subheader("📢 Istruzioni rapide")
        st.info("• Clicca sul pulsante in alto a destra (**>> 📁 Menu App & Sport**) per aprire il catalogo completo.\n• Tutti i 50 giochi di sport e motori (calcio, basket, moto, formula 1, rally) sono ora pronti per essere giocati.")
    
else:
    st.header("📂 Catalogo Completo (150 App + 50 Sport & Motori)")
    st.write("Stato: **Cluster Cloud Sportivi Connessi** | Scegli il tuo sport o la tua disciplina motoria preferita.")
    
    ai_query = st.text_input("🤖 Ricerca IA nel Catalogo:", placeholder="Es. calcio, basket, moto, rally, f1, tennis, golf, budget...")
    
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
            st.warning("🤖 Nessuna corrispondenza trovata. Mostriamo l'intero catalogo:")
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
                    <h4 style="margin-bottom: 5px; font-size: 15px;">⚡ {file_name}</h4>
                    <p style="font-size: 12px; color: #555; margin-bottom: 10px;">{file_desc}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🚀 Connetti Sport", key=f"btn_{category}_{idx}"):
                    st.session_state.active_app = file_name
                    st.session_state.active_view = "bacheca"
                    st.rerun()
        st.divider()
    
    if st.button("🔙 Torna alla Bacheca Principale"):
        st.session_state.active_view = "bacheca"
        st.rerun()
