import sys
import os
import json
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.readers.microsoft_sharepoint import SharePointReader

from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

from tools import process_documents, display_documents, manage_index, configure_chat_memory, setup_chat_engine, chat_loop

with open('config.json', 'r') as f:
        config = json.load(f)
        
def add_tools_to_path():
    """Adiciona a pasta 'tools' ao sys.path, se ainda não estiver."""
    tools_path = os.path.join(os.path.dirname(__file__), 'tools')
    if tools_path not in sys.path:
        sys.path.append(tools_path)

def configure_models():
    """Configura os modelos de embedding e LLM."""
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2", device="cuda")
    Settings.llm = Ollama(model="gemma2:27b", temperature=0, request_timeout=500.0, device="cuda")

def main():
    """Função principal que orquestra a execução do projeto."""
    add_tools_to_path()  # Adiciona o caminho das ferramentas
    configure_models()   # Configura os modelos
    
    ### DOCUMENTOS DO SHAREPOINT ### - para utilizar documentos do SharePoint, descomente as linhas abaixo e comente a linha de documentos locais
    loader = SharePointReader(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        tenant_id=config['tenant_id'],
        sharepoint_site_name=config['sharepoint_site_name'],
        sharepoint_folder_path=config['sharepoint_folder_path'],
        recursive=True,
    )
    documents = loader.load_data()
    
    ### DOCUMENTOS LOCAIS ### - para utilizar documentos locais, descomente essa linha e comente as linhas do sharepoint
    # documents = process_documents(input_dir="./data")
    
    display_documents(documents)  # Exibe os documentos processados no terminal
    
    # Gerenciar o índice de documentos
    index_pickle = manage_index(documents, index_path="index/index.pkl")  # Cria e carrega o índice
    
    """ ## Testar no futuro -> https://docs.llamaindex.ai/en/stable/understanding/querying/querying/ ##################################
    retriever = VectorIndexRetriever(
        index=index_pickle,
        similarity_top_k=10,
    )
    response_synthesizer = get_response_synthesizer()
    ## Consigo usar no chat? ##
    # query_engine = RetrieverQueryEngine(
    #     retriever=retriever,
    #     response_synthesizer=response_synthesizer,
    #     node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],
    # )
    ###############################################################################################################################
    """
    
    # Configurar o chat
    user_name = input("Digite seu nome: ")
    print(f"Seja Bem-Vindo(a), {user_name}\n")
    
    memory, memory_path = configure_chat_memory(user_name)  # Configura o armazenamento de memória do chat
    chat_engine = setup_chat_engine(index_pickle, memory, user_name)   # Configura o motor de chat

    # Inicia o loop de interação do chat
    chat_loop(chat_engine, memory.chat_store, memory_path)

if __name__ == "__main__":
    main()
