import streamlit as st
import cohere

class CoHere:
    def __init__(self, api_key):
        self.co = cohere.Client(f'{bCcjvMi9w7ymOC7MgnmT5ehN3Vu2ueMvurn6jod1}', '2021-11-08')
    def cohere(self, question):
            return self.co.generate(
                  model='medium',
                  prompt=stevenQa(question),
                  max_tokens=50,
                  temperature=1).generations[0].text
    def stevenAa(question):
            return f''"Steven is a chatbot that answers questions:"

st.header("Co:here application")

api_key = st.text_input("OpenAI API Key:", type="password")

st.header("Your personal chat bot - Steven")

question_for_steven = st.text_input("Question for Steven:")

cohere = CoHere(api_key)

if st.button("Answer"):
    st.write(cohere.cohere(question_for_steven))






#bCcjvMi9w7ymOC7MgnmT5ehN3Vu2ueMvurn6jod1







































