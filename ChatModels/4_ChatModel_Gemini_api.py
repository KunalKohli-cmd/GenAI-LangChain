from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # a text model, not the "-image" one
    temperature=0.7,
    timeout=30,
    max_retries=0,
)
result = model.invoke("what is the capital of India?")
print(result.text)