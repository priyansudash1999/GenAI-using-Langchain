from langchain_core.prompts import PromptTemplate

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

chat_template.save('template.json')