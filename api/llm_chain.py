from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that make {product}?",
)
chain = LLMChain(llm=llm, prompt=prompt)

if __name__ == "__main__":
    print(chain.run("ice cream"))