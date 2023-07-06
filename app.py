import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_wpqugzlc.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am your personal pharmacist :wave:")
    st.title("A 24/7 pharmacist")
    st.write(
        "I am a Personal Pharmacist 24/7 that provides a chatbot service to answer any questions related to medicines."
    )
 

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Overview")
        st.write("##")
        st.write(
            """
          Our project focuses on the development of an advanced virtual assistant bot specifically designed to assist diabetes patients with inquiries about potential conflicts between their medications. 
        Diabetes medication conflicts can occur when certain medications, taken together, produce harmful or undesirable effects.
        We aim to enhance medication safety and improve patient education for diabetes management. 
        Our website serves as the platform for this bot, offering a user-friendly interface for easy access to reliable and up-to-date information on diabetes medications. 
        Through our project, we strive to empower individuals with the knowledge necessary to make informed decisions about their diabetes healthcare.
        Together, let's embark on this journey towards a safer and more informed diabetes management experience for all.
          """
        )
        st.write("[chatbot link >](  )")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Your Personal Phamacist for more details!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/RahafRafdan@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
