# 🚀 Processador de Perguntas Matemáticas com IA

Este projeto utiliza um modelo de Inteligência Artificial (IA) para processar e resolver equações matemáticas digitadas pelo usuário. O código valida se a entrada do usuário é uma equação matemática, corrige possíveis erros de sintaxe e utiliza um modelo de IA para fornecer a resposta.

## 📌 Tecnologias Utilizadas
- Python 3
- [LangChain](https://python.langchain.com/): Framework para modelos de IA
- [LangGraph](https://github.com/langchain-ai/langgraph): Biblioteca para criação de grafos de estados
- Expressões regulares (Regex) para validação de entrada
- Integração com API Groq para processamento de linguagem natural

## 📂 Estrutura do Código
- **Validação da Pergunta**: Verifica se a entrada contém uma equação matemática válida.
- **Correção de Sintaxe**: Ajusta a formatação da equação (ex: adiciona `*` entre números e variáveis quando necessário).
- **Processamento com IA**: Envia a equação ao modelo de IA e recebe a resposta.
- **Grafo de Estados**: Controla o fluxo de entrada e saída usando os agentes "Receptor" e "Professor Virtual".

## 🚀 Como Executar
### 1️⃣ Pré-requisitos
Antes de rodar o código, certifique-se de ter:
- Python 3 instalado
- As bibliotecas necessárias instaladas. Para isso, execute:
  ```sh
  pip install langchain langgraph
  ```

### 2️⃣ Rodando o Código
Execute o script diretamente no terminal ou em um ambiente Python:
```sh
python Parte2_LangGraph.py
```
Digite uma equação matemática quando solicitado, como:
```
Digite uma equação para resolver:
```
A resposta será processada e exibida na tela.

## 🛠️ Personalização
Se desejar alterar o modelo de IA, basta modificar esta linha do código:
```python
model = init_chat_model("llama3-8b-8192", model_provider="groq")
```
Você pode substituir `llama3-8b-8192` por outro modelo compatível.

Não esqueca de colocar sua API Key!



