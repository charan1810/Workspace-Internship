import streamlit as st
import google.generativeai as genai

st.title("Chatbot 🤖")

# Configure the generative model
configuration = {
    "temperature": 1,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 5013,
    "response_mime_type": "text/plain",
}

llm = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=configuration,
)

# Load custom CSS from file
def load_css():
    try:
        with open("static/styles.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Make sure 'styles.css' is in the 'static' folder.")

load_css()  # Load CSS at the start

# Callback function to handle user input and generate bot response
def on_click_callback():
    human_prompt = st.session_state.human_prompt
    if human_prompt:
        # Append user prompt to conversation history
        st.session_state.history.append(("User", human_prompt))
        
        chat_session = llm.start_chat(history=[])
        
        # Generate response using generate_text
        response = chat_session.send_message(human_prompt).text
        st.session_state.history.append(("Bot", response))

# Initialize session state
def initialise_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

initialise_session_state()

# Set up chat interface
chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

# Display conversation history
with chat_placeholder:
    for speaker, text in st.session_state.history:
        div = f"""
        <div class="chat-row">
            <strong>{speaker}:</strong> {text}
        </div>
        """
        st.markdown(div, unsafe_allow_html=True)

# Input form for user prompt
with prompt_placeholder:
    st.markdown("**Chat** - _press enter to submit_")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit",
        type="primary",
        on_click=on_click_callback,
    )
