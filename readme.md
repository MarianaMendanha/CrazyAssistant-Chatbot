
# 🤖 CrazyAssistant Chatbot

CrazyAssistant é um chatbot avançado com suporte a processamento de documentos, geração de descrições de imagens e interações dinâmicas com usuários, utilizando tecnologia de última geração. Este projeto usa **LLaMA** para criação de chatbots personalizados, integrando **RAG (Retrieval-Augmented Generation)** com **documentos locais** e serviços na nuvem.

---

## 📋 Índice
- [🚀 Funcionalidades](#-funcionalidades)
- [⚙️ Tecnologias](#-tecnologias)
- [📦 Estrutura de Diretórios](#-estrutura-de-diretórios)
- [💻 Instalação](#-instalação)
- [📝 Como Usar](#-como-usar)
- [🙋‍♀️ Contribuições](#-contribuições)
- [🔐 Licença](#-licença)

---

## 🚀 Funcionalidades
- **Interações baseadas em documentos**: O chatbot responde às perguntas com base em arquivos armazenados localmente ou em serviços como **SharePoint**.
- **Descrição de imagens**: Geração automática de descrições para imagens usando processamento avançado de linguagem natural e OCR.
- **Memória de chat personalizada**: O chatbot armazena conversas e permite uma interação contínua com o usuário, adaptando-se conforme o histórico.
- **Integração com LLaMA**: Integração com o modelo LLaMA para melhorar o desempenho e a qualidade das respostas.
- **Persistência de dados**: Armazena conversas e índices de documentos para consultas futuras.

---

## ⚙️ Tecnologias
As principais tecnologias e ferramentas utilizadas no projeto incluem:
- [**LLaMA**](https://github.com/facebookresearch/llama) – Large Language Model para geração de respostas inteligentes.
- **Hugging Face** – Para embeddings de linguagem com o modelo `sentence-transformers/all-mpnet-base-v2`.
- **Ollama** – LLM especializado usado no projeto.
- **Pytesseract** – Extração de texto em imagens com OCR.
- **BLIP** – Geração de descrições de imagens.

---

## 📦 Estrutura de Diretórios

A estrutura do projeto está organizada da seguinte maneira:

```
C:.
│   .gitignore                # Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo controle de versão (Git).
│   config.json               # Arquivo de configuração que armazena informações sensíveis, como credenciais de SharePoint e configurações de projeto.
│   main.py                   # Arquivo principal que contém o código que orquestra o fluxo do projeto, incluindo o carregamento de documentos, processamento e interação com o chat.
│   readme.md                 # Arquivo de documentação que fornece uma visão geral do projeto, instruções de uso e configuração.
│   requirements.txt          # Lista de dependências do Python necessárias para o projeto, usada para configurar o ambiente com `pip install -r requirements.txt`.
│
├───chat-memory               # Diretório que armazena a memória do chat para diferentes usuários.
│       fulano_memory.json    # Arquivo de memória do chat para um usuário específico (neste exemplo, "Fulano"), onde são armazenadas interações anteriores do chat.
│
├───data                      # Diretório onde os documentos locais são armazenados para processamento.
│                             # Subdiretórios e arquivos podem ser adicionados aqui para diferentes tipos de documentos (PDF, DOCX, imagens, etc.).
│
├───index                     # Diretório que armazena os arquivos de índice gerados após o processamento dos documentos.
│       index.pkl             # Arquivo principal de índice usado para buscar e recuperar documentos no chat.
│
├───persist-content           # Diretório onde são armazenados conteúdos persistentes, como vetores de embedding e estruturas de documentos.
│       default__vector_store.json  # Armazena vetores de embedding padrão para a busca vetorial.
│       docstore.json               # Armazena os metadados e informações sobre os documentos processados.
│       graph_store.json            # Armazena a estrutura de grafos entre os documentos, útil para relacionamentos e consultas complexas.
│       image__vector_store.json    # Vetores de embedding para imagens processadas, caso haja suporte para consultas de imagens.
│       index_store.json            # Armazena a estrutura do índice que associa documentos com seus vetores de embedding.
│
└───tools                     # Diretório com scripts auxiliares usados para processar documentos, gerenciar índices e configurar o chat.
        chat_helpers.py        # Script com funções auxiliares para o chat, como configuração e gerenciamento de memória.
        document_processing.py # Script que contém funções para processar e preparar documentos para inclusão no índice.
        index_management.py    # Script responsável pela criação e gerenciamento de índices de documentos.
        __init__.py            # Arquivo que marca este diretório como um pacote Python, permitindo que os módulos sejam importados no projeto.

```

---

## 💻 Instalação

Siga os passos abaixo para configurar o ambiente do projeto:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/MarianaMendanha/CrazyAssistant-Chatbot.git
   ```

2. **Instale as dependências**:
   Certifique-se de ter o **Miniconda** instalado e crie um ambiente:
   ```bash
   conda create --name llama python=3.9
   conda activate llama
   pip install -r requirements.txt
   ```

3. **Configure o Tesseract**:
   Baixe e instale o [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) e ajuste o caminho no código.


4. **Instale os Drivers da NVIDIA:**
   - Baixe e instale os drivers NVIDIA mais recentes para sua GPU. Isso é essencial para garantir que o CUDA e outros componentes funcionem corretamente.
   - **Tutorial:** [Como Instalar os Drivers NVIDIA](https://www.youtube.com/watch?v=r7Am-ZGMef8)


5. **Instale o Ollama:**
   - Baixe e instale o Ollama para criar e gerenciar seus LLMs.
   - **Tutorial:** [Instalação do Ollama](https://github.com/ollama/ollama)
   - Após instalar o Ollama, faça o pull do modelo LLM que você deseja usar.

5. **Instale a Versão Correta do PyTorch:**
   - Baixe e instale a versão do PyTorch compatível com a versão do CUDA e drivers da NVIDIA que você instalou.
   - **Tutorial:** [Instalação do PyTorch](https://pytorch.org/get-started/locally/)

Siga esses passos para garantir que todos os componentes estejam corretamente configurados para o funcionamento adequado do projeto.

---

## 📝 Como Usar

1. **Iniciar o chatbot**:
   Execute o script principal:
   ```bash
   python main.py
   ```

2. **Carregue seus documentos**:
   - Coloque seus arquivos na pasta `data`.

3. **Interaja com o chatbot**:
   - Após carregar os documentos, você pode fazer perguntas ao chatbot sobre eles.
   - O chatbot responde com base no conteúdo dos documentos.

4. **Persistência da Conversa**:
   - O histórico da conversa é salvo na pasta `chat-memory`, permitindo que a interação continue em sessões futuras.

---

## 🙋‍♀️ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests. Aqui está como você pode contribuir:

1. **Fork o repositório**.
2. **Crie uma branch para sua feature** (`git checkout -b feature/nome-da-feature`).
3. **Faça o commit de suas alterações** (`git commit -m 'Adiciona nova feature'`).
4. **Faça o push para a branch** (`git push origin feature/nome-da-feature`).
5. **Abra um Pull Request**.

---

## 🔐 Licença
