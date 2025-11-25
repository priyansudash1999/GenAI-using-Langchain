from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chatHistory = []

while True:
  user_input = input("You: ")
  chatHistory.append(user_input)
  if user_input == 'exit':
    break
  result = model.invoke(chatHistory)
  chatHistory.append(result.content)
  print("AI: ", result.content)
print("AI: ", chatHistory)