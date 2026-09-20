from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash"
)

response = model.invoke("What is name of Ravana's Father in Ramayan?")

print(response.conten)