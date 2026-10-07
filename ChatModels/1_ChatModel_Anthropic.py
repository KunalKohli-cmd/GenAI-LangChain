from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()  # Load environment variables from .env file

model = ChatAnthropic(model="claude-2", temperature=0.7)
result = model.invoke("what is the capital of India?")
print(result.content)