from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")


st.header('Research Tool')
user_input = st.text_input('Enter your prompts')

if st.button('Summarize'):
  res = model.invoke(user_input)
  st.write(res.content)