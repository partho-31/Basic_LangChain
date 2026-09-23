from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=100,
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("What is the name of the capital of Bangladesh?")

print(response.content)