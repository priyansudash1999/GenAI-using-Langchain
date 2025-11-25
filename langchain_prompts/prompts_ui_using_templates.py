from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")


st.header('Research Tool')

paper_input = st.selectbox("Select Research paper name", ["Attention is all you need", "BERT: Pre-training of deep bidirectional transformers", "GPT-3: Language Models are few-shot Learners", "Diffusion models beat GANs on Image synthesis"])

style_input = st.selectbox("Select Explanation style", ["Begineer", "Technical", "Code-oriented", "Mathemetical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-4 Paragraphs)", "Long (Detailed Explanation)"])

chat_template = load_prompt('template.json')

prompts = chat_template.invoke({
  'paper_input': paper_input,
  'style_input': style_input,
  'length_input': length_input
})

if st.button('Summarize'):
  res = model.invoke(prompts)
  st.write(res.content)