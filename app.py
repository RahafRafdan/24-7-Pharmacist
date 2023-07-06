import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Pharmacist 24/7", page_icon=":robot:", layout="wide")


def make_chain(openai_api_key):
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature="0",
        openai_api_key=openai_api_key,
        # verbose=True
    )
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

    vector_store = Chroma(
        collection_name="answer",
        embedding_function=embedding,
        persist_directory="ldata/chroma",
    )

    return ConversationalRetrievalChain.from_llm(
        model,
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        # verbose=True,
    )

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
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Your Personal Phamacist")
    st.write("##")

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()


def get_text():
    input_text = st.text_area(label="question Input", label_visibility='collapsed', placeholder="Your question ...", key="question_input")
    return input_text

question_input = get_text()

if len(question_input.split(" ")) > 700:
    st.write("Please enter a shorter question. The maximum length is 700 words.")
    st.stop()

def update_text_with_example():
    print ("in updated")
    st.session_state.question_input = "can i drink milk with metformin?"

st.button("*See An Example*", type='secondary', help="Click to see an example of a question.", on_click=update_text_with_example)

st.markdown("### 🤖:")

if question_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    llm = make_chain(openai_api_key=openai_api_key)
    chat_history = []


    response = llm({"question": question_input, "chat_history": chat_history})
    
# Retrieve answer
    answer = response["answer"]
    source = response["source_documents"]
    chat_history.append(HumanMessage(content=question_input))
    chat_history.append(AIMessage(content=answer))
    st.write(answer)


    st.markdown("### source:")
    st.write(source)