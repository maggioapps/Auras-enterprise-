import streamlit as st
import streamlit.components.v1 as components

# Configurazione della pagina principale
st.set_page_config(
    page_title="AuraSync - Cognitive Operating System", 
    page_icon="🧠", 
    layout="wide"
)

# --- 1. MEMORIA E DATABASE UTENTI SIMULATO ---
if 'utenti_registrati' not in st.session_state:
    st.session_state.utenti_registrati = {"admin_principale": "TuaPasswordAdminSegreta123"}

if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None

if 'wallet_oro' not in st.session_state:
    st.session_state.wallet_oro = 10  # Bonus onboarding iniziale
if 'wallet_platino' not in st.session_state:
    st.session_state.wallet_platino = 3
if 'streak_giorni' not in st.session_state:
    st.session_state.streak_giorni = 1
if 'pet_health' not in st.session_state:
    st.session_state.pet_health = 100 

if 'mostra_ruota_auto' not in st.session_state:
    st.session_state.mostra_ruota_auto = True

# --- 2. BARRA LATERALE: ACCOUNT, WALLET, ABBONAMENTI & ADMIN ---
st.sidebar.markdown("### 🔐 AuraSync Security Hub")

if st.session_state.utente_corrente is None:
    azione_acc = st.sidebar.radio("Accesso:", ["Accedi (Login)", "Crea Nuovo Account"])
    
    if azione_acc == "Crea Nuovo Account":
        st.sidebar.subheader("Registrazione PWA")
        u_reg = st.sidebar.text_input("Scegli Username")
        p_reg = st.sidebar.text_input("Scegli Password", type="password")
        eta_reg = st.sidebar.number_input("Età", min_value=1, max_value=120, value=25)
        if st.sidebar.button("Registrati Ora"):
            if u_reg and p_reg:
                if u_reg in st.session_state.utenti_registrati:
                    st.sidebar.error("Username già in uso!")
                else:
                    st.session_state.utenti_registrati[u_reg] = {"pass": p_reg, "eta": eta_reg}
                    st.sidebar.success("Account creato con successo! Fai il login.")
            else:
                st.sidebar.warning("Compila tutti i campi.")
    else:
        st.sidebar.subheader("Login Utente")
        u_log = st.sidebar.text_input("Username")
        p_log = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Entra"):
            db_user = st.session_state.utenti_registrati.get(u_log)
            pass_valida = False
            eta_utente = 25
            
            if isinstance(db_user, dict) and db_user.get("pass") == p_log:
                pass_valida = True
                eta_utente = db_user.get("eta", 25)
            elif u_log == "admin_principale" and p_log == "TuaPasswordAdminSegreta123":
                pass_valida = True
                eta_utente = 30
                
            if pass_valida:
                st.session_state.utente_corrente = u_log
                st.session_state.utente_eta = eta_utente
                st.session_state.mostra_ruota_auto = True
                st.rerun()
            else:
                st.sidebar.error("Credenziali non valide!")
else:
    st.sidebar.success(f"Benvenuto, **{st.session_state.utente_corrente}**!")
    st.sidebar.markdown(f"🪙 **Oro:** {st.session_state.wallet_oro} | 💎 **Platino:** {st.session_state.wallet_platino}")
    st.sidebar.markdown(f"🔥 **Streak:** {st.session_state.streak_giorni} giorni | 🐾 **Pet Health:** {st.session_state.pet_health}%")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💳 Abbonamenti & Store Stripe")
    st.sidebar.markdown("[🪙 Acquista Gettoni](https://buy.stripe.com/tuo_link_gettoni)")
    st.sidebar.markdown("[⭐ Abbonamento Full Access (49€)](https://buy.stripe.com/tuo_link_abbonamento)")
    st.sidebar.markdown("[🚀 Licenza Master Branch (100€)](https://buy.stripe.com/tuo_link_100_euro)")
    st.sidebar.markdown("---")
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.utente_corrente = None
        st.session_state.mostra_ruota_auto = True
        st.rerun()

SEI_ADMIN = (st.session_state.utente_corrente == "admin_principale")
ETA_UTENTE = st.session_state.get('utente_eta', 25)
IS_MAGGIORENNE = (SEI_ADMIN or ETA_UTENTE >= 18)

if SEI_ADMIN:
    st.sidebar.info("👑 **Modalità Admin Suprema:** Risorse illimitate e sbloccate.")

# --- 3. INTESTAZIONE CON BOTTONE SOS ---
col_head1, col_head2 = st.columns([4, 1])

with col_head1:
    st.title("🚀 AuraSync - Cognitive Operating System")

with col_head2:
    st.markdown("<br>", unsafe_allow_html=True) 
    if st.button("🚨 AURA SOS", type="primary", use_container_width=True):
        st.error("⚡ **EMERGENZA ATTIVATA!** Protocollo di crisi avviato in background.")

st.write("Piattaforma SaaS PWA globale. Esplora liberamente i moduli specialistici e i tool di intelligenza artificiale.")

# --- 4. VERA RUOTA DELLA FORTUNA GRAFICA (HTML/JS INTERATTIVA) ---
if st.session_state.mostra_ruota_auto:
    st.markdown("---")
    col_rw1, col_rw2 = st.columns([3, 1])
    with col_rw1:
        st.warning("🎁 **Bonus Benvenuto Rilevato!** Gira la ruota interattiva qui sotto per vincere i tuoi gettoni gratuiti.")
    with col_rw2:
        if st.button("❌ Chiudi Finestra Ruota", use_container_width=True):
            st.session_state.mostra_ruota_auto = False
            st.rerun()

    # Componente HTML personalizzato con la ruota grafica rotante
    ruota_html = """
    <div style="text-align: center; font-family: sans-serif;">
        <div style="position: relative; display: inline-block;">
            <canvas id="wheel" width="300" height="300" style="border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.2);"></canvas>
            <div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-bottom: 20px solid #ff4b4b;"></div>
        </div>
        <br><br>
        <button onclick="spinWheel()" id="spinBtn" style="background-color: #ff4b4b; color: white; border: none; padding: 12px 24px; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">🎡 Gira la Ruota Grafica!</button>
        <p id="resultText" style="margin-top: 15px; font-size: 18px; font-weight: bold; color: #31333F;"></p>
    </div>

    <script>
        const sectors = [
            {color: "#FF5733", text: "+1 Oro"},
            {color: "#33FF57", text: "+5 Oro"},
            {color: "#3357FF", text: "+2 Oro"},
            {color: "#F3FF33", text: "+3 Oro"},
            {color: "#FF33F3", text: "+10 Oro"},
            {color: "#33FFF6", text: "+2 Platino"}
        ];

        const canvas = document.getElementById("wheel");
        const ctx = canvas.getContext("2d");
        const numSectors = sectors.length;
        const arc = Math.PI / (numSectors / 2);
        let startAngle = 0;
        let outsideRadius = 140;
        let textRadius = 90;
        let insideRadius = 20;

        function drawSector(sector, i) {
            let angle = startAngle + i * arc;
            ctx.fillStyle = sector.color;
            ctx.beginPath();
            ctx.arc(150, 150, outsideRadius, angle, angle + arc, false);
            ctx.arc(150, 150, insideRadius, angle + arc, angle, true);
            ctx.stroke();
            ctx.fill();

            ctx.save();
            ctx.shadowOffsetX = -1;
            ctx.shadowOffsetY = -1;
            ctx.shadowBlur = 0;
            ctx.fillStyle = "white";
            ctx.translate(150 + Math.cos(angle + arc / 2) * textRadius, 150 + Math.sin(angle + arc / 2) * textRadius);
            ctx.rotate(angle + arc / 2 + Math.PI / 2);
            ctx.font = "bold 14px sans-serif";
            ctx.fillText(sector.text, -ctx.measureText(sector.text).width / 2, 0);
            ctx.restore();
        }

        function drawWheel() {
            ctx.clearRect(0,0,300,300);
            for(let i = 0; i < numSectors; i++) {
                drawSector(sectors[i], i);
            }
        }

        let spinAngleStart = 0;
        let spinTime = 0;
        let spinTimeTotal = 0;

        function spinWheel() {
            spinAngleStart = Math.random() * 10 + 10;
            spinTime = 0;
            spinTimeTotal = Math.random() * 3000 + 4000;
            rotateWheel();
            document.getElementById("spinBtn").disabled = true;
        }

        function rotateWheel() {
            spinTime += 30;
            if(spinTime >= spinTimeTotal) {
                stopRotateWheel();
                return;
            }
            let spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
            startAngle += (spinAngle * Math.PI / 180);
            drawWheel();
            setTimeout(rotateWheel, 30);
        }

        function stopRotateWheel() {
            let degrees = startAngle * 180 / Math.PI + 90;
            let arcd = arc * 180 / Math.PI;
            let index = Math.floor((360 - degrees % 360) / arcd);
            ctx.save();
            let winningText = sectors[index % numSectors].text;
            document.getElementById("resultText").innerHTML = "🎉 Hai vinto: " + winningText + "!";
            document.getElementById("spinBtn").disabled = false;
            ctx.restore();
        }

        function easeOut(t, b, c, d) {
            let ts = (t/=d)*t;
            let tc = ts*t;
            return b+c*(tc + -3*ts + 3*t);
        }

        drawWheel();
    </script>
    """
    components.html(ruota_html, height=420)
    st.markdown("---")

st.subheader("🗂️ Indice Generale delle Opzioni (In ordine alfabetico)")

# Gestione navigazione moduli
if 'modulo_attivo' not in st.session_state:
    st.session_state.modulo_attivo = "Home"

if st.session_state.modulo_attivo == "Home":
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("### 🤖 AuraBot & Modelli IA")
        st.write("Libreria completa di Branch IA e Trend globali.")
        if st.button("Apri AuraBot & Modelli"):
            st.session_state.modulo_attivo = "ModelliIA"
            st.rerun()
            
        st.markdown("### 🌿 AuraGreen & Botanica")
        st.write("Pollice verde digitale e diagnosi piante.")
        if st.button("Apri AuraGreen"):
            st.session_state.modulo_attivo = "AuraGreen"
            st.rerun()

        st.markdown("### 👨‍👩‍👧‍👦 AuraKids & Paws (0-18)")
        st.write("Nutrizione, svezzamento e supporto emotivo.")
        if st.button("Apri AuraKids"):
            st.session_state.modulo_attivo = "AuraKids"
            st.rerun()

    with c2:
        st.markdown("### 🛠️ AuraFix & Meccanica")
        st.write("Guide di riparazione fai-da-te.")
        if st.button("Apri AuraFix"):
            st.session_state.modulo_attivo = "AuraFix"
            st.rerun()

        st.markdown("### 🐾 AuraPets & Paws")
        st.write("Companion empatico per animali domestici.")
        if st.button("Apri AuraPets"):
            st.session_state.modulo_attivo = "AuraPets"
            st.rerun()

        if IS_MAGGIORENNE:
            st.markdown("### 💬 AuraMatch (Incontri 18+)")
            st.write("Matchmaking basato su compatibilità neurale.")
            if st.button("Apri AuraMatch"):
                st.session_state.modulo_attivo = "AuraMatch"
                st.rerun()

    with c3:
        st.markdown("### 🚨 AuraTwin & Extra")
        st.write("Aura Twin, Capsula del tempo e favole.")
        if st.button("Apri Funzioni Extra"):
            st.session_state.modulo_attivo = "Extra"
            st.rerun()

        if IS_MAGGIORENNE:
            st.markdown("### 🎰 AuraSlots (Mini-Casinò 18+)")
            st.write("Arcade virtuale con micro-puntate.")
            if st.button("Apri AuraSlots"):
                st.session_state.modulo_attivo = "AuraSlots"
                st.rerun()

        st.markdown("### 💎 Token Economy & Store")
        st.write("Gestione wallet e abbonamenti Stripe.")
        if st.button("Apri Wallet & Store"):
            st.session_state.modulo_attivo = "WalletStore"
            st.rerun()

else:
    if st.button("⬅️ Torna alla Home Principale"):
        st.session_state.modulo_attivo = "Home"
        st.rerun()
    st.markdown("---")

    # Routing dei moduli
    if st.session_state.modulo_attivo == "ModelliIA":
        st.header("🤖 Libreria Modelli Branch IA & Trend Globali")
        st.write("Seleziona le categorie dalla libreria avanzata.")
    elif st.session_state.modulo_attivo == "AuraGreen":
        st.header("🌿 AuraGreen & Botanica Digitale")
        st.file_uploader("Carica foto pianta", type=["jpg", "png", "jpeg"])
    elif st.session_state.modulo_attivo == "AuraKids":
        st.header("👨‍👩‍👧‍👦 AuraKids & Paws (Fascia 0-18 Anni)")
        st.slider("Fascia d'età:", 0, 18, 5)
    elif st.session_state.modulo_attivo == "AuraFix":
        st.header("🛠️ AuraFix & Meccanica Pratica")
        st.text_input("Cosa devi riparare?")
    elif st.session_state.modulo_attivo == "AuraPets":
        st.header("🐾 AuraPets & Paws")
        st.selectbox("Animale:", ["Cane", "Gatto", "Altro"])
    elif st.session_state.modulo_attivo == "AuraMatch" and IS_MAGGIORENNE:
        st.header("💬 AuraMatch (18+)")
    elif st.session_state.modulo_attivo == "Extra":
        st.header("🚨 Funzioni Extra")
    elif st.session_state.modulo_attivo == "AuraSlots" and IS_MAGGIORENNE:
        st.header("🎰 AuraSlots (18+)")
    elif st.session_state.modulo_attivo == "WalletStore":
        st.header("💎 Token Economy & Store")
        st.write(f"Oro: {st.session_state.wallet_oro} | Platino: {st.session_state.wallet_platino}")
