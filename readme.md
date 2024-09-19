
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
├── chat-memory/         # Memória de chats por usuário
├── data/                # Diretório de dados, contendo documentos e imagens
│   ├── docx/
│   ├── images/
│   ├── pdf/
│   └── text/
├── persist-content/      # Conteúdos persistidos (índices e modelos)
├── tools/               # Ferramentas e funções auxiliares
│   ├── __init__.py
│   ├── document_processing.py
│   ├── index_management.py
│   └── chat_helpers.py
└── main.py              # Arquivo principal do projeto
```

---

## 💻 Instalação

Siga os passos abaixo para configurar o ambiente do projeto:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/crazyassistant-chatbot.git
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
