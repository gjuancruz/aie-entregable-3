import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"), override=False)
model = ChatOpenAI(model="gpt-4o", temperature=0.7)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Respondé brevemente, en 15 palabras o menos."),
    ("human", "{question}"),
])

chain = prompt | model | parser

async def main():
    question = "¿Cuál es la capital de Argentina?"
    response = await chain.ainvoke({"question": question})
    print(response)

if __name__ == "__main__":
    asyncio.run(main())