import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

def load_text_file():
    
    #creating a temporary file
    with tempfile.NamedTemporaryFile(delete=False,suffix=".txt") as temp_file:
        temp_file.write(b"Hello \n World")   
        temp_file_path = temp_file.name

    try:

        #using textloader
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        for doc in documents:
            #print("Document_Content: ")
            #print(doc) # gives everything
            print(doc.page_content)
            print(documents[0].page_content[:100])
            print(documents[0].metadata)

    finally:
        os.remove(temp_file_path)

def pdf_loader(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"No. of documents loaded: {len(documents)}")
    for i, doc in enumerate(documents):
        print(f"Document {i+1}, Content preview : {doc.page_content[:1000]}")
        #print(doc.metadata)

if __name__ == "__main__":
    #load_text_file()
    pdf_loader("docs/Objectives_of_Algorithms_Case_Study.pdf")