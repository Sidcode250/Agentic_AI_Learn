import os
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage


llm = ChatOllama(model="llama3.1:8b", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is the capital of France?")
]

response = llm.invoke(messages)



embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector = embeddings.embed_query(response.content)

print(vector)
print(response.content)
print(len(vector))