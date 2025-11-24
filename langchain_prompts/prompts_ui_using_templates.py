from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")


st.header('Research Tool')

paper_input = st.selectbox("Select Research paper name", ["Attention is all you need", "BERT: Pre-training of deep bidirectional transformers", "GPT-3: Language Models are few-shot Learners", "Diffusion models beat GANs on Image synthesis"])

style_input = st.selectbox("Select Explanation style", ["Begineer", "Technical", "Code-oriented", "Mathemetical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-4 Paragraphs)", "Long (Detailed Explanation)"])

chat_template = PromptTemplate(
  template = """
                Please Summarize the research paper titled "{paper_input}" with the following specifications.
                Explanation style: {style_input}
                Explanation_length: {length_input}

                1. Mathematical Details:
                  - Include relevant mathematical equations if present in paper.
                  - Explain the mathematical concpts using simple, intuitive code snippets where applicable
                2. Annalogies:
                  - Use relatable analogies to simplify complex ideas.
                If certain informataion is not available in the paper, respond with Insufficient Information Available instead of guessing.
                Ensure the summary is clear, accuarate and alligned with the provided style and length.
             """,
             input_variables = ["paper_input", "style_input", "length_input"]
)

prompts = chat_template.invoke({
  'paper_input': paper_input,
  'style_input': style_input,
  'length_input': length_input
})

if st.button('Summarize'):
  res = model.invoke(prompts)
  st.write(res.content)