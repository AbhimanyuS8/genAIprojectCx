from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()
chat = ChatAnthropic()
response = chat.predict_messages()