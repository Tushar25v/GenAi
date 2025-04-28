from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from openai import OpenAI

api_key = "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"

file_path = Path(__file__).parent / "cheat_code.pdf"

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()  # makes documents ... list of pages 

#print(docs[0])   to see reding od pdf

text_splitter = RecursiveCharacterTextSplitter(  # splitting into character is the dumbest thing 
    chunk_size = 100,
    chunk_overlap=50,
)

split_docs = text_splitter.split_documents(documents=docs)


#print("Docs" ,len(docs))
#print("split", len(split_docs))

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key= api_key,

)


'''vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="learning_langchain",    # injection part
     embedding=embedding
)

vector_store.add_documents(documents=split_docs)'''
#print("injection complete")


retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedding
)

relevent_chunk = retriver.similarity_search(
    query="What is variable scope ?"
)


#print("Relevant Chunks", relevent_chunk)


system_prompt = f'''
You r a great ai assistant helping coding related query
Context : {relevent_chunk} Each chunk contains a page n and its page_content. Base all responses only and only on this information.
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