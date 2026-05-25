import random
import streamlit as st
from engine import OrderFSM

st.set_page_config(page_title="Pemesanan Tiket Konser", layout="wide")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Work+Sans:wght@400;500;600&display=swap');

:root {
    --ink: #1f2328;
    --muted: #5b6772;
    --accent: #ff7a00;
    --accent-2: #0fa3b1;
    --card: #ffffff;
    --border: rgba(31, 35, 40, 0.12);
    --shadow: 0 18px 40px rgba(19, 39, 56, 0.12);
}

html, body, [class*="css"]  {
    font-family: 'Work Sans', sans-serif;
    color: var(--ink);
}

.stApp {
    background:
        radial-gradient(1200px 500px at 10% -10%, #ffe7d1 0%, rgba(255, 231, 209, 0) 60%),
        radial-gradient(900px 420px at 90% 0%, #d8f1ff 0%, rgba(216, 241, 255, 0) 60%),
        linear-gradient(180deg, #fff8f0 0%, #f8fbff 60%, #fffdf9 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, .hero-title {
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -0.02em;
}

.hero {
    background: linear-gradient(120deg, #ffffff 0%, #fff1e3 60%, #e7f6ff 100%);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 1.8rem 2rem;
    box-shadow: var(--shadow);
    animation: fadeUp 600ms ease both;
    margin-bottom: 2rem;
}

.hero-inner {
    display: flex;
    gap: 2rem;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.eyebrow {
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    color: var(--accent-2);
    margin-bottom: 0.3rem;
    font-weight: 600;
}

.hero-title {
    font-size: 2.5rem;
    margin: 0 0 0.5rem 0;
}

.hero-sub {
    margin: 0;
    color: var(--muted);
    font-size: 1rem;
    max-width: 520px;
}

.badge-row {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.badge {
    background: var(--accent-2);
    color: #ffffff;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge.alt {
    background: var(--accent);
}

.badge.neutral {
    background: #1f2328;
}

.hero-panel {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1rem 1.2rem;
    min-width: 220px;
    box-shadow: 0 12px 28px rgba(19, 39, 56, 0.12);
}

.panel-title {
    font-weight: 600;
    margin: 0 0 0.3rem 0;
}

.panel-text {
    margin: 0 0 0.6rem 0;
    color: var(--muted);
}

.panel-stat {
    font-weight: 700;
    font-size: 1.1rem;
    margin: 0;
}

.stepper {
    display: flex;
    gap: 0.35rem;
    flex-wrap: wrap;
    margin: 1.2rem 0 1.5rem 0;
}

.step {
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
    border: 1px solid var(--border);
    font-size: 0.78rem;
    color: var(--muted);
    background: #ffffff;
    animation: fadeUp 500ms ease both;
    transition: all 0.3s ease;
}

.step.done {
    background: #f2fff9;
    border-color: #86d3b7;
    color: #2f7b5c;
}

.step.active {
    background: var(--accent-2);
    border-color: var(--accent-2);
    color: #ffffff;
}

.stepper .step:nth-child(1) { animation-delay: 0ms; }
.stepper .step:nth-child(2) { animation-delay: 60ms; }
.stepper .step:nth-child(3) { animation-delay: 120ms; }
.stepper .step:nth-child(4) { animation-delay: 180ms; }
.stepper .step:nth-child(5) { animation-delay: 240ms; }
.stepper .step:nth-child(6) { animation-delay: 300ms; }

.section-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.4rem;
}

div[data-testid="stButton"] button {
    background: linear-gradient(90deg, #ff7a00, #ffb347);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    box-shadow: 0 12px 24px rgba(255, 122, 0, 0.2);
    transition: all 0.2s ease;
}

div[data-testid="stButton"] button:hover {
    transform: translateY(-2px);
    box-shadow: 0 16px 32px rgba(255, 122, 0, 0.3);
}

div[data-testid="stButton"] button:disabled {
    background: #f1f1f1;
    color: #9aa0a6;
    box-shadow: none;
    transform: none;
}

div[data-testid="stMetric"] {
    background: #fff5ea;
    border: 1px solid #ffd9b3;
    border-radius: 14px;
    padding: 0.6rem 0.8rem;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 900px) {
    .hero-title { font-size: 2rem; }
    .hero-inner { align-items: flex-start; }
}

/* Fix mobile scaling issues */
@media (max-width: 600px) {
    .hero-title { font-size: 1.75rem; }
    .hero { padding: 1.2rem 1rem; }
}
</style>
"""
    , unsafe_allow_html=True
)

if "fsm" not in st.session_state:
    st.session_state.fsm = OrderFSM()
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False
if "booking_code" not in st.session_state:
    st.session_state.booking_code = None

if "ev_key" not in st.session_state: st.session_state.ev_key = "Pilih event..."
if "dt_key" not in st.session_state: st.session_state.dt_key = "Pilih tanggal..."
if "kt_key" not in st.session_state: st.session_state.kt_key = "Pilih kategori..."
if "qt_key" not in st.session_state: st.session_state.qt_key = 1

events = {
    "Konser Harmoni Nusantara": {
        "dates": ["2026-06-01", "2026-06-02"],
        "venue": "Gedung Musik Indonesia",
    },
    "Festival Senja Elektronik": {
        "dates": ["2026-06-10"],
        "venue": "Lapangan Kota",
    },
    "Orkestra Pagi": {
        "dates": ["2026-07-01", "2026-07-02"],
        "venue": "Aula Budaya",
    },
}

categories = {
    "VIP": 350000,
    "Reguler": 200000,
    "Ekonomi": 120000,
}

def format_rupiah(value):
    return f"Rp {value:,}".replace(",", ".")

def generate_code():
    digits = "".join(random.choice("0123456789") for _ in range(6))
    return f"TKT-{digits}"

def reset_all():
    st.session_state.fsm.reset()
    st.session_state.confirmed = False
    st.session_state.booking_code = None
    st.session_state.ev_key = "Pilih event..."
    st.session_state.dt_key = "Pilih tanggal..."
    st.session_state.kt_key = "Pilih kategori..."
    st.session_state.qt_key = 1

# Logic parsing FSM and Order
def build_current_state():
    st.session_state.fsm.reset()
    
    ev = st.session_state.ev_key if st.session_state.ev_key != "Pilih event..." else None
    dt = st.session_state.dt_key if st.session_state.dt_key != "Pilih tanggal..." else None
    kt = st.session_state.kt_key if st.session_state.kt_key != "Pilih kategori..." else None
    qt = int(st.session_state.qt_key)
    
    # Simulate automaton
    if st.session_state.confirmed:
        st.session_state.fsm.state = "q5"
        return
        
    st.session_state.fsm.state = "q0"
    if ev is not None:
        st.session_state.fsm.step("E") 
        if dt is not None:
            st.session_state.fsm.step("T")
            if kt is not None:
                st.session_state.fsm.step("K")
                if qt >= 1:
                    st.session_state.fsm.step("J")

def on_event_change():
    st.session_state.dt_key = "Pilih tanggal..."
    st.session_state.kt_key = "Pilih kategori..."
    st.session_state.confirmed = False
    
def on_date_change():
    st.session_state.kt_key = "Pilih kategori..."
    st.session_state.confirmed = False

def on_category_change():
    st.session_state.confirmed = False
    
def on_qty_change():
    st.session_state.confirmed = False

hero_html = f"""
<div class="hero">
    <div class="hero-inner">
        <div>
            <p class="eyebrow">Ticketing Portal</p>
            <h1 class="hero-title">KonserPass</h1>
            <p class="hero-sub">Pesan tiket konser favorit dengan alur yang cepat, jelas, dan rapi.</p>
            <div class="badge-row">
                <span class="badge">Event kurasi</span>
                <span class="badge alt">Booking instan</span>
                <span class="badge neutral">Harga transparan</span>
            </div>
        </div>
        <div class="hero-panel">
            <p class="panel-title">Ringkas</p>
            <p class="panel-text">Satu alur, tanpa langkah berulang.</p>
            <p class="panel-stat">{len(events)} event aktif</p>
        </div>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

build_current_state()
fsm = st.session_state.fsm
current_state = fsm.state

steps = [
    ("q0", "Event"),
    ("q1", "Tanggal"),
    ("q2", "Kategori"),
    ("q3", "Jumlah"),
    ("q4", "Konfirmasi"),
    ("q5", "Selesai"),
]
current_index = next((index for index, (state, _) in enumerate(steps) if state == current_state), 0)
step_html = "".join(
    f"<span class='step {'done' if index < current_index else 'active' if index == current_index else ''}'>{label}</span>"
    for index, (_, label) in enumerate(steps)
)
st.markdown(f"<div class='stepper'>{step_html}</div>", unsafe_allow_html=True)

col_form, col_summary = st.columns([12, 10])

with col_form:
    st.markdown("<p class='section-title'>Form Pemesanan</p>", unsafe_allow_html=True)
    st.caption(f"Status: {fsm.current_label()}")

    event_options = ["Pilih event..."] + list(events.keys())
    st.selectbox(
        "Pilih Event",
        event_options,
        key="ev_key",
        disabled=current_state == "q5",
        on_change=on_event_change
    )

    ev_val = st.session_state.ev_key
    if ev_val != "Pilih event...":
        st.info(f"📍 Venue: {events[ev_val]['venue']}")
        date_options = ["Pilih tanggal..."] + events[ev_val]["dates"]
    else:
        date_options = ["Pilih tanggal..."]

    st.selectbox(
        "Pilih Tanggal",
        date_options,
        key="dt_key",
        disabled=ev_val == "Pilih event..." or current_state == "q5",
        on_change=on_date_change
    )
    
    dt_val = st.session_state.dt_key
    category_options = ["Pilih kategori..."] + list(categories.keys())
    st.selectbox(
        "Pilih Kategori",
        category_options,
        key="kt_key",
        disabled=dt_val == "Pilih tanggal..." or current_state == "q5",
        on_change=on_category_change
    )

    kt_val = st.session_state.kt_key
    st.number_input(
        "Jumlah tiket",
        min_value=1,
        max_value=10,
        step=1,
        key="qt_key",
        disabled=kt_val == "Pilih kategori..." or current_state == "q5",
        on_change=on_qty_change
    )
    
    qt_val = st.session_state.qt_key

    if ev_val != "Pilih event..." and dt_val != "Pilih tanggal..." and kt_val != "Pilih kategori..." and qt_val >= 1:
        if not st.session_state.confirmed:
            st.divider()
            st.info("✅ Pesanan siap dikonfirmasi. Periksa ringkasan di samping lalu klik tombol di bawah.")
            if st.button("Konfirmasi Pesanan", use_container_width=True):
                st.session_state.confirmed = True
                if st.session_state.booking_code is None:
                    st.session_state.booking_code = generate_code()
                st.rerun()

    if current_state == "q5":
        st.divider()
        st.success("🎉 Pesanan selesai!")
        st.text_input("Kode Booking Anda (Simpan ini)", value=st.session_state.booking_code, disabled=True)
        if st.button("Buat Pesanan Baru", use_container_width=True):
            reset_all()
            st.rerun()

with col_summary:
    st.markdown("<p class='section-title'>Ringkasan Tiket</p>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"**🎟️ Event:** {ev_val if ev_val != 'Pilih event...' else '-'}")
        st.markdown(f"**📅 Tanggal:** {dt_val if dt_val != 'Pilih tanggal...' else '-'}")
        st.markdown(f"**🎫 Kategori:** {kt_val if kt_val != 'Pilih kategori...' else '-'}")
        st.markdown(f"**👥 Jumlah Set:** {qt_val if (ev_val != 'Pilih event...' and dt_val != 'Pilih tanggal...' and kt_val != 'Pilih kategori...') else 0} tiket")

        price = categories.get(kt_val, 0) if kt_val != 'Pilih kategori...' else 0
        total = price * int(qt_val) if price else 0
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        col1.markdown(f"<div style='color:var(--muted); font-size: 0.9rem;'>Harga Satuan<br/><b>{format_rupiah(price)}</b></div>", unsafe_allow_html=True)
        col2.markdown(f"<div style='color:var(--muted); font-size: 0.9rem;'>Total Harga<br/><b>{format_rupiah(total)}</b></div>", unsafe_allow_html=True)
        
        st.write("")

    if st.button("Reset Data", use_container_width=True):
        reset_all()
        st.rerun()