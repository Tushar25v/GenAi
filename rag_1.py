from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

file_path = Path(__file__).parent / "cheat_code.pdf"

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=api_key,
)

# Vector store setup for injection (uncomment when needed)
# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="learning_langchain",
#     embedding=embedding
# )
# vector_store.add_documents(documents=split_docs)


retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedding
)

relevent_chunk = retriver.similarity_search(
    query="What is variable scope ?"
)

system_prompt = f'''
You are a great AI assistant helping with coding related queries.
Context: {relevent_chunk} Each chunk contains a page number and its page_content. Base all responses only on this information.
'''

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content":system_prompt},
        {"role": "user", "content": "What is variable scope ?"},
    ],
    stream=False
)
print(response.choices[0].message.content)
