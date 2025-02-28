import re  # Importa o módulo de expressões regulares para buscar padrões na string
import os  # Importa a biblioteca para manipulação de variáveis de ambiente
import json  # Importa o módulo JSON para trabalhar com objetos JSON
from langchain.chat_models import init_chat_model  # Biblioteca para inicializar e configurar o modelo da IA
from langgraph.graph import StateGraph, END  # Biblioteca para criar um grafo de estados
from langchain.schema import HumanMessage  # Estrutura de mensagem usada pelo modelo de IA


# Define a chave da API para autenticação com o serviço Groq 
os.environ["GROQ_API_KEY"] = "Digite sua API KEY" 

# Inicializa o modelo de IA (chamando um modelo Llama) utilizando o provedor "groq"
model = init_chat_model("llama3-8b-8192", model_provider="groq")


# Função para validar a pergunta
# Verifica se a pergunta contém termos matemáticos como números, operadores, ou símbolos de parênteses e multiplicação
def validate_question(question: str):
    """Valida se a pergunta contém termos matemáticos."""
    math_terms = r"[\d\+\-\*\/\=\(\)x]"
    is_valid = re.search(math_terms, question, re.IGNORECASE)

    if not is_valid:
        raise ValueError("A pergunta deve ser sobre matemática.")  # Lança exceção caso a pergunta não seja válida

    return question


# Função que envia a pergunta matemática para o modelo de IA e retorna a resposta
def process_question_ai(question: str) -> str:
    """Envia a pergunta matemática para o modelo de IA e retorna a resposta."""
    prompt_template = f"Responda a seguinte pergunta matemática: {question}"
    response = model.invoke([HumanMessage(content=prompt_template)])
    return response.content


# Agente "Receptor" - processa a entrada do usuário e define a categoria da pergunta
def receiver(state: dict[str, str | None]) -> dict[str, str | None]:
    """Processa a entrada do usuário e define a categoria da pergunta."""
    if validate_question(state["pergunta"]):
        state["categoria"] = "matemática"
    else:
        state["resposta"] = "A pergunta não é uma equação matemática válida."
    return state


# Agente "Professor Virtual" - resolve a equação e retorna a resposta
def virtual_teacher(state: dict[str, str | None]) -> dict[str, str | None]:
    """Resolve a equação matemática e retorna a resposta da IA."""
    if state["categoria"] == "matemática":
        state["resposta"] = process_question_ai(state["pergunta"])
    return state


def run():
    """Executa o fluxo do grafo para processar a equação matemática."""
    # Criando um grafo de estados para representar o fluxo da pergunta e resposta
    graph = StateGraph(dict)

    # Adiciona os nós do grafo (agentes)
    graph.add_node("receiver", receiver)
    graph.add_node("virtual_teacher", virtual_teacher)

    # Define o ponto de entrada do grafo
    graph.set_entry_point("receiver")

    # Conecta os nós do grafo
    graph.add_edge("receiver", "virtual_teacher")
    graph.add_edge("virtual_teacher", END)

    # Compila o grafo para execução
    compiled_graph = graph.compile()

    # Solicita a entrada do usuário (equação matemática)
    user_question = input("Digite uma equação para resolver: ")

    # Cria um dicionário representando o estado inicial do processo
    input_data = {"pergunta": user_question, "categoria": "", "resposta": None}

    # Executa o grafo com os dados inseridos pelo usuário
    try:
        result = compiled_graph.invoke(input_data)
        print(result["resposta"])
    except ValueError:
        print("A pergunta deve ser matemática. Tente novamente!")


if __name__ == "__main__":
    run()
