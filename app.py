import streamlit as st
from google import genai

# ==================================================
# CONFIG
# ==================================================

MODEL_NAME = "gemma-4-26b-a4b-it"

client = genai.Client()

st.set_page_config(
    page_title="CampusLens AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
"""
<style>

.stApp {
    background: #f7f8fc;
}

/* HERO */
.hero {
    padding: 2.5rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #111827, #312e81);
    color: white;
    margin-bottom: 1.8rem;
}

.hero h1 {
    font-size: 3rem;
    margin: 0 0 0.6rem 0;
    font-weight: 800;
}

.hero p {
    font-size: 1.15rem;
    margin: 0;
    opacity: 0.9;
}

/* CARDS */
.card {
    padding: 1.4rem;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
}

/* WORKFLOW */
.step {
    padding: 1.3rem;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    min-height: 150px;
}

.step-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.step-title {
    font-size: 1.15rem;
    font-weight: 700;
}

.step-text {
    color: #6b7280;
    margin-top: 0.4rem;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #6b7280;
    padding: 2rem 0;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #111827;
}

section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""",
unsafe_allow_html=True,
)

# ==================================================
# GEMMA 4 FUNCTIONS
# ==================================================


def analyze_notice(image_path):
    """Analyze a college notice using Gemma 4."""

    notice = client.files.upload(file=image_path)

    prompt = """
You are CampusLens AI, an intelligent assistant for college students.

Read the uploaded college notice, poster, or visual document carefully.

Extract the important information.

Return the answer using exactly this structure:

EVENT:
DATE:
TIME:
VENUE:
DEADLINE:
REQUIREMENTS:

SUMMARY:

IMPORTANT DETAILS:

Rules:
- Only use information actually present in the document.
- Never guess or invent information.
- If something is not mentioned, write "Not mentioned".
- Keep the answer clear and concise.
- Include multiple dates, times, or venues if present.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[notice, prompt],
    )

    return response.text


def ask_question(image_path, question):
    """Answer a question about the uploaded notice."""

    notice = client.files.upload(file=image_path)

    prompt = f"""
You are CampusLens AI.

Answer the student's question using ONLY the information
contained in the uploaded college notice.

Student question:
{question}

Rules:
- Do not guess.
- Do not use outside knowledge.
- If the answer is not present in the notice, say:
  "That information is not mentioned in the notice."
- Give a short and direct answer.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[notice, prompt],
    )

    return response.text


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        """
        <h2>🎓 CampusLens</h2>
        <h3>Understand. Extract. Ask.</h3>
        <p>
        Your AI assistant for college notices
        and visual documents.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <h3>🧠 Powered by</h3>
        <h3>Gemma 4 26B</h3>
        <p>
        Multimodal AI for understanding
        visual college information.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <h3>✨ What CampusLens does</h3>
        <p>📄 Understand notices</p>
        <p>🧠 Extract important information</p>
        <p>📅 Find dates and deadlines</p>
        <p>📍 Find venues</p>
        <p>💬 Answer questions</p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.caption("Built for MLH Hack Day 2026")


# ==================================================
# HERO
# ==================================================

st.markdown(
"""<div class="hero">
<h1>🎓 CampusLens AI</h1>
<p>Turn confusing college notices into clear, useful information — instantly.</p>
</div>""",
unsafe_allow_html=True,
)


# ==================================================
# HOW IT WORKS
# ==================================================

st.subheader("⚡ How CampusLens works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
"""<div class="step">
<div class="step-icon">📄</div>
<div class="step-title">Understand</div>
<div class="step-text">
Upload a poster, notice or visual document.
</div>
</div>""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
"""<div class="step">
<div class="step-icon">🧠</div>
<div class="step-title">Extract</div>
<div class="step-text">
Gemma 4 identifies dates, times, venues and key details.
</div>
</div>""",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
"""<div class="step">
<div class="step-icon">💬</div>
<div class="step-title">Ask</div>
<div class="step-text">
Ask natural-language questions about the notice.
</div>
</div>""",
        unsafe_allow_html=True,
    )


st.divider()


# ==================================================
# UPLOAD
# ==================================================

st.subheader("📄 Analyze a College Notice")

uploaded_file = st.file_uploader(
    "Upload a notice, poster, assignment sheet or campus document",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file:

    left, right = st.columns([1, 1])

    with left:

        st.image(
            uploaded_file,
            caption="Uploaded document",
            use_container_width=True,
        )

    with right:

        st.markdown(
"""<div class="card">
<h3>🔍 Ready to analyze</h3>
<p>
Gemma 4 will identify dates, times, venues,
deadlines, requirements and other important details.
</p>
</div>""",
            unsafe_allow_html=True,
        )

        analyze_button = st.button(
            "🚀 Analyze with Gemma 4",
            type="primary",
            use_container_width=True,
        )

        if analyze_button:

            with st.spinner("🧠 Gemma 4 is analyzing the document..."):

                try:

                    with open("uploaded_notice.jpg", "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    result = analyze_notice("uploaded_notice.jpg")

                    st.session_state["analysis"] = result

                    st.success("✅ Analysis complete!")

                except Exception as e:

                    st.error(f"Something went wrong: {e}")


# ==================================================
# ANALYSIS RESULT
# ==================================================

if "analysis" in st.session_state:

    st.divider()

    st.subheader("📋 What Gemma 4 found")

    st.info(
        "Gemma 4 converted the visual notice into useful information."
    )

    st.markdown(st.session_state["analysis"])


# ==================================================
# Q&A
# ==================================================

if "analysis" in st.session_state:

    st.divider()

    st.subheader("💬 Ask CampusLens")

    st.write(
        "Ask anything about the uploaded notice."
    )

    # Suggested questions

    q1, q2, q3, q4 = st.columns(4)

    if q1.button(
        "📍 Where is the event?",
        use_container_width=True,
    ):
        st.session_state["question"] = "Where is the event?"

    if q2.button(
        "📅 When is it?",
        use_container_width=True,
    ):
        st.session_state["question"] = "When is the event?"

    if q3.button(
        "⏰ What time?",
        use_container_width=True,
    ):
        st.session_state["question"] = "What time does the event start?"

    if q4.button(
        "📋 Requirements?",
        use_container_width=True,
    ):
        st.session_state["question"] = "What are the requirements?"

    question = st.text_input(
        "Your question",
        value=st.session_state.get("question", ""),
        placeholder="Example: Where is the movie screening?",
    )

    if st.button(
        "🤖 Ask Gemma 4",
        type="primary",
        use_container_width=True,
    ):

        if not question.strip():

            st.warning("Please enter a question first.")

        else:

            with st.spinner("🧠 Gemma 4 is thinking..."):

                try:

                    answer = ask_question(
                        "uploaded_notice.jpg",
                        question,
                    )

                    st.markdown("### 💡 Answer")

                    st.success(answer)

                except Exception as e:

                    st.error(f"Something went wrong: {e}")


# ==================================================
# FOOTER
# ==================================================

st.markdown(
"""<div class="footer">
<b>CampusLens AI</b> · Powered by Gemma 4 · Built for MLH Hack Day 2026 🚀
</div>""",
unsafe_allow_html=True,
)