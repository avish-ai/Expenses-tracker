import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
from pydub import AudioSegment
import io

st.set_page_config(page_title="Expense Tracker with Voice", layout="centered")
st.title("💸 Personal Expense Tracker")
st.caption("Track your daily expenses — now with voice input for descriptions!")

# Session state to store expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Voice input section
st.markdown("### 🎤 Record Expense Description (optional)")
audio_bytes = audio_recorder()

voice_description = ""

if audio_bytes:
    try:
        # Convert webm audio to wav
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="webm")
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)
            voice_description = recognizer.recognize_google(audio_data)
            st.success(f"Recognized: {voice_description}")

    except Exception as e:
        st.error(f"Speech recognition failed: {e}")

# Expense input form
with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount (₹)", min_value=1, step=1)
    with col2:
        category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])

    description = st.text_input("Description (auto-filled from voice if available)", value=voice_description)
    submitted = st.form_submit_button("➕ Add Expense")

    if submitted:
        st.session_state.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        st.success("Expense added!")

# Divider
st.markdown("---")

# Expense Summary
st.subheader("📊 Expense Summary")
selected = st.multiselect("Filter by category", options=["Food", "Transport", "Shopping", "Bills", "Other"])

filtered = [e for e in st.session_state.expenses if not selected or e["category"] in selected]

if not filtered:
    st.warning("No expenses to show.")
else:
    total = sum(e["amount"] for e in filtered)
    st.metric(label="Total Spent", value=f"₹{total:,.2f}")

    st.markdown("#### 🧁 Expense Breakdown")
    cat_totals = {}
    for e in filtered:
        cat_totals[e["category"]] = cat_totals.get(e["category"], 0) + e["amount"]

    for cat, amt in cat_totals.items():
        percent = int((amt / total) * 100)
        bar = "🟩" * (percent // 5)
        st.markdown(f"{cat}: ₹{amt:,.2f} ({percent}%)  {bar}")

    st.markdown("#### 🧾 Expense Details")
    for i, e in enumerate(filtered):
        st.write(f"{i+1}. ₹{e['amount']} | {e['category']} | {e['description']}")

# Clear all expenses
if st.button("🧹 Clear All Data"):
    st.session_state.expenses.clear()
    st.success("All expense records cleared!")

# Rate the app
rating = st.slider("Rate this app (1-10)", 1, 10)
st.write("Your rating:", rating)