from dotenv import load_dotenv # keys can now be used
load_dotenv()

from langchain_core import __version__ as core_version
#from langgraph import __version__ as lg_version # does not work for this version of langgraph

from importlib.metadata import version
lg_version = version("langgraph")

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

print(f"langchain-core version : {core_version}")
print(f"langgrapg version : {lg_version}")

def main():
    print("Hello from rag-fcc!")


if __name__ == "__main__":
    main()
