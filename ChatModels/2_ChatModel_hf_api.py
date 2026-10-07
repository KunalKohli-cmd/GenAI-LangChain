from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = HuggingFaceEndpoint(
    repo_id="edwardcapriolo/granite-4.0-h-tiny-JQ4",  # or "Qwen/Qwen2.5-7B-Instruct"
    task="text-generation",
    temperature=0.7,
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of India?")
print(result.content)
