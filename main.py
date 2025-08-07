from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load the local model (e.g., mistral or llama2)
llm = Ollama(model="mistral")

# Example prompt template for generating credit memo
template = """
You are a credit analyst. Based on the following customer data, generate a credit memo.

Customer Info:
- Name: {name}
- Income: {income}
- Behavioral Score: {score}
- Recent Transactions: {transactions}

Write a clear and concise credit memo.
"""

prompt = PromptTemplate(
    input_variables=["name", "income", "score", "transactions"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)

# Example input
response = chain.run({
    "name": "Jane Doe",
    "income": "$85,000",
    "score": "760",
    "transactions": "3 large payments to utilities, 1 travel-related expense, 5 small e-commerce purchases"
})

print(response)
