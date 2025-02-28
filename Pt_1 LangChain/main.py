import re  # Importa o módulo de expressões regulares para buscar padrões na string
import os  # Importa o módulo para manipular variáveis de ambiente do sistema
import json  # Importa o módulo JSON para converter dados entre Python e JSON
from langchain.chat_models import init_chat_model  # Importa a função para inicializar o modelo de IA
from langchain_core.prompts import PromptTemplate  # Importa a classe para estruturar perguntas enviadas à IA
from langchain_core.runnables import RunnableLambda, RunnableSequence  # Importa funções para criar um pipeline de execução


# Define a chave da API para autenticação no serviço Groq (⚠️ Nunca compartilhe sua API Key publicamente!)
os.environ["GROQ_API_KEY"] = "Digite sua API KEY aqui"  # 🔴 Substitua pela sua API KEY

# Inicializa o modelo de IA usando o provedor "groq"
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Criação de etapas do pipeline para processamento da pergunta

# 1. Valida se a pergunta contém uma expressão matemática e levanta erro se não for válida
validation_chain = RunnableLambda(lambda x: {"question": validate_question(x["question"])})

# 2. Processa a pergunta usando a IA e gera uma resposta
ai_chain = RunnableLambda(lambda x: {**x, "answer": process_ai_question(x["question"])})

# Montagem do pipeline de execução
pipeline = RunnableSequence(
    validation_chain,  # Valida se é uma pergunta matemática
    ai_chain  # Se passou na validação, a IA processa a pergunta
)


def validate_question(question: str):
    # Expressão regular para identificar perguntas matemáticas
    math_terms = r"[\d\+\-\*\/\=\(\)x]"
    is_valid = re.search(math_terms, question, re.IGNORECASE)
    if not is_valid:
        raise Exception("A pergunta deve ser sobre matemática")  # Lança exceção caso a pergunta não seja válida
    return question


def process_ai_question(question: str) -> str:
    # Cria um template de prompt para estruturar a pergunta antes de enviá-la ao modelo
    prompt_template = PromptTemplate.from_template("Responda a seguinte pergunta matemática: {question}")
    # Cria uma cadeia (pipeline) onde o prompt formatado é processado pelo modelo de IA
    chain = prompt_template | model
    # Executa o pipeline passando a pergunta e recebe a resposta da IA
    answer = chain.invoke({"question": question})
    # Retorna o conteúdo gerado pela IA
    return answer.content


def receiver(question: str):
    try:
        result = pipeline.invoke({"question": question})  # Executa o pipeline com a pergunta fornecida
        # Retorna a resposta gerada pela IA no formato JSON
        return json.dumps({
            "Pergunta": question,
            "Categoria": "matemática",
            "Resposta": result["answer"]
        }, indent=4)
    except Exception as e:
        return json.dumps({
            "Erro": str(e)
        }, indent=4)


def run():
    # Solicita ao usuário que insira uma pergunta matemática no terminal
    question = input("Insira sua pergunta matemática: ")
    # Chama a função receiver para processar a pergunta e exibe a resposta ou erro
    print(receiver(question))


if __name__ == "__main__":
    run()
