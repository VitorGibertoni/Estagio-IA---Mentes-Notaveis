# 🚀 Processador de Perguntas Matemáticas com IA

Este projeto usa a biblioteca **LangChain** para processar perguntas matemáticas enviadas pelo usuário. Ele valida se a pergunta é realmente matemática, corrige possíveis erros de sintaxe e envia para um modelo de IA (**Llama3-8b-8192**) via **Groq API** para obter a resposta.

---

## 📌 Funcionalidades
- **Valida se a entrada é uma expressão matemática**
- **Corrige a sintaxe** (ex.: adiciona `*` entre números e letras (2x -->2*x))
- **Encaminha a pergunta para IA** e retorna a resposta formatada em JSON

---

## 🛠️ Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/VitorGibertoni/Estagio-IA---Mentes-Notaveis.git 
   cd Estagio-IA---Mentes-Notaveis 
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
   *(Crie um arquivo `requirements.txt` se necessário, incluindo: `langchain`, `re`, `os`, `json`)*

---

## 🚀 Como Usar
Execute o script e insira uma pergunta matemática:
```sh
python Parte1_Langchain.py
```
Digite algo como:
```
Insira a pergunta matematica: quanto é 2+2?
```
Saída esperada:
```json
{
    "pergunta": "2+2",
    "categoria": "matematica",
    "resposta": "4"
}
```

---

## ⚙️ Como Funciona
- **`validar_pergunta(pergunta: str) -> bool`**: Confere se a entrada contém símbolos matemáticos.
- **`corrigir_sintaxe(pergunta: str) -> str`**: Adiciona operadores ausentes, como `2x` -> `2*x`.
- **`processar_pergunta_ia(pergunta: str) -> str`**: Formata o prompt e envia para a IA.
- **`pipeline`**: Estrutura que primeiro valida e depois processa a resposta.
- **`receptor(pergunta: str)`**: Orquestra tudo e retorna a resposta formatada.

---



## 📝 Notas
- Certifique-se de substituir a chave da API **Groq**(linha 10) antes de rodar o projeto.
- A IA responde apenas a perguntas matemáticas, outras entradas gerarão erro.
- Futuras melhorias podem incluir suporte a perguntas matemáticas mais complexas.

---



