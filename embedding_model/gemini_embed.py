from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-2"
)

array = [
    "this is new",
    "Also this"
]

vector = embedding.embed_documents(array)


print(vector)