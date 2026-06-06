from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

from chains.parallel_chain import get_parallel_chain
from chains.formatter_chain import get_formatted_report

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.7)

topic = "Generative AI in 2026"

parallel_chain = get_parallel_chain(model, topic)

formatted_chain = get_formatted_report(topic)


final_chain = parallel_chain | formatted_chain

response = final_chain.invoke({})

# print(response)

# final_chain.get_graph().print_ascii()

# for output to be stored in the project as report
with open("output/report.txt", "w", encoding= "utf-8" ) as f:
    f.write(response)

