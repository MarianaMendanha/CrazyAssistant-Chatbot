import sys, os
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.storage.chat_store import SimpleChatStore
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Função para desativar logs temporariamente
def disable_logging():
    logging.disable(logging.INFO)

# Função para reativar logs
def enable_logging():
    logging.disable(logging.NOTSET)
    
terminal_width = os.get_terminal_size().columns

# Configurar o sistema de memória do chat
def configure_chat_memory(user_name, memory_dir="chat-memory"):
    memory_path = os.path.join(memory_dir, f"{user_name.lower()}_memory.json")
    if os.path.exists(memory_path):
        chat_store = SimpleChatStore.from_persist_path(persist_path=memory_path)
    else:
        chat_store = SimpleChatStore()

    memory = ChatMemoryBuffer.from_defaults(
        token_limit=10000,
        chat_store=chat_store,
        chat_store_key=user_name.lower(),
    )
    return memory, memory_path

# Configurar o mecanismo de chat
def setup_chat_engine(index_pickle, memory, user_name):
    chat_engine = index_pickle.as_chat_engine(
        chat_mode="condense_plus_context",
        memory=memory,
            context_prompt = (
            f"You are a chatbot called CrazyAssistant, that speaks im portuguese-BR, able to have normal interactions, as well as help"
            f" employees with their questions about the documents of the CrazyTechLabs Company. "
            f"Your current user is {user_name}. Here are the relevant documents for the context:\n"
            "{context_str}"
            "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
            " If the user asks something outside the scope of the CrazyTechLabs documents, just say you don't know."
            " If the user asks you to list the documents, list all of them."
        ),
        verbose=False,
        max_results=100,
        top_k=100,
        similarity_top_k=10,
        streaming=True
    )
    return chat_engine

# Loop de interação do chat
def chat_loop(chat_engine, chat_store, memory_path):
    while True:
        question = input("Prompt: ")
        if question.lower() == "exit":
            chat_store.persist(persist_path=memory_path)
            sys.exit()
        else:
            disable_logging()
            response = chat_engine.stream_chat(question)
            # print(response)
            print("ChatAssistant:\n")
            response.print_response_stream()
            print("\n")
            print('-' * terminal_width)
            enable_logging()
