# Tutor Matemático com IA

Este projeto é um tutor matemático que utiliza **Inteligência Artificial** para responder perguntas matemáticas. Ele valida se a pergunta contém uma expressão matemática e então processa a resposta usando um modelo de IA baseado no **Llama 3**, fornecido pelo serviço **Groq**.

## 📌 Tecnologias Utilizadas

- **Python** (linguagem principal)
- **LangChain** (estruturação do fluxo da IA)
- **Regex (re)** (validação de expressões matemáticas)
- **JSON** (estruturação da resposta)
- **Groq API** (serviço de IA)

## 🚀 Como Executar

1. **Instale as dependências** (se ainda não tiver):
   ```sh
   pip install langchain langchain-core groq
   ```

2. **Adicione sua API Key do Groq** no código-fonte:
   ```python
   os.environ["GROQ_API_KEY"] = "Digite sua API KEY aqui"
   ```

3. **Execute o programa** no terminal:
   ```sh
   python part1_langchain.py
   ```

4. **Digite sua pergunta matemática** e receba a resposta da IA!

## 🔧 Estrutura do Código

- `validate_question(question: str)`: Valida se a entrada do usuário contém uma equação matemática.
- `process_ai_question(question: str)`: Envia a pergunta ao modelo de IA e retorna a resposta.
- `receiver(question: str)`: Pipeline que valida e processa a pergunta, retornando um JSON com a resposta.
- `run()`: Função principal que solicita a pergunta do usuário e exibe a resposta.

## ⚠️ Aviso

- **Nunca compartilhe sua API Key publicamente!**
- O modelo só responde perguntas matemáticas.
- Certifique-se de que sua pergunta contenha números e operadores matemáticos.

## 📄 Licença

Este projeto é livre para uso e modificação. Caso utilize ou modifique, sinta-se à vontade para contribuir!

---

