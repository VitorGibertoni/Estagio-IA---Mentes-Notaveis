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
- **Processamento com IA**: Envia a equação ao modelo de IA e recebe a resposta.
- **Grafo de Estados**: Controla o fluxo de entrada e saída usando os agentes "Receptor" e "Professor Virtual".

## 🚀 Como Executar 

**✅Instale o Docker em sua Maquina** |
**✅Instale o GIT em sua Maquina**

**Clone o Repositorio** pelo Terminal: 
```sh
git clone https://github.com/VitorGibertoni/Estagio-IA---Mentes-Notaveis
 ```

1. **Adicione sua API Key do Groq** no código-fonte (main.py):
   ```python
   os.environ["GROQ_API_KEY"] = "Digite sua API KEY aqui"
   ```

 **Adicione sua API Key do Groq** no código-fonte:
   ```python
   os.environ["GROQ_API_KEY"] = "Digite sua API KEY aqui"
   ```


Execute o script diretamente no terminal ou em um ambiente Python:
```sh
docker build . --tag part2:v1
docker run -i part2:v1
```

## 🛠️ Personalização
Se desejar alterar o modelo de IA, basta modificar esta linha do código:
```python
model = init_chat_model("llama3-8b-8192", model_provider="groq")
```
Você pode substituir `llama3-8b-8192` por outro modelo compatível.

Não esqueca de colocar sua API Key!



