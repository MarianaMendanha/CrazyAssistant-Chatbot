import sys
import os
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from tools import process_documents, display_documents, manage_index, configure_chat_memory, setup_chat_engine, chat_loop

def add_tools_to_path():
    """Adiciona a pasta 'tools' ao sys.path, se ainda não estiver."""
    tools_path = os.path.join(os.path.dirname(__file__), 'tools')
    if tools_path not in sys.path:
        sys.path.append(tools_path)

def configure_models():
    """Configura os modelos de embedding e LLM."""
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2", device="cuda")
    Settings.llm = Ollama(model="CrazyAssistant", request_timeout=500.0, device="cuda")

def main():
    """Função principal que orquestra a execução do projeto."""
    add_tools_to_path()  # Adiciona o caminho das ferramentas
    configure_models()   # Configura os modelos

    # Carregar e processar documentos
    documents = process_documents(input_dir="./data")
    display_documents(documents)  # Exibe os documentos processados no terminal
    
    # Gerenciar o índice de documentos
    index_pickle = manage_index(documents)  # Cria e carrega o índice

    # Configurar o chat
    user_name = input("Digite seu nome: ")
    print(f"Seja Bem-Vindo(a), {user_name}")
    
    memory, memory_path = configure_chat_memory(user_name)  # Configura o armazenamento de memória do chat
    chat_engine = setup_chat_engine(index_pickle, memory, user_name)   # Configura o motor de chat

    # Inicia o loop de interação do chat
    chat_loop(chat_engine, memory.chat_store, memory_path)

if __name__ == "__main__":
    main()
