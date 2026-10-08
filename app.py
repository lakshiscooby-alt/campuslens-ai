import streamlit as st
from google import genai


# -----------------------------
# Gemma 4 setup
# -----------------------------
client = genai.Client()


def analyze_notice(image_path):
    notice = client.files.upload(file=image_path)

    prompt = """
You are CampusLens AI, an assistant for college students.

Read the college notice carefully and extract the important information.

Return the answer in this format:

EVENT:
DATE:
TIME:
VENUE:
DEADLINE:
REQUIREMENTS:

SUMMARY:

IMPORTANT DETAILS:

If something is not mentioned in the notice, write "Not mentioned".
Do not guess or invent information.
"""

    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it"
,        contents=[notice, prompt]
    )

    return response.text


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="CampusLens AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 CampusLens AI")
st.write("Your AI assistant for understanding college notices and documents.")

st.divider()

st.header("📄 Upload a Notice")

uploaded_file = st.file_uploader(
    "Upload a college notice or poster",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    st.image(
        uploaded_file,
        caption="Uploaded Notice",
        width=600
    )

    if st.button("🔍 Analyze with Gemma 4"):

        with st.spinner("Gemma 4 is analyzing the notice..."):

            # Save uploaded image temporarily
            with open("uploaded_notice.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())

            try:
                result = analyze_notice("uploaded_notice.jpg")

                st.session_state["analysis"] = result

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -----------------------------
# Display AI result
# -----------------------------
if "analysis" in st.session_state:

    st.divider()

    st.header("📋 Gemma 4 Analysis")

    st.markdown(st.session_state["analysis"])


# -----------------------------
# Q&A
# -----------------------------
st.divider()

st.header("💬 Ask CampusLens")

question = st.text_input(
    "Ask a question about the uploaded notice",
    placeholder="Example: What should I bring?"
)

if st.button("Ask AI"):

    if not question:
        st.warning("Please enter a question.")

    elif "analysis" not in st.session_state:
        st.warning("Please analyze a notice first.")

    else:
        st.info(
            "Q&A integration is the next step. "
            "The notice analysis is already working!"
        )