import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
'''
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

# Invoke the model
response = llm.invoke("What is the capital of France?")

print(response.content)
'''

'''
llm_google_genai = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
response_google_genai = llm_google_genai.invoke("What is the capital of France")
print(f"Response from anthropic = {response_google_genai.content}")
'''

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

# Send messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?")
]

response = llm.invoke(messages)

print(response.content)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

vector = embeddings.embed_query(response.content)
print(f"Embedding dimension: {len(vector)}")
print(vector)