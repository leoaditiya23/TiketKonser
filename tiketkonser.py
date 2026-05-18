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

.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.3rem 1.3rem 0.6rem 1.3rem;
    box-shadow: var(--shadow);
    animation: fadeUp 600ms ease both;
}

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
}

div[data-testid="stButton"] button:disabled {
    background: #f1f1f1;
    color: #9aa0a6;
    box-shadow: none;
}

div[data-testid="stSelectbox"] > div,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 12px;
    border: 1px solid var(--border);
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
</style>
""",
    unsafe_allow_html=True,
)

if "fsm" not in st.session_state:
    st.session_state.fsm = OrderFSM()
if "order" not in st.session_state:
    st.session_state.order = {
        "event": None,
        "date": None,
        "category": None,
        "qty": 1,
    }
if "booking_code" not in st.session_state:
    st.session_state.booking_code = None
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

fsm = st.session_state.fsm
order = st.session_state.order

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
    return f"Rp {value:,}"


def generate_code():
    digits = "".join(random.choice("0123456789") for _ in range(6))
    return f"TKT-{digits}"


def reset_all():
    fsm.reset()
    st.session_state.order = {
        "event": None,
        "date": None,
        "category": None,
        "qty": 1,
    }
    st.session_state.booking_code = None
    st.session_state.confirmed = False


def compute_state(order_data, confirmed):
    if confirmed:
        return "q5"
    if order_data["event"] is None:
        return "q0"
    if order_data["date"] is None:
        return "q1"
    if order_data["category"] is None:
        return "q2"
    if order_data["qty"] < 1:
        return "q3"
    return "q4"


st.title("Pemesanan Tiket Konser")
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

steps = [
    ("q0", "Event"),
    ("q1", "Tanggal"),
    ("q2", "Kategori"),
    ("q3", "Jumlah"),
    ("q4", "Konfirmasi"),
    ("q5", "Selesai"),
]
current_state = compute_state(order, st.session_state.confirmed)
fsm.state = current_state
current_index = next(index for index, (state, _) in enumerate(steps) if state == current_state)
step_html = "".join(
    f"<span class='step {'done' if index < current_index else 'active' if index == current_index else ''}'>{label}</span>"
    for index, (_, label) in enumerate(steps)
)
st.markdown(f"<div class='stepper'>{step_html}</div>", unsafe_allow_html=True)

col_form, col_summary = st.columns([2, 1], gap="large")

with col_form:
    st.markdown("<p class='section-title'>Form Pemesanan</p>", unsafe_allow_html=True)
    st.caption(f"Langkah saat ini: {fsm.current_label()}")

    event_options = ["Pilih event..."] + list(events.keys())
    event_default = order["event"] if order["event"] else "Pilih event..."
    event_choice = st.selectbox(
        "Event",
        event_options,
        index=event_options.index(event_default),
        disabled=fsm.state != "q0",
    )
    order["event"] = None if event_choice == "Pilih event..." else event_choice

    if order["event"]:
        st.caption(f"Venue: {events[order['event']]['venue']}")
        date_options = ["Pilih tanggal..."] + events[order["event"]]["dates"]
    else:
        date_options = ["Pilih tanggal..."]
    date_default = order["date"] if order["date"] in date_options else "Pilih tanggal..."
    date_choice = st.selectbox(
        "Tanggal",
        date_options,
        index=date_options.index(date_default),
        disabled=order["event"] is None,
    )
    order["date"] = None if date_choice == "Pilih tanggal..." else date_choice

    category_options = ["Pilih kategori..."] + list(categories.keys())
    category_default = order["category"] if order["category"] else "Pilih kategori..."
    category_choice = st.selectbox(
        "Kategori",
        category_options,
        index=category_options.index(category_default),
        disabled=order["date"] is None,
    )
    order["category"] = None if category_choice == "Pilih kategori..." else category_choice

    qty_value = st.number_input(
        "Jumlah tiket",
        min_value=1,
        max_value=10,
        value=int(order["qty"]),
        step=1,
        disabled=order["category"] is None,
    )
    order["qty"] = int(qty_value)

    order_ready = (
        order["event"] is not None
        and order["date"] is not None
        and order["category"] is not None
        and order["qty"] >= 1
    )
    if not order_ready:
        st.session_state.confirmed = False
        st.session_state.booking_code = None

    current_state = compute_state(order, st.session_state.confirmed)
    if fsm.state != current_state:
        fsm.state = current_state
        st.rerun()

    if current_state == "q4" and not st.session_state.confirmed:
        st.info("Silakan cek ringkasan, lalu konfirmasi pesanan.")
        if st.button("Konfirmasi Pesanan"):
            st.session_state.confirmed = True
            if st.session_state.booking_code is None:
                st.session_state.booking_code = generate_code()
            st.rerun()

    if current_state == "q5":
        st.success("Pesanan selesai.")
        st.text_input("Kode booking", value=st.session_state.booking_code, disabled=True)
        if st.button("Buat Pesanan Baru"):
            reset_all()
            st.rerun()

with col_summary:
    st.markdown("<p class='section-title'>Ringkasan Pesanan</p>", unsafe_allow_html=True)

    event_label = order["event"] if order["event"] else "-"
    date_label = order["date"] if order["date"] else "-"
    category_label = order["category"] if order["category"] else "-"
    qty_label = order["qty"] if order["qty"] else 0

    st.markdown(f"Event: {event_label}")
    if order["event"]:
        st.caption(f"Venue: {events[order['event']]['venue']}")
    st.markdown(f"Tanggal: {date_label}")
    st.markdown(f"Kategori: {category_label}")
    st.markdown(f"Jumlah tiket: {qty_label}")

    price = categories.get(order["category"], 0)
    total = price * int(order["qty"]) if price else 0
    st.markdown("---")
    st.markdown(f"Harga per tiket: {format_rupiah(price)}")
    st.metric("Total", format_rupiah(total))

    if st.button("Reset Pesanan"):
        reset_all()
        st.rerun()
