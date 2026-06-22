from dotenv import load_dotenv
from importlib.metadata import version 

load_dotenv() # keys can now be used

core_version = version("langchain-core")
lg_version = version("langgraph")

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama


#print(f"langchain-core version : {core_version}")
#print(f"langgrapg version : {lg_version}")

def main():

    #llm_openai = ChatOpenAI(model_name="gpt-4o-mini",temperature=0)
    #response_openai = llm_openai.invoke("Say 'Setup complete!' in one word")
    #print(f"Response from openai = {response_openai}")

    #llm_anthropic = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
    #response_anthropic = llm_anthropic.invoke("Say 'Setup complete!' in one word")
    #print(f"Response from anthropic = {response_anthropic}")

    #llm_google_genai = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    #response_google_genai = llm_google_genai.invoke("Say 'Setup complete!' in one word")
    #print(f"Response from anthropic = {response_google_genai}")

    llm_ollama = ChatOllama(model="llama3.1:8b", temperature=0)
    response_ollama = llm_ollama.invoke("Say 'Setup complete!' in one word")
    print(f"Response from ollama = {response_ollama}")

    print("Setup complete")


if __name__ == "__main__":
    main()
