import pickle, os
from llama_index.core import VectorStoreIndex

def create_index(documents):
    index = VectorStoreIndex.from_documents([])
    for doc in documents:
        index.insert(doc)
    return index

def save_index(index, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(index, f)

def load_index(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)
    
# Gerenciar o índice (criação, salvamento e carregamento)
def manage_index(documents, index_path="index.pkl"):
    if os.path.exists(index_path):
        index = load_index(index_path)
    else:
        index = create_index(documents)
        save_index(index, index_path)
    return index