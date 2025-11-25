from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI()

chatHistory = [
  SystemMessage(content= "You are an programmer")
]

while True:
  user_input = input("You: ")
  chatHistory.append(HumanMessage(content=user_input))
  if user_input == 'exit':
    break
  result = model.invoke(chatHistory)
  chatHistory.append(AIMessage(content=result.content))
  print("AI: ", result.content)
print(chatHistory)