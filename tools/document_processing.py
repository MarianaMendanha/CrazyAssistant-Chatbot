from llama_index.core import SimpleDirectoryReader
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

# Carrega e processa documentos da pasta
def process_documents(input_dir):
    documents = load_folder_docs(input_dir)
    for doc in documents:
        if doc.metadata['file_type'] in ["image/jpeg", "image/png"]:
            image_path = doc.metadata['file_path']
            description = generate_image_description(image_path)
            doc.set_content(description)
    setting_metadata(documents)
    exclude_metadata_key(documents)
    return documents

# Exibe os documentos processados no terminal
def display_documents(documents):
    terminal_width = os.get_terminal_size().columns
    print('-' * terminal_width)

    for doc in documents:
        formatted_name = format_file_name(doc.metadata['file_name'])
        content_size = terminal_width - len(f"ID: {doc.doc_id},  File Name : {formatted_name:<30},  Content: ....")
        if content_size < 15:
            content_size = 15
        print(f"ID: {doc.doc_id},  File Name : {formatted_name:<30},  Content: {doc.get_content()[:17]}...")
    
    print('-' * terminal_width)

# Função para carregar documentos da pasta ----------------------------------------------------------------------------
def load_folder_docs(input_dir):
    """
    Carrega todos os documentos de um diretório, de forma recursiva.
    
    Args:
        input_dir (str): Diretório de entrada onde os documentos estão localizados.

    Returns:
        list: Lista de documentos carregados.
    """
    return SimpleDirectoryReader(input_dir=input_dir, recursive=True).load_data(show_progress=True)

# Função para gerar descrições de imagens ----------------------------------------------------------------------------
def generate_image_description(image_path):
    """
    Gera uma descrição de uma imagem usando um modelo de legendagem e extrai texto usando OCR.

    Args:
        image_path (str): Caminho do arquivo da imagem.

    Returns:
        str: Descrição combinada da imagem e texto extraído.
    """
    # Configurar o caminho do Tesseract
    pytesseract.pytesseract.tesseract_cmd = "C:/Users/mariana.cruz/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
    
    # Carregar o modelo de legendagem de imagens
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Abrir a imagem
    image = Image.open(image_path)
    
    # Gerar descrição geral da imagem
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=50)
    description = processor.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    
    # Extrair texto da imagem usando OCR
    ocr_text = pytesseract.image_to_string(image)
    
    # Combinar a descrição geral com o texto extraído
    full_description = f"{description}, Extracted Text: {ocr_text.strip()}"
    return full_description

# Função para definir metadados --------------------------------------------------------------------------------------
def setting_metadata(list_of_docs):
    """
    Configura o template e separador de metadados para uma lista de documentos.

    Args:
        list_of_docs (list): Lista de documentos.
    """
    text_template = "Content Metadata:\n{metadata_str}\n\nContent:\n{content}"
    metadata_template = "{key}: {value}"
    metadata_seperator = "\n"

    try:
        docx, images, pdf, text = list_of_docs
        for doc in docx + images + pdf + text:
            doc.text_template = text_template
            doc.metadata_template = metadata_template
            doc.metadata_seperator = metadata_seperator
    except Exception:
        for doc in list_of_docs:
            doc.text_template = text_template
            doc.metadata_template = metadata_template
            doc.metadata_seperator = metadata_seperator

# Função para excluir certas chaves de metadados ---------------------------------------------------------------------
def exclude_metadata_key(documents):
    """
    Exclui determinadas chaves de metadados dos documentos.

    Args:
        documents (list): Lista de documentos.
    """
    excluded_llm_metadata_keys = ["file_size"]
    excluded_embed_metadata_keys = ["file_size"]
    for doc in documents:
        doc.excluded_llm_metadata_keys = excluded_llm_metadata_keys
        doc.excluded_embed_metadata_keys = excluded_embed_metadata_keys

# Função para formatar nomes de arquivos -----------------------------------------------------------------------------
def format_file_name(file_name, max_length=30):
    """
    Formata o nome de um arquivo, encurtando-o se for muito longo.

    Args:
        file_name (str): Nome original do arquivo.
        max_length (int): Comprimento máximo permitido para o nome do arquivo.

    Returns:
        str: Nome do arquivo formatado.
    """
    if len(file_name) < max_length:
        return file_name
    half_length = (max_length - 3) // 2
    return f"{file_name[:half_length]}...{file_name[-half_length:]}"
