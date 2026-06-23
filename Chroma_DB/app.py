import chromadb

chroma_client = chromadb.Client()

collection_name = "test_collection"

collection = chroma_client.get_or_create_collection(collection_name)

documents = [
    {"id":"doc1", "text":"Hello World!"},
    {"id":"doc2", "text":"How are you?"},
    {"id":"doc3", "text":"Good Bye."},   # if same doc_id it will replace the previous
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=[doc["text"]])


query_text = "Hello World!"

results = collection.query(
    query_texts=[query_text],
    n_results=3,
)

print(results)