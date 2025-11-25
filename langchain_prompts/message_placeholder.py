from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Chat Template

chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful customer support agent'),
  MessagesPlaceholder(variable_name= 'chatHistory'),
  ('human', '{query}')
])

chatHistory = []
# load chat history
with open('chatHistory.txt') as f:
  chatHistory.extend(f.readlines())


# Create prompt
prompt = chat_template.invoke({'chatHistory': chatHistory, 'query': "Where is my refund"})


print(prompt)